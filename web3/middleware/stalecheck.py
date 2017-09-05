from collections import defaultdict
import datetime
import time

from web3.exceptions import StaleBlockchain

SKIP_STALECHECK_FOR_METHODS = set([
    'eth_getBlockByNumber',
])


def _isfresh(block, allowable_delay):
    return block and time.time() - block['timestamp'] <= allowable_delay


def make_stalecheck_middleware(seconds=0, minutes=0, hours=0, days=0):
    '''
    Use to require that a function will run only of the blockchain is recently updated.

    This middleware takes an argument, so unlike other middleware, you must make the middleware
    with a method call.
    For example: `make_stalecheck_middleware(hours=6, days=1)`

    If the latest block in the chain is older than 30 hours ago in this example, then the
    middleware will raise a StaleBlockchain exception.
    '''
    allowable_delta = datetime.timedelta(seconds=seconds, minutes=minutes, hours=hours, days=days)
    allowable_delay = allowable_delta.total_seconds()

    def stalecheck_middleware(make_request, web3):
        cache = {'latest': None}

        def middleware(method, params):
            if method not in SKIP_STALECHECK_FOR_METHODS:
                if _isfresh(cache['latest'], allowable_delay):
                    pass
                else:
                    latest = web3.eth.getBlock('latest')
                    if _isfresh(latest, allowable_delay):
                        cache['latest'] = latest
                    else:
                        raise StaleBlockchain(latest, allowable_delay)

            return make_request(method, params)
        return middleware
    return stalecheck_middleware
