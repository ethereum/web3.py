import random

from flaky import flaky

import gevent

from web3.utils.encoding import decode_hex


@flaky(max_runs=3)
def test_miner_setExtra(web3_empty, wait_for_block):
    web3 = web3_empty

    initial_extra = decode_hex(web3.eth.getBlock(web3.eth.blockNumber)['extraData'])

    new_extra_data = b'-this-is-32-bytes-of-extra-data-'

    # sanity
    assert initial_extra != new_extra_data

    web3.miner.setExtra(new_extra_data)

    with gevent.Timeout(60):
        while True:
            extra_data = decode_hex(web3.eth.getBlock(web3.eth.blockNumber)['extraData'])
            if extra_data == new_extra_data:
                break
            gevent.sleep(random.random())

    after_extra = decode_hex(web3.eth.getBlock(web3.eth.blockNumber)['extraData'])

    assert after_extra == new_extra_data
