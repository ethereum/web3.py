import sys


if sys.version_info.major == 2:
    from .compat_py2 import (
        urlparse,
        urlunparse,
        Generator,
    )
else:
    from .compat_py3 import (  # noqa: #401
        urlparse,
        urlunparse,
        Generator,
    )
