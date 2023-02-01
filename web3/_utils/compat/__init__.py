import sys

# remove once web3 supports python>=3.8
# Types was added to typing in 3.8
if sys.version_info >= (3, 8):
    from typing import (
        Literal,
        Protocol,
        TypedDict,
    )
else:
    from typing_extensions import (  # noqa: F401
        Literal,
        Protocol,
        TypedDict,
    )
