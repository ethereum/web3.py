# remove once web3 supports python>=3.8
# TypedDict was added to typing in 3.8
try:
    from typing import Literal, TypedDict  # type: ignore
except ImportError:
    from mypy_extensions import TypedDict  # noqa: F401
    from typing_extensions import Literal  # noqa: F401
