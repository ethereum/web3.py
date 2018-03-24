import asyncio
import json
import os
from threading import (
    Thread,
    current_thread,
)

import websockets

from web3.providers.base import (
    JSONBaseProvider,
)

THREAD_POLLING_INTERVAL = 2  # secs


async def _stop_loop(loop, parent_thread):
    while parent_thread.is_alive():
        await asyncio.sleep(THREAD_POLLING_INTERVAL)
    else:
        print('stopping loop')
        loop.stop()


def _start_event_loop(loop, parent_thread):
    asyncio.set_event_loop(loop)
    asyncio.run_coroutine_threadsafe(_stop_loop(loop, parent_thread), loop)
    loop.run_forever()
    print('closing loop')
    loop.close()


def _get_threaded_loop():
    new_loop = asyncio.new_event_loop()
    thread_loop = Thread(target=_start_event_loop, args=(new_loop, current_thread()))
    thread_loop.start()
    return new_loop


def get_default_endpoint():
    return os.environ.get('WEB3_WS_PROVIDER_URI', 'ws://127.0.0.1:8546')


class WebsocketProvider(JSONBaseProvider):

    _loop = None

    def __init__(self, endpoint_uri=None):
        self.endpoint_uri = endpoint_uri
        if self.endpoint_uri is None:
            self.endpoint_uri = get_default_endpoint()
        if self._loop is None:
            self._loop = _get_threaded_loop()
        super().__init__()

    def __str__(self):
        return "WS connection {0}".format(self.endpoint_uri)

    async def coro_make_request(self, request_data):
        # TODO: Find out if there's a way of not establishing a connection every time
        async with websockets.client.connect(uri=self.endpoint_uri, loop=self._loop) as conn:
            await conn.send(request_data)
            return await conn.recv()

    def make_request(self, method, params):
        request_data = self.encode_rpc_request(method, params)
        future = asyncio.run_coroutine_threadsafe(self.coro_make_request(request_data), self._loop)
        return json.loads(future.result())
