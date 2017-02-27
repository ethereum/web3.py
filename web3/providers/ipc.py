from __future__ import absolute_import

import sys
import os
import contextlib
import json

try:
    from json import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError

from eth_utils import (
    force_text,
)

from web3.utils.compat import (
    Timeout,
    threading,
    socket,
)

from .base import JSONBaseProvider


@contextlib.contextmanager
def get_ipc_socket(ipc_path, timeout=0.1):
    # is_linux = sys.platform.startswith('linux')
    # is_darwin = sys.platform == 'darwin'
    is_win32 = sys.platform == 'win32'
    if is_win32:
        import win32file
        sock = win32file.CreateFile(ipc_path,
                                    win32file.win32file.GENERIC_READ | win32file.GENERIC_WRITE,
                                    0, None,
                                    win32file.OPEN_EXISTING, 0, None)
        def recv(self, max_length):
            data = win32file.ReadFile(self, max_length)
            if data[0] == 0:
                return data[1]
            return ""
        sock.recv = recv
        def sendall(data):
            return win32file.WriteFile(self, data)
        sock.sendall = sendall
        yield sock
        sock
    else:
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
        return "\\\\.\\pipe\\geth.ipc",
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

        self._lock = threading.Lock()
        super(IPCProvider, self).__init__(*args, **kwargs)

    def make_request(self, method, params):
        request = self.encode_rpc_request(method, params)

        self._lock.acquire()

        try:
            with get_ipc_socket(self.ipc_path) as sock:
                sock.sendall(request)
                # TODO: use a BytesIO object here
                response_raw = b""

                with Timeout(10) as timeout:
                    while True:
                        try:
                            response_raw += sock.recv(4096)
                        except socket.timeout:
                            timeout.sleep(0)
                            continue

                        if response_raw == b"":
                            timeout.sleep(0)
                        else:
                            try:
                                json.loads(force_text(response_raw))
                            except JSONDecodeError:
                                timeout.sleep(0)
                                continue
                            else:
                                break
        finally:
            self._lock.release()

        return response_raw
