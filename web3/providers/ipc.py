import os
import socket
import sys
import threading

from web3.utils.threads import (
    Timeout,
)

from .base import (
    JSONBaseProvider,
)

try:
    from json import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError


def get_ipc_socket(ipc_path, timeout=0.1):
    if sys.platform == 'win32':
        # On Windows named pipe is used. Simulate socket with it.
        from web3.utils.windows import NamedPipe

        return NamedPipe(ipc_path)
    else:
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.connect(ipc_path)
        sock.settimeout(timeout)
        return sock


class PersistantSocket:
    sock = None

    def __init__(self, ipc_path):
        self.ipc_path = ipc_path

    def __enter__(self):
        if not self.ipc_path:
            raise FileNotFoundError("cannot connect to IPC socket at path: %r" % self.ipc_path)

        if not self.sock:
            self.sock = self._open()
        return self.sock

    def __exit__(self, exc_type, exc_value, traceback):
        # only close the socket if there was an error
        if exc_value is not None:
            try:
                self.sock.close()
            except Exception:
                pass
            self.sock = None

    def _open(self):
        return get_ipc_socket(self.ipc_path)

    def reset(self):
        self.sock.close()
        self.sock = self._open()
        return self.sock


def get_default_ipc_path(testnet=False):
    if testnet:
        testnet = "testnet"
    else:
        testnet = ""

    if sys.platform == 'darwin':
        ipc_path = os.path.expanduser(os.path.join(
            "~",
            "Library",
            "Ethereum",
            testnet,
            "geth.ipc"
        ))
        if os.path.exists(ipc_path):
            return ipc_path

        ipc_path = os.path.expanduser(os.path.join(
            "~",
            "Library",
            "Application Support",
            "io.parity.ethereum",
            "jsonrpc.ipc"
        ))
        if os.path.exists(ipc_path):
            return ipc_path

    elif sys.platform.startswith('linux'):
        ipc_path = os.path.expanduser(os.path.join(
            "~",
            ".ethereum",
            testnet,
            "geth.ipc"
        ))
        if os.path.exists(ipc_path):
            return ipc_path

        ipc_path = os.path.expanduser(os.path.join(
            "~",
            ".local",
            "share",
            "io.parity.ethereum",
            "jsonrpc.ipc"
        ))
        if os.path.exists(ipc_path):
            return ipc_path

    elif sys.platform == 'win32':
        ipc_path = os.path.join(
            "\\\\",
            ".",
            "pipe",
            "geth.ipc"
        )
        if os.path.exists(ipc_path):
            return ipc_path

        ipc_path = os.path.join(
            "\\\\",
            ".",
            "pipe",
            "jsonrpc.ipc"
        )
        if os.path.exists(ipc_path):
            return ipc_path

    else:
        raise ValueError(
            "Unsupported platform '{0}'.  Only darwin/linux2/win32 are "
            "supported.  You must specify the ipc_path".format(sys.platform)
        )


class IPCProvider(JSONBaseProvider):
    _socket = None

    def __init__(self, ipc_path=None, testnet=False, timeout=10, *args, **kwargs):
        if ipc_path is None:
            self.ipc_path = get_default_ipc_path(testnet)
        else:
            self.ipc_path = ipc_path

        self.timeout = timeout
        self._lock = threading.Lock()
        self._socket = PersistantSocket(self.ipc_path)
        super().__init__(*args, **kwargs)

    def make_request(self, method, params):
        request = self.encode_rpc_request(method, params)

        with self._lock, self._socket as sock:
            try:
                sock.sendall(request)
            except BrokenPipeError:
                # one extra attempt, then give up
                sock = self._socket.reset()
                sock.sendall(request)

            raw_response = b""
            with Timeout(self.timeout) as timeout:
                while True:
                    try:
                        raw_response += sock.recv(4096)
                    except socket.timeout:
                        timeout.sleep(0)
                        continue
                    if raw_response == b"":
                        timeout.sleep(0)
                    else:
                        try:
                            response = self.decode_rpc_response(raw_response)
                        except JSONDecodeError:
                            timeout.sleep(0)
                            continue
                        else:
                            return response
