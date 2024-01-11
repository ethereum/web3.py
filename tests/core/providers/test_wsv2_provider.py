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

from web3 import (
    AsyncWeb3,
)
from web3._utils.caching import (
    RequestInformation,
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
async def test_async_make_request_returns_desired_response():
    provider = WebsocketProviderV2("ws://mocked")

    with patch(
        "web3.providers.websocket.websocket_v2.connect", new=lambda *_1, **_2: _coro()
    ):
        await provider.connect()

    _mock_ws(provider)
    method_under_test = provider.make_request

    undesired_responses_count = 10
    ws_messages = [
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
    ws_messages.append(b'{"jsonrpc": "2.0", "id": 0, "result": "0x1337"}')
    provider._ws = WebsocketMessageStreamMock(messages=ws_messages)

    response = await method_under_test(RPCEndpoint("some_method"), ["desired_params"])
    assert response == json.loads(ws_messages.pop())

    qsize = provider._request_processor._subscription_response_queue.qsize()
    assert qsize == len(ws_messages) == undesired_responses_count

    for i in range(qsize):
        cached_response = (
            await provider._request_processor._subscription_response_queue.get()
        )
        # assert all cached responses are in the list of responses we received
        assert to_bytes(text=json.dumps(cached_response)) in ws_messages

    assert provider._request_processor._subscription_response_queue.empty()
    assert len(provider._request_processor._request_response_cache) == 0

    await provider.disconnect()


@pytest.mark.asyncio
async def test_async_make_request_times_out_of_while_loop_looking_for_response():
    timeout = 0.001
    provider = WebsocketProviderV2("ws://mocked", request_timeout=timeout)

    method_under_test = provider.make_request
    _mock_ws(provider)

    with pytest.raises(
        TimeExhausted,
        match=r"Timed out waiting for response with request id `0` after "
        rf"{timeout} second\(s\)",
    ):
        await method_under_test(RPCEndpoint("some_method"), ["desired_params"])


@pytest.mark.asyncio
async def test_msg_listener_task_starts_on_provider_connect_and_cancels_on_disconnect():
    provider = WebsocketProviderV2("ws://mocked")
    _mock_ws(provider)

    assert provider._message_listener_task is None

    with patch(
        "web3.providers.websocket.websocket_v2.connect", new=lambda *_1, **_2: _coro()
    ):
        await provider.connect()  # connect

    assert provider._message_listener_task is not None
    assert not provider._message_listener_task.cancelled()

    await provider.disconnect()  # disconnect

    assert provider._message_listener_task.cancelled()
    assert provider._message_listener_task.done()


@pytest.mark.asyncio
async def test_msg_listener_task_silences_exceptions_by_default_and_error_logs(caplog):
    provider = WebsocketProviderV2("ws://mocked")
    _mock_ws(provider)

    with patch(
        "web3.providers.websocket.websocket_v2.connect", new=lambda *_1, **_2: _coro()
    ):
        await provider.connect()
        assert provider._message_listener_task is not None
        assert provider.raise_listener_task_exceptions is False

    provider._ws = WebsocketMessageStreamMock(
        raise_exception=Exception("test exception")
    )
    await provider._message_listener_task

    assert "test exception" in caplog.text
    assert (
        "Exception caught in listener, error logging and keeping listener background "
        "task alive.\n    error=test exception"
    ) in caplog.text


@pytest.mark.asyncio
async def test_msg_listener_task_raises_when_raise_listener_task_exceptions_is_true():
    provider = WebsocketProviderV2("ws://mocked", raise_listener_task_exceptions=True)
    _mock_ws(provider)

    with patch(
        "web3.providers.websocket.websocket_v2.connect", new=lambda *_1, **_2: _coro()
    ):
        await provider.connect()
        assert provider._message_listener_task is not None

    provider._ws = WebsocketMessageStreamMock(
        raise_exception=Exception("test exception")
    )
    with pytest.raises(Exception, match="test exception"):
        await provider._message_listener_task

    assert provider._message_listener_task.done()


@pytest.mark.asyncio
@skip_if_py37
async def test_listen_event_awaits_msg_processing_when_subscription_queue_is_full():
    """
    This test is to ensure that the `listen_event` method will wait for the
    `process_subscriptions` method to process a message when the subscription queue
    is full.
    """
    from unittest.mock import (
        AsyncMock,
    )

    with patch(
        "web3.providers.websocket.websocket_v2.connect", new=lambda *_1, **_2: _coro()
    ):
        async_w3 = await AsyncWeb3.persistent_websocket(
            WebsocketProviderV2("ws://mocked")
        )

    _mock_ws(async_w3.provider)

    assert async_w3.provider._message_listener_task is not None
    assert not async_w3.provider._message_listener_task.cancelled()

    # assert queue is instance of asyncio.Queue and replace with a new queue, maxsize=1
    assert isinstance(
        async_w3.provider._request_processor._subscription_response_queue,
        type(asyncio.Queue()),
    )
    async_w3.provider._request_processor._subscription_response_queue = asyncio.Queue(
        maxsize=1
    )
    assert not async_w3.provider._request_processor._subscription_response_queue.full()

    # mock listen event
    async_w3.provider._listen_event.wait = AsyncMock()
    async_w3.provider._listen_event.set = AsyncMock()

    # mock subscription and add to active subscriptions
    sub_id = "0x1"
    sub_request_information = RequestInformation(
        method=RPCEndpoint("eth_subscribe"),
        params=["mock"],
        response_formatters=(),
        subscription_id=sub_id,
    )
    async_w3.provider._request_processor._request_information_cache.cache(
        "", sub_request_information
    )

    mocked_sub = {
        "jsonrpc": "2.0",
        "method": "eth_subscription",
        "params": {"subscription": sub_id, "result": "0x1337"},
    }

    # fill queue with one item so it is full
    async_w3.provider._request_processor._subscription_response_queue.put_nowait(
        mocked_sub
    )
    assert async_w3.provider._request_processor._subscription_response_queue.full()

    # wait will be called on the _listen_event when the next message comes in
    async_w3.provider._listen_event.wait.assert_not_called()

    # mock the message stream with a single message
    # the message listener task should then call the _listen_event.wait since the
    # queue is full
    async_w3.provider._ws = WebsocketMessageStreamMock(
        messages=[to_bytes(text=json.dumps(mocked_sub))]
    )
    await asyncio.sleep(0.05)
    async_w3.provider._listen_event.wait.assert_called_once()

    # set is not called until we start consuming messages
    async_w3.provider._listen_event.set.assert_not_called()

    async for message in async_w3.ws.process_subscriptions():
        # assert the very next message is the mocked subscription
        assert message == mocked_sub
        break

    # assert we set the _listen_event after we consume the message
    async_w3.provider._listen_event.set.assert_called_once()
