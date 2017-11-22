import pytest

from web3.utils.module_testing.math_contract import (
    MATH_BYTECODE,
    MATH_ABI,
)
from web3.utils.module_testing.emitter_contract import (
    EMITTER_BYTECODE,
    EMITTER_ABI,
)


@pytest.fixture(scope="session")
def math_contract_factory(web3):
    contract_factory = web3.eth.contract(abi=MATH_ABI, bytecode=MATH_BYTECODE)
    return contract_factory


@pytest.fixture(scope="session")
def emitter_contract_factory(web3):
    contract_factory = web3.eth.contract(abi=EMITTER_ABI, bytecode=EMITTER_BYTECODE)
    return contract_factory
