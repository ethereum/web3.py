import pytest

from eth_utils import (
    to_canonical_address,
)
from ethpm import (
    Package,
)
from ethpm.exceptions import (
    InsufficientAssetsError,
)
from ethpm.tools import (
    get_manifest as get_ethpm_manifest,
)


def test_pm_init_with_minimal_manifest(w3):
    owned_manifest = get_ethpm_manifest('owned', '1.0.1.json')
    pm = w3.pm.get_package_from_manifest(owned_manifest)
    assert pm.name == 'owned'


def test_get_contract_factory_raises_insufficient_assets_error(w3):
    insufficient_owned_manifest = get_ethpm_manifest('owned', '1.0.0.json')
    owned_package = w3.pm.get_package_from_manifest(insufficient_owned_manifest)
    with pytest.raises(InsufficientAssetsError):
        owned_package.get_contract_factory('Owned')


def test_get_contract_factory_with_valid_owned_manifest(w3):
    owned_manifest = get_ethpm_manifest('owned', '1.0.1.json')
    owned_package = w3.pm.get_package_from_manifest(owned_manifest)
    owned_factory = owned_package.get_contract_factory('Owned')
    tx_hash = owned_factory.constructor().transact()
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    owned_address = to_canonical_address(tx_receipt.contractAddress)
    owned_instance = owned_package.get_contract_instance("Owned", owned_address)
    assert owned_instance.abi == owned_factory.abi


def test_get_contract_factory_with_valid_safe_math_lib_manifest(w3):
    safe_math_lib_manifest = get_ethpm_manifest('safe-math-lib', '1.0.1.json')
    safe_math_package = w3.pm.get_package_from_manifest(safe_math_lib_manifest)
    safe_math_factory = safe_math_package.get_contract_factory("SafeMathLib")
    tx_hash = safe_math_factory.constructor().transact()
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    safe_math_address = to_canonical_address(tx_receipt.contractAddress)
    safe_math_instance = safe_math_package.get_contract_instance("SafeMathLib", safe_math_address)
    assert safe_math_instance.functions.safeAdd(1, 2).call() == 3


def test_get_contract_factory_with_valid_escrow_manifest(w3):
    escrow_manifest = get_ethpm_manifest("escrow", "1.0.2.json")
    escrow_package = w3.pm.get_package_from_manifest(escrow_manifest)
    escrow_factory = escrow_package.get_contract_factory('Escrow')
    assert escrow_factory.needs_bytecode_linking
    safe_send_factory = escrow_package.get_contract_factory('SafeSendLib')
    safe_send_tx_hash = safe_send_factory.constructor().transact()
    safe_send_tx_receipt = w3.eth.waitForTransactionReceipt(safe_send_tx_hash)
    safe_send_address = to_canonical_address(safe_send_tx_receipt.contractAddress)
    linked_escrow_factory = escrow_factory.link_bytecode({"SafeSendLib": safe_send_address})
    assert linked_escrow_factory.needs_bytecode_linking is False
    escrow_tx_hash = linked_escrow_factory.constructor(w3.eth.accounts[0]).transact()
    escrow_tx_receipt = w3.eth.waitForTransactionReceipt(escrow_tx_hash)
    escrow_address = to_canonical_address(escrow_tx_receipt.contractAddress)
    escrow_instance = linked_escrow_factory(address=escrow_address)
    assert escrow_instance.functions.sender().call() == w3.eth.accounts[0]


def test_deploy_a_standalone_package_integration(w3):
    standard_token_manifest = get_ethpm_manifest("standard-token", "1.0.1.json")
    token_package = w3.pm.get_package_from_manifest(standard_token_manifest)
    # Added deployment bytecode to manifest to be able to generate factory
    ERC20 = token_package.get_contract_factory('StandardToken')
    # totalSupply = 100
    tx_hash = ERC20.constructor(100).transact()
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    address = to_canonical_address(tx_receipt["contractAddress"])
    erc20 = w3.eth.contract(address=address, abi=ERC20.abi)
    total_supply = erc20.functions.totalSupply().call()
    assert total_supply == 100


def test_pm_init_with_manifest_uri(w3, monkeypatch):
    monkeypatch.setenv(
        "ETHPM_IPFS_BACKEND_CLASS", "ethpm.backends.ipfs.DummyIPFSBackend"
    )
    dummy_standard_token_uri = "ipfs://QmVu9zuza5mkJwwcFdh2SXBugm1oSgZVuEKkph9XLsbUwg"
    pkg = w3.pm.get_package_from_uri(dummy_standard_token_uri)
    assert isinstance(pkg, Package)
    assert pkg.name == "standard-token"
