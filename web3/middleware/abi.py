from web3._utils.method_formatters import (
    ABI_REQUEST_FORMATTERS,
)
from web3.middleware.formatting import (
    FormattingMiddlewareBuilder,
)

abi_middleware = FormattingMiddlewareBuilder.build(
    request_formatters=ABI_REQUEST_FORMATTERS
)
