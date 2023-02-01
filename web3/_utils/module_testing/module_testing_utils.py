import time
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    Generator,
    Sequence,
    Union,
)

from aiohttp import (
    ClientTimeout,
)
from eth_typing import (
    ChecksumAddress,
    HexStr,
)
from eth_utils import (
    is_same_address,
)
from hexbytes import (
    HexBytes,
)

from web3._utils.compat import (
    Literal,
)
from web3._utils.request import (
    async_cache_and_return_session,
    cache_and_return_session,
)
from web3.types import (
    BlockData,
    LogReceipt,
)

if TYPE_CHECKING:
    from _pytest.monkeypatch import MonkeyPatch  # noqa: F401
    from aiohttp import ClientResponse  # noqa: F401
    from requests import Response  # noqa: F401

    from web3 import Web3  # noqa: F401


def mine_pending_block(w3: "Web3") -> None:
    timeout = 10

    w3.geth.miner.start()  # type: ignore
    start = time.time()
    while time.time() < start + timeout:
        if len(w3.eth.get_block("pending")["transactions"]) == 0:
            break
    w3.geth.miner.stop()  # type: ignore


def assert_contains_log(
    result: Sequence[LogReceipt],
    block_with_txn_with_log: BlockData,
    emitter_contract_address: ChecksumAddress,
    txn_hash_with_log: HexStr,
) -> None:
    assert len(result) == 1
    log_entry = result[0]
    assert log_entry["blockNumber"] == block_with_txn_with_log["number"]
    assert log_entry["blockHash"] == block_with_txn_with_log["hash"]
    assert log_entry["logIndex"] == 0
    assert is_same_address(log_entry["address"], emitter_contract_address)
    assert log_entry["transactionIndex"] == 0
    assert log_entry["transactionHash"] == HexBytes(txn_hash_with_log)


def mock_offchain_lookup_request_response(
    monkeypatch: "MonkeyPatch",
    http_method: Literal["GET", "POST"] = "GET",
    mocked_request_url: str = None,
    mocked_status_code: int = 200,
    mocked_json_data: str = "0x",
    json_data_field: str = "data",
    # required only for POST validation:
    sender: str = None,
    calldata: str = None,
) -> None:
    class MockedResponse:
        status_code = mocked_status_code

        @staticmethod
        def json() -> Dict[str, str]:
            return {json_data_field: mocked_json_data}  # noqa: E704

        @staticmethod
        def raise_for_status() -> None:
            raise Exception("called raise_for_status()")  # noqa: E704

    def _mock_specific_request(
        *args: Any, **kwargs: Any
    ) -> Union["Response", MockedResponse]:
        url_from_args = args[1]

        # mock response only to specified url while validating appropriate fields
        if url_from_args == mocked_request_url:
            assert kwargs["timeout"] == 10
            if http_method.upper() == "POST":
                assert kwargs["data"] == {"data": calldata, "sender": sender}
            return MockedResponse()

        # else, make a normal request (no mocking)
        session = cache_and_return_session(url_from_args)
        return session.request(method=http_method.upper(), url=url_from_args, **kwargs)

    monkeypatch.setattr(
        f"requests.Session.{http_method.lower()}", _mock_specific_request
    )


# -- async -- #


def async_mock_offchain_lookup_request_response(
    monkeypatch: "MonkeyPatch",
    http_method: Literal["GET", "POST"] = "GET",
    mocked_request_url: str = None,
    mocked_status_code: int = 200,
    mocked_json_data: str = "0x",
    json_data_field: str = "data",
    # required only for POST validation:
    sender: str = None,
    calldata: str = None,
) -> None:
    class AsyncMockedResponse:
        status = mocked_status_code

        def __await__(self) -> Generator[Any, Any, Any]:
            yield
            return self

        @staticmethod
        async def json() -> Dict[str, str]:
            return {json_data_field: mocked_json_data}  # noqa: E704

        @staticmethod
        def raise_for_status() -> None:
            raise Exception("called raise_for_status()")  # noqa: E501, E704

    async def _mock_specific_request(
        *args: Any, **kwargs: Any
    ) -> Union["ClientResponse", AsyncMockedResponse]:
        url_from_args = args[1]

        # mock response only to specified url while validating appropriate fields
        if url_from_args == mocked_request_url:
            assert kwargs["timeout"] == ClientTimeout(10)
            if http_method.upper() == "post":
                assert kwargs["data"] == {"data": calldata, "sender": sender}
            return AsyncMockedResponse()

        # else, make a normal request (no mocking)
        session = await async_cache_and_return_session(url_from_args)
        return await session.request(
            method=http_method.upper(), url=url_from_args, **kwargs
        )

    monkeypatch.setattr(
        f"aiohttp.ClientSession.{http_method.lower()}", _mock_specific_request
    )
