import pytest

from eth_typing import (
    ChecksumAddress,
)
from eth_utils import (
    is_checksum_address,
    is_dict,
)

from web3._utils.contract_sources.contract_data._custom_contract_data import (
    EMITTER_ENUM,
)
from web3._utils.contract_sources.contract_data.panic_errors_contract import (
    PANIC_ERRORS_CONTRACT_DATA,
)
from web3._utils.contract_sources.contract_data.storage_contract import (
    STORAGE_CONTRACT_DATA,
)

# set up the keyfile account with a known address (same from geth setup)
KEYFILE_ACCOUNT_PKEY = (
    "0x58d23b55bc9cdce1f18c2500f40ff4ab7245df9a89505e9b1fa4851f623d241d"
)
KEYFILE_ACCOUNT_ADDRESS = "0xdC544d1AA88Ff8bbd2F2AeC754B1F1e99e1812fd"


def _deploy_contract(w3, contract_factory):
    deploy_txn_hash = contract_factory.constructor().transact(
        {"from": w3.eth.default_account}
    )
    deploy_receipt = w3.eth.wait_for_transaction_receipt(deploy_txn_hash)
    assert is_dict(deploy_receipt)
    contract_address = deploy_receipt["contractAddress"]
    assert is_checksum_address(contract_address)
    return contract_factory(contract_address)


@pytest.fixture(scope="module")
def keyfile_account_pkey():
    yield KEYFILE_ACCOUNT_PKEY


@pytest.fixture(scope="module")
def keyfile_account_address():
    yield KEYFILE_ACCOUNT_ADDRESS


@pytest.fixture(scope="module")
def math_contract_deploy_txn_hash(w3, math_contract_factory):
    deploy_txn_hash = math_contract_factory.constructor().transact(
        {"from": w3.eth.default_account}
    )
    return deploy_txn_hash


@pytest.fixture(scope="module")
def math_contract(w3, math_contract_factory, math_contract_deploy_txn_hash):
    deploy_receipt = w3.eth.wait_for_transaction_receipt(math_contract_deploy_txn_hash)
    assert is_dict(deploy_receipt)
    contract_address = deploy_receipt["contractAddress"]
    assert is_checksum_address(contract_address)
    return math_contract_factory(contract_address)


@pytest.fixture(scope="module")
def math_contract_address(math_contract, address_conversion_func):
    return address_conversion_func(math_contract.address)


@pytest.fixture(scope="module")
def storage_contract(w3):
    contract_factory = w3.eth.contract(**STORAGE_CONTRACT_DATA)
    return _deploy_contract(w3, contract_factory)


@pytest.fixture(scope="module")
def emitter_contract(w3, emitter_contract_factory):
    return _deploy_contract(w3, emitter_contract_factory)


@pytest.fixture(scope="module")
def emitter_contract_address(emitter_contract, address_conversion_func):
    return address_conversion_func(emitter_contract.address)


@pytest.fixture(scope="module")
def empty_block(w3):
    w3.testing.mine()
    block = w3.eth.get_block("latest")
    assert not block["transactions"]
    return block


@pytest.fixture(scope="module")
def block_with_txn(w3):
    txn_hash = w3.eth.send_transaction(
        {
            "from": ChecksumAddress(w3.eth.default_account),
            "to": ChecksumAddress(w3.eth.default_account),
            "value": w3.to_wei(1, "gwei"),
            "gas": 21000,
            "gasPrice": w3.to_wei(1, "gwei"),  # needs to be > base_fee post London
        }
    )
    txn = w3.eth.get_transaction(txn_hash)
    block = w3.eth.get_block(txn["blockNumber"])
    return block


@pytest.fixture(scope="module")
def mined_txn_hash(block_with_txn):
    return block_with_txn["transactions"][0]


@pytest.fixture(scope="module")
def block_with_txn_with_log(w3, emitter_contract):
    txn_hash = emitter_contract.functions.logDouble(
        which=EMITTER_ENUM["LogDoubleWithIndex"],
        arg0=12345,
        arg1=54321,
    ).transact({"from": w3.eth.default_account})
    txn = w3.eth.get_transaction(txn_hash)
    block = w3.eth.get_block(txn["blockNumber"])
    return block


@pytest.fixture(scope="module")
def txn_hash_with_log(block_with_txn_with_log):
    return block_with_txn_with_log["transactions"][0]


@pytest.fixture(scope="module")
def revert_contract(w3, revert_contract_factory):
    return _deploy_contract(w3, revert_contract_factory)


#
# Offchain Lookup Contract Setup
#
@pytest.fixture(scope="module")
def offchain_lookup_contract(w3, offchain_lookup_contract_factory):
    return _deploy_contract(w3, offchain_lookup_contract_factory)


@pytest.fixture(scope="module")
def panic_errors_contract(w3):
    panic_errors_contract_factory = w3.eth.contract(**PANIC_ERRORS_CONTRACT_DATA)
    return _deploy_contract(w3, panic_errors_contract_factory)


@pytest.fixture
def keyfile_account_address_dual_type(keyfile_account_address, address_conversion_func):
    yield keyfile_account_address
