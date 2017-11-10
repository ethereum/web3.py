from contextlib import contextmanager

from web3.utils.ens import (
    StaticENS,
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
    'eth_getLogs',
}


def address_getter(ens):
    if ens is None:

        def reject_name(val):
            if is_ens_name(val):
                raise ValueError("Could not look up name, because no web3 connection available")
            else:
                return val
        return reject_name
    else:
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


def name_to_address_middleware(ens):
    def middleware(make_request, web3):
        to_address = address_getter(ens)

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

        def wrapper(method, params):
            for applicable_methods, formatter in all_formatters:
                if method in applicable_methods:
                    formatted_params = formatter(params)
                    return make_request(method, formatted_params)
            # if no matching methods found, noop:
            return make_request(method, params)
        return wrapper
    return middleware


@contextmanager
def contract_ens_addresses(contract, name_addr_pairs):
    '''
    Use this context manager to temporarily resolve name/address pairs
    supplied as the argument. For example:

    with contract_ens_addresses(mycontract, [('resolve-as-1s.eth', '0x111...111')]):
        # any contract call or transaction in here would only resolve the above ENS pair
    '''

    ens = StaticENS(name_addr_pairs)
    old_ens, contract.ens = contract.ens, ens

    with web3_ens_addresses(contract.web3, name_addr_pairs):
        yield

    contract.ens = old_ens


@contextmanager
def web3_ens_addresses(w3, name_addr_pairs):
    '''
    Use this context manager to temporarily resolve name/address pairs
    supplied as the argument. For example:

    with web3_ens_addresses(w3, [('resolve-as-1s.eth', '0x111...111')]):
        # any web3 method call in here would only resolve the above ENS pair
    '''
    ens = StaticENS(name_addr_pairs)
    static_middleware = name_to_address_middleware(ens)
    old_middleware = w3.middleware_stack.replace('name_to_address', static_middleware)
    yield
    w3.middleware_stack.replace('name_to_address', old_middleware)
