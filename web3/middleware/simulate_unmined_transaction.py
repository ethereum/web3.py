import collections
import itertools

counter = itertools.count()

INVOCATIONS_BEFORE_RESULT = 5


def unmined_receipt_simulator_middleware(make_request, web3):
    receipt_counters = collections.defaultdict(itertools.count)

    def middleware(method, params):
        if method == 'eth_getTransactionReceipt':
            txn_hash = params[0]
            if next(receipt_counters[txn_hash]) < INVOCATIONS_BEFORE_RESULT:
                return {'result': None}
            else:
                return make_request(method, params)
        else:
            return make_request(method, params)
    return middleware
