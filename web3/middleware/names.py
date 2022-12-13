from typing import (
    TYPE_CHECKING,
)

from web3._utils.normalizers import (
    abi_ens_resolver,
    async_abi_ens_resolver,
)
from web3._utils.rpc_abi import (
    RPC_ABIS,
    abi_request_formatters,
)
from web3.types import (
    Middleware,
)

from .formatting import (
    async_construct_formatting_middleware,
    construct_formatting_middleware,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401


def name_to_address_middleware(w3: "Web3") -> Middleware:
    normalizers = [
        abi_ens_resolver(w3),
    ]
    return construct_formatting_middleware(
        request_formatters=abi_request_formatters(normalizers, RPC_ABIS)
    )


async def async_name_to_address_middleware(async_w3: "Web3") -> Middleware:
    normalizers = [
        async_abi_ens_resolver(async_w3),
    ]

    _construct_name_to_address_middleware = await async_construct_formatting_middleware(
        request_formatters=abi_request_formatters(normalizers, RPC_ABIS)
    )

    return _construct_name_to_address_middleware
