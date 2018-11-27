import pytest

from eth_utils import (
    is_address,
    to_checksum_address,
)
from ethpm import (
    Package,
)
from ethpm.contract import (
    LinkableContract,
)

from web3 import Web3
from web3.exceptions import (
    PMError,
)
from web3.pm import (
    PM,
    ERCRegistry,
    VyperReferenceRegistry,
    get_vyper_registry_manifest,
)


@pytest.fixture
def fresh_w3():
    w3 = Web3(Web3.EthereumTesterProvider())
    w3.eth.defaultAccount = w3.eth.accounts[0]
    w3.eth.defaultContractFactory = LinkableContract
    PM.attach(w3, "pm")
    return w3


def test_pm_get_package_from_manifest(w3):
    manifest = get_vyper_registry_manifest()
    package = w3.pm.get_package_from_manifest(manifest)
    assert isinstance(package, Package)
    assert package.name == "vyper-registry"


def test_pm_deploy_and_set_registry(fresh_w3):
    assert not hasattr(fresh_w3.pm, "registry")
    registry_address = fresh_w3.pm.deploy_and_set_registry()
    assert isinstance(fresh_w3.pm.registry, VyperReferenceRegistry)
    assert is_address(registry_address)


def test_pm_set_registry_with_vyper_default(empty_vy_registry, fresh_w3):
    assert not hasattr(fresh_w3.pm, "registry")
    fresh_w3.pm.set_registry(address=to_checksum_address(empty_vy_registry.address))
    assert isinstance(fresh_w3.pm.registry, ERCRegistry)
    assert is_address(fresh_w3.pm.registry.address)


def test_pm_set_solidity_registry(empty_sol_registry, fresh_w3):
    assert not hasattr(fresh_w3.pm, "registry")
    fresh_w3.pm.registry = empty_sol_registry
    assert isinstance(fresh_w3.pm.registry, ERCRegistry)
    assert is_address(fresh_w3.pm.registry.address)


def test_pm_must_set_registry_before_all_registry_interaction_functions(fresh_w3):
    with pytest.raises(PMError):
        fresh_w3.pm.release_package(
            "package", "1.0.0", "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGe"
        )
    with pytest.raises(PMError):
        fresh_w3.pm.get_release_id_data(b"invalid_release_id")
    with pytest.raises(PMError):
        fresh_w3.pm.get_release_id("package", "1.0.0")
    with pytest.raises(PMError):
        fresh_w3.pm.get_release_data("package", "1.0.0")
    with pytest.raises(PMError):
        fresh_w3.pm.get_package("package", "1.0.0")
    with pytest.raises(PMError):
        fresh_w3.pm.get_all_package_names()
    with pytest.raises(PMError):
        fresh_w3.pm.get_all_package_releases("package")
    with pytest.raises(PMError):
        fresh_w3.pm.get_release_count("package")
    with pytest.raises(PMError):
        fresh_w3.pm.get_package_count()


@pytest.mark.parametrize(
    "registry_getter", ["empty_vy_registry", "empty_sol_registry"], indirect=True
)
def test_pm_release_package(registry_getter, w3):
    w3.pm.registry = registry_getter
    w3.pm.release_package(
        "package123", "1.0.0", "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGE"
    )
    w3.pm.release_package(
        "package456", "1.0.0", "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGI"
    )
    release_id_1 = w3.pm.get_release_id("package123", "1.0.0")
    release_id_2 = w3.pm.get_release_id("package456", "1.0.0")
    package_data_1 = w3.pm.get_release_id_data(release_id_1)
    package_data_2 = w3.pm.get_release_id_data(release_id_2)
    assert package_data_1[0] == "package123"
    assert package_data_1[1] == "1.0.0"
    assert package_data_1[2] == "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGE"
    assert package_data_2[0] == "package456"
    assert package_data_2[1] == "1.0.0"
    assert package_data_2[2] == "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGI"


@pytest.mark.parametrize(
    "registry_getter", ["loaded_vy_registry", "loaded_sol_registry"], indirect=True
)
def test_pm_get_release_data(registry_getter, w3):
    registry, _, _ = registry_getter
    w3.pm.registry = registry
    package_data = w3.pm.get_release_data("package", "1.0.0")
    assert package_data[0] == "package"
    assert package_data[1] == "1.0.0"
    assert package_data[2] == "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGV"


@pytest.mark.parametrize(
    "registry_getter", ["loaded_vy_registry", "loaded_sol_registry"], indirect=True
)
def test_pm_get_all_package_names(registry_getter, w3):
    registry, _, _ = registry_getter
    w3.pm.registry = registry
    all_pkgs = w3.pm.get_all_package_names()
    assert all_pkgs == (
        "package",
        "package1",
        "package2",
        "package3",
        "package4",
        "package5",
    )


@pytest.mark.parametrize(
    "registry_getter", ["loaded_vy_registry", "loaded_sol_registry"], indirect=True
)
def test_pm_package_count(registry_getter, w3):
    registry, _, _ = registry_getter
    w3.pm.registry = registry
    assert w3.pm.get_package_count() == 6


@pytest.mark.parametrize(
    "registry_getter", ["loaded_vy_registry", "loaded_sol_registry"], indirect=True
)
def test_pm_get_release_count(registry_getter, w3):
    registry, _, _ = registry_getter
    w3.pm.registry = registry
    pkg_0_release_count = w3.pm.get_release_count("package")
    pkg_1_release_count = w3.pm.get_release_count("package1")
    pkg_2_release_count = w3.pm.get_release_count("package2")
    assert pkg_0_release_count == 6
    assert pkg_1_release_count == 1
    assert pkg_2_release_count == 1


@pytest.mark.parametrize(
    "registry_getter", ["loaded_vy_registry", "loaded_sol_registry"], indirect=True
)
def test_pm_get_all_package_versions(registry_getter, w3):
    registry, _, _ = registry_getter
    w3.pm.registry = registry
    all_rls_pkg_0 = w3.pm.get_all_package_releases("package")
    all_rls_pkg_1 = w3.pm.get_all_package_releases("package1")
    all_rls_pkg_2 = w3.pm.get_all_package_releases("package2")
    assert all_rls_pkg_0 == (
        ("1.0.0", "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGV"),
        ("1.0.1", "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGW"),
        ("1.0.2", "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGX"),
        ("1.0.3", "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGJ"),
        ("1.0.4", "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGK"),
        ("1.0.5", "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGH"),
    )
    assert all_rls_pkg_1 == (
        ("1.0.1", "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGZ"),
    )
    assert all_rls_pkg_2 == (
        ("1.0.1", "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGT"),
    )


@pytest.mark.parametrize(
    "registry_getter", ["loaded_vy_registry", "loaded_sol_registry"], indirect=True
)
def test_pm_get_package(registry_getter, w3, monkeypatch):
    registry, _, _ = registry_getter
    w3.pm.registry = registry
    monkeypatch.setenv(
        "ETHPM_IPFS_BACKEND_CLASS", "ethpm.backends.ipfs.DummyIPFSBackend"
    )
    w3.pm.deploy_and_set_registry()
    w3.pm.release_package(
        "owned", "1.0.0", "ipfs://QmbeVyFLSuEUxiXKwSsEjef6icpdTdA4kGG9BcrJXKNKUW"
    )
    pkg = w3.pm.get_package("owned", "1.0.0")
    assert isinstance(pkg, Package)
    assert pkg.name == "owned"
