from web3._utils.method_formatters import (
    PYTHONIC_REQUEST_FORMATTERS,
    PYTHONIC_RESULT_FORMATTERS,
)
from web3.middleware.formatting import (
    construct_formatting_middleware,
)

pythonic_middleware = construct_formatting_middleware(
    request_formatters=PYTHONIC_REQUEST_FORMATTERS,
    result_formatters=PYTHONIC_RESULT_FORMATTERS,
)
