import pytest

from hexbytes import (
    HexBytes,
)

from web3 import Web3
from web3.datastructures import (
    AttributeDict,
)
from web3.middleware import (
    construct_result_generator_middleware,
    local_filter_middleware,
)
from web3.middleware.filter import (
    block_ranges,
    iter_latest_block_ranges,
)
from web3.providers.base import (
    BaseProvider,
)


class DummyProvider(BaseProvider):
    def make_request(self, method, params):
        raise NotImplementedError(f"Cannot make request for {method}:{params}")


BLOCK_HASH = '0xfe88c94d860f01a17f961bf4bdfb6e0c6cd10d3fda5cc861e805ca1240c58553'
FILTER_LOG = [AttributeDict({'address': '0xDc3A9Db694BCdd55EBaE4A89B22aC6D12b3F0c24', 'blockHash': HexBytes('0xb72256286ca528e09022ffd408856a73ef90e7216ac560187c6e43b4c4efd2f0'), 'blockNumber': 2217196, 'data': '0x0000000000000000000000000000000000000000000000000000000000000001', 'logIndex': 0, 'topics': [HexBytes('0xe65b00b698ba37c614af350761c735c5f4a82b4ab365a1f1022d49d9dfc8e930'), HexBytes('0x000000000000000000000000754c50465885f1ed1fa1a55b95ee8ecf3f1f4324'), HexBytes('0x296c7fb6ccafa3e689950b947c2895b07357c95b066d5cdccd58c301f41359a3')], 'transactionHash': HexBytes('0xfe1289fd3915794b99702202f65eea2e424b2f083a12749d29b4dd51f6dce40d'), 'transactionIndex': 1})]  # noqa: E501


@pytest.fixture(scope='function')
def iter_block_number(start=0):
    def iterator():
        block_number = start
        while True:
            sent_value = (yield block_number)
            if sent_value is not None:
                block_number = sent_value
    block_number = iterator()
    next(block_number)
    return block_number


@pytest.fixture(scope='function')
def result_generator_middleware(iter_block_number):
    return construct_result_generator_middleware({
        'eth_getLogs': lambda *_: FILTER_LOG,
        'eth_getBlockByNumber': lambda *_: {'hash': BLOCK_HASH},
        'net_version': lambda *_: 1,
        'eth_blockNumber': lambda *_: next(iter_block_number),
    })


@pytest.fixture(scope='function')
def w3_base():
    return Web3(provider=DummyProvider(), middlewares=[])


@pytest.fixture(scope='function')
def w3(w3_base, result_generator_middleware):
    w3_base.middleware_onion.add(result_generator_middleware)
    w3_base.middleware_onion.add(local_filter_middleware)
    return w3_base


@pytest.mark.parametrize("start, stop, expected", [
    (2, 7, [
        (2, 6),
        (7, 7)
    ]),
    (0, 12, [
        (0, 4),
        (5, 9),
        (10, 12)
    ]),
    (0, 15, [
        (0, 4),
        (5, 9),
        (10, 14),
        (15, 15)
    ]),
    (0, 0, [
        (0, 0),
    ]),
    (1, 1, [
        (1, 1),
    ]),
    (5, 0, TypeError),
])
def test_block_ranges(start, stop, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            block_ranges(start, stop)
    else:
        actual = tuple(block_ranges(start, stop))
        assert len(actual) == len(expected)
        for actual, expected in zip(actual, expected):
            assert actual == expected


@pytest.mark.parametrize("from_block,to_block,current_block,expected", [
    (0, 10, [10], [
        (0, 10),
    ]),
    (0, 55, [0, 19, 55], [
        (0, 0),
        (1, 19),
        (20, 55),
    ]),
    (0, None, [10], [
        (0, 10),
    ]),
    (0, 10, [12], [
        (None, None),
    ]),
    (12, 10, [12], [
        (None, None),
    ]),
    (12, 10, [None], [
        (None, None),
    ]),
])
def test_iter_latest_block_ranges(
        w3,
        iter_block_number,
        from_block,
        to_block,
        current_block,
        expected):
    latest_block_ranges = iter_latest_block_ranges(w3, from_block, to_block)
    for index, block in enumerate(current_block):
        iter_block_number.send(block)
        expected_tuple = expected[index]
        actual_tuple = next(latest_block_ranges)
        assert actual_tuple == expected_tuple


def test_pending_block_filter_middleware(w3):
    with pytest.raises(NotImplementedError):
        w3.eth.filter('pending')


def test_local_filter_middleware(w3, iter_block_number):
    block_filter = w3.eth.filter('latest')
    block_filter.get_new_entries()
    iter_block_number.send(1)

    log_filter = w3.eth.filter(filter_params={'fromBlock': 'latest'})

    assert w3.eth.getFilterChanges(block_filter.filter_id) == [HexBytes(BLOCK_HASH)]

    iter_block_number.send(2)
    results = w3.eth.getFilterChanges(log_filter.filter_id)
    assert results == FILTER_LOG

    assert w3.eth.getFilterLogs(log_filter.filter_id) == FILTER_LOG

    filter_ids = (
        block_filter.filter_id,
        log_filter.filter_id
    )

    # Test that all ids are str types
    assert all(isinstance(_filter_id, (str,)) for _filter_id in filter_ids)

    # Test that all ids are unique
    assert len(filter_ids) == len(set(filter_ids))
