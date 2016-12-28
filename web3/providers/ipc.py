from __future__ import absolute_import

import sys
import os
import contextlib
import json

try:
    from json import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError

import gevent
from gevent import socket
from gevent.threading import Lock

from web3.utils.string import (
    force_text,
)

from .base import JSONBaseProvider


@contextlib.contextmanager
def get_ipc_socket(ipc_path, timeout=0.1):
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect(ipc_path)
    sock.settimeout(timeout)

    yield sock

    sock.close()


def get_default_ipc_path(testnet=False):
    if testnet:
        testnet = "testnet"
    else:
        testnet = ""

    if sys.platform == 'darwin':
        return os.path.expanduser(os.path.join(
            "~",
            "Library",
            "Ethereum",
            testnet,
            "geth.ipc",
        ))
    elif sys.platform.startswith('linux'):
        return os.path.expanduser(os.path.join(
            "~",
            ".ethereum",
            testnet,
            "geth.ipc",
        ))
    elif sys.platform == 'win32':
        return os.path.expanduser(os.path.join(
            "~",
            "AppData",
            "Roaming",
            "Ethereum",
        ))
    else:
        raise ValueError(
            "Unsupported platform '{0}'.  Only darwin/linux2/win32 are "
            "supported.  You must specify the ipc_path".format(sys.platform)
        )


class IPCProvider(JSONBaseProvider):
    def __init__(self, ipc_path=None, testnet=False, *args, **kwargs):
        if ipc_path is None:
            self.ipc_path = get_default_ipc_path(testnet)
        else:
            self.ipc_path = ipc_path

        self._lock = Lock()
        super(IPCProvider, self).__init__(*args, **kwargs)

    def make_request(self, method, params):
        request = self.encode_rpc_request(method, params)

        self._lock.acquire()

        try:
            with get_ipc_socket(self.ipc_path) as sock:
                sock.sendall(request)
                response_raw = b""

                with gevent.Timeout(10):
                    while True:
                        try:
                            response_raw += sock.recv(4096)
                        except socket.timeout:
                            gevent.sleep(0)
                            continue

                        if response_raw == b"":
                            gevent.sleep(0)
                        else:
                            try:
                                json.loads(force_text(response_raw))
                            except JSONDecodeError:
                                gevent.sleep(0)
                                continue
                            else:
                                break
        finally:
            self._lock.release()

        return response_raw
