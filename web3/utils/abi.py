import itertools
import re

from eth_abi.abi import (
    process_type,
)

from .crypto import sha3
from .string import (
    coerce_args_to_bytes,
    coerce_args_to_text,
    coerce_return_to_text,
)
from .formatting import (
    add_0x_prefix,
)
from .types import (
    is_array,
    is_string,
    is_integer,
    is_boolean,
)
from .address import (
    is_address,
)


def filter_by_type(_type, contract_abi):
    return [abi for abi in contract_abi if abi['type'] == _type]


def filter_by_name(name, contract_abi):
    return [abi for abi in contract_abi if abi['name'] == name]


def get_abi_input_types(abi):
    return [arg['type'] for arg in abi['inputs']]


def get_abi_output_types(abi):
    return [arg['type'] for arg in abi['outputs']]


def get_abi_input_names(abi):
    return [arg['name'] for arg in abi['inputs']]


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


def is_encodable(_type, value):
    try:
        base, sub, arrlist = _type
    except ValueError:
        base, sub, arrlist = process_type(_type)

    if arrlist:
        if not is_array(value):
            return False
        if arrlist[-1] and len(value) != arrlist[-1][0]:
            return False
        sub_type = (base, sub, arrlist[:-1])
        return all(is_encodable(sub_type, sub_value) for sub_value in value)
    elif base == 'bool':
        return is_boolean(value)
    elif base == 'uint':
        if not is_integer(value):
            return False
        exp = int(sub)
        if value < 0 or value >= 2**exp:
            return False
        return True
    elif base == 'int':
        if not is_integer(value):
            return False
        exp = int(sub)
        if value <= -1 * 2**(exp - 1) or value >= 2**(exp - 1):
            return False
        return True
    elif base == 'string':
        if not is_string(value):
            return False
        return True
    elif base == 'bytes':
        if not is_string(value):
            return False

        if not sub:
            return True

        max_length = int(sub)
        return len(value) <= max_length
    elif base == 'address':
        if not is_address(value):
            return False
        return True
    else:
        raise ValueError("Unsupported type")


def filter_by_encodability(args, kwargs, contract_abi):
    return [
        function_abi
        for function_abi
        in contract_abi
        if check_if_arguments_can_be_encoded(function_abi, args, kwargs)
    ]


@coerce_args_to_bytes
def check_if_arguments_can_be_encoded(function_abi, args, kwargs):
    try:
        arguments = merge_args_and_kwargs(function_abi, args, kwargs)
    except TypeError:
        return False

    if len(function_abi['inputs']) != len(arguments):
        return False

    types = get_abi_input_types(function_abi)

    return all(
        is_encodable(_type, arg)
        for _type, arg in zip(types, arguments)
    )


@coerce_args_to_text
def merge_args_and_kwargs(function_abi, args, kwargs):
    if len(args) + len(kwargs) != len(function_abi['inputs']):
        raise TypeError(
            "Incorrect argument count.  Expected '{0}'.  Got '{1}'".format(
                len(function_abi['inputs']),
                len(args) + len(kwargs),
            )
        )
    args_as_kwargs = {
        arg_abi['name']: arg
        for arg_abi, arg in zip(function_abi['inputs'], args)
    }
    duplicate_keys = set(args_as_kwargs).intersection(kwargs.keys())
    if duplicate_keys:
        raise TypeError(
            "{fn_name}() got multiple values for argument(s) '{dups}'".format(
                fn_name=function_abi['name'],
                dups=', '.join(duplicate_keys),
            )
        )

    sorted_arg_names = [arg_abi['name'] for arg_abi in function_abi['inputs']]

    unknown_kwargs = {key for key in kwargs.keys() if key not in sorted_arg_names}
    if unknown_kwargs:
        raise TypeError(
            "{fn_name}() got unexpected keyword argument(s) '{dups}'".format(
                fn_name=function_abi['name'],
                dups=', '.join(unknown_kwargs),
            )
        )

    sorted_args = list(zip(
        *sorted(
            itertools.chain(kwargs.items(), args_as_kwargs.items()),
            key=lambda kv: sorted_arg_names.index(kv[0])
        )
    ))
    if sorted_args:
        return sorted_args[1]
    else:
        return tuple()


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

STATIC_TYPES = list(itertools.chain(
    ['address', 'bool'],
    ['uint{0}'.format(i) for i in range(8, 257, 8)],
    ['int{0}'.format(i) for i in range(8, 257, 8)],
    ['bytes{0}'.format(i) for i in range(1, 33)],
))

BASE_TYPE_REGEX = '|'.join((
    _type + '(?![a-z0-9])'
    for _type
    in itertools.chain(STATIC_TYPES, DYNAMIC_TYPES)
))

SUB_TYPE_REGEX = (
    '\['
    '[0-9]*'
    '\]'
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


NAME_REGEX = (
    '[a-zA-Z_]'
    '[a-zA-Z0-9_]*'
)


ENUM_REGEX = (
    '^'
    '{lib_name}'
    '\.'
    '{enum_name}'
    '$'
).format(lib_name=NAME_REGEX, enum_name=NAME_REGEX)


def is_probably_enum(abi_type):
    return bool(re.match(ENUM_REGEX, abi_type))


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


def function_abi_to_4byte_selector(function_abi):
    function_signature = abi_to_signature(function_abi)
    return add_0x_prefix(sha3(function_signature)[:8])


def event_abi_to_log_topic(event_abi):
    event_signature = abi_to_signature(event_abi)
    return add_0x_prefix(sha3(event_signature))


@coerce_return_to_text
def normalize_return_type(data_type, data_value):
    try:
        base, sub, arrlist = data_type
    except ValueError:
        base, sub, arrlist = process_type(data_type)

    if arrlist:
        sub_type = (base, sub, arrlist[:-1])
        return [normalize_return_type(sub_type, sub_value) for sub_value in data_value]
    elif base == 'address':
        return add_0x_prefix(data_value)
    else:
        return data_value
