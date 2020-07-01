from pathlib import (
    Path,
)
import pytest

from ethpm import (
    ETHPM_SPEC_DIR,
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
def escrow_deployer(deployer):
    escrow_manifest_path = ETHPM_SPEC_DIR / "examples" / "escrow" / "v3.json"
    return deployer(escrow_manifest_path)
