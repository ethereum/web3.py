import codecs
import itertools
import pytest
import time
import uuid

from eth_utils import (
    is_integer,
    to_tuple,
)

from web3 import Web3
from web3.middleware import (  # noqa: F401
    construct_error_generator_middleware,
    construct_latest_block_based_cache_middleware,
    construct_result_generator_middleware,
)
from web3.providers.base import (
    BaseProvider,
)
from web3.utils.caching import (
    generate_cache_key,
)


@pytest.fixture
def w3_base():
    return Web3(providers=[BaseProvider()], middlewares=[])


def _mk_block(n, timestamp):
    return {
        'hash': codecs.decode(str(n).zfill(32), 'hex'),
        'number': n,
        'timestamp': timestamp,
    }


@to_tuple
def generate_block_history(num_mined_blocks=5, block_time=1):
    genesis = _mk_block(0, time.time())
    yield genesis
    for block_number in range(1, num_mined_blocks + 1):
        yield _mk_block(
            block_number,
            genesis['timestamp'] + 2 * block_number,
        )


@pytest.fixture
def construct_block_data_middleware():
    def _construct_block_data_middleware(num_blocks):
        blocks = generate_block_history(num_blocks)
        _block_info = {
            'blocks': blocks,
            'head_block_number': blocks[0]['number']
        }

        def _evm_mine(method, params, block_info=_block_info):
            num_blocks = params[0]
            head_block_number = block_info['head_block_number']
            if head_block_number + num_blocks >= len(block_info['blocks']):
                raise ValueError("no more blocks to mine")

            block_info['head_block_number'] += num_blocks

        def _get_block_by_number(method, params, block_info=_block_info):
            block_id = params[0]
            blocks = block_info['blocks']
            head_block_number = block_info['head_block_number']

            if block_id == 'latest':
                return blocks[head_block_number]
            elif block_id == 'pending':
                if head_block_number + 1 >= len(blocks):
                    raise ValueError("no pending block")
                return blocks[head_block_number + 1]
            elif block_id == 'earliest':
                return blocks[0]
            elif is_integer(block_id):
                if block_id <= head_block_number:
                    return blocks[block_id]
                else:
                    return None
            else:
                raise TypeError('Invalid type for block_id')

        def _get_block_by_hash(method, params, block_info=_block_info):
            block_hash = params[0]
            blocks = block_info['blocks']
            head_block_number = block_info['head_block_number']

            blocks_by_hash = {
                block['hash']: block
                for block
                in blocks
            }
            try:
                block = blocks_by_hash[block_hash]
                if block['number'] <= head_block_number:
                    return block
                else:
                    return None
            except KeyError:
                return None

        return construct_result_generator_middleware({
            'eth_getBlockByNumber': _get_block_by_number,
            'eth_getBlockByHash': _get_block_by_hash,
            'evm_mine': _evm_mine,
        })
    return _construct_block_data_middleware


@pytest.fixture
def block_data_middleware(construct_block_data_middleware):
    return construct_block_data_middleware(5)


@pytest.fixture
def result_generator_middleware():
    return construct_result_generator_middleware({
        'fake_endpoint': lambda *_: str(uuid.uuid4()),
        'not_whitelisted': lambda *_: str(uuid.uuid4()),
    })


@pytest.fixture
def latest_block_based_cache_middleware():
    return construct_latest_block_based_cache_middleware(
        cache_class=dict,
        average_block_time_sample_size=1,
        default_average_block_time=0.1,
        rpc_whitelist={'fake_endpoint'},
    )


@pytest.fixture
def w3(w3_base,
       result_generator_middleware,
       block_data_middleware,
       latest_block_based_cache_middleware):
    w3_base.middleware_stack.add(block_data_middleware)
    w3_base.middleware_stack.add(result_generator_middleware)
    w3_base.middleware_stack.add(latest_block_based_cache_middleware)
    return w3_base


def test_latest_block_based_cache_middleware_pulls_from_cache(
        w3_base,
        block_data_middleware,
        result_generator_middleware):
    w3 = w3_base
    w3.middleware_stack.add(block_data_middleware)
    w3.middleware_stack.add(result_generator_middleware)

    current_block_hash = w3.eth.getBlock('latest')['hash']

    def cache_class():
        return {
            generate_cache_key(
                (current_block_hash, 'fake_endpoint', [1])
            ): {'result': 'value-a'},
        }

    w3.middleware_stack.add(construct_latest_block_based_cache_middleware(
        cache_class=cache_class,
        rpc_whitelist={'fake_endpoint'},
    ))

    assert w3.manager.request_blocking('fake_endpoint', [1]) == 'value-a'


def test_latest_block_based_cache_middleware_populates_cache(w3):
    result = w3.manager.request_blocking('fake_endpoint', [])

    assert w3.manager.request_blocking('fake_endpoint', []) == result
    assert w3.manager.request_blocking('fake_endpoint', [1]) != result


def test_latest_block_based_cache_middleware_busts_cache(w3, mocker):
    result = w3.manager.request_blocking('fake_endpoint', [])

    assert w3.manager.request_blocking('fake_endpoint', []) == result
    w3.testing.mine()

    # should still be cached for at least 1 second.  This also verifies that
    # the middleware caches the latest block based on the block time.
    assert w3.manager.request_blocking('fake_endpoint', []) == result

    mocker.patch('time.time', return_value=time.time() + 5)

    assert w3.manager.request_blocking('fake_endpoint', []) != result


def test_latest_block_cache_middleware_does_not_cache_bad_responses(
        w3_base,
        block_data_middleware,
        latest_block_based_cache_middleware):
    counter = itertools.count()
    w3 = w3_base

    def result_cb(method, params):
        next(counter)
        return None

    w3 = w3_base
    w3.middleware_stack.add(block_data_middleware)
    w3.middleware_stack.add(construct_result_generator_middleware({
        'fake_endpoint': result_cb,
    }))
    w3.middleware_stack.add(latest_block_based_cache_middleware)

    w3.manager.request_blocking('fake_endpoint', [])
    w3.manager.request_blocking('fake_endpoint', [])

    assert next(counter) == 2


def test_latest_block_cache_middleware_does_not_cache_error_response(
        w3_base,
        block_data_middleware,
        latest_block_based_cache_middleware):
    counter = itertools.count()
    w3 = w3_base

    def error_cb(method, params):
        next(counter)
        return "the error message"

    w3.middleware_stack.add(block_data_middleware)
    w3.middleware_stack.add(construct_error_generator_middleware({
        'fake_endpoint': error_cb,
    }))
    w3.middleware_stack.add(latest_block_based_cache_middleware)

    with pytest.raises(ValueError):
        w3.manager.request_blocking('fake_endpoint', [])
    with pytest.raises(ValueError):
        w3.manager.request_blocking('fake_endpoint', [])

    assert next(counter) == 2
