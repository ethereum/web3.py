import asyncio
import pytest

from web3.utils.module_testing.emitter_contract import (
    EMITTER_ABI,
    EMITTER_BYTECODE,
)
from web3.utils.module_testing.math_contract import (
    MATH_ABI,
    MATH_BYTECODE,
)


@pytest.fixture(scope="module")
def math_contract_factory(web3):
    contract_factory = web3.eth.contract(abi=MATH_ABI, bytecode=MATH_BYTECODE)
    return contract_factory


@pytest.fixture(scope="module")
def emitter_contract_factory(web3):
    contract_factory = web3.eth.contract(abi=EMITTER_ABI, bytecode=EMITTER_BYTECODE)
    return contract_factory


@pytest.yield_fixture(scope="module")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
