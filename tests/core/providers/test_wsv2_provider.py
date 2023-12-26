import asyncio
import json
import pytest
from unittest.mock import (
    AsyncMock,
    patch,
)

from eth_utils import (
    to_bytes,
)

from web3._utils.module_testing.module_testing_utils import (
    WebsocketMessageStreamMock,
)
from web3.exceptions import (
    TimeExhausted,
)
from web3.providers.websocket import (
    WebsocketProviderV2,
)
from web3.types import (
    RPCEndpoint,
)


def _mock_ws(provider):
    provider._ws = AsyncMock()


async def _coro():
    return None


@pytest.mark.asyncio
async def test_async_make_request_caches_all_undesired_responses_and_returns_desired():
    provider = WebsocketProviderV2("ws://mocked")

    with patch(
        "web3.providers.websocket.websocket_v2.connect", new=lambda *_1, **_2: _coro()
    ):
        await provider.connect()

    _mock_ws(provider)
    method_under_test = provider.make_request

    undesired_responses_count = 10
    ws_recv_responses = [
        to_bytes(
            text=json.dumps(
                {
                    "jsonrpc": "2.0",
                    "method": "eth_subscription",
                    "params": {"subscription": "0x1", "result": f"0x{i}"},
                }
            )
        )
        for i in range(undesired_responses_count)
    ]
    # The first request we make should have an id of `0`, expect the response to match
    # that id. Append it as the last response in the list.
    ws_recv_responses.append(b'{"jsonrpc": "2.0", "id": 0, "result": "0x1337"}')
    provider._ws = WebsocketMessageStreamMock(ws_recv_responses)

    response = await method_under_test(RPCEndpoint("some_method"), ["desired_params"])
    assert response == json.loads(ws_recv_responses.pop())

    qsize = provider._request_processor._subscription_response_queue.qsize()
    assert qsize == len(ws_recv_responses) == undesired_responses_count

    for i in range(qsize):
        cached_response = (
            await provider._request_processor._subscription_response_queue.get()
        )
        # assert all cached responses are in the list of responses we received
        assert to_bytes(text=json.dumps(cached_response)) in ws_recv_responses

    assert provider._request_processor._subscription_response_queue.empty()
    assert len(provider._request_processor._request_response_cache) == 0

    await provider.disconnect()


@pytest.mark.asyncio
async def test_async_make_request_times_out_of_while_loop_looking_for_response():
    timeout = 0.001
    provider = WebsocketProviderV2("ws://mocked", request_timeout=timeout)

    method_under_test = provider.make_request

    _mock_ws(provider)
    # mock the websocket to never receive a response & sleep longer than the timeout
    provider._ws.recv = lambda *args, **kwargs: asyncio.sleep(1)

    with pytest.raises(
        TimeExhausted,
        match=r"Timed out waiting for response with request id `0` after "
        rf"{timeout} second\(s\)",
    ):
        await method_under_test(RPCEndpoint("some_method"), ["desired_params"])
