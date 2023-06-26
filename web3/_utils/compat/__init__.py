# Changelog for `typing_extensions` for checking which types were added when
# https://github.com/python/typing_extensions/blob/main/CHANGELOG.md

# Note that we do not need to explicitly check for python version here,
# because `typing_extensions` will do it for us and either import from `typing`
# or use the back-ported version of the type.

# Once web3 supports >= the noted python version, the type may be directly
# imported from `typing`

from typing_extensions import (  # noqa: F401
    Literal,  # py38
    Protocol,  # py38
    TypedDict,  # py38
    Self,  # py311
)
