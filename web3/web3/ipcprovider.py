import socket
from web3.web3.provider import Provider
import sys
import os
import six


def getDefaultIPCPath(testnet=False):
    if testnet:
        testnet = "testnet/"
    else:
        testnet = ""

    if sys.platform == 'darwin':
        ipc_path = os.path.expanduser("~/Library/Ethereum/"+testnet+"geth.ipc")
    elif sys.platform.startswith('linux'):
        ipc_path = os.path.expanduser("~/.ethereum/"+testnet+"geth.ipc")
    elif sys.platform == 'win32':
        ipc_path = os.path.expanduser("\\~\\AppData\\Roaming\\Ethereum")
    else:
        raise ValueError(
            "Unsupported platform '{0}'.  Only darwin/linux2/win32 are "
            "supported.  You must specify the ipc_path".format(sys.platform)
        )
    return ipc_path


class IPCProvider(Provider):

    def __init__(self, ipcpath=None, testnet=False, *args, **kwargs):
        if ipcpath is None:
            self.ipcpath = getDefaultIPCPath(testnet)
        else:
            self.ipcpath = ipcpath

        self.socket = self.getSocket()

        super(IPCProvider, self).__init__(*args, **kwargs)

    def getSocket(self):
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.connect(self.ipcpath)
        sock.settimeout(0.001)
        return sock

    def _make_request(self, request):

        for _ in range(3):
            self.socket.sendall(request)
            response_raw = u""
            while True:
                try:
                    response_raw += self.socket.recv(4096).decode()
                except socket.timeout:
                    if response_raw != "":
                        break

            if response_raw == "":
                self.socket.close()
                self.socket = self.getSocket()
                continue

            break
        else:
            raise ValueError("No JSON returned by socket")
        return response_raw
