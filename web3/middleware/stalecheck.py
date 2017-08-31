import datetime
import time


SKIP_STALECHECK_FOR_METHODS = set([
    'eth_getBlockByHash',
    'eth_getBlockByNumber',
    'eth_getBlockTransactionCountByHash',
    'eth_getBlockTransactionCountByNumber',
    'eth_getTransactionByBlockHashAndIndex',
    'eth_getTransactionByBlockNumberAndIndex',
    'eth_getUncleCountByBlockHash',
    'eth_getUncleCountByBlockNumber',
])


def _isfresh(block, allowable_delay):
    return block and time.time() - block.timestamp <= allowable_delay


def make_stalecheck_middleware(**kwargs):
    '''
    Use to require that a function will run only of the blockchain is recently updated.

    This middleware takes an argument, so unlike other middleware, you must make the middleware
    with a method call.
    For example: `make_stalecheck_middleware(hours=12)`

    If the latest block in the chain is older than 12 hours ago in this example, then the
    middleware will raise a StaleBlockchain exception.

    `make_stalecheck_middleware(...)` takes the same keyword arguments as datetime.timedelta()
    '''
    allowable_delay = datetime.timedelta(**kwargs).total_seconds()

    def stalecheck_middleware(make_request, web3):
        def middleware(method, params):
            if method not in SKIP_STALECHECK_FOR_METHODS:
                last_block = web3.eth.getBlock('latest')
                if not _isfresh(last_block, allowable_delay):
                    raise StaleBlockchain(last_block, allowable_delay)

            return make_request(method, params)
        return middleware
    return stalecheck_middleware


class StaleBlockchain(Exception):
    def __init__(self, block, allowable_delay):
        last_block_date = datetime.datetime.fromtimestamp(block.timestamp).strftime('%c')
        super().__init__(
            "The latest block, #%d, is %d seconds old, but is only allowed to be %d s old. "
            "The date of the most recent block is %s. Continue syncing and try again..." %
            (block.number, time.time() - block.timestamp, allowable_delay, last_block_date)
        )
