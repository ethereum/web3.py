from web3._utils.method_formatters import (
    METHOD_NORMALIZERS,
)

from .formatting import (
    FormattingMiddleware,
)

request_parameter_normalizer = FormattingMiddleware.build_middleware(
    request_formatters=METHOD_NORMALIZERS,
)
