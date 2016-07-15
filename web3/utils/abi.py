from eth_abi.abi import (
    process_type,
)

from .crypto import sha3
from .string import coerce_args_to_bytes
from .formatting import (
    add_0x_prefix,
)
from .types import (
    is_array,
    is_string,
    is_integer,
    is_boolean,
)


def filter_by_type(_type, contract_abi):
    return [abi for abi in contract_abi if abi['type'] == _type]


def filter_by_name(name, contract_abi):
    return [abi for abi in contract_abi if abi['name'] == name]


def get_abi_input_types(abi):
    return [arg['type'] for arg in abi['inputs']]


def get_abi_output_types(abi):
    return [arg['type'] for arg in abi['outputs']]


def filter_by_argument_count(arguments, contract_abi):
    return [
        abi
        for abi
        in contract_abi
        if len(abi['inputs']) == len(arguments)
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
    elif base == 'bytes':
        if not is_string(value):
            return False

        if not sub:
            return True

        max_length = int(sub)
        return len(value) <= max_length
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


def abi_to_4byte_function_selector(function_abi):
    function_signature = "{fn_name}({fn_input_types})".format(
        fn_name=function_abi['name'],
        fn_input_types=','.join([
            arg['type'] for arg in function_abi.get('inputs', [])
        ]),
    )
    return function_signature


def function_abi_to_4byte_selector(function_abi):
    function_signature = abi_to_4byte_function_selector(function_abi)
    return add_0x_prefix(sha3(function_signature)[:8])
