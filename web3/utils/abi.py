import itertools

from eth_abi.abi import (
    process_type,
    encode_single,
)

from .encoding import encode_hex
from .crypto import sha3
from .string import (
    coerce_args_to_bytes,
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


def filter_by_argument_count(arguments, contract_abi):
    return [
        abi
        for abi
        in contract_abi
        if len(abi['inputs']) == len(arguments)
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


def filter_by_encodability(arguments, contract_abi):
    return [
        abi
        for abi
        in contract_abi
        if check_if_arguments_can_be_encoded(get_abi_input_types(abi), arguments)
    ]


@coerce_args_to_bytes
def check_if_arguments_can_be_encoded(types, arguments):
    if len(types) != len(arguments):
        raise ValueError("Length mismatch between types and arguments")
    return all(
        is_encodable(_type, arg)
        for _type, arg in zip(types, arguments)
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


def abi_to_signature(function_abi):
    function_signature = "{fn_name}({fn_input_types})".format(
        fn_name=function_abi['name'],
        fn_input_types=','.join([
            arg['type'] for arg in function_abi.get('inputs', [])
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
def construct_event_topic_set(event_abi, arguments=None):
    if arguments is None:
        arguments = {}
    if isinstance(arguments, (list, tuple)):
        if len(arguments) != len(event_abi['inputs']):
            raise ValueError(
                "When passing an argument list, the number of arguments must "
                "match the event constructor."
            )
        arguments = {
            arg['name']: [arg_value]
            for arg, arg_value
            in zip(event_abi['inputs'], arguments)
        }

    normalized_args = {
        key: value if is_array(value) else [value]
        for key, value in arguments.items()
    }

    event_topic = event_abi_to_log_topic(event_abi)
    indexed_args = get_indexed_event_inputs(event_abi)
    zipped_abi_and_args = [
        (arg, normalized_args.get(arg['name'], [None]))
        for arg in indexed_args
    ]
    encoded_args = [
        [
            None if option is None else encode_hex(encode_single(arg['type'], option))
            for option in arg_options]
        for arg, arg_options in zipped_abi_and_args
    ]

    topics = [
        [event_topic] + list(permutation)
        if any(value is not None for value in permutation)
        else [event_topic]
        for permutation in itertools.product(*encoded_args)
    ]
    return topics


@coerce_return_to_text
def construct_event_data_set(event_abi, arguments=None):
    if arguments is None:
        arguments = {}
    if isinstance(arguments, (list, tuple)):
        if len(arguments) != len(event_abi['inputs']):
            raise ValueError(
                "When passing an argument list, the number of arguments must "
                "match the event constructor."
            )
        arguments = {
            arg['name']: [arg_value]
            for arg, arg_value
            in zip(event_abi['inputs'], arguments)
        }

    normalized_args = {
        key: value if is_array(value) else [value]
        for key, value in arguments.items()
    }

    indexed_args = exclude_indexed_event_inputs(event_abi)
    zipped_abi_and_args = [
        (arg, normalized_args.get(arg['name'], [None]))
        for arg in indexed_args
    ]
    encoded_args = [
        [
            None if option is None else encode_hex(encode_single(arg['type'], option))
            for option in arg_options]
        for arg, arg_options in zipped_abi_and_args
    ]

    topics = [
        list(permutation)
        if any(value is not None for value in permutation)
        else []
        for permutation in itertools.product(*encoded_args)
    ]
    return topics
