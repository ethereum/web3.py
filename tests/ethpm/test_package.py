import pytest

from eth_utils import (
    is_same_address,
)

from ethpm.exceptions import (
    EthPMValidationError,
    InsufficientAssetsError,
)
from ethpm.package import (
    Package,
)
from web3 import Web3


@pytest.fixture()
def safe_math_package(get_manifest, w3):
    safe_math_manifest = get_manifest("safe-math-lib")
    return Package(safe_math_manifest, w3)


@pytest.fixture()
def deployed_safe_math(safe_math_package, w3):
    SafeMath = safe_math_package.get_contract_factory("SafeMathLib")
    tx_hash = SafeMath.constructor().transact()
    tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    return safe_math_package, tx_receipt.contractAddress


def test_package_object_instantiates_with_a_web3_object(all_manifests, w3):
    package = Package(all_manifests, w3)
    assert package.w3 is w3


def test_update_web3(deployed_safe_math, w3):
    new_w3 = Web3(Web3.EthereumTesterProvider())
    original_package, _ = deployed_safe_math
    assert original_package.w3 is w3
    new_package = original_package.update_w3(new_w3)
    assert new_package.w3 is new_w3
    assert original_package is not new_package
    assert original_package.manifest == new_package.manifest
    with pytest.raises(EthPMValidationError, match="Package has no matching URIs on chain."):
        new_package.deployments


def test_get_contract_factory_with_default_web3(safe_math_package, w3):
    contract_factory = safe_math_package.get_contract_factory("SafeMathLib")
    assert hasattr(contract_factory, "address")
    assert hasattr(contract_factory, "abi")
    assert hasattr(contract_factory, "bytecode")
    assert hasattr(contract_factory, "bytecode_runtime")


def test_get_contract_factory_with_missing_contract_types(safe_math_package, w3):
    safe_math_package.manifest.pop("contractTypes", None)
    with pytest.raises(InsufficientAssetsError):
        assert safe_math_package.get_contract_factory("SafeMathLib")


def test_get_contract_factory_throws_if_name_isnt_present(safe_math_package):
    with pytest.raises(InsufficientAssetsError):
        assert safe_math_package.get_contract_factory("DoesNotExist")


def test_get_contract_instance(deployed_safe_math):
    safe_math_package, address = deployed_safe_math
    contract_instance = safe_math_package.get_contract_instance("SafeMathLib", address)
    assert contract_instance.abi is not False
    assert is_same_address(contract_instance.address, address)


def test_get_contract_instance_throws_with_insufficient_assets(deployed_safe_math):
    safe_math_package, address = deployed_safe_math
    with pytest.raises(InsufficientAssetsError):
        assert safe_math_package.get_contract_instance("IncorrectLib", address)
    safe_math_package.manifest["contractTypes"]["SafeMathLib"].pop("abi")
    with pytest.raises(InsufficientAssetsError):
        assert safe_math_package.get_contract_instance("SafeMathLib", address)


def test_package_object_properties(safe_math_package):
    assert safe_math_package.name == "safe-math-lib"
    assert safe_math_package.version == "1.0.0"
    assert safe_math_package.manifest_version == "ethpm/3"
    assert safe_math_package.uri is None
    assert safe_math_package.__repr__() == "<Package safe-math-lib==1.0.0>"
    assert safe_math_package.contract_types == ["SafeMathLib"]
