

def test_filtering_sequential_blocks(
        web3,
        emitter,
        Emitter,
        wait_for_transaction):
    builder = emitter.events.LogNoArguments.build_filter()
    filter_ = builder.deploy(web3)
    initial_block_number = web3.eth.blockNumber
    for i in range(100):
        emitter.functions.logNoArgs(which=1).transact()
    assert web3.eth.blockNumber == initial_block_number + 100
    assert len(filter_.get_new_entries()) == 100
