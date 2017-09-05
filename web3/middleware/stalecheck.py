import time

from web3.exceptions import StaleBlockchain

SKIP_STALECHECK_FOR_METHODS = set([
    'eth_getBlockByNumber',
])


def _isfresh(block, allowable_delay):
    return block and time.time() - block['timestamp'] <= allowable_delay


def make_stalecheck_middleware(allowable_delay=0):
    '''
    Use to require that a function will run only of the blockchain is recently updated.

    This middleware takes an argument, so unlike other middleware, you must make the middleware
    with a method call.
    For example: `make_stalecheck_middleware(allowable_delay=60*5)`

    If the latest block in the chain is older than 5 minutes in this example, then the
    middleware will raise a StaleBlockchain exception.
    '''
    if not allowable_delay:
        raise ValueError("You must set a non-zero allowable delay for this middleware")

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
