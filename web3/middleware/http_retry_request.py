from requests.exceptions import HTTPError, ConnectionError, Timeout, TooManyRedirects

'''
Creates middleware that retries failed HTTP requests. Is a default
middleware for HTTPProvider.
'''


def http_retry_request_middleware(make_request, web3):

  whitelist = [
        'admin',
        'shh',
        'miner',
        'net',
        'txpool'
        'testing',
        'evm',
        'eth_protocolVersion',
        'eth_syncing',
        'eth_coinbase',
        'eth_mining',
        'eth_hashrate',
        'eth_gasPrice',
        'eth_accounts',
        'eth_blockNumber',
        'eth_getBalance',
        'eth_getStorageAt',
        'eth_getCode',
        'eth_getBlockByNumber',
        'eth_getBlockByHash',
        'eth_getBlockTransactionCountByNumber',
        'eth_getBlockTransactionCountByHash',
        'eth_getUncleCountByBlockNumber',
        'eth_getUncleCountByBlockHash',
        'eth_getTransactionByHash',
        'eth_getTransactionByBlockHashAndIndex',
        'eth_getTransactionByBlockNumberAndIndex',
        'eth_getTransactionReceipt',
        'eth_getTransactionCount',
        'eth_call',
        'eth_estimateGas',
        'eth_newBlockFilter',
        'eth_newPendingTransactionFilter',
        'eth_newFilter',
        'eth_getFilterChanges',
        'eth_getFilterLogs',
        'eth_getLogs',
        'eth_uninstallFilter',
        'eth_getCompilers',
        'eth_getWork',
        'eth_sign',
        'personal_importRawKey',
        'personal_newAccount',
        'personal_listAccounts',
        'personal_lockAccount',
        'personal_unlockAccount',
        'personal_ecRecover',
        'personal_sign'
    ]

    def check_method(method):
        root = method.split('_')[0]
        if root in whitelist:
            return True
        elif method in whitelist:
            return True
        else:
            return False

    def middleware(method, params):
        if check_method(method):
            MAX_TRIES = 5
            for i in range(MAX_TRIES):
                try:
                    return make_request(method, params)
                except (ConnectionError, HTTPError, Timeout, TooManyRedirects):
                    if i < MAX_TRIES - 1:
                        continue
                    else:
                        raise
        else:
            make_request(method, params)
    return middleware
