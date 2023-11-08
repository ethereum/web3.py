from web3._utils.method_formatters import (
    ABI_REQUEST_FORMATTERS,
)
from web3.middleware.formatting import (
    FormattingMiddleware,
)


abi_middleware = FormattingMiddleware(request_formatters=ABI_REQUEST_FORMATTERS)
