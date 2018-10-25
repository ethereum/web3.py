import json
import pytest

from eth_utils import (
    is_address,
    to_canonical_address,
)
from ethpm import (
    ASSETS_DIR,
)
from ethpm.contract import (
    LinkableContract,
)
from ethpm.exceptions import (
    CannotHandleURI,
)
import pytest_ethereum as pte

from ethpm import (
    ASSETS_DIR,
    Package,
)
from ethpm.contract import (
    LinkableContract,
)
from ethpm.exceptions import (
    CannotHandleURI,
)
from web3 import Web3
from web3.exceptions import (
    PMError,
)
from web3.pm import (
    PM,
    Registry,
)


@pytest.fixture
def w3():
    w3 = Web3(Web3.EthereumTesterProvider())
    w3.eth.defaultAccount = w3.eth.accounts[0]
    w3.eth.defaultContractFactory = LinkableContract
    PM.attach(w3, "pm")
    return w3


# Solidity registry
def test_with_solidity_registry_manifest(w3):
    manifest_path = ASSETS_DIR / "registry" / "1.0.3.json"
    manifest = json.loads(manifest_path.read_text())
    Registry = w3.pm.get_package_from_manifest(manifest)
    assert Registry.name == "registry"
    PackageRegistryFactory = Registry.get_contract_factory("PackageRegistry")
    PackageDBFactory = Registry.get_contract_factory("PackageDB")
    ReleaseDBFactory = Registry.get_contract_factory("ReleaseDB")
    assert PackageRegistryFactory.needs_bytecode_linking is False
    assert PackageDBFactory.needs_bytecode_linking
    assert ReleaseDBFactory.needs_bytecode_linking


# Vyper registry
@pytest.fixture
def vy_registry(twig_deployer, w3):
    registry_path = ASSETS_DIR / "vyper_registry"
    registry_deployer = twig_deployer(registry_path)
    registry_package = registry_deployer.deploy("registryV2")
    registry_instance = registry_package.deployments.get_instance("registryV2")
    owner = registry_instance.functions.owner().call()
    assert owner == w3.eth.accounts[0]
    return Registry(registry_instance.address, w3)


def test_pm_get_package_from_manifest(w3):
    manifest_path = ASSETS_DIR / "vyper_registry" / "1.0.2.json"
    manifest = json.loads(manifest_path.read_text())
    package = w3.pm.get_package_from_manifest(manifest)
    assert isinstance(package, Package)
    assert package.name == "registry-v2"


def test_pm_deploy_and_set_registry(w3):
    assert not hasattr(w3.pm, "registry")
    w3.pm.deploy_and_set_registry()
    assert isinstance(w3.pm.registry, Registry)
    assert is_address(w3.pm.registry.address)


def test_pm_set_registry(vy_registry, w3):
    assert not hasattr(w3.pm, "registry")
    w3.pm.set_registry(address=to_canonical_address(vy_registry.address))
    assert isinstance(w3.pm.registry, Registry)
    assert is_address(w3.pm.registry.address)


def test_pm_must_set_registry_before_registry_interaction_functions(w3):
    with pytest.raises(PMError):
        w3.pm.release_package(
            b"package",
            b"1.0.0",
            b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGe",
        )
    with pytest.raises(PMError):
        w3.pm.get_release_data(b"package", b"1.0.0")
    with pytest.raises(PMError):
        w3.pm.get_package(b"package", b"1.0.0")


def test_pm_release_package(w3):
    w3.pm.deploy_and_set_registry()
    w3.pm.release_package(
        b"package", b"1.0.0", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGe"
    )
    package_data = w3.pm.get_release_data(b"package", b"1.0.0")
    assert package_data[0] == b"package"
    assert package_data[1] == b"1.0.0"
    assert package_data[2] == b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGe"


def test_pm_release_package_raises_exception_with_invalid_from_address(vy_registry, w3):
    w3.pm.deploy_and_set_registry()
    w3.eth.defaultAccount = w3.eth.accounts[1]
    with pytest.raises(PMError):
        w3.pm.release_package(
            b"package",
            b"1.0.0",
            b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGe",
        )


def test_pm_get_package(w3, monkeypatch):
    monkeypatch.setenv(
        "ETHPM_IPFS_BACKEND_CLASS", "ethpm.backends.ipfs.DummyIPFSBackend"
    )
    w3.pm.deploy_and_set_registry()
    w3.pm.release_package(
        b"package", b"1.0.0", b"ipfs://QmbeVyFLSuEUxiXKwSsEjef6icpdTdA4kGG9BcrJXKNKUW"
    )
    pkg = w3.pm.get_package(b"package", b"1.0.0")
    assert isinstance(pkg, Package)
    assert pkg.name == "owned"


def test_pm_get_package_raises_exception_with_invalid_uri(w3):
    w3.pm.deploy_and_set_registry()
    w3.pm.release_package(
        b"package", b"1.0.0", b"https://raw.githubusercontent.com/invalid/uri"
    )
    with pytest.raises(CannotHandleURI):
        w3.pm.get_package(b"package", b"1.0.0")
