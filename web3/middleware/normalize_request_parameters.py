from web3._utils.method_formatters import (
    METHOD_NORMALIZERS,
)

from .formatting import (
    FormattingMiddlewareBuilder,
)

request_parameter_normalizer = FormattingMiddlewareBuilder.build(
    request_formatters=METHOD_NORMALIZERS,
)
