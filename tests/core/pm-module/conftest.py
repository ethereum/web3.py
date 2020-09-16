import pytest

from eth_tester import (
    EthereumTester,
    PyEVMBackend,
)
from eth_utils import (
    to_bytes,
)

from ethpm import (
    Package,
)
from ethpm.contract import (
    LinkableContract,
)
from ethpm.tools import (
    get_ethpm_local_manifest,
)
from web3 import Web3
from web3.pm import (
    SimpleRegistry,
)
from web3.tools.pytest_ethereum.deployer import (
    Deployer,
)

SOL_PACKAGE_ID_1 = to_bytes(hexstr='0x60c5112b61159e6b42d54d945078394e9d5fc9c6ff0f3df78977006f8bbc06d4')  # noqa: E501
SOL_PACKAGE_ID_2 = to_bytes(hexstr='0xdbcfb0bd7115bf659350d77bb22bb889ca8294f61b0ca480f8a47bb8fc904cc9')  # noqa: E501
SOL_PACKAGE_ID_3 = to_bytes(hexstr='0xf3e4002c48a7f8f3485d62988317849c175340b66517c3b2993f725643eba84b')  # noqa: E501
SOL_RELEASE_ID_1 = to_bytes(hexstr='0x13414014c4f3c0ee41f1ede8e612e0377ae741f3abaa8d22e84e6b3759334fe9')  # noqa: E501
SOL_RELEASE_ID_2 = to_bytes(hexstr='0x30cb63a88e721b461e294fa212af64f12e9500b3892e0e65fa70090ab63afb4d')  # noqa: E501
SOL_RELEASE_ID_3 = to_bytes(hexstr='0x73f5fafa3d9bd5080d9b27c092cd65fdbf7c8f982df4d5d0de22eb2cd56f4fcb')  # noqa: E501
SOL_RELEASE_ID_4 = to_bytes(hexstr='0x7fc4e4c04e1a4e5cba315f8fce216f8a77e1a1dd7c6539635555f95d1042667f')  # noqa: E501


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


def sol_registry(w3):
    manifest = get_ethpm_local_manifest("simple-registry", "v3.json")
    registry_package = Package(manifest, w3)
    registry_deployer = Deployer(registry_package)
    deployed_registry_package = registry_deployer.deploy("PackageRegistry")
    assert isinstance(registry_package, Package)
    registry = deployed_registry_package.deployments.get_instance("PackageRegistry")
    return SimpleRegistry(registry.address, w3)


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
FRESH_SOL_REGISTRY = sol_registry(W3)
LOADED_SOL_REGISTRY = release_packages(sol_registry(W3))
SOL_PKG_IDS = (SOL_PACKAGE_ID_1, SOL_PACKAGE_ID_2, SOL_PACKAGE_ID_3)
SOL_RLS_IDS = (SOL_RELEASE_ID_1, SOL_RELEASE_ID_2, SOL_RELEASE_ID_3, SOL_RELEASE_ID_4)


@pytest.fixture
def w3():
    return W3


@pytest.fixture
def empty_sol_registry():
    return FRESH_SOL_REGISTRY


@pytest.fixture
def loaded_sol_registry():
    return LOADED_SOL_REGISTRY, SOL_PKG_IDS, SOL_RLS_IDS
