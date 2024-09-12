from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    Sequence,
    TypeVar,
    Union,
)

from eth_utils import (
    to_int,
)

if TYPE_CHECKING:
    from web3.providers import (  # noqa: F401
        AsyncBaseProvider,
        BaseProvider,
    )

UNCACHEABLE_BLOCK_IDS = {"finalized", "safe", "latest", "pending"}

ASYNC_PROVIDER_TYPE = TypeVar("ASYNC_PROVIDER_TYPE", bound="AsyncBaseProvider")
SYNC_PROVIDER_TYPE = TypeVar("SYNC_PROVIDER_TYPE", bound="BaseProvider")


def _error_log(
    provider: Union[ASYNC_PROVIDER_TYPE, SYNC_PROVIDER_TYPE], e: Exception
) -> None:
    provider.logger.error(
        "There was an exception while caching the request.", exc_info=e
    )


def is_beyond_validation_threshold(provider: SYNC_PROVIDER_TYPE, blocknum: int) -> bool:
    try:
        # `threshold` is either "finalized" or "safe"
        threshold = provider.request_cache_validation_threshold.value
        response = provider.make_request("eth_getBlockByNumber", [threshold, False])
        return blocknum <= to_int(hexstr=response["result"]["number"])
    except Exception as e:
        _error_log(provider, e)
        return False


def always_cache_request(*_args: Any, **_kwargs: Any) -> bool:
    return True


def validate_blocknum_in_params(
    provider: SYNC_PROVIDER_TYPE, params: Sequence[Any], _result: Dict[str, Any]
) -> bool:
    block_id = params[0]
    if block_id == "earliest":
        # `earliest` should always be cacheable
        return True
    blocknum = to_int(hexstr=block_id)
    return is_beyond_validation_threshold(provider, blocknum)


def validate_blocknum_in_result(
    provider: SYNC_PROVIDER_TYPE, _params: Sequence[Any], result: Dict[str, Any]
) -> bool:
    # `number` if block result, `blockNumber` if transaction result
    blocknum = to_int(hexstr=result.get("number", result.get("blockNumber")))
    return is_beyond_validation_threshold(provider, blocknum)


def validate_blockhash_in_params(
    provider: SYNC_PROVIDER_TYPE, params: Sequence[Any], _result: Dict[str, Any]
) -> bool:
    try:
        # make an extra call to get the block number from the hash
        response = provider.make_request("eth_getBlockByHash", [params[0], False])
    except Exception as e:
        _error_log(provider, e)
        return False

    blocknum = to_int(hexstr=response["result"]["number"])
    return is_beyond_validation_threshold(provider, blocknum)


# -- async -- #


async def async_is_beyond_validation_threshold(
    provider: ASYNC_PROVIDER_TYPE, blocknum: int
) -> bool:
    try:
        # `threshold` is either "finalized" or "safe"
        threshold = provider.request_cache_validation_threshold.value
        response = await provider.make_request(
            "eth_getBlockByNumber", [threshold, False]
        )
        return blocknum <= to_int(hexstr=response["result"]["number"])
    except Exception as e:
        _error_log(provider, e)
        return False


async def async_validate_blocknum_in_params(
    provider: ASYNC_PROVIDER_TYPE, params: Sequence[Any], _result: Dict[str, Any]
) -> bool:
    block_id = params[0]
    if block_id == "earliest":
        # `earliest` should always be cacheable
        return True
    blocknum = to_int(hexstr=params[0])
    return await async_is_beyond_validation_threshold(provider, blocknum)


async def async_validate_blocknum_in_result(
    provider: ASYNC_PROVIDER_TYPE, _params: Sequence[Any], result: Dict[str, Any]
) -> bool:
    # `number` if block result, `blockNumber` if transaction result
    blocknum = to_int(hexstr=result.get("number", result.get("blockNumber")))
    return await async_is_beyond_validation_threshold(provider, blocknum)


async def async_validate_blockhash_in_params(
    provider: ASYNC_PROVIDER_TYPE, params: Sequence[Any], _result: Dict[str, Any]
) -> bool:
    try:
        response = await provider.make_request("eth_getBlockByHash", [params[0], False])
    except Exception as e:
        _error_log(provider, e)
        return False

    blocknum = to_int(hexstr=response["result"]["number"])
    return await async_is_beyond_validation_threshold(provider, blocknum)
