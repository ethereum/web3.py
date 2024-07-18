import asyncio
import pytest

from web3._utils.contract_sources.contract_data.emitter_contract import (
    EMITTER_CONTRACT_ABI,
    EMITTER_CONTRACT_BYTECODE,
)
from web3._utils.contract_sources.contract_data.math_contract import (
    MATH_CONTRACT_ABI,
    MATH_CONTRACT_BYTECODE,
)
from web3._utils.contract_sources.contract_data.offchain_lookup import (
    OFFCHAIN_LOOKUP_ABI,
    OFFCHAIN_LOOKUP_BYTECODE,
)
from web3._utils.contract_sources.contract_data.revert_contract import (
    REVERT_CONTRACT_ABI,
    REVERT_CONTRACT_BYTECODE,
)


@pytest.fixture(scope="module")
def math_contract_factory(w3):
    contract_factory = w3.eth.contract(
        abi=MATH_CONTRACT_ABI, bytecode=MATH_CONTRACT_BYTECODE
    )
    return contract_factory


@pytest.fixture(scope="module")
def emitter_contract_factory(w3):
    contract_factory = w3.eth.contract(
        abi=EMITTER_CONTRACT_ABI, bytecode=EMITTER_CONTRACT_BYTECODE
    )
    return contract_factory


@pytest.fixture(scope="module")
def revert_contract_factory(w3):
    contract_factory = w3.eth.contract(
        abi=REVERT_CONTRACT_ABI, bytecode=REVERT_CONTRACT_BYTECODE
    )
    return contract_factory


@pytest.fixture(scope="module")
def offchain_lookup_contract_factory(w3):
    contract_factory = w3.eth.contract(
        abi=OFFCHAIN_LOOKUP_ABI, bytecode=OFFCHAIN_LOOKUP_BYTECODE
    )
    return contract_factory


@pytest.fixture(scope="module")
def async_offchain_lookup_contract_factory(async_w3):
    contract_factory = async_w3.eth.contract(
        abi=OFFCHAIN_LOOKUP_ABI, bytecode=OFFCHAIN_LOOKUP_BYTECODE
    )
    return contract_factory


@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(autouse=True)
def _async_test_setup(request) -> None:
    # Check if the 'async_w3' fixture is available in the current context
    if "async_w3" in request.fixturenames:
        async_w3 = request.getfixturevalue("async_w3")
        if hasattr(async_w3.provider, "_request_processor"):
            # Clear the request processor cache for persistent connection provider tests
            async_w3.provider._request_processor.clear_caches()
    yield
