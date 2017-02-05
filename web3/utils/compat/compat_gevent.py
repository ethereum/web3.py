import collections

import gevent
from gevent.pywsgi import (  # noqa: F401
    WSGIServer,
)
from gevent import (  # noqa: F401
    subprocess,
    socket,
    threading,
)

import pylru

from geventhttpclient import HTTPClient

from web3.utils.six import urlparse


_client_cache = pylru.lrucache(8)


sleep = gevent.sleep
spawn = gevent.spawn
GreenletThread = gevent.Greenlet


class Timeout(gevent.Timeout):
    def check(self):
        pass

    def sleep(self, seconds):
        gevent.sleep(seconds)


def make_server(host, port, application, *args, **kwargs):
    server = WSGIServer((host, port), application, *args, **kwargs)
    return server


def _get_client(host, port, **kwargs):
    ordered_kwargs = collections.OrderedDict(sorted(kwargs.items()))
    cache_key = '{0}:{1}:{2}'.format(
        host,
        port,
        ':'.join((
            "{0}={1}".format(str(key), str(value))
            for key, value in ordered_kwargs.items()
        ))
    )
    if cache_key not in _client_cache:
        _client_cache[cache_key] = HTTPClient(host, port, **kwargs)
    return _client_cache[cache_key]


def make_post_request(endpoint_uri, data, **kwargs):
    url_parts = urlparse(endpoint_uri)

    host, _, port = url_parts.netloc.partition(':')

    if not port:
        if url_parts.scheme == 'http':
            port = 80
        elif url_parts.scheme == 'https':
            port = 443
        else:
            raise ValueError("Unsupported scheme: '{0}'".format(url_parts.scheme))

    kwargs.setdefault('ssl', url_parts.scheme == 'https')
    kwargs.setdefault('connection_timeout', 10)
    kwargs.setdefault('network_timeout', 10)
    kwargs.setdefault('concurrency', 10)

    client = _get_client(host, port, **kwargs)
    response = client.post(url_parts.path, body=data)
    response_body = response.read()

    return response_body
