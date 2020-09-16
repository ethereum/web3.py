import asyncio
import socket
import time

import websockets


def get_open_port():
    sock = socket.socket()
    sock.bind(('127.0.0.1', 0))
    port = sock.getsockname()[1]
    sock.close()
    return str(port)


async def wait_for_ws(endpoint_uri, event_loop, timeout=60):
    start = time.time()
    while time.time() < start + timeout:
        try:
            async with websockets.connect(uri=endpoint_uri, loop=event_loop):
                pass
        except (ConnectionRefusedError, OSError):
            await asyncio.sleep(0.01)
        else:
            break
