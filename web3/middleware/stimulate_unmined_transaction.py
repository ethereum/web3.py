import collections
import itertools

counter = itertools.count()


def unmined_receipt_simulator_middleware(make_request, web3):
    receipt_counters = collections.defaultdict(itertools.count)

    def middleware(method, params):
        if method == 'eth_getTransactionReceipt':
            txn_hash = params[0]
            if next(receipt_counters[txn_hash]) < 2:
                return {'result': None}
        return make_request(method, params)
    return middleware
