import json
import pytest

from eth_tester import (
    EthereumTester,
    PyEVMBackend,
)
from eth_utils import (
    function_abi_to_4byte_selector,
    to_bytes,
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
    linker,
)
from pytest_ethereum.deployer import (
    Deployer,
)

from web3 import Web3
from web3.pm import (
    SolidityReferenceRegistry,
    VyperReferenceRegistry,
)

VY_PACKAGE_ID_1 = to_bytes(hexstr='0xd059e8a6ea5a8bbf8dd097a7b8922316dcb7f024e8220b56d3c9e7188a6a7640')  # noqa: E501
VY_PACKAGE_ID_2 = to_bytes(hexstr='0x6df709a85698ad921462b8979547e3a873e22e1c73b1cb691f9376847fb2d402')  # noqa: E501
VY_PACKAGE_ID_3 = to_bytes(hexstr='0x80e41a42e3b8c3af0ea51c3fd50d481eef1367dd9d3797ba93d35dcf60660882')  # noqa: E501
VY_RELEASE_ID_1 = to_bytes(hexstr='0x595e26f1b2247bacc57e32807f8059e0b0837dd9c47e6946994196bd29c9ca97')  # noqa: E501
VY_RELEASE_ID_2 = to_bytes(hexstr='0x04592cb9ced5413e1b09e87b089bf696a05efb76ee87c8c41259635fac6d938a')  # noqa: E501
VY_RELEASE_ID_3 = to_bytes(hexstr='0xa06dbc51f8891894778ce03dc23d706d228c99789595758bd3dcac3a93f47f0a')  # noqa: E501
VY_RELEASE_ID_4 = to_bytes(hexstr='0x9c6f87dda6435b2506e81206b39ed782a44b92d826c24ab02bbded321b86e2ad')  # noqa: E501
SOL_PACKAGE_ID_1 = to_bytes(hexstr='0x60c5112b61159e6b42d54d945078394e9d5fc9c6ff0f3df78977006f8bbc06d4')  # noqa: E501
SOL_PACKAGE_ID_2 = to_bytes(hexstr='0xdbcfb0bd7115bf659350d77bb22bb889ca8294f61b0ca480f8a47bb8fc904cc9')  # noqa: E501
SOL_PACKAGE_ID_3 = to_bytes(hexstr='0xf3e4002c48a7f8f3485d62988317849c175340b66517c3b2993f725643eba84b')  # noqa: E501
SOL_RELEASE_ID_1 = to_bytes(hexstr='0x73835668f71c7ae85cbdcdbb5a9905fa420ffe85a847d283fa9beefcd56cacc4')  # noqa: E501
SOL_RELEASE_ID_2 = to_bytes(hexstr='0xe5ef0292a3b36b6ac2be07ee92df61be15e0b9f102df32cbe3f0c012ef69d462')  # noqa: E501
SOL_RELEASE_ID_3 = to_bytes(hexstr='0x1280148e0af5c47e95b41df15734d0726c7320fc4cf21efe3923fb047b53899d')  # noqa: E501
SOL_RELEASE_ID_4 = to_bytes(hexstr='0x7082e954e4fd6adf8a25c6cefe218f32ec66d8a197197f1d05aa67a65caf5111')  # noqa: E501


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
    w3.enable_unstable_package_management_api()
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

    strategy = linker.linker(
        linker.deploy("IndexedOrderedSetLib"),
        linker.link("PackageDB", "IndexedOrderedSetLib"),
        linker.link("ReleaseDB", "IndexedOrderedSetLib"),
        linker.deploy("PackageRegistry"),
        linker.deploy("WhitelistAuthority"),
        linker.deploy("PackageDB"),
        linker.deploy("ReleaseDB"),
        linker.deploy("ReleaseValidator"),
        linker.run_python(set_authority),
        linker.run_python(set_dependencies),
        linker.run_python(set_permissions),
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
    manifest = json.loads((registry_path / "0.1.0.json").read_text().rstrip('\n'))
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
