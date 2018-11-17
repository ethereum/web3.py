import json
import pytest

from eth_tester import (
    EthereumTester,
    PyEVMBackend,
)
from eth_utils import (
    function_abi_to_4byte_selector,
    is_address,
    to_canonical_address,
)
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
from pytest_ethereum import (
    linker as l,
)

from web3 import Web3
from web3.exceptions import (
    PMError,
)
from web3.pm import (
    PM,
    Registry,
)

pytest_plugins = ["pytest_ethereum.plugins"]


@pytest.fixture
def w3():
    genesis_overrides = {"gas_limit": 4500000}
    custom_genesis_params = PyEVMBackend._generate_genesis_params(
        overrides=genesis_overrides
    )
    pyevm_backend = PyEVMBackend(genesis_parameters=custom_genesis_params)
    t = EthereumTester(backend=pyevm_backend)
    w3 = Web3(Web3.EthereumTesterProvider(ethereum_tester=t))
    w3.eth.defaultAccount = w3.eth.accounts[0]
    w3.eth.defaultContractFactory = LinkableContract
    PM.attach(w3, "pm")
    return w3


def solidity_registry_strategy():
    def set_authority(package):
        w3 = package.w3
        authority = package.deployments.get_instance("WhitelistAuthority").address
        package_registry = package.deployments.get_instance("PackageRegistry")
        package_db = package.deployments.get_instance("PackageDB")
        release_db = package.deployments.get_instance("ReleaseDB")
        txh_1 = package_registry.functions.setAuthority(authority).transact()
        w3.eth.waitForTransactionReceipt(txh_1)
        txh_2 = package_db.functions.setAuthority(authority).transact()
        w3.eth.waitForTransactionReceipt(txh_2)
        txh_3 = release_db.functions.setAuthority(authority).transact()
        w3.eth.waitForTransactionReceipt(txh_3)

    def set_dependencies(package):
        w3 = package.w3
        package_db = package.deployments.get_instance("PackageDB").address
        release_db = package.deployments.get_instance("ReleaseDB").address
        release_validator = package.deployments.get_instance("ReleaseValidator").address
        package_registry = package.deployments.get_instance("PackageRegistry")
        txh_1 = package_registry.functions.setPackageDb(package_db).transact()
        w3.eth.waitForTransactionReceipt(txh_1)
        txh_2 = package_registry.functions.setReleaseDb(release_db).transact()
        w3.eth.waitForTransactionReceipt(txh_2)
        txh_3 = package_registry.functions.setReleaseValidator(
            release_validator
        ).transact()
        w3.eth.waitForTransactionReceipt(txh_3)

    def get_selector(deployments, contract, fn):
        function_abi = [
            x for x in deployments.get_instance(contract).abi if x["name"] == fn
        ][0]
        return function_abi_to_4byte_selector(function_abi)

    def set_permissions(package):
        w3 = package.w3
        deployments = package.deployments
        set_version = get_selector(deployments, "ReleaseDB", "setVersion")
        set_release = get_selector(deployments, "ReleaseDB", "setRelease")
        set_package = get_selector(deployments, "PackageDB", "setPackage")
        set_package_owner = get_selector(deployments, "PackageDB", "setPackageOwner")
        release = get_selector(deployments, "PackageRegistry", "release")
        transfer_package_owner = get_selector(
            deployments, "PackageRegistry", "transferPackageOwner"
        )
        package_db = package.deployments.get_instance("PackageDB").address
        release_db = package.deployments.get_instance("ReleaseDB").address
        package_registry = package.deployments.get_instance("PackageRegistry").address
        authority = package.deployments.get_instance("WhitelistAuthority")
        txh_1 = authority.functions.setCanCall(
            package_registry, release_db, set_release, True
        ).transact()
        w3.eth.waitForTransactionReceipt(txh_1)
        txh_2 = authority.functions.setCanCall(
            package_registry, package_db, set_package, True
        ).transact()
        w3.eth.waitForTransactionReceipt(txh_2)
        txh_3 = authority.functions.setCanCall(
            package_registry, package_db, set_package_owner, True
        ).transact()
        w3.eth.waitForTransactionReceipt(txh_3)
        txh_4 = authority.functions.setAnyoneCanCall(
            release_db, set_version, True
        ).transact()
        w3.eth.waitForTransactionReceipt(txh_4)
        txh_5 = authority.functions.setAnyoneCanCall(
            package_registry, release, True
        ).transact()
        w3.eth.waitForTransactionReceipt(txh_5)
        txh_6 = authority.functions.setAnyoneCanCall(
            package_registry, transfer_package_owner, True
        ).transact()
        w3.eth.waitForTransactionReceipt(txh_6)

    strategy = l.linker(
        l.deploy("IndexedOrderedSetLib"),
        l.link("PackageDB", "IndexedOrderedSetLib"),
        l.link("ReleaseDB", "IndexedOrderedSetLib"),
        l.deploy("PackageRegistry"),
        l.deploy("WhitelistAuthority"),
        l.deploy("PackageDB"),
        l.deploy("ReleaseDB"),
        l.deploy("ReleaseValidator"),
        l.run_python(set_authority),
        l.run_python(set_dependencies),
        l.run_python(set_permissions),
    )
    return strategy


# Solidity registry
def test_with_solidity_registry_manifest(w3, solc_deployer):
    manifest_path = ASSETS_DIR / "registry" / "1.0.4.json"
    registry_deployer = solc_deployer(manifest_path)
    strategy = solidity_registry_strategy()
    registry_deployer.register_strategy("PackageRegistry", strategy)
    registry_package = registry_deployer.deploy("PackageRegistry")
    assert isinstance(registry_package, Package)
    registry = registry_package.deployments.get_instance("PackageRegistry")
    tx1 = registry.functions.release(
        "package", "1.0.0", "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGV"
    ).transact()
    w3.eth.waitForTransactionReceipt(tx1)
    release_id = registry.functions.generateReleaseId("package", "1.0.0").call()
    release_data = registry.functions.getReleaseData(release_id).call()
    owner = registry.functions.owner().call()
    assert release_data[0] == "package"
    assert release_data[1] == "1.0.0"
    assert release_data[2] == "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGV"
    assert owner == w3.eth.defaultAccount


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
