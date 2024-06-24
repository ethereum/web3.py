import functools
import pytest

from eth_utils import (
    apply_key_map,
)
import pytest_asyncio

from tests.core.filtering.utils import (
    _async_emitter_fixture_logic,
    _async_w3_fixture_logic,
    _emitter_fixture_logic,
    _w3_fixture_logic,
)
from tests.utils import (
    async_partial,
)


@pytest.fixture(
    scope="function",
    params=[True, False],
    ids=["LocalFilterMiddleware", "node_based_filter"],
)
def w3(request):
    return _w3_fixture_logic(request)


@pytest.fixture
def emitter_contract_factory(w3, emitter_contract_data):
    return w3.eth.contract(**emitter_contract_data)


@pytest.fixture
def emitter(
    w3,
    emitter_contract_factory,
    wait_for_transaction,
    wait_for_block,
    address_conversion_func,
):
    return _emitter_fixture_logic(
        w3,
        emitter_contract_factory,
        wait_for_transaction,
        wait_for_block,
        address_conversion_func,
    )


def return_filter(contract, args):
    event_name = args[0]
    kwargs = apply_key_map({"filter": "argument_filters"}, args[1])
    if "from_block" not in kwargs:
        kwargs["from_block"] = "latest"
    return contract.events[event_name].create_filter(**kwargs)


@pytest.fixture(scope="module")
def create_filter(request):
    return functools.partial(return_filter)


# --- async --- #


@pytest_asyncio.fixture(
    scope="function",
    params=[True, False],
    ids=["LocalFilterMiddleware", "node_based_filter"],
)
async def async_w3(request):
    return await _async_w3_fixture_logic(request)


@pytest.fixture
def async_emitter_contract_factory(async_w3, emitter_contract_data):
    return async_w3.eth.contract(**emitter_contract_data)


@pytest_asyncio.fixture
async def async_emitter(
    async_w3,
    async_emitter_contract_factory,
    async_wait_for_transaction,
    async_wait_for_block,
    address_conversion_func,
):
    return await _async_emitter_fixture_logic(
        async_w3,
        async_emitter_contract_factory,
        async_wait_for_transaction,
        async_wait_for_block,
        address_conversion_func,
    )


async def async_return_filter(contract, args):
    event_name = args[0]
    kwargs = apply_key_map({"filter": "argument_filters"}, args[1])
    if "from_block" not in kwargs:
        kwargs["from_block"] = "latest"
    return await contract.events[event_name].create_filter(**kwargs)


@pytest_asyncio.fixture(scope="module")
async def async_create_filter(request):
    return async_partial(async_return_filter)
