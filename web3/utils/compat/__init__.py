import os


def get_threading_backend():
    if 'WEB3_THREADING_BACKEND' in os.environ:
        return os.environ['WEB3_THREADING_BACKEND']
    elif 'THREADING_BACKEND' in os.environ:
        return os.environ['THREADING_BACKEND']
    else:
        return 'stdlib'


THREADING_BACKEND = get_threading_backend()


if THREADING_BACKEND == 'stdlib':
    from .compat_requests import (  # noqa: F401
        make_post_request,
    )
else:
    raise ValueError("Unsupported threading backend.  Must be 'stdlib'")
