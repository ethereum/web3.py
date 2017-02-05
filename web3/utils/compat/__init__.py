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
    from .compat_stdlib import (
        Timeout,
        sleep,
        socket,
        threading,
        make_server,
        GreenletThread,
        spawn,
        subprocess,
    )
    from .compat_requests import (
        make_post_request,
    )
elif THREADING_BACKEND == 'gevent':
    from .compat_gevent import (  # noqa: F401
        Timeout,
        sleep,
        socket,
        threading,
        make_server,
        GreenletThread,
        spawn,
        subprocess,
        make_post_request,
    )
else:
    raise ValueError("Unsupported threading backend.  Must be one of 'gevent' or 'stdlib'")
