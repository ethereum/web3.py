from web3._utils.method_formatters import (
    ABI_REQUEST_FORMATTERS,
)

from .formatting import (
    construct_formatting_middleware,
)

abi_middleware = construct_formatting_middleware(
    request_formatters=ABI_REQUEST_FORMATTERS
)
