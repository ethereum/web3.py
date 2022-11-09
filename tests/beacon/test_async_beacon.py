import pytest
from random import (
    randint,
)

from web3._utils.request import (
    _async_session_cache,
)
from web3.beacon import (
    AsyncBeacon,
)


def _assert_valid_response(response):
    # assert valid response according to Beacon API spec
    assert isinstance(response, dict)
    assert "data" in response


@pytest.fixture
def async_beacon():
    # tested against lighthouse which uses port 5052 by default
    return AsyncBeacon(base_url="http://127.0.0.1:5052")


@pytest.fixture(autouse=True)
def _cleanup():
    yield
    _async_session_cache.clear()


# Beacon endpoint tests:


@pytest.mark.asyncio
async def test_async_cl_beacon_get_genesis(async_beacon):
    response = await async_beacon.get_genesis()
    _assert_valid_response(response)

    [await session.close() for session in _async_session_cache._data.values()]


@pytest.mark.asyncio
async def test_async_cl_beacon_get_hash_root(async_beacon):
    response = await async_beacon.get_hash_root()
    _assert_valid_response(response)

    [await session.close() for session in _async_session_cache._data.values()]


@pytest.mark.asyncio
async def test_async_cl_beacon_get_fork_data(async_beacon):
    response = await async_beacon.get_fork_data()
    _assert_valid_response(response)

    [await session.close() for session in _async_session_cache._data.values()]


@pytest.mark.asyncio
async def test_async_cl_beacon_get_finality_checkpoint(async_beacon):
    response = await async_beacon.get_finality_checkpoint()
    _assert_valid_response(response)

    [await session.close() for session in _async_session_cache._data.values()]


@pytest.mark.asyncio
async def test_async_cl_beacon_get_validators(async_beacon):
    response = await async_beacon.get_validators()
    _assert_valid_response(response)

    [await session.close() for session in _async_session_cache._data.values()]


@pytest.mark.asyncio
async def test_async_cl_beacon_get_validator(async_beacon):
    validators_response = await async_beacon.get_validators()
    _assert_valid_response(validators_response)

    validators = validators_response["data"]
    random_validator = validators[randint(0, len(validators))]
    random_validator_pubkey = random_validator["validator"]["pubkey"]

    response = await async_beacon.get_validator(random_validator_pubkey)
    _assert_valid_response(response)

    [await session.close() for session in _async_session_cache._data.values()]


@pytest.mark.asyncio
async def test_async_cl_beacon_get_validator_balances(async_beacon):
    response = await async_beacon.get_validator_balances()
    _assert_valid_response(response)

    [await session.close() for session in _async_session_cache._data.values()]


@pytest.mark.asyncio
async def test_async_cl_beacon_get_epoch_committees(async_beacon):
    response = await async_beacon.get_epoch_committees()
    _assert_valid_response(response)

    [await session.close() for session in _async_session_cache._data.values()]


@pytest.mark.asyncio
async def test_async_cl_beacon_get_block_headers(async_beacon):
    response = await async_beacon.get_block_headers()
    _assert_valid_response(response)

    [await session.close() for session in _async_session_cache._data.values()]


@pytest.mark.asyncio
async def test_async_cl_beacon_get_block_header(async_beacon):
    response = await async_beacon.get_block_header("head")
    _assert_valid_response(response)

    [await session.close() for session in _async_session_cache._data.values()]


@pytest.mark.asyncio
async def test_async_cl_beacon_get_block(async_beacon):
    response = await async_beacon.get_block("head")
    _assert_valid_response(response)

    [await session.close() for session in _async_session_cache._data.values()]


@pytest.mark.asyncio
async def test_async_cl_beacon_get_block_root(async_beacon):
    response = await async_beacon.get_block_root("head")
    _assert_valid_response(response)

    [await session.close() for session in _async_session_cache._data.values()]


@pytest.mark.asyncio
async def test_async_cl_beacon_get_block_attestations(async_beacon):
    response = await async_beacon.get_block_attestations("head")
    _assert_valid_response(response)

    [await session.close() for session in _async_session_cache._data.values()]


@pytest.mark.asyncio
async def test_async_cl_beacon_get_attestations(async_beacon):
    response = await async_beacon.get_attestations()
    _assert_valid_response(response)

    [await session.close() for session in _async_session_cache._data.values()]


@pytest.mark.asyncio
async def test_async_cl_beacon_get_attester_slashings(async_beacon):
    response = await async_beacon.get_attester_slashings()
    _assert_valid_response(response)

    [await session.close() for session in _async_session_cache._data.values()]


@pytest.mark.asyncio
async def test_async_cl_beacon_get_proposer_slashings(async_beacon):
    response = await async_beacon.get_proposer_slashings()
    _assert_valid_response(response)

    [await session.close() for session in _async_session_cache._data.values()]


@pytest.mark.asyncio
async def test_async_cl_beacon_get_voluntary_exits(async_beacon):
    response = await async_beacon.get_voluntary_exits()
    _assert_valid_response(response)

    [await session.close() for session in _async_session_cache._data.values()]


# Config endpoint tests:


@pytest.mark.asyncio
async def test_async_cl_config_get_fork_schedule(async_beacon):
    response = await async_beacon.get_fork_schedule()
    _assert_valid_response(response)

    [await session.close() for session in _async_session_cache._data.values()]


@pytest.mark.asyncio
async def test_async_cl_config_get_spec(async_beacon):
    response = await async_beacon.get_spec()
    _assert_valid_response(response)

    [await session.close() for session in _async_session_cache._data.values()]


@pytest.mark.asyncio
async def test_async_cl_config_get_deposit_contract(async_beacon):
    response = await async_beacon.get_deposit_contract()
    _assert_valid_response(response)

    [await session.close() for session in _async_session_cache._data.values()]


# Debug endpoint tests:


@pytest.mark.asyncio
async def test_async_cl_debug_get_beacon_state(async_beacon):
    response = await async_beacon.get_beacon_state()
    _assert_valid_response(response)

    [await session.close() for session in _async_session_cache._data.values()]


@pytest.mark.asyncio
async def test_async_cl_debug_get_beacon_heads(async_beacon):
    response = await async_beacon.get_beacon_heads()
    _assert_valid_response(response)

    [await session.close() for session in _async_session_cache._data.values()]


# Node endpoint tests:


@pytest.mark.asyncio
async def test_async_cl_node_get_node_identity(async_beacon):
    response = await async_beacon.get_node_identity()
    _assert_valid_response(response)

    [await session.close() for session in _async_session_cache._data.values()]


@pytest.mark.asyncio
async def test_async_cl_node_get_peers(async_beacon):
    response = await async_beacon.get_peers()
    _assert_valid_response(response)

    [await session.close() for session in _async_session_cache._data.values()]


@pytest.mark.asyncio
async def test_async_cl_node_get_peer(async_beacon):
    response = await async_beacon.get_peer("")
    _assert_valid_response(response)

    [await session.close() for session in _async_session_cache._data.values()]


@pytest.mark.asyncio
async def test_async_cl_node_get_health(async_beacon):
    response = await async_beacon.get_health()
    assert response <= 206

    [await session.close() for session in _async_session_cache._data.values()]


@pytest.mark.asyncio
async def test_async_cl_node_get_version(async_beacon):
    response = await async_beacon.get_version()
    _assert_valid_response(response)

    [await session.close() for session in _async_session_cache._data.values()]


@pytest.mark.asyncio
async def test_async_cl_node_get_syncing(async_beacon):
    response = await async_beacon.get_syncing()
    _assert_valid_response(response)

    [await session.close() for session in _async_session_cache._data.values()]
