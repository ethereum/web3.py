import json
from pathlib import (
    Path,
)
import pytest

from web3 import Web3

try:
    from web3.pm import PM
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
    PM.attach(w3, 'pm')
    return w3


@pytest.fixture
def owned_manifest():
    with open(str(V2_PACKAGES_DIR / 'owned' / '1.0.0.json')) as file_obj:
        return json.load(file_obj)


@pytest.mark.skipif(ethpm_installed is False, reason="ethpm is not installed")
def test_pm_init_with_minimal_manifest(web3, owned_manifest):
    pm = web3.pm.get_package_from_manifest(owned_manifest)
    assert pm.name == 'owned'


@pytest.mark.skipif(ethpm_installed is False, reason="ethpm is not installed")
def test_get_contract_type_raises_insufficient_assets_error(web3, owned_manifest):
    owned_package = web3.pm.get_package_from_manifest(owned_manifest)
    with pytest.raises(InsufficientAssetsError):
        owned_package.get_contract_factory('owned')
