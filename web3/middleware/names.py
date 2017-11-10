from contextlib import contextmanager

from web3.utils.ens import (
    StaticENS,
)

from web3.utils.normalizers import (
    abi_ens_resolver,
)
from web3.utils.rpc_abi import (
    RPC_ABIS,
    abi_request_formatters,
)

from .formatting import (
    construct_formatting_middleware,
)


def name_to_address_middleware(ens):
    normalizers = [
        abi_ens_resolver(ens),
    ]
    return construct_formatting_middleware(
        request_formatters=abi_request_formatters(normalizers, RPC_ABIS)
    )


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
