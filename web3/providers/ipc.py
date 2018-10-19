import asyncio
import logging
import os
import pathlib
import sys

from web3._utils.threads import (
    Timeout,
)

from .base import (
    JSONBaseProvider,
)

try:
    from json import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError

DEFAULT_LIMIT = 2 ** 16


if sys.platform == 'win32':
    asyncio.set_event_loop(asyncio.ProactorEventLoop())


async def open_named_pipe_connection(
        path=None,
        *,
        loop=None,
        limit=DEFAULT_LIMIT,
        **kwargs):
    """Connect to a server using a Win32 named pipe."""
    if sys.platform != 'win32':
        raise TypeError("open_named_pipe_connection is a windows only method")

    loop = loop or asyncio.get_event_loop()
    if not isinstance(loop, (asyncio.ProactorEventLoop,)):
        raise TypeError(
            "Using the IPCProvider on windows requires an asyncio.ProactorEventLoop. "
            "try: asyncio.set_event_loop(asyncio.ProactorEventLoop()).")

    reader = asyncio.StreamReader(limit=limit, loop=loop)
    protocol = asyncio.StreamReaderProtocol(reader, loop=loop)
    #  create_pipe_connection is part of the windows event loop using IOCP
    transport, _ = await loop.create_pipe_connection(
        lambda: protocol, path, **kwargs
    )
    writer = asyncio.StreamWriter(transport, protocol, reader, loop)
    return reader, writer


def get_ipc_connection(ipc_path):
    if sys.platform == 'win32':
        return open_named_pipe_connection(ipc_path)
    else:
        return asyncio.open_unix_connection(ipc_path)


class IPCConnection:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    async def send(self, data):
        self.writer.write(data)
        await self.writer.drain()

    async def read(self, n=-1):
        return await self.reader.read(n)

    def close(self):
        self.writer.close()


class PersistantSocket:
    conn = None

    def __init__(self, ipc_path):
        self.ipc_path = ipc_path

    async def __aenter__(self):
        if not self.ipc_path:
            raise FileNotFoundError("cannot connect to IPC socket at path: %r" % self.ipc_path)

        if not self.conn:
            self.conn = IPCConnection(*(await self._open()))
        return self.conn

    async def __aexit__(self, exc_type, exc_value, traceback):
        # only close the socket if there was an error
        if exc_value is not None:
            try:
                self.conn.close()
            except Exception:
                pass
            self.conn = None

    async def _open(self):
        return await get_ipc_connection(self.ipc_path)

    async def reset(self):
        self.conn.close()
        self.conn = IPCConnection(*(await self._open()))
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

    elif sys.platform.startswith('linux') or sys.platform.startswith('freebsd'):
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
            "Unsupported platform '{0}'.  Only darwin/linux/win32/freebsd are "
            "supported.  You must specify the ipc_path".format(sys.platform)
        )


def get_dev_ipc_path():
    if sys.platform == 'darwin':
        tmpdir = os.environ.get('TMPDIR', '')
        ipc_path = os.path.expanduser(os.path.join(
            tmpdir,
            "geth.ipc"
        ))
        if os.path.exists(ipc_path):
            return ipc_path

    elif sys.platform.startswith('linux') or sys.platform.startswith('freebsd'):
        ipc_path = os.path.expanduser(os.path.join(
            "/tmp",
            "geth.ipc"
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
            "Unsupported platform '{0}'.  Only darwin/linux/win32/freebsd are "
            "supported.  You must specify the ipc_path".format(sys.platform)
        )


class IPCProvider(JSONBaseProvider):
    logger = logging.getLogger("web3.providers.IPCProvider")
    _conn = None

    def __init__(self, ipc_path=None, testnet=False, timeout=10, *args, **kwargs):
        if ipc_path is None:
            self.ipc_path = get_default_ipc_path(testnet)
        else:
            if isinstance(ipc_path, pathlib.Path):
                ipc_path = str(ipc_path.resolve())
            self.ipc_path = ipc_path

        self.timeout = timeout
        self._lock = asyncio.Lock()
        self._conn = PersistantSocket(self.ipc_path)
        super().__init__(*args, **kwargs)

    async def make_request(self, method, params):
        self.logger.debug("Making request IPC. Path: %s, Method: %s",
                          self.ipc_path, method)
        request = self.encode_rpc_request(method, params)

        async with self._lock, self._conn as conn:
            try:
                await conn.send(request)
            except BrokenPipeError:
                # one extra attempt, then give up
                conn = await self._conn.reset()
                await conn.send(request)

            raw_response = b""
            async with Timeout(self.timeout) as timeout:
                while True:
                    raw_response += await conn.read(4096)
                    if raw_response == b"":
                        timeout.sleep(0)
                    elif has_valid_json_rpc_ending(raw_response):
                        try:
                            response = self.decode_rpc_response(raw_response)
                        except JSONDecodeError:
                            await timeout.sleep(0)
                            continue
                        else:
                            return response
                    else:
                        await timeout.sleep(0)
                        continue


# A valid JSON RPC response can only end in } or ] http://www.jsonrpc.org/specification
def has_valid_json_rpc_ending(raw_response):
    stripped_raw_response = raw_response.rstrip()
    for valid_ending in [b"}", b"]"]:
        if stripped_raw_response.endswith(valid_ending):
            return True
    else:
        return False
