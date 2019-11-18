from web3._utils.method_formatters import (
    METHOD_NORMALIZERS,
)

from .formatting import (
    construct_formatting_middleware,
)

request_parameter_normalizer = construct_formatting_middleware(
    request_formatters=METHOD_NORMALIZERS,
)
