from ens import ENS

from web3.utils.ens import (
    is_ens_name,
    validate_name_has_address,
)

from web3.utils.formatters import (
    apply_formatter_at_index,
    apply_formatters_to_dict,
)


TRANSACTION_METHODS = {
    'eth_call',
    'eth_estimateGas',
    'eth_sendTransaction',
    'personal_sendTransaction',
}

ZERO_INDEX_ADDRESSES = {
    'eth_getBalance',
    'eth_getStorageAt',
    'eth_getTransactionCount',
    'eth_getCode',
    'eth_sign',
}

ADDRESS_KEY_AT_0 = {
    'eth_newFilter',
}


def address_getter(web3):
    if web3 is None:

        def reject_name(val):
            if is_ens_name(val):
                raise ValueError("Could not look up name, because no web3 connection available")
            else:
                return val
        return reject_name
    else:
        ens = ENS.fromWeb3(web3)

        def to_address(name):
            if is_ens_name(name):
                address = validate_name_has_address(ens, name)
            else:
                address = name
            return address
        return to_address


def transaction_name_formatter(to_address):
    transaction_formatter_fields = {
        'from': to_address,
        'to': to_address,
    }
    return apply_formatters_to_dict(transaction_formatter_fields)


def filter_formatter(to_address):
    filter_formatter_fields = {
        'address': to_address,
    }
    return apply_formatters_to_dict(filter_formatter_fields)


def name_to_address_middleware(make_request, web3):
    to_address = address_getter(web3)

    transaction_formatter = apply_formatter_at_index(
        transaction_name_formatter(to_address),
        0,
    )
    index_0_formatter = apply_formatter_at_index(to_address, 0)
    address_key_formatter = apply_formatter_at_index(
        filter_formatter(to_address),
        0,
    )

    all_formatters = (
        (TRANSACTION_METHODS, transaction_formatter),
        (ZERO_INDEX_ADDRESSES, index_0_formatter),
        (ADDRESS_KEY_AT_0, address_key_formatter),
    )

    def middleware(method, params):
        for applicable_methods, formatter in all_formatters:
            if method in applicable_methods:
                formatted_params = formatter(params)
                return make_request(method, formatted_params)
        # if no matching methods found, noop:
        return make_request(method, params)
    return middleware
