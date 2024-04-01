import pytest
from random import (
    randint,
)

import pytest_asyncio

from web3._utils.request import (
    _async_session_cache,
)
from web3.beacon import (
    AsyncBeacon,
)
from web3.exceptions import (
    Web3ValueError,
)

# tested against lighthouse which uses port 5052 by default
BASE_URL = "http://localhost:5052"


def _assert_valid_response(response):
    # assert valid response according to Beacon API spec
    assert isinstance(response, dict)
    assert "data" in response


@pytest.fixture
def async_beacon():
    return AsyncBeacon(base_url=BASE_URL)


@pytest_asyncio.fixture(autouse=True)
async def _cleanup():
    yield
    [await session.close() for _, session in _async_session_cache.items()]
    _async_session_cache.clear()


# sanity check to make sure the positive test cases are valid
@pytest.mark.asyncio
async def test_async_cl_beacon_raises_exception_on_invalid_url(async_beacon):
    with pytest.raises(Web3ValueError):
        await async_beacon._async_make_get_request(
            BASE_URL + "/eth/v1/beacon/nonexistent"
        )


@pytest.mark.asyncio
async def test_async_beacon_user_request_timeout():
    beacon = AsyncBeacon(base_url=BASE_URL, request_timeout=0.001)
    with pytest.raises(TimeoutError):
        await beacon.get_validators()


# Beacon endpoint tests:


@pytest.mark.asyncio
async def test_async_cl_beacon_get_genesis(async_beacon):
    response = await async_beacon.get_genesis()
    _assert_valid_response(response)


@pytest.mark.asyncio
async def test_async_cl_beacon_get_hash_root(async_beacon):
    response = await async_beacon.get_hash_root()
    _assert_valid_response(response)


@pytest.mark.asyncio
async def test_async_cl_beacon_get_fork_data(async_beacon):
    response = await async_beacon.get_fork_data()
    _assert_valid_response(response)


@pytest.mark.asyncio
async def test_async_cl_beacon_get_finality_checkpoint(async_beacon):
    response = await async_beacon.get_finality_checkpoint()
    _assert_valid_response(response)


@pytest.mark.asyncio
async def test_async_cl_beacon_get_validators(async_beacon):
    response = await async_beacon.get_validators()
    _assert_valid_response(response)


@pytest.mark.asyncio
async def test_async_cl_beacon_get_validator(async_beacon):
    validators_response = await async_beacon.get_validators()
    _assert_valid_response(validators_response)

    validators = validators_response["data"]
    random_validator = validators[randint(0, len(validators))]
    random_validator_pubkey = random_validator["validator"]["pubkey"]

    response = await async_beacon.get_validator(random_validator_pubkey)
    _assert_valid_response(response)


@pytest.mark.asyncio
async def test_async_cl_beacon_get_validator_balances(async_beacon):
    response = await async_beacon.get_validator_balances()
    _assert_valid_response(response)


@pytest.mark.asyncio
async def test_async_cl_beacon_get_epoch_committees(async_beacon):
    response = await async_beacon.get_epoch_committees()
    _assert_valid_response(response)


@pytest.mark.asyncio
async def test_async_cl_beacon_get_epoch_sync_committees(async_beacon):
    response = await async_beacon.get_epoch_sync_committees()
    _assert_valid_response(response)


@pytest.mark.asyncio
async def test_async_cl_beacon_get_epoch_randao(async_beacon):
    response = await async_beacon.get_epoch_randao()
    _assert_valid_response(response)


@pytest.mark.asyncio
async def test_async_cl_beacon_get_block_headers(async_beacon):
    response = await async_beacon.get_block_headers()
    _assert_valid_response(response)


@pytest.mark.asyncio
async def test_async_cl_beacon_get_block_header(async_beacon):
    response = await async_beacon.get_block_header("head")
    _assert_valid_response(response)


@pytest.mark.asyncio
async def test_async_cl_beacon_get_block(async_beacon):
    response = await async_beacon.get_block("head")
    _assert_valid_response(response)


@pytest.mark.asyncio
async def test_async_cl_beacon_get_block_root(async_beacon):
    response = await async_beacon.get_block_root("head")
    _assert_valid_response(response)


@pytest.mark.asyncio
async def test_async_cl_beacon_get_blinded_blocks(async_beacon):
    response = await async_beacon.get_blinded_blocks("head")
    _assert_valid_response(response)


@pytest.mark.asyncio
async def test_async_cl_beacon_get_rewards(async_beacon):
    response = await async_beacon.get_rewards("head")
    _assert_valid_response(response)


@pytest.mark.asyncio
async def test_async_cl_beacon_get_block_attestations(async_beacon):
    response = await async_beacon.get_block_attestations("head")
    _assert_valid_response(response)


@pytest.mark.asyncio
async def test_async_cl_beacon_get_attestations(async_beacon):
    response = await async_beacon.get_attestations()
    _assert_valid_response(response)


@pytest.mark.asyncio
async def test_async_cl_beacon_get_attester_slashings(async_beacon):
    response = await async_beacon.get_attester_slashings()
    _assert_valid_response(response)


@pytest.mark.asyncio
async def test_async_cl_beacon_get_proposer_slashings(async_beacon):
    response = await async_beacon.get_proposer_slashings()
    _assert_valid_response(response)


@pytest.mark.asyncio
async def test_async_cl_beacon_get_voluntary_exits(async_beacon):
    response = await async_beacon.get_voluntary_exits()
    _assert_valid_response(response)


@pytest.mark.asyncio
async def test_async_cl_beacon_get_bls_to_execution_changes(async_beacon):
    response = await async_beacon.get_bls_to_execution_changes()
    _assert_valid_response(response)


# Config endpoint tests:


@pytest.mark.asyncio
async def test_async_cl_config_get_fork_schedule(async_beacon):
    response = await async_beacon.get_fork_schedule()
    _assert_valid_response(response)


@pytest.mark.asyncio
async def test_async_cl_config_get_spec(async_beacon):
    response = await async_beacon.get_spec()
    _assert_valid_response(response)


@pytest.mark.asyncio
async def test_async_cl_config_get_deposit_contract(async_beacon):
    response = await async_beacon.get_deposit_contract()
    _assert_valid_response(response)


# Debug endpoint tests:


@pytest.mark.asyncio
async def test_async_cl_debug_get_beacon_state(async_beacon):
    response = await async_beacon.get_beacon_state()
    _assert_valid_response(response)


@pytest.mark.asyncio
async def test_async_cl_debug_get_beacon_heads(async_beacon):
    response = await async_beacon.get_beacon_heads()
    _assert_valid_response(response)


# Node endpoint tests:


@pytest.mark.asyncio
async def test_async_cl_node_get_node_identity(async_beacon):
    response = await async_beacon.get_node_identity()
    _assert_valid_response(response)


@pytest.mark.asyncio
async def test_async_cl_node_get_peers(async_beacon):
    response = await async_beacon.get_peers()
    _assert_valid_response(response)


@pytest.mark.asyncio
async def test_async_cl_node_get_peer(async_beacon):
    response = await async_beacon.get_peer("")
    _assert_valid_response(response)


@pytest.mark.asyncio
async def test_async_cl_node_get_health(async_beacon):
    response = await async_beacon.get_health()
    assert isinstance(response, int)


@pytest.mark.asyncio
async def test_async_cl_node_get_version(async_beacon):
    response = await async_beacon.get_version()
    _assert_valid_response(response)


@pytest.mark.asyncio
async def test_async_cl_node_get_syncing(async_beacon):
    response = await async_beacon.get_syncing()
    _assert_valid_response(response)
