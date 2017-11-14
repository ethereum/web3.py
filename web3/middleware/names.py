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


def name_to_address_middleware(w3):
    normalizers = [
        abi_ens_resolver(w3),
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
    w3 = contract.web3
    original_ens = w3.ens
    w3.ens = StaticENS(name_addr_pairs)
    yield
    w3.ens = original_ens
