import pytest
from random import (
    randint,
)

from requests import (
    Timeout,
)

from web3._utils.request import (
    _session_cache,
)
from web3.beacon import (
    Beacon,
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
def beacon():
    return Beacon(base_url=BASE_URL)


@pytest.fixture(autouse=True)
def _cleanup():
    yield
    _session_cache.clear()


# sanity check to make sure the positive test cases are valid
def test_cl_beacon_raises_exception_on_invalid_url(beacon):
    with pytest.raises(Web3ValueError):
        beacon._make_get_request(BASE_URL + "/eth/v1/beacon/nonexistent")


def test_beacon_user_defined_request_timeout():
    beacon = Beacon(base_url=BASE_URL, request_timeout=0.001)
    with pytest.raises(Timeout):
        beacon.get_validators()


# Beacon endpoint tests:


def test_cl_beacon_get_genesis(beacon):
    response = beacon.get_genesis()
    _assert_valid_response(response)


def test_cl_beacon_get_hash_root(beacon):
    response = beacon.get_hash_root()
    _assert_valid_response(response)


def test_cl_beacon_get_fork_data(beacon):
    response = beacon.get_fork_data()
    _assert_valid_response(response)


def test_cl_beacon_get_finality_checkpoint(beacon):
    response = beacon.get_finality_checkpoint()
    _assert_valid_response(response)


def test_cl_beacon_get_validators(beacon):
    response = beacon.get_validators()
    _assert_valid_response(response)


def test_cl_beacon_get_validator(beacon):
    validators_response = beacon.get_validators()
    _assert_valid_response(validators_response)

    validators = validators_response["data"]
    random_validator = validators[randint(0, len(validators))]
    random_validator_pubkey = random_validator["validator"]["pubkey"]

    response = beacon.get_validator(random_validator_pubkey)
    _assert_valid_response(response)


def test_cl_beacon_get_validator_balances(beacon):
    response = beacon.get_validator_balances()
    _assert_valid_response(response)


def test_cl_beacon_get_epoch_committees(beacon):
    response = beacon.get_epoch_committees()
    _assert_valid_response(response)


def test_cl_beacon_get_epoch_sync_committees(beacon):
    response = beacon.get_epoch_sync_committees()
    _assert_valid_response(response)


def test_cl_beacon_get_epoch_randao(beacon):
    response = beacon.get_epoch_randao()
    _assert_valid_response(response)


def test_cl_beacon_get_block_headers(beacon):
    response = beacon.get_block_headers()
    _assert_valid_response(response)


def test_cl_beacon_get_block_header(beacon):
    response = beacon.get_block_header("head")
    _assert_valid_response(response)


def test_cl_beacon_get_block(beacon):
    response = beacon.get_block("head")
    _assert_valid_response(response)


def test_cl_beacon_get_block_root(beacon):
    response = beacon.get_block_root("head")
    _assert_valid_response(response)


def test_cl_beacon_get_blinded_blocks(beacon):
    response = beacon.get_blinded_blocks("head")
    _assert_valid_response(response)


def test_cl_beacon_get_rewards(beacon):
    response = beacon.get_rewards("head")
    _assert_valid_response(response)


def test_cl_beacon_get_block_attestations(beacon):
    response = beacon.get_block_attestations("head")
    _assert_valid_response(response)


def test_cl_beacon_get_attestations(beacon):
    response = beacon.get_attestations()
    _assert_valid_response(response)


def test_cl_beacon_get_attester_slashings(beacon):
    response = beacon.get_attester_slashings()
    _assert_valid_response(response)


def test_cl_beacon_get_proposer_slashings(beacon):
    response = beacon.get_proposer_slashings()
    _assert_valid_response(response)


def test_cl_beacon_get_voluntary_exits(beacon):
    response = beacon.get_voluntary_exits()
    _assert_valid_response(response)


def test_cl_beacon_get_bls_to_execution_changes(beacon):
    response = beacon.get_bls_to_execution_changes()
    _assert_valid_response(response)


# Config endpoint tests:


def test_cl_config_get_fork_schedule(beacon):
    response = beacon.get_fork_schedule()
    _assert_valid_response(response)


def test_cl_config_get_spec(beacon):
    response = beacon.get_spec()
    _assert_valid_response(response)


def test_cl_config_get_deposit_contract(beacon):
    response = beacon.get_deposit_contract()
    _assert_valid_response(response)


# Debug endpoint tests:


def test_cl_debug_get_beacon_state(beacon):
    response = beacon.get_beacon_state()
    _assert_valid_response(response)


def test_cl_debug_get_beacon_heads(beacon):
    response = beacon.get_beacon_heads()
    _assert_valid_response(response)


# Node endpoint tests:


def test_cl_node_get_node_identity(beacon):
    response = beacon.get_node_identity()
    _assert_valid_response(response)


def test_cl_node_get_peers(beacon):
    response = beacon.get_peers()
    _assert_valid_response(response)


def test_cl_node_get_peer(beacon):
    response = beacon.get_peer("")
    _assert_valid_response(response)


def test_cl_node_get_health(beacon):
    response = beacon.get_health()
    assert isinstance(response, int)


def test_cl_node_get_version(beacon):
    response = beacon.get_version()
    _assert_valid_response(response)


def test_cl_node_get_syncing(beacon):
    response = beacon.get_syncing()
    _assert_valid_response(response)
