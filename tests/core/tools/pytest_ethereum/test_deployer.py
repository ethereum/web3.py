import logging
import pytest

from eth_utils import (
    is_address,
)

from ethpm import (
    ASSETS_DIR,
)
import web3
from web3.tools.pytest_ethereum.exceptions import (
    DeployerError,
)

logging.getLogger("evm").setLevel(logging.INFO)


#
# Vyper Contracts
#


# User Code
@pytest.fixture
def greeter(deployer, pte_assets_dir):
    return deployer(pte_assets_dir / "greeter.json").deploy("greeter")


def test_user_code_with_fixture(greeter):
    greeter_instance = greeter.deployments.get_instance("greeter")
    assert isinstance(greeter_instance, web3.contract.Contract)
    greeting = greeter_instance.functions.greet().call()
    assert greeting == b"Hello"


#
# Solidity Compiler Output
#


# SIMPLE
@pytest.fixture
def owned(deployer):
    owned_manifest_path = ASSETS_DIR / "owned" / "with_contract_type_v3.json"
    owned_deployer = deployer(path=owned_manifest_path)
    return owned_deployer.deploy("Owned")


def test_owned_deployer(owned):
    owned_contract_instance = owned.deployments.get_instance("Owned")
    assert is_address(owned_contract_instance.address)


# CONSTRUCTOR ARGS
@pytest.fixture
def standard_token(deployer):
    standard_token_manifest_path = ASSETS_DIR / "standard-token" / "with_bytecode_v3.json"
    standard_token_deployer = deployer(standard_token_manifest_path)
    return standard_token_deployer.deploy("StandardToken", 100)


def test_standard_token_deployer(standard_token):
    standard_token_instance = standard_token.deployments.get_instance("StandardToken")
    assert standard_token_instance.functions.totalSupply().call() == 100


# LIBRARY
@pytest.fixture
def safe_math(deployer, ethpm_spec_dir):
    safe_math_manifest_path = ethpm_spec_dir / "examples" / "safe-math-lib" / "v3.json"
    safe_math_deployer = deployer(safe_math_manifest_path)
    return safe_math_deployer.deploy("SafeMathLib")


def test_safe_math_deployer(safe_math):
    safe_math_instance = safe_math.deployments.get_instance("SafeMathLib")
    assert is_address(safe_math_instance.address)


def test_escrow_deployer_unlinked(escrow_deployer):
    with pytest.raises(DeployerError):
        escrow_deployer.deploy("Escrow", escrow_deployer.package.w3.eth.accounts[0])
