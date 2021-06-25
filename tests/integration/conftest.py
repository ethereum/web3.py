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
from web3._utils.module_testing.revert_contract import (
    _REVERT_CONTRACT_ABI,
    REVERT_CONTRACT_BYTECODE,
)


def pytest_collection_modifyitems(items):
    """
    Certain tests have issues running after most of our test suite has run. If we run
    these tests in the beginning, we can ensure that the client isn't overloaded with
    context from our other tests and therefore reduce the noise for these more sensitive
    tests. We can somewhat control when tests are run by overriding this pytest hook and
    customizing the test order. You may find it helpful to move a conflicting test to
    the beginning of the test suite or configure the test order in some other way here.
    """
    test_names_to_append_to_start = [
        'test_eth_get_logs_with_logs',
        'test_eth_call_old_contract_state',
    ]
    for index, item in enumerate(items):
        # We run two versions of some tests that end with [<lambda>] or [address_conversion_func1].
        # This step cleans up the name depending on whether or not they exist as two separate
        # tests or just one without the bracketed "[]" suffix.
        test_name = item.name if "[" not in item.name else item.name[:item.name.find("[")]

        if test_name in test_names_to_append_to_start:
            test_item = items.pop(index)
            items.insert(0, test_item)


@pytest.fixture(scope="module")
def math_contract_factory(web3):
    contract_factory = web3.eth.contract(abi=MATH_ABI, bytecode=MATH_BYTECODE)
    return contract_factory


@pytest.fixture(scope="module")
def emitter_contract_factory(web3):
    contract_factory = web3.eth.contract(
        abi=CONTRACT_EMITTER_ABI, bytecode=CONTRACT_EMITTER_CODE
    )
    return contract_factory


@pytest.fixture(scope="module")
def revert_contract_factory(web3):
    contract_factory = web3.eth.contract(
        abi=_REVERT_CONTRACT_ABI, bytecode=REVERT_CONTRACT_BYTECODE
    )
    return contract_factory


@pytest.yield_fixture(scope="module")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()
