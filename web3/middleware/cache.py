import time

import lru

from web3.utils.caching import (
    generate_cache_key,
)


SIMPLE_CACHE_RPC_WHITELIST = {
    'web3_clientVersion',
    'web3_sha3',
    'net_version',
    # 'net_peerCount',
    # 'net_listening',
    'eth_protocolVersion',
    # 'eth_syncing',
    # 'eth_coinbase',
    # 'eth_mining',
    # 'eth_hashrate',
    # 'eth_gasPrice',
    # 'eth_accounts',
    # 'eth_blockNumber',
    # 'eth_getBalance',
    # 'eth_getStorageAt',
    # 'eth_getTransactionCount',
    'eth_getBlockTransactionCountByHash',
    # 'eth_getBlockTransactionCountByNumber',
    'eth_getUncleCountByBlockHash',
    # 'eth_getUncleCountByBlockNumber',
    # 'eth_getCode',
    # 'eth_sign',
    # 'eth_sendTransaction',
    # 'eth_sendRawTransaction',
    # 'eth_call',
    # 'eth_estimateGas',
    'eth_getBlockByHash',
    # 'eth_getBlockByNumber',
    'eth_getTransactionByHash',
    'eth_getTransactionByBlockHashAndIndex',
    # 'eth_getTransactionByBlockNumberAndIndex',
    # 'eth_getTransactionReceipt',
    'eth_getUncleByBlockHashAndIndex',
    # 'eth_getUncleByBlockNumberAndIndex',
    # 'eth_getCompilers',
    # 'eth_compileLLL',
    # 'eth_compileSolidity',
    # 'eth_compileSerpent',
    # 'eth_newFilter',
    # 'eth_newBlockFilter',
    # 'eth_newPendingTransactionFilter',
    # 'eth_uninstallFilter',
    # 'eth_getFilterChanges',
    # 'eth_getFilterLogs',
    # 'eth_getLogs',
    # 'eth_getWork',
    # 'eth_submitWork',
    # 'eth_submitHashrate',
}


def should_cache(method, params, response):
    if 'error' in response:
        return False
    elif 'result' not in response:
        return False

    if response['result'] is None:
        return False
    return True


def construct_simple_cache_middleware(cache,
                                      rpc_whitelist=SIMPLE_CACHE_RPC_WHITELIST,
                                      should_cache_fn=should_cache):
    def simple_cache_middleware(make_request, web3):
        def middleware(method, params):
            if method in rpc_whitelist:
                cache_key = generate_cache_key((method, params))
                if cache_key not in cache:
                    response = make_request(method, params)
                    if should_cache_fn(method, params, response):
                        cache[cache_key] = response
                    return response
                return cache[cache_key]
            else:
                return make_request(method, params)
        return middleware
    return simple_cache_middleware


simple_cache_middleware = construct_simple_cache_middleware(cache=lru.LRU(256))


TIME_BASED_CACHE_RPC_WHITELIST = {
    # 'web3_clientVersion',
    # 'web3_sha3',
    # 'net_version',
    # 'net_peerCount',
    # 'net_listening',
    # 'eth_protocolVersion',
    # 'eth_syncing',
    'eth_coinbase',
    # 'eth_mining',
    # 'eth_hashrate',
    # 'eth_gasPrice',
    'eth_accounts',
    # 'eth_blockNumber',
    # 'eth_getBalance',
    # 'eth_getStorageAt',
    # 'eth_getTransactionCount',
    # 'eth_getBlockTransactionCountByHash',
    # 'eth_getBlockTransactionCountByNumber',
    # 'eth_getUncleCountByBlockHash',
    # 'eth_getUncleCountByBlockNumber',
    # 'eth_getCode',
    # 'eth_sign',
    # 'eth_sendTransaction',
    # 'eth_sendRawTransaction',
    # 'eth_call',
    # 'eth_estimateGas',
    # 'eth_getBlockByHash',
    # 'eth_getBlockByNumber',
    # 'eth_getTransactionByHash',
    # 'eth_getTransactionByBlockHashAndIndex',
    # 'eth_getTransactionByBlockNumberAndIndex',
    # 'eth_getTransactionReceipt',
    # 'eth_getUncleByBlockHashAndIndex',
    # 'eth_getUncleByBlockNumberAndIndex',
    # 'eth_getCompilers',
    # 'eth_compileLLL',
    # 'eth_compileSolidity',
    # 'eth_compileSerpent',
    # 'eth_newFilter',
    # 'eth_newBlockFilter',
    # 'eth_newPendingTransactionFilter',
    # 'eth_uninstallFilter',
    # 'eth_getFilterChanges',
    # 'eth_getFilterLogs',
    # 'eth_getLogs',
    # 'eth_getWork',
    # 'eth_submitWork',
    # 'eth_submitHashrate',
}


def construct_time_based_cache_middleware(cache,
                                          cache_expire_seconds=15,
                                          rpc_whitelist=TIME_BASED_CACHE_RPC_WHITELIST,
                                          should_cache_fn=should_cache):
    def simple_cache_middleware(make_request, web3):
        def middleware(method, params):
            if method in rpc_whitelist:
                cache_key = generate_cache_key((method, params))
                if cache_key in cache:
                    # check that the cached response is not expired.
                    cached_at, cached_response = cache[cache_key]
                    cached_for = time.time() - cached_at

                    if cached_for <= cache_expire_seconds:
                        return cached_response
                    else:
                        del cache[cache_key]

                # cache either missed or expired so make the request.
                response = make_request(method, params)

                if should_cache_fn(response):
                    cache[cache_key] = (time.time(), response)

                return response
            else:
                return make_request(method, params)
        return middleware
    return simple_cache_middleware


time_based_cache_middleware = construct_time_based_cache_middleware(
    cache=lru.LRU(256),
)


BLOCK_NUMBER_RPC_WHITELIST = {
    # 'web3_clientVersion',
    # 'web3_sha3',
    # 'net_version',
    # 'net_peerCount',
    # 'net_listening',
    # 'eth_protocolVersion',
    # 'eth_syncing',
    # 'eth_coinbase',
    # 'eth_mining',
    # 'eth_hashrate',
    'eth_gasPrice',
    # 'eth_accounts',
    'eth_blockNumber',
    'eth_getBalance',
    'eth_getStorageAt',
    'eth_getTransactionCount',
    # 'eth_getBlockTransactionCountByHash',
    'eth_getBlockTransactionCountByNumber',
    # 'eth_getUncleCountByBlockHash',
    'eth_getUncleCountByBlockNumber',
    'eth_getCode',
    # 'eth_sign',
    # 'eth_sendTransaction',
    # 'eth_sendRawTransaction',
    'eth_call',
    'eth_estimateGas',
    # 'eth_getBlockByHash',
    'eth_getBlockByNumber',
    # 'eth_getTransactionByHash',
    # 'eth_getTransactionByBlockHashAndIndex',
    'eth_getTransactionByBlockNumberAndIndex',
    'eth_getTransactionReceipt',
    # 'eth_getUncleByBlockHashAndIndex',
    'eth_getUncleByBlockNumberAndIndex',
    # 'eth_getCompilers',
    # 'eth_compileLLL',
    # 'eth_compileSolidity',
    # 'eth_compileSerpent',
    # 'eth_newFilter',
    # 'eth_newBlockFilter',
    # 'eth_newPendingTransactionFilter',
    # 'eth_uninstallFilter',
    # 'eth_getFilterChanges',
    # 'eth_getFilterLogs',
    'eth_getLogs',
    # 'eth_getWork',
    # 'eth_submitWork',
    # 'eth_submitHashrate',
}


AVG_BLOCK_TIME_KEY = 'avg_block_time'
AVG_BLOCK_SAMPLE_SIZE_KEY = 'avg_block_sample_size'
AVG_BLOCK_TIME_UPDATED_AT_KEY = 'avg_block_time_updated_at'


def should_cache_by_block_number(method, params, response):
    if method == 'eth_getBlockByNumber':
        if params == ['latest'] or params == ['pending']:
            return False

    if 'error' in response:
        return False
    elif 'result' not in response:
        return False

    if response['result'] is None:
        return False
    return True


def construct_block_number_based_cache_middleware(cache,
                                                  rpc_whitelist=BLOCK_NUMBER_RPC_WHITELIST,
                                                  average_block_time_sample_size=240,
                                                  default_average_block_time=15,
                                                  should_cache_fn=should_cache_by_block_number):

    def block_number_based_cache_middleware(make_request, web3):
        block_info = {}

        def _update_block_info_cache(web3):
            avg_block_time = block_info.get(AVG_BLOCK_TIME_KEY, default_average_block_time)
            avg_block_sample_size = block_info.get(AVG_BLOCK_SAMPLE_SIZE_KEY, 0)
            avg_block_time_updated_at = block_info.get(AVG_BLOCK_TIME_UPDATED_AT_KEY, 0)

            # compute age as counted by number of blocks since the avg_block_time
            if avg_block_time == 0:
                avg_block_time_age_in_blocks = avg_block_sample_size
            else:
                avg_block_time_age_in_blocks = (
                    (time.time() - avg_block_time_updated_at) / avg_block_time
                )

            if avg_block_time_age_in_blocks >= avg_block_sample_size:
                # If the length of time since the average block time as
                # measured by blocks is greater than or equal to the number of
                # blocks sampled then we need to recompute the average block
                # time.
                latest_block = web3.eth.getBlock('latest')
                ancestor_block_number = max(
                    0,
                    latest_block['number'] - average_block_time_sample_size,
                )
                ancestor_block = web3.eth.getBlock(ancestor_block_number)
                sample_size = latest_block['number'] - ancestor_block_number

                block_info[AVG_BLOCK_SAMPLE_SIZE_KEY] = sample_size
                block_info[AVG_BLOCK_TIME_KEY] = (
                    (latest_block['timestamp'] - ancestor_block['timestamp']) / sample_size
                )
                block_info[AVG_BLOCK_TIME_UPDATED_AT_KEY] = time.time()

            if 'latest_block' in block_info:
                latest_block = block_info['latest_block']
                time_since_latest_block = time.time() - latest_block['timestamp']

                # latest block is too old so update cache
                if time_since_latest_block > avg_block_time:
                    block_info['latest_block'] = web3.eth.getBlock('latest')
            else:
                # latest block has not been fetched so we fetch it.
                block_info['latest_block'] = web3.eth.getBlock('latest')

        def middleware(method, params):
            if method in rpc_whitelist:
                _update_block_info_cache()
                latest_block_hash = block_info['latest_block']['hash']
                cache_key = generate_cache_key((latest_block_hash, method, params))
                if cache_key in cache:
                    return cache[cache_key]

                response = make_request(method, params)
                if should_cache_fn(method, params, response):
                    cache[cache_key] = response
                return response
            else:
                return make_request(method, params)
        return middleware
    return block_number_based_cache_middleware


block_number_cache_middleware = construct_block_number_based_cache_middleware(
    cache=lru.LRU(256),
    rpc_whitelist=BLOCK_NUMBER_RPC_WHITELIST,
)
