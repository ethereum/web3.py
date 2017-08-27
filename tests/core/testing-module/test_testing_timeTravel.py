def test_time_traveling(web3):
    current_block_time = web3.eth.getBlock("pending")['timestamp']

    time_travel_to = current_block_time + 12345

    web3.testing.timeTravel(time_travel_to)

    latest_block_time = web3.eth.getBlock("pending")['timestamp']
    assert latest_block_time >= time_travel_to
