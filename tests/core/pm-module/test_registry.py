import json
import pytest

from eth_utils import (
    is_address,
)
import pytest_ethereum as pte

from ethpm import (
    ASSETS_DIR,
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


def test_registry_init(vy_registry, w3):
    assert vy_registry.registry.functions.owner().call() == w3.eth.accounts[0]


def test_registry_init_deploy_new_instance(w3):
    registry = Registry.deploy_new_instance(w3)
    assert isinstance(registry, Registry)
    assert is_address(registry.address)


def test_registry_releases_properly(vy_registry):
    # uri > 32 bytes
    vy_registry.release(
        b"package", b"1.0.0", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGV"
    )
    # uri = 32 bytes
    vy_registry.release(b"package", b"1.0.2", b"ipfs://Qme4otpS88NV8yQi8TfTP89Es")
    # uri < 32 bytes
    vy_registry.release(b"package", b"1.0.1", b"ipfs://Qme4otpS88N")
    release_data = vy_registry.get_release_data(b"package", b"1.0.0")
    release_data_2 = vy_registry.get_release_data(b"package", b"1.0.1")
    assert release_data[0][:7] == b"package"
    assert release_data[1][:5] == b"1.0.0"
    assert release_data[2] == b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGV"
    assert release_data_2[2] == b"ipfs://Qme4otpS88N"


def test_registry_release_raises_exception_for_invalid_types(vy_registry):
    with pytest.raises(PMError):
        vy_registry.release(
            "package", b"1.0.0", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi"
        )
    with pytest.raises(PMError):
        vy_registry.release(
            b"package", "1.0.0", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi"
        )
    with pytest.raises(PMError):
        vy_registry.release(
            b"package", b"1.0.0", "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi"
        )
    # uri > 64 bytes (not currently supported)
    with pytest.raises(PMError):
        vy_registry.release(
            b"package",
            b"1.0.0",
            b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGV123abc123abc1",
        )


def test_registry_get_all_package_names(vy_registry):
    vy_registry.release(
        b"package1", b"1.0.0", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGV"
    )
    vy_registry.release(
        b"package1", b"1.0.1", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGU"
    )
    all_pkgs_1 = vy_registry.get_all_package_names()
    assert all_pkgs_1 == (b"package1",)
    vy_registry.release(
        b"package2", b"1.0.0", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGT"
    )
    vy_registry.release(
        b"package3", b"1.0.0", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGx"
    )
    vy_registry.release(
        b"package3", b"1.0.1", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGA"
    )
    all_pkgs_2 = vy_registry.get_all_package_names()
    assert all_pkgs_2 == (b"package1", b"package2", b"package3")
    vy_registry.release(
        b"package4", b"1.0.0", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGb"
    )
    vy_registry.release(
        b"package5", b"1.0.0", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGC"
    )
    vy_registry.release(
        b"package6", b"1.0.0", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGs"
    )
    vy_registry.release(
        b"package7", b"1.0.0", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGZ"
    )
    all_pkgs_3 = vy_registry.get_all_package_names()
    assert all_pkgs_3 == (
        b"package1",
        b"package2",
        b"package3",
        b"package4",
        b"package5",
        b"package6",
        b"package7",
    )


def test_registry_get_release_count(vy_registry):
    vy_registry.release(
        b"package1", b"1.0.0", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGa"
    )
    vy_registry.release(
        b"package1", b"1.0.1", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGb"
    )
    vy_registry.release(
        b"package2", b"1.0.0", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGc"
    )
    vy_registry.release(
        b"package2", b"1.0.1", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGd"
    )
    vy_registry.release(
        b"package2", b"1.0.2", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGe"
    )
    pkg_1_release_count = vy_registry.get_release_count(b"package1")
    pkg_2_release_count = vy_registry.get_release_count(b"package2")
    assert pkg_1_release_count == 2
    assert pkg_2_release_count == 3
    vy_registry.release(
        b"package2", b"1.0.3", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGf"
    )
    pkg_2_release_count_2 = vy_registry.get_release_count(b"package2")
    assert pkg_2_release_count_2 == 4
    # nonexistent package
    with pte.tx_fail():
        vy_registry.get_release_count(b"nope")


def test_registry_get_all_package_versions(vy_registry):
    vy_registry.release(
        b"package", b"1.0.0", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGa"
    )
    vy_registry.release(
        b"package", b"1.0.1", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGb"
    )
    vy_registry.release(
        b"package", b"1.0.2", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGc"
    )
    vy_registry.release(
        b"package", b"1.1.0", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGd"
    )
    vy_registry.release(
        b"package", b"2.0.0", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGe"
    )
    all_rls_1 = vy_registry.get_all_package_versions(b"package")
    assert all_rls_1 == (
        (b"1.0.0", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGa"),
        (b"1.0.1", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGb"),
        (b"1.0.2", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGc"),
        (b"1.1.0", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGd"),
        (b"2.0.0", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGe"),
    )
    vy_registry.release(
        b"package", b"3.0.0", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGf"
    )
    vy_registry.release(
        b"package", b"4.0.0", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGg"
    )
    vy_registry.release(
        b"package", b"5.0.0", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGh"
    )
    all_rls_2 = vy_registry.get_all_package_versions(b"package")
    assert all_rls_2 == (
        (b"1.0.0", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGa"),
        (b"1.0.1", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGb"),
        (b"1.0.2", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGc"),
        (b"1.1.0", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGd"),
        (b"2.0.0", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGe"),
        (b"3.0.0", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGf"),
        (b"4.0.0", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGg"),
        (b"5.0.0", b"ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGh"),
    )


def test_registry_transfer_owner(vy_registry, w3):
    vy_registry.transfer_owner(w3.eth.accounts[1])
    assert vy_registry.registry.functions.owner().call() == w3.eth.accounts[1]
    # default account no longer registry owner
    with pte.tx_fail():
        vy_registry.transfer_owner(w3.eth.accounts[2])
