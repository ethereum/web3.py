import json
from pathlib import Path
import pytest

from eth_tester import EthereumTester
from eth_tester.backends import PyEVMBackend
from eth_utils import is_address, to_canonical_address
from ethpm import Package, ASSETS_DIR
from ethpm.contract import LinkableContract
from pytest_ethereum.plugins import twig_deployer

from web3 import Web3
from web3.pm import Registry
from ens import ENS


@pytest.fixture
def w3():
    w3 = Web3(Web3.EthereumTesterProvider())
    w3.eth.defaultAccount = w3.eth.accounts[0]
    w3.eth.defaultContractFactory = LinkableContract
    try:
        from web3.pm import PM  # noqa: F811
    except ModuleNotFoundError as exc:
        assert False, "eth-pm import failed because: %s" % exc
    PM.attach(w3, 'pm')
    return w3

# Solidity registry

def test_with_solidiy_registry_manifest(w3):
    manifest_path = ASSETS_DIR / 'registry' / "1.0.2.json"
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
    registry_path = ASSETS_DIR / 'vyper_registry'
    registry_deployer = twig_deployer(registry_path)
    registry_package = registry_deployer.deploy("registry")
    registry_instance = registry_package.deployments.get_instance("registry")
    owner = registry_instance.functions.owner().call()
    assert owner == w3.eth.accounts[0]
    return Registry(registry_instance.address, w3)

# `Registry` class tests

def test_registry_init(vy_registry, w3):
    # todo ens linking
    # update to get_package_from_uri
    assert vy_registry.registry.functions.owner().call() == w3.eth.accounts[0]

def test_registry_releases_properly(vy_registry):
    vy_registry.release(b"package",b"1.0.0",b"google.com")
    release_data = vy_registry.get_release_data(b'package', b'1.0.0')
    assert release_data[0][:7] == b'package'
    assert release_data[1][:5] == b'1.0.0'
    assert release_data[2][:10] == b'google.com'
    
def test_registry_get_all_packages(vy_registry):
    vy_registry.release(b"package1",b"1.0.0",b"p1.v1.0.0.com")
    vy_registry.release(b"package1",b"1.0.1",b"p1.v1.0.1.com")
    all_pkgs_1 = vy_registry.get_all_package_ids()
    assert all_pkgs_1 == ((b'package1', 2),)
    vy_registry.release(b"package2",b"1.0.0",b"p2.v1.0.0.com")
    vy_registry.release(b"package3",b"1.0.0",b"p3.v1.0.0.com")
    vy_registry.release(b"package3",b"1.0.1",b"p3.v1.0.1.com")
    all_pkgs_2 = vy_registry.get_all_package_ids()
    assert all_pkgs_2 == (
        (b'package1', 2),
        (b'package2', 1),
        (b'package3', 2),
    )
    vy_registry.release(b"package4",b"1.0.0",b"p2.v1.0.0.com")
    vy_registry.release(b"package5",b"1.0.0",b"p2.v1.0.0.com")
    vy_registry.release(b"package6",b"1.0.0",b"p2.v1.0.0.com")
    vy_registry.release(b"package7",b"1.0.0",b"p2.v1.0.0.com")
    all_pkgs_3 = vy_registry.get_all_package_ids()
    assert all_pkgs_3 == (
        (b'package1', 2),
        (b'package2', 1),
        (b'package3', 2),
        (b'package4', 1),
        (b'package5', 1),
        (b'package6', 1),
        (b'package7', 1),
    )

def test_registry_get_all_package_versions(vy_registry):
    vy_registry.release(b"package",b"1.0.0",b"p1.v1.0.0.com")
    vy_registry.release(b"package",b"1.0.1",b"p1.v1.0.1.com")
    vy_registry.release(b"package",b"1.0.2",b"p1.v1.0.2.com")
    vy_registry.release(b"package",b"1.1.0",b"p1.v1.1.0.com")
    vy_registry.release(b"package",b"2.0.0",b"p1.v2.0.0.com")
    all_rls_1 = vy_registry.get_all_package_versions(b"package")
    assert all_rls_1 == (
        (b'1.0.0',b'p1.v1.0.0.com'),
        (b'1.0.1',b'p1.v1.0.1.com'),
        (b'1.0.2',b'p1.v1.0.2.com'),
        (b'1.1.0',b'p1.v1.1.0.com'),
        (b'2.0.0',b'p1.v2.0.0.com'),
    )
    vy_registry.release(b"package",b"3.0.0",b"p1.v3.0.0.com")
    vy_registry.release(b"package",b"4.0.0",b"p1.v4.0.0.com")
    vy_registry.release(b"package",b"5.0.0",b"p1.v5.0.0.com")
    all_rls_2 = vy_registry.get_all_package_versions(b'package')
    assert all_rls_2 == (
        (b'1.0.0',b'p1.v1.0.0.com'),
        (b'1.0.1',b'p1.v1.0.1.com'),
        (b'1.0.2',b'p1.v1.0.2.com'),
        (b'1.1.0',b'p1.v1.1.0.com'),
        (b'2.0.0',b'p1.v2.0.0.com'),
        (b'3.0.0',b'p1.v3.0.0.com'),
        (b'4.0.0',b'p1.v4.0.0.com'),
        (b'5.0.0',b'p1.v5.0.0.com'),
    )


def test_registry_transfer_owner(vy_registry, w3):
    vy_registry.transfer_owner(w3.eth.accounts[1])
    assert vy_registry.registry.functions.owner().call() == w3.eth.accounts[1]


# web3.pm integration

def test_pm_set_registry_without_address(w3):
    w3.pm.set_registry()
    assert isinstance(w3.pm.registry, Registry)


def test_pm_set_registry_with_address(vy_registry, w3):
    w3.pm.set_registry(address=vy_registry.address)
    assert isinstance(w3.pm.registry, Registry)


def test_pm_must_set_registry_before_registry_interaction_functions(w3):
    with pytest.raises(AttributeError):
        w3.pm.release_package(b'package', b'1.0.0', b'google.com')
    with pytest.raises(AttributeError):
        w3.pm.get_release_data_from_registry(b'package', b'1.0.0')


def test_pm_release_package(w3):
    w3.pm.set_registry()
    w3.pm.release_package(b'package', b'1.0.0', b'google.com')
    package_data = w3.pm.get_release_data_from_registry(b'package', b'1.0.0')
    assert package_data[0][:7] == b'package'


def test_pm_release_package_raises_exception_with_invalid_from_address(vy_registry, w3):
    w3.pm.set_registry()
    w3.eth.defaultAccount = w3.eth.accounts[1]
    with pytest.raises(AttributeError):
        w3.pm.release_package(b'package', b'1.0.0', b'google.com')

# more integration tests
