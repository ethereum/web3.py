import pytest

import requests

from web3.beacon import (
    Beacon,
)


@pytest.fixture
def beacon():
    return Beacon(base_url="http://localhost:5051", session=requests.Session())


# Beacon endpoint tests:


def test_cl_beacon_get_genesis(beacon):
    response = beacon.get_genesis()
    assert response is not None


def test_cl_beacon_get_hash_root(beacon):
    response = beacon.get_hash_root()
    assert response is not None


def test_cl_beacon_get_fork_data(beacon):
    response = beacon.get_fork_data()
    assert response is not None


def test_cl_beacon_get_finality_checkpoint(beacon):
    response = beacon.get_finality_checkpoint()
    assert response is not None


def test_cl_beacon_get_validators(beacon):
    response = beacon.get_validators()
    assert response is not None


def test_cl_beacon_get_validator(beacon):
    sepolia_validator_pub_key = "0xa9f6b6b04e36850d2dbbc390a9614013da239375f105b0f3738138431f0a3a8c685445f6c518e0b0e72fb3244ddc0d9e"  # noqa: E501
    response = beacon.get_validator(sepolia_validator_pub_key)
    assert response is not None


def test_cl_beacon_get_validator_balances(beacon):
    response = beacon.get_validator_balances()
    assert response is not None


def test_cl_beacon_get_epoch_committees(beacon):
    response = beacon.get_epoch_committees()
    assert response is not None


def test_cl_beacon_get_block_headers(beacon):
    response = beacon.get_block_headers()
    assert response is not None


def test_cl_beacon_get_block_header(beacon):
    response = beacon.get_block_header("head")
    assert response is not None


def test_cl_beacon_get_block(beacon):
    response = beacon.get_block("head")
    assert response is not None


def test_cl_beacon_get_block_root(beacon):
    response = beacon.get_block_root("head")
    assert response is not None


def test_cl_beacon_get_block_attestations(beacon):
    response = beacon.get_block_attestations("head")
    assert response is not None


def test_cl_beacon_get_attestations(beacon):
    response = beacon.get_attestations()
    assert response is not None


def test_cl_beacon_get_attester_slashings(beacon):
    response = beacon.get_attester_slashings()
    assert response is not None


def test_cl_beacon_get_proposer_slashings(beacon):
    response = beacon.get_proposer_slashings()
    assert response is not None


def test_cl_beacon_get_voluntary_exits(beacon):
    response = beacon.get_voluntary_exits()
    assert response is not None


# Config endpoint tests:


def test_cl_config_get_fork_schedule(beacon):
    response = beacon.get_fork_schedule()
    assert response is not None


def test_cl_config_get_spec(beacon):
    response = beacon.get_spec()
    assert response is not None


def test_cl_config_get_deposit_contract(beacon):
    response = beacon.get_deposit_contract()
    assert response is not None


# Debug endpoint tests:


def test_cl_debug_get_beacon_state(beacon):
    response = beacon.get_beacon_state()
    assert response is not None


def test_cl_debug_get_beacon_heads(beacon):
    response = beacon.get_beacon_heads()
    assert response is not None


# Node endpoint tests:


def test_cl_node_get_node_identity(beacon):
    response = beacon.get_node_identity()
    assert response is not None


def test_cl_node_get_peers(beacon):
    response = beacon.get_peers()
    assert response is not None


def test_cl_node_get_peer(beacon):
    response = beacon.get_peer("")
    assert response is not None


def test_cl_node_get_health(beacon):
    response = beacon.get_health()
    assert response <= 206


def test_cl_node_get_version(beacon):
    response = beacon.get_version()
    assert response is not None


def test_cl_node_get_syncing(beacon):
    response = beacon.get_syncing()
    assert response is not None
