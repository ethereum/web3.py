import random

from eth_utils import (
    decode_hex,
)
from flaky import (
    flaky,
)

from web3._utils.threads import (
    Timeout,
)


@flaky(max_runs=3)
def test_miner_set_extra(web3_empty, wait_for_block):
    web3 = web3_empty

    initial_extra = decode_hex(web3.eth.get_block(web3.eth.block_number)["extraData"])

    new_extra_data = b"-this-is-32-bytes-of-extra-data-"

    # sanity
    assert initial_extra != new_extra_data

    web3.geth.miner.set_extra(new_extra_data)

    with Timeout(60) as timeout:
        while True:
            extra_data = decode_hex(
                web3.eth.get_block(web3.eth.block_number)["extraData"]
            )
            if extra_data == new_extra_data:
                break
            timeout.sleep(random.random())

    after_extra = decode_hex(web3.eth.get_block(web3.eth.block_number)["extraData"])

    assert after_extra == new_extra_data
