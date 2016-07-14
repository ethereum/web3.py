from eth_abi import (
    encode_abi,
)
from eth_abi.exceptions import (
    EncodingError,
)


def filter_by_type(_type, contract_abi):
    return [abi for abi in contract_abi if abi['type'] == _type]


def filter_by_name(name, contract_abi):
    return [abi for abi in contract_abi if abi['name'] == name]


def get_abi_types(abi):
    return [input['type'] for input in abi['inputs']]


def filter_by_encodability(arguments, contract_abi):
    return [
        abi
        for abi
        in contract_abi
        if check_if_arguments_can_be_encoded(get_abi_types(abi), arguments)
    ]


def check_if_arguments_can_be_encoded(types, arguments):
    try:
        encode_abi(types, arguments)
    except EncodingError:
        return False
    else:
        return True
