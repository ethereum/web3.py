import asyncio
import pytest

from web3._utils.module_testing.emitter_contract import (
    CONTRACT_EMITTER_ABI,
    CONTRACT_EMITTER_CODE,
)
from web3._utils.module_testing.math_contract import (
    MATH_ABI,
    MATH_BYTECODE,
)
from web3._utils.module_testing.offchain_lookup_contract import (
    OFFCHAIN_LOOKUP_ABI,
    OFFCHAIN_LOOKUP_BYTECODE,
)
from web3._utils.module_testing.revert_contract import (
    _REVERT_CONTRACT_ABI,
    REVERT_CONTRACT_BYTECODE,
)


def pytest_addoption(parser):
    parser.addoption("--flaky")


def pytest_collection_modifyitems(items, config):
    flaky_tests = []
    non_flaky_tests = []

    for item in items:
        if any(_ in item.fixturenames for _ in (
                "unlocked_account", "unlocked_account_dual_type"
        )) or "offchain_lookup" in item.name:
            flaky_tests.append(item)
        else:
            non_flaky_tests.append(item)

    if config.option.flaky == "True":
        items[:] = flaky_tests
        config.hook.pytest_deselected(items=non_flaky_tests)
    else:
        items[:] = non_flaky_tests
        config.hook.pytest_deselected(items=flaky_tests)


@pytest.fixture(scope="module")
def math_contract_factory(w3):
    contract_factory = w3.eth.contract(abi=MATH_ABI, bytecode=MATH_BYTECODE)
    return contract_factory


@pytest.fixture(scope="module")
def emitter_contract_factory(w3):
    contract_factory = w3.eth.contract(
        abi=CONTRACT_EMITTER_ABI, bytecode=CONTRACT_EMITTER_CODE
    )
    return contract_factory


@pytest.fixture(scope="module")
def revert_contract_factory(w3):
    contract_factory = w3.eth.contract(
        abi=_REVERT_CONTRACT_ABI, bytecode=REVERT_CONTRACT_BYTECODE
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
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
