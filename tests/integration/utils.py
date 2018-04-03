import asyncio
import time

import websockets


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
