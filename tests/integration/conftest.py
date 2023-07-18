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

# --- integration test configurations --- #


def pytest_collection_modifyitems(items, config):
    """
    It is ideal to keep this configuration as simple as possible so that we don't
    risk missing some tests.
    """
    # TODO: See if there is a better way to address the timeout issues present
    #  in unlocked account tests.

    flaky_tests = []
    non_flaky_tests = []

    for item in items:
        if (
            # Unlocked account tests are problematic - separate them into their own
            # test run.
            any(
                _ in item.fixturenames
                for _ in (
                    "async_unlocked_account",
                    "async_unlocked_account_dual_type",
                    "unlocked_account",
                    "unlocked_account_dual_type",
                )
            )
            # Leave offchain_lookup tests split between eth sync and async tests as
            # those can conflict with each other as well.
            and "offchain_lookup" not in item.name
        ):
            flaky_tests.append(item)
        else:
            non_flaky_tests.append(item)

    if config.option.flaky:
        items[:] = flaky_tests
        config.hook.pytest_deselected(items=non_flaky_tests)
    else:
        items[:] = non_flaky_tests
        config.hook.pytest_deselected(items=flaky_tests)


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
