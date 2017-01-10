import os


if 'WEB3_ASYNC_GEVENT' in os.environ:
    from .requests_http import (
        make_post_request,
    )
else:
    from .gevent_http import (  # noqa: F401
        make_post_request,
    )
