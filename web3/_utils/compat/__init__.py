import sys

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

if sys.version_info >= (3, 11):
    from typing import (
        Unpack,
    )
else:
    from typing_extensions import (  # noqa: F401
        Unpack,
    )
