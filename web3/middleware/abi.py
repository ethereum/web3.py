from web3.utils.normalizers import (
    abi_address_to_hex,
    abi_bytes_to_hex,
    abi_int_to_hex,
    abi_string_to_hex,
)
from web3.utils.rpc_abi import (
    RPC_ABIS,
    abi_request_formatters,
)

from .formatting import (
    construct_formatting_middleware,
)

STANDARD_NORMALIZERS = [
    abi_bytes_to_hex,
    abi_int_to_hex,
    abi_string_to_hex,
    abi_address_to_hex,
]


abi_middleware = construct_formatting_middleware(
    request_formatters=abi_request_formatters(STANDARD_NORMALIZERS, RPC_ABIS)
)
