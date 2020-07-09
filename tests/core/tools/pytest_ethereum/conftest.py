from pathlib import (
    Path,
)
import pytest

from ethpm import (
    get_ethpm_spec_dir,
)
from web3 import Web3

PYTEST_ETH_TESTS_DIR = Path(__file__).parent


@pytest.fixture
def pte_assets_dir():
    return PYTEST_ETH_TESTS_DIR / "assets"


@pytest.fixture
def w3():
    return Web3(Web3.EthereumTesterProvider())


@pytest.fixture
def ethpm_spec_dir():
    return get_ethpm_spec_dir()


@pytest.fixture
def escrow_deployer(deployer, ethpm_spec_dir):
    escrow_manifest_path = ethpm_spec_dir / "examples" / "escrow" / "v3.json"
    return deployer(escrow_manifest_path)
