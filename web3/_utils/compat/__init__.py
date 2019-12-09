# remove once web3 supports python>=3.8
# TypedDict was added to typing in 3.8
try:
    from typing import Literal, Protocol, TypedDict  # type: ignore
except ImportError:
    from typing_extensions import Literal, Protocol, TypedDict  # type: ignore # noqa: F401
