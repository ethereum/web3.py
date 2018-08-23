import json
from pathlib import (
    Path,
)
import pytest

from web3 import Web3

try:
    from web3.pm import PM  # noqa: F401
    from ethpm import Package  # noqa: E402
    from ethpm.exceptions import InsufficientAssetsError
except ImportError:
    ethpm_installed = False
else:
    ethpm_installed = True


V2_PACKAGES_DIR = Path(__file__).parent / 'packages'


# Returns web3 instance with `pm` module attached
@pytest.fixture
def web3():
    w3 = Web3(Web3.EthereumTesterProvider())
    w3.eth.defaultAccount = w3.eth.accounts[0]
    try:
        from web3.pm import PM  # noqa: F811
    except ModuleNotFoundError as exc:
        assert False, "eth-pm import failed because: %s" % exc
    PM.attach(w3, 'pm')
    return w3


@pytest.fixture
def owned_manifest():
    with open(str(V2_PACKAGES_DIR / 'owned' / '1.0.0.json')) as file_obj:
        return json.load(file_obj)


@pytest.fixture
def standard_token_manifest():
    with open(str(V2_PACKAGES_DIR / 'standard-token' / '1.0.0.json')) as file_obj:
        return json.load(file_obj)


@pytest.mark.skipif(ethpm_installed is False, reason="ethpm is not installed")
def test_pm_init_with_minimal_manifest(web3, owned_manifest):
    pm = web3.pm.get_package_from_manifest(owned_manifest)
    assert pm.name == 'owned'


@pytest.mark.skipif(ethpm_installed is False, reason="ethpm is not installed")
def test_get_contract_factory_raises_insufficient_assets_error(web3, owned_manifest):
    owned_package = web3.pm.get_package_from_manifest(owned_manifest)
    with pytest.raises(InsufficientAssetsError):
        owned_package.get_contract_factory('owned')


@pytest.mark.skipif(ethpm_installed is False, reason="ethpm is not installed")
def test_deploy_a_standalone_package_integration(web3, standard_token_manifest):
    token_package = web3.pm.get_package_from_manifest(standard_token_manifest)
    # Added deployment bytecode to manifest to be able to generate factory
    ERC20 = token_package.get_contract_factory('StandardToken')
    # totalSupply = 100
    tx_hash = ERC20.constructor(100).transact()
    tx_receipt = web3.eth.getTransactionReceipt(tx_hash)
    address = tx_receipt["contractAddress"]
    erc20 = web3.eth.contract(address=address, abi=ERC20.abi)
    total_supply = erc20.functions.totalSupply().call()
    assert total_supply == 100


@pytest.mark.skipif(ethpm_installed is False, reason="ethpm is not installed")
def test_pm_init_with_manifest_uri(web3, monkeypatch):
    monkeypatch.setenv(
        "ETHPM_IPFS_BACKEND_CLASS", "ethpm.backends.ipfs.DummyIPFSBackend"
    )
    dummy_standard_token_uri = "ipfs://QmVu9zuza5mkJwwcFdh2SXBugm1oSgZVuEKkph9XLsbUwg"
    pkg = web3.pm.get_package_from_uri(dummy_standard_token_uri)
    assert isinstance(pkg, Package)
