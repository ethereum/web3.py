import os


if 'WEB3_ASYNC_GEVENT' in os.environ:
    from .gevent_http import (  # noqa: F401
        make_post_request,
    )
else:
    from .requests_http import (  # noqa: F401
        make_post_request,
    )
