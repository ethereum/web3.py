import json
import pytest
import sys

from eth_utils import (
    to_bytes,
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
    # move to top of file when python 3.7 is no longer supported in web3.py
    from unittest.mock import (
        AsyncMock,
    )

    provider._ws = AsyncMock()


@pytest.mark.asyncio
@pytest.mark.skipif(
    # TODO: remove when python 3.7 is no longer supported in web3.py
    #  python 3.7 is already sunset so this feels like a reasonable tradeoff
    sys.version_info < (3, 8),
    reason="Uses AsyncMock, not supported by python 3.7",
)
async def test_async_make_request_caches_all_undesired_responses_and_returns_desired():
    provider = WebsocketProviderV2("ws://mocked")

    method_under_test = provider.make_request

    _mock_ws(provider)
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
        for i in range(0, undesired_responses_count)
    ]
    # The first request we make should have an id of `0`, expect the response to match
    # that id. Append it as the last response in the list.
    ws_recv_responses.append(b'{"jsonrpc": "2.0", "id":0, "result": "0x1337"}')
    provider._ws.recv.side_effect = ws_recv_responses

    response = await method_under_test(RPCEndpoint("some_method"), ["desired_params"])
    assert response == json.loads(ws_recv_responses.pop())  # pop the expected response

    assert (
        len(provider._request_processor._request_response_cache)
        == len(ws_recv_responses)
        == undesired_responses_count
    )

    for (
        _cache_key,
        cached_response,
    ) in provider._request_processor._request_response_cache.items():
        # assert all cached responses are in the list of responses we received
        assert to_bytes(text=json.dumps(cached_response)) in ws_recv_responses


@pytest.mark.asyncio
@pytest.mark.skipif(
    # TODO: remove when python 3.7 is no longer supported in web3.py
    #  python 3.7 is already sunset so this feels like a reasonable tradeoff
    sys.version_info < (3, 8),
    reason="Uses AsyncMock, not supported by python 3.7",
)
async def test_async_make_request_returns_cached_response_with_no_recv_if_cached():
    provider = WebsocketProviderV2("ws://mocked")

    method_under_test = provider.make_request

    _mock_ws(provider)

    # cache the response, so we should get it immediately & should never call `recv()`
    desired_response = {"jsonrpc": "2.0", "id": 0, "result": "0x1337"}
    await provider._request_processor.cache_raw_response(desired_response)

    response = await method_under_test(RPCEndpoint("some_method"), ["desired_params"])
    assert response == desired_response

    assert len(provider._request_processor._request_response_cache) == 0
    assert not provider._ws.recv.called  # type: ignore


@pytest.mark.asyncio
@pytest.mark.skipif(
    # TODO: remove when python 3.7 is no longer supported in web3.py
    #  python 3.7 is already sunset so this feels like a reasonable tradeoff
    sys.version_info < (3, 8),
    reason="Uses AsyncMock, not supported by python 3.7",
)
async def test_async_make_request_times_out_of_while_loop_looking_for_response():
    provider = WebsocketProviderV2("ws://mocked", call_timeout=0.1)

    method_under_test = provider.make_request

    _mock_ws(provider)
    provider._ws.recv.side_effect = lambda *args, **kwargs: b'{"jsonrpc": "2.0"}'

    with pytest.raises(
        TimeExhausted,
        match="Timed out waiting for response with request id `0` after 0.1 seconds.",
    ):
        await method_under_test(RPCEndpoint("some_method"), ["desired_params"])
