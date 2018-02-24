from cytoolz import (
    assoc,
    dissoc,
)


def normalize_errors_middleware(make_request, web3):
    def middleware(method, params):
        result = make_request(method, params)
        if method == 'eth_getTransactionReceipt' and 'error' in result:
            is_geth = web3.version.node.startswith('Geth')
            if is_geth and result['error']['code'] == -32000:
                return assoc(
                    dissoc(result, 'error'),
                    'result',
                    None,
                )
            else:
                return result
        else:
            return result
    return middleware
