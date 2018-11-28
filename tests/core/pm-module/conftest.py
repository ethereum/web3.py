import json
import logging
import pytest
import sys

from eth_tester import (
    EthereumTester,
    PyEVMBackend,
)
from eth_utils import (
    function_abi_to_4byte_selector,
    to_canonical_address,
)
from ethpm import (
    ASSETS_DIR,
    Package,
)
from ethpm.contract import (
    LinkableContract,
)
from pytest_ethereum import (
    linker as l,
)
from pytest_ethereum.deployer import (
    Deployer,
)
from pytest_ethereum.plugins import (
    twig_manifest,
)

from web3 import Web3
from web3.pm import (
    PM,
    SolidityReferenceRegistry,
    VyperReferenceRegistry,
)

VY_PACKAGE_ID_1 = b'\xd0Y\xe8\xa6\xeaZ\x8b\xbf\x8d\xd0\x97\xa7\xb8\x92#\x16\xdc\xb7\xf0$\xe8"\x0bV\xd3\xc9\xe7\x18\x8ajv@'  # noqa: E501
VY_PACKAGE_ID_2 = b"m\xf7\t\xa8V\x98\xad\x92\x14b\xb8\x97\x95G\xe3\xa8s\xe2.\x1cs\xb1\xcbi\x1f\x93v\x84\x7f\xb2\xd4\x02"  # noqa: E501
VY_PACKAGE_ID_3 = b"\x80\xe4\x1aB\xe3\xb8\xc3\xaf\x0e\xa5\x1c?\xd5\rH\x1e\xef\x13g\xdd\x9d7\x97\xba\x93\xd3]\xcf`f\x08\x82"  # noqa: E501
VY_RELEASE_ID_1 = b"Y^&\xf1\xb2${\xac\xc5~2\x80\x7f\x80Y\xe0\xb0\x83}\xd9\xc4~iF\x99A\x96\xbd)\xc9\xca\x97"  # noqa: E501
VY_RELEASE_ID_2 = b"\x04Y,\xb9\xce\xd5A>\x1b\t\xe8{\x08\x9b\xf6\x96\xa0^\xfbv\xee\x87\xc8\xc4\x12Yc_\xacm\x93\x8a"  # noqa: E501
VY_RELEASE_ID_3 = b'\xa0m\xbcQ\xf8\x89\x18\x94w\x8c\xe0=\xc2=pm"\x8c\x99x\x95\x95u\x8b\xd3\xdc\xac:\x93\xf4\x7f\n'  # noqa: E501
VY_RELEASE_ID_4 = b"\x9co\x87\xdd\xa6C[%\x06\xe8\x12\x06\xb3\x9e\xd7\x82\xa4K\x92\xd8&\xc2J\xb0+\xbd\xed2\x1b\x86\xe2\xad"  # noqa: E501
SOL_PACKAGE_ID_1 = b"`\xc5\x11+a\x15\x9ekB\xd5M\x94Px9N\x9d_\xc9\xc6\xff\x0f=\xf7\x89w\x00o\x8b\xbc\x06\xd4"  # noqa: E501
SOL_PACKAGE_ID_2 = b"\xdb\xcf\xb0\xbdq\x15\xbfe\x93P\xd7{\xb2+\xb8\x89\xca\x82\x94\xf6\x1b\x0c\xa4\x80\xf8\xa4{\xb8\xfc\x90L\xc9"  # noqa: E501
SOL_PACKAGE_ID_3 = b"\xf3\xe4\x00,H\xa7\xf8\xf3H]b\x98\x83\x17\x84\x9c\x17S@\xb6e\x17\xc3\xb2\x99?rVC\xeb\xa8K"  # noqa: E501
SOL_RELEASE_ID_1 = b"s\x83Vh\xf7\x1cz\xe8\\\xbd\xcd\xbbZ\x99\x05\xfaB\x0f\xfe\x85\xa8G\xd2\x83\xfa\x9b\xee\xfc\xd5l\xac\xc4"  # noqa: E501
SOL_RELEASE_ID_2 = b"\xe5\xef\x02\x92\xa3\xb3kj\xc2\xbe\x07\xee\x92\xdfa\xbe\x15\xe0\xb9\xf1\x02\xdf2\xcb\xe3\xf0\xc0\x12\xefi\xd4b"  # noqa: E501
SOL_RELEASE_ID_3 = b"\x12\x80\x14\x8e\n\xf5\xc4~\x95\xb4\x1d\xf1W4\xd0rls \xfcL\xf2\x1e\xfe9#\xfb\x04{S\x89\x9d"  # noqa: E501
SOL_RELEASE_ID_4 = b"p\x82\xe9T\xe4\xfdj\xdf\x8a%\xc6\xce\xfe!\x8f2\xecf\xd8\xa1\x97\x19\x7f\x1d\x05\xaag\xa6\\\xafQ\x11"  # noqa: E501


logging.basicConfig(stream=sys.stdout, level=logging.INFO, format="%(message)s")


def setup_w3():
    genesis_overrides = {"gas_limit": 5500000}
    custom_genesis_params = PyEVMBackend._generate_genesis_params(
        overrides=genesis_overrides
    )
    pyevm_backend = PyEVMBackend(genesis_parameters=custom_genesis_params)
    t = EthereumTester(backend=pyevm_backend)
    w3 = Web3(Web3.EthereumTesterProvider(ethereum_tester=t))
    w3.eth.defaultAccount = w3.eth.accounts[0]
    w3.eth.defaultContractFactory = LinkableContract
    PM.attach(w3, 'pm')
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


def sol_registry(w3):
    manifest = json.loads((ASSETS_DIR / "registry" / "1.0.0.json").read_text())
    strategy = solidity_registry_strategy()
    registry_package = Package(manifest, w3)
    registry_deployer = Deployer(registry_package)
    registry_deployer.register_strategy("PackageRegistry", strategy)
    deployed_registry_package = registry_deployer.deploy("PackageRegistry")
    assert isinstance(registry_package, Package)
    registry = deployed_registry_package.deployments.get_instance("PackageRegistry")
    return SolidityReferenceRegistry(to_canonical_address(registry.address), w3)


def vy_registry(w3):
    registry_path = ASSETS_DIR / "vyper_registry"
    manifest = twig_manifest(registry_path, "registry", "1.0.0")
    registry_package = Package(manifest, w3)
    registry_deployer = Deployer(registry_package)
    deployed_registry_package = registry_deployer.deploy("registry")
    registry_instance = deployed_registry_package.deployments.get_instance("registry")
    assert registry_instance.functions.owner().call() == w3.eth.defaultAccount
    return VyperReferenceRegistry(to_canonical_address(registry_instance.address), w3)


def release_packages(registry):
    registry._release(
        "package", "1.0.0", "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGV"
    )
    registry._release(
        "package", "1.0.1", "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGW"
    )
    registry._release(
        "package", "1.0.2", "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGX"
    )
    registry._release(
        "package", "1.0.3", "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGJ"
    )
    registry._release(
        "package", "1.0.4", "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGK"
    )
    registry._release(
        "package", "1.0.5", "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGH"
    )
    registry._release(
        "package1", "1.0.1", "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGZ"
    )
    registry._release(
        "package2", "1.0.1", "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGT"
    )
    registry._release(
        "package3", "1.0.0", "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGA"
    )
    registry._release(
        "package4", "1.0.0", "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGB"
    )
    registry._release(
        "package5", "1.0.0", "ipfs://Qme4otpS88NV8yQi8TfTP89EsQC5bko3F5N1yhRoi6cwGC"
    )
    return registry


# Module-level variables used here for efficiency
# Tests are written against the sample packages released in `release_packages()` above, if more
# tests are needed, they should take into account the releases that exist on a "loaded registry".
W3 = setup_w3()
FRESH_VY_REGISTRY = vy_registry(W3)
FRESH_SOL_REGISTRY = sol_registry(W3)
LOADED_VY_REGISTRY = release_packages(vy_registry(W3))
LOADED_SOL_REGISTRY = release_packages(sol_registry(W3))
VY_PKG_IDS = (VY_PACKAGE_ID_1, VY_PACKAGE_ID_2, VY_PACKAGE_ID_3)
SOL_PKG_IDS = (SOL_PACKAGE_ID_1, SOL_PACKAGE_ID_2, SOL_PACKAGE_ID_3)
VY_RLS_IDS = (VY_RELEASE_ID_1, VY_RELEASE_ID_2, VY_RELEASE_ID_3, VY_RELEASE_ID_4)
SOL_RLS_IDS = (SOL_RELEASE_ID_1, SOL_RELEASE_ID_2, SOL_RELEASE_ID_3, SOL_RELEASE_ID_4)


@pytest.fixture
def w3():
    return W3


@pytest.fixture
def empty_vy_registry():
    return FRESH_VY_REGISTRY


@pytest.fixture
def empty_sol_registry():
    return FRESH_SOL_REGISTRY


@pytest.fixture
def loaded_vy_registry():
    return LOADED_VY_REGISTRY, VY_PKG_IDS, VY_RLS_IDS


@pytest.fixture
def loaded_sol_registry():
    return LOADED_SOL_REGISTRY, SOL_PKG_IDS, SOL_RLS_IDS


@pytest.fixture
def registry_getter(request):
    return request.getfixturevalue(request.param)
