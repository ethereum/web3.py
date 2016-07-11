from __future__ import absolute_import
import socket
import contextlib


@contextlib.contextmanager
def get_ipc_socket(ipc_path, timeout=0.1):
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect(ipc_path)
    sock.settimeout(timeout)

    yield sock

    sock.close()
