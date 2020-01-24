from typing import (
    TYPE_CHECKING,
)

from web3._utils.normalizers import (
    abi_address_to_hex,
    abi_ens_resolver,
)
from web3._utils.rpc_abi import (
    RPC_ABIS,
    abi_request_formatters,
)
from web3.types import (
    Middleware,
)

from .formatting import (
    construct_formatting_middleware,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401


def name_to_address_middleware(w3: "Web3") -> Middleware:
    normalizers = [
        abi_ens_resolver(w3),
        # abi_address_to_hex validates the address,
        # so it needs to be called after the ens name is resolved
        # this fixes the name middleware tests, but breaks sign and send raw middleware. need to dig in to find out why that's the case.
        abi_address_to_hex,
    ]
    return construct_formatting_middleware(
        request_formatters=abi_request_formatters(normalizers, RPC_ABIS)
    )
