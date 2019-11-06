# remove once web3 supports python>=3.8
# TypedDict was added to typing in 3.8
try:
    from typing import TypedDict  # type: ignore
except ImportError:
    from mypy_extensions import TypedDict  # noqa: F401
