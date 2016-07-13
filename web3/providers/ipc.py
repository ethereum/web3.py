from __future__ import absolute_import

import socket
import sys
import os
import threading
import contextlib

from .base import BaseProvider


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
            "ethereum",
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


class IPCProvider(BaseProvider):
    def __init__(self, ipc_path=None, testnet=False, *args, **kwargs):
        if ipc_path is None:
            self.ipc_path = get_default_ipc_path(testnet)
        else:
            self.ipc_path = ipc_path

        self._lock = threading.Lock()
        super(IPCProvider, self).__init__(*args, **kwargs)

    def make_request(self, method, params):
        request = self.encode_rpc_request(method, params)

        self._lock.acquire()

        try:
            with get_ipc_socket(self.ipc_path) as sock:
                sock.sendall(request)
                response_raw = b""

                while True:
                    try:
                        response_raw += sock.recv(4096)
                    except socket.timeout:
                        if response_raw != b"":
                            break

                    if response_raw == b"":
                        continue

                    break
                else:
                    raise ValueError("No JSON returned by socket")
        finally:
            self._lock.release()

        return response_raw
