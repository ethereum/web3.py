import gevent
from gevent.pywsgi import (  # noqa: F401
    WSGIServer,
)
from gevent import (  # noqa: F401
    subprocess,
    socket,
    threading,
)


sleep = gevent.sleep
spawn = gevent.spawn
GreenletThread = gevent.Greenlet


class Timeout(gevent.Timeout):
    def check(self):
        pass


def make_server(host, port, application, *args, **kwargs):
    server = WSGIServer((host, port), application, *args, **kwargs)
    return server
