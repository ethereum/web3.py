import os


if 'WEB3_ASYNC_GEVENT' in os.environ:
    from .gevent_async import (  # noqa
        Timeout,
        sleep,
        socket,
        threading,
        make_server,
    )
else:
    from .stdlib_async import (  # noqa
        Timeout,
        sleep,
        socket,
        threading,
        make_server,
    )
