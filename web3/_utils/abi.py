import binascii
from collections import (
    abc,
    namedtuple,
)
import copy
import itertools
import re
from typing import (
    Any,
    Optional,
    Tuple,
    Union,
)

from eth_abi import (
    decoding,
    encoding,
)
from eth_abi.codec import (
    ABICodec,
)
from eth_abi.grammar import (
    ABIType,
    TupleType,
    parse,
)
from eth_abi.registry import (
    BaseEquals,
    registry as default_registry,
)
from eth_typing import (
    TypeStr,
)
from eth_utils import (
    decode_hex,
    is_bytes,
    is_list_like,
    is_text,
    to_text,
    to_tuple,
)
from eth_utils.abi import (
    collapse_if_tuple,
)
from eth_utils.toolz import (
    curry,
    partial,
    pipe,
)

from web3._utils.ens import (
    is_ens_name,
)
from web3._utils.formatters import (
    recursive_map,
)
from web3.exceptions import (
    FallbackNotFound,
)


def filter_by_type(_type, contract_abi):
    return [abi for abi in contract_abi if abi['type'] == _type]


def filter_by_name(name, contract_abi):
    return [
        abi
        for abi
        in contract_abi
        if (
            abi['type'] not in ('fallback', 'constructor') and
            abi['name'] == name
        )
    ]


def get_abi_input_types(abi):
    if 'inputs' not in abi and abi['type'] == 'fallback':
        return []
    else:
        return [collapse_if_tuple(arg) for arg in abi['inputs']]


def get_abi_output_types(abi):
    if abi['type'] == 'fallback':
        return []
    else:
        return [collapse_if_tuple(arg) for arg in abi['outputs']]


def get_abi_input_names(abi):
    if 'inputs' not in abi and abi['type'] == 'fallback':
        return []
    else:
        return [arg['name'] for arg in abi['inputs']]


def get_fallback_func_abi(contract_abi):
    fallback_abis = filter_by_type('fallback', contract_abi)
    if fallback_abis:
        return fallback_abis[0]
    else:
        raise FallbackNotFound("No fallback function was found in the contract ABI.")


def fallback_func_abi_exists(contract_abi):
    return filter_by_type('fallback', contract_abi)


def get_indexed_event_inputs(event_abi):
    return [arg for arg in event_abi['inputs'] if arg['indexed'] is True]


def exclude_indexed_event_inputs(event_abi):
    return [arg for arg in event_abi['inputs'] if arg['indexed'] is False]


def filter_by_argument_count(num_arguments, contract_abi):
    return [
        abi
        for abi
        in contract_abi
        if len(abi['inputs']) == num_arguments
    ]


def filter_by_argument_name(argument_names, contract_abi):
    return [
        abi
        for abi in contract_abi
        if set(argument_names).intersection(
            get_abi_input_names(abi)
        ) == set(argument_names)
    ]


class AddressEncoder(encoding.AddressEncoder):
    @classmethod
    def validate_value(cls, value):
        if is_ens_name(value):
            return

        super().validate_value(value)


class AcceptsHexStrMixin:
    def validate_value(self, value):
        if is_text(value):
            try:
                value = decode_hex(value)
            except binascii.Error:
                self.invalidate_value(
                    value,
                    msg='invalid hex string',
                )

        super().validate_value(value)


class BytesEncoder(AcceptsHexStrMixin, encoding.BytesEncoder):
    pass


class ByteStringEncoder(AcceptsHexStrMixin, encoding.ByteStringEncoder):
    pass


class TextStringEncoder(encoding.TextStringEncoder):
    @classmethod
    def validate_value(cls, value):
        if is_bytes(value):
            try:
                value = to_text(value)
            except UnicodeDecodeError:
                cls.invalidate_value(
                    value,
                    msg='not decodable as unicode string',
                )

        super().validate_value(value)


# We make a copy here just to make sure that eth-abi's default registry is not
# affected by our custom encoder subclasses
registry = default_registry.copy()

registry.unregister('address')
registry.unregister('bytes<M>')
registry.unregister('bytes')
registry.unregister('string')

registry.register(
    BaseEquals('address'),
    AddressEncoder, decoding.AddressDecoder,
    label='address',
)
registry.register(
    BaseEquals('bytes', with_sub=True),
    BytesEncoder, decoding.BytesDecoder,
    label='bytes<M>',
)
registry.register(
    BaseEquals('bytes', with_sub=False),
    ByteStringEncoder, decoding.ByteStringDecoder,
    label='bytes',
)
registry.register(
    BaseEquals('string'),
    TextStringEncoder, decoding.StringDecoder,
    label='string',
)

codec = ABICodec(registry)
is_encodable = codec.is_encodable


def filter_by_encodability(args, kwargs, contract_abi):
    return [
        function_abi
        for function_abi
        in contract_abi
        if check_if_arguments_can_be_encoded(function_abi, args, kwargs)
    ]


def check_if_arguments_can_be_encoded(function_abi, args, kwargs):
    try:
        arguments = merge_args_and_kwargs(function_abi, args, kwargs)
    except TypeError:
        return False

    if len(function_abi.get('inputs', [])) != len(arguments):
        return False

    try:
        types, aligned_args = get_aligned_abi_inputs(function_abi, arguments)
    except TypeError:
        return False

    return all(
        is_encodable(_type, arg)
        for _type, arg in zip(types, aligned_args)
    )


def merge_args_and_kwargs(function_abi, args, kwargs):
    """
    Takes a list of positional args (``args``) and a dict of keyword args
    (``kwargs``) defining values to be passed to a call to the contract function
    described by ``function_abi``.  Checks to ensure that the correct number of
    args were given, no duplicate args were given, and no unknown args were
    given.  Returns a list of argument values aligned to the order of inputs
    defined in ``function_abi``.
    """
    # Ensure the function is being applied to the correct number of args
    if len(args) + len(kwargs) != len(function_abi.get('inputs', [])):
        raise TypeError(
            "Incorrect argument count.  Expected '{0}'.  Got '{1}'".format(
                len(function_abi['inputs']),
                len(args) + len(kwargs),
            )
        )

    # If no keyword args were given, we don't need to align them
    if not kwargs:
        return args

    kwarg_names = set(kwargs.keys())
    sorted_arg_names = tuple(arg_abi['name'] for arg_abi in function_abi['inputs'])
    args_as_kwargs = dict(zip(sorted_arg_names, args))

    # Check for duplicate args
    duplicate_args = kwarg_names.intersection(args_as_kwargs.keys())
    if duplicate_args:
        raise TypeError(
            "{fn_name}() got multiple values for argument(s) '{dups}'".format(
                fn_name=function_abi['name'],
                dups=', '.join(duplicate_args),
            )
        )

    # Check for unknown args
    unknown_args = kwarg_names.difference(sorted_arg_names)
    if unknown_args:
        if function_abi.get('name'):
            raise TypeError(
                "{fn_name}() got unexpected keyword argument(s) '{dups}'".format(
                    fn_name=function_abi.get('name'),
                    dups=', '.join(unknown_args),
                )
            )
        raise TypeError(
            "Type: '{_type}' got unexpected keyword argument(s) '{dups}'".format(
                _type=function_abi.get('type'),
                dups=', '.join(unknown_args),
            )
        )

    # Sort args according to their position in the ABI and unzip them from their
    # names
    sorted_args = tuple(zip(
        *sorted(
            itertools.chain(kwargs.items(), args_as_kwargs.items()),
            key=lambda kv: sorted_arg_names.index(kv[0]),
        )
    ))

    if sorted_args:
        return sorted_args[1]
    else:
        return tuple()


TUPLE_TYPE_STR_RE = re.compile(r'^(tuple)(\[([1-9][0-9]*)?\])?$')


def get_tuple_type_str_parts(s: str) -> Optional[Tuple[str, Optional[str]]]:
    """
    Takes a JSON ABI type string.  For tuple type strings, returns the separated
    prefix and array dimension parts.  For all other strings, returns ``None``.
    """
    match = TUPLE_TYPE_STR_RE.match(s)

    if match is not None:
        tuple_prefix = match.group(1)
        tuple_dims = match.group(2)

        return tuple_prefix, tuple_dims

    return None


def _align_abi_input(arg_abi, arg):
    """
    Aligns the values of any mapping at any level of nesting in ``arg``
    according to the layout of the corresponding abi spec.
    """
    tuple_parts = get_tuple_type_str_parts(arg_abi['type'])

    if tuple_parts is None:
        # Arg is non-tuple.  Just return value.
        return arg

    tuple_prefix, tuple_dims = tuple_parts
    if tuple_dims is None:
        # Arg is non-list tuple.  Each sub arg in `arg` will be aligned
        # according to its corresponding abi.
        sub_abis = arg_abi['components']
    else:
        # Arg is list tuple.  A non-list version of its abi will be used to
        # align each element in `arg`.
        new_abi = copy.copy(arg_abi)
        new_abi['type'] = tuple_prefix

        sub_abis = itertools.repeat(new_abi)

    if isinstance(arg, abc.Mapping):
        # Arg is mapping.  Align values according to abi order.
        aligned_arg = tuple(arg[abi['name']] for abi in sub_abis)
    else:
        aligned_arg = arg

    if not is_list_like(aligned_arg):
        raise TypeError(
            'Expected non-string sequence for "{}" component type: got {}'.format(
                arg_abi['type'],
                aligned_arg,
            ),
        )

    return type(aligned_arg)(
        _align_abi_input(sub_abi, sub_arg)
        for sub_abi, sub_arg in zip(sub_abis, aligned_arg)
    )


def get_aligned_abi_inputs(abi, args):
    """
    Takes a function ABI (``abi``) and a sequence or mapping of args (``args``).
    Returns a list of type strings for the function's inputs and a list of
    arguments which have been aligned to the layout of those types.  The args
    contained in ``args`` may contain nested mappings or sequences corresponding
    to tuple-encoded values in ``abi``.
    """
    input_abis = abi.get('inputs', [])

    if isinstance(args, abc.Mapping):
        # `args` is mapping.  Align values according to abi order.
        args = tuple(args[abi['name']] for abi in input_abis)

    return (
        tuple(collapse_if_tuple(abi) for abi in input_abis),
        type(args)(
            _align_abi_input(abi, arg)
            for abi, arg in zip(input_abis, args)
        ),
    )


def get_constructor_abi(contract_abi):
    candidates = [
        abi for abi in contract_abi if abi['type'] == 'constructor'
    ]
    if len(candidates) == 1:
        return candidates[0]
    elif len(candidates) == 0:
        return None
    elif len(candidates) > 1:
        raise ValueError("Found multiple constructors.")


DYNAMIC_TYPES = ['bytes', 'string']

INT_SIZES = range(8, 257, 8)
BYTES_SIZES = range(1, 33)
UINT_TYPES = ['uint{0}'.format(i) for i in INT_SIZES]
INT_TYPES = ['int{0}'.format(i) for i in INT_SIZES]
BYTES_TYPES = ['bytes{0}'.format(i) for i in BYTES_SIZES] + ['bytes32.byte']

STATIC_TYPES = list(itertools.chain(
    ['address', 'bool'],
    UINT_TYPES,
    INT_TYPES,
    BYTES_TYPES,
))

BASE_TYPE_REGEX = '|'.join((
    _type + '(?![a-z0-9])'
    for _type
    in itertools.chain(STATIC_TYPES, DYNAMIC_TYPES)
))

SUB_TYPE_REGEX = (
    r'\['
    '[0-9]*'
    r'\]'
)

TYPE_REGEX = (
    '^'
    '(?:{base_type})'
    '(?:(?:{sub_type})*)?'
    '$'
).format(
    base_type=BASE_TYPE_REGEX,
    sub_type=SUB_TYPE_REGEX,
)


def is_recognized_type(abi_type):
    return bool(re.match(TYPE_REGEX, abi_type))


def is_bool_type(abi_type):
    return abi_type == 'bool'


def is_uint_type(abi_type):
    return abi_type in UINT_TYPES


def is_int_type(abi_type):
    return abi_type in INT_TYPES


def is_address_type(abi_type):
    return abi_type == 'address'


def is_bytes_type(abi_type):
    return abi_type in BYTES_TYPES + ['bytes']


def is_string_type(abi_type):
    return abi_type == 'string'


@curry
def is_length(target_length, value):
    return len(value) == target_length


def size_of_type(abi_type):
    """
    Returns size in bits of abi_type
    """
    if 'string' in abi_type:
        return None
    if 'byte' in abi_type:
        return None
    if '[' in abi_type:
        return None
    if abi_type == 'bool':
        return 8
    if abi_type == 'address':
        return 160
    return int(re.sub(r"\D", "", abi_type))


END_BRACKETS_OF_ARRAY_TYPE_REGEX = r"\[[^]]*\]$"


def sub_type_of_array_type(abi_type):
    if not is_array_type(abi_type):
        raise ValueError(
            "Cannot parse subtype of nonarray abi-type: {0}".format(abi_type)
        )

    return re.sub(END_BRACKETS_OF_ARRAY_TYPE_REGEX, '', abi_type, 1)


def length_of_array_type(abi_type):
    if not is_array_type(abi_type):
        raise ValueError(
            "Cannot parse length of nonarray abi-type: {0}".format(abi_type)
        )

    inner_brackets = re.search(END_BRACKETS_OF_ARRAY_TYPE_REGEX, abi_type).group(0).strip("[]")
    if not inner_brackets:
        return None
    else:
        return int(inner_brackets)


ARRAY_REGEX = (
    "^"
    "[a-zA-Z0-9_]+"
    "({sub_type})+"
    "$"
).format(sub_type=SUB_TYPE_REGEX)


def is_array_type(abi_type):
    return bool(re.match(ARRAY_REGEX, abi_type))


NAME_REGEX = (
    '[a-zA-Z_]'
    '[a-zA-Z0-9_]*'
)


ENUM_REGEX = (
    '^'
    '{lib_name}'
    r'\.'
    '{enum_name}'
    '$'
).format(lib_name=NAME_REGEX, enum_name=NAME_REGEX)


def is_probably_enum(abi_type):
    return bool(re.match(ENUM_REGEX, abi_type))


@to_tuple
def normalize_event_input_types(abi_args):
    for arg in abi_args:
        if is_recognized_type(arg['type']):
            yield arg
        elif is_probably_enum(arg['type']):
            yield {k: 'uint8' if k == 'type' else v for k, v in arg.items()}
        else:
            yield arg


def abi_to_signature(abi):
    function_signature = "{fn_name}({fn_input_types})".format(
        fn_name=abi['name'],
        fn_input_types=','.join([
            arg['type'] for arg in normalize_event_input_types(abi.get('inputs', []))
        ]),
    )
    return function_signature


########################################################
#
#  Conditionally modifying data, tagged with ABI Types
#
########################################################


@curry
def map_abi_data(normalizers, types, data):
    """
    This function will apply normalizers to your data, in the
    context of the relevant types. Each normalizer is in the format:

    def normalizer(datatype, data):
        # Conditionally modify data
        return (datatype, data)

    Where datatype is a valid ABI type string, like "uint".

    In case of an array, like "bool[2]", normalizer will receive `data`
    as an iterable of typed data, like `[("bool", True), ("bool", False)]`.

    Internals
    ---

    This is accomplished by:

    1. Decorating the data tree with types
    2. Recursively mapping each of the normalizers to the data
    3. Stripping the types back out of the tree
    """
    pipeline = itertools.chain(
        [abi_data_tree(types)],
        map(data_tree_map, normalizers),
        [partial(recursive_map, strip_abi_type)],
    )

    return pipe(data, *pipeline)


@curry
def abi_data_tree(types, data):
    """
    Decorate the data tree with pairs of (type, data). The pair tuple is actually an
    ABITypedData, but can be accessed as a tuple.

    As an example:

    >>> abi_data_tree(types=["bool[2]", "uint"], data=[[True, False], 0])
    [("bool[2]", [("bool", True), ("bool", False)]), ("uint256", 0)]
    """
    return [
        abi_sub_tree(data_type, data_value)
        for data_type, data_value
        in zip(types, data)
    ]


@curry
def data_tree_map(func, data_tree):
    """
    Map func to every ABITypedData element in the tree. func will
    receive two args: abi_type, and data
    """
    def map_to_typed_data(elements):
        if isinstance(elements, ABITypedData) and elements.abi_type is not None:
            return ABITypedData(func(*elements))
        else:
            return elements
    return recursive_map(map_to_typed_data, data_tree)


class ABITypedData(namedtuple('ABITypedData', 'abi_type, data')):
    """
    This class marks data as having a certain ABI-type.

    >>> a1 = ABITypedData(['address', addr1])
    >>> a2 = ABITypedData(['address', addr2])
    >>> addrs = ABITypedData(['address[]', [a1, a2]])

    You can access the fields using tuple() interface, or with
    attributes:

    >>> assert a1.abi_type == a1[0]
    >>> assert a1.data == a1[1]

    Unlike a typical `namedtuple`, you initialize with a single
    positional argument that is iterable, to match the init
    interface of all other relevant collections.
    """
    def __new__(cls, iterable):
        return super().__new__(cls, *iterable)


def abi_sub_tree(type_str_or_abi_type: Optional[Union[TypeStr, ABIType]],
                 data_value: Any) -> ABITypedData:
    if type_str_or_abi_type is None:
        return ABITypedData([None, data_value])

    if isinstance(type_str_or_abi_type, TypeStr):
        abi_type = parse(type_str_or_abi_type)
    else:
        abi_type = type_str_or_abi_type

    # In the two special cases below, we rebuild the given data structures with
    # annotated items
    if abi_type.is_array:
        # If type is array, determine item type and annotate all
        # items in iterable with that type
        item_type_str = abi_type.item_type.to_type_str()
        value_to_annotate = [
            abi_sub_tree(item_type_str, item_value)
            for item_value in data_value
        ]
    elif isinstance(abi_type, TupleType):
        # Otherwise, if type is tuple, determine component types and annotate
        # tuple components in iterable respectively with those types
        value_to_annotate = type(data_value)(
            abi_sub_tree(comp_type.to_type_str(), comp_value)
            for comp_type, comp_value in zip(abi_type.components, data_value)
        )
    else:
        value_to_annotate = data_value

    return ABITypedData([
        abi_type.to_type_str(),
        value_to_annotate,
    ])


def strip_abi_type(elements):
    if isinstance(elements, ABITypedData):
        return elements.data
    else:
        return elements
