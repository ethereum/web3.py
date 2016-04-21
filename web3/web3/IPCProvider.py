import socket
from web3.web3.provider import Provider
import sys
import os

def getDefaultIPCPath():
    if sys.platform == 'darwin':
        ipc_path = os.path.expanduser("~/Library/Ethereum/geth.ipc")
    elif sys.platform == 'linux2':
        ipc_path = os.path.expanduser("~/.ethereum/geth.ipc")
    elif sys.platform == 'win32':
        ipc_path = os.path.expanduser("\\~\\AppData\\Roaming\\Ethereum")
    else:
        raise ValueError(
            "Unsupported platform.  Only darwin/linux2/win32 are "
            "supported.  You must specify the ipc_path"
        )
    return ipc_path


class IPCProvider(Provider):

    def __init__(self, ipcpath=None):
        if path is None:
            self.ipcpath = getDefaultIPCPath()
        else:
            self.ipcpath = path

        self.socket = self.getSocket()

        super(IPCProvider, self).__init__()

    def getSocket(self):
        socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        socket.connect(self.ipcpath)
        socket.settimeout(2)
        return socket

    def _make_request(self, request):
        for _ in range(3):
            self.socket.sendall(request)

            response_raw = ""
            while True:
                try:
                    response_raw += self.socket.recv(4096)
                except socket.timeout:
                    break

            if response_raw == "":
                self.socket.close()
                self.socket = self.getSocket()
                continue

            break
        else:
            raise ValueError("No JSON returned by socket")

        return response_raw