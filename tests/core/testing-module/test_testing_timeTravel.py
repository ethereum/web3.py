def test_time_traveling(w3):
    current_block_time = w3.eth.get_block("pending")["timestamp"]

    time_travel_to = current_block_time + 12345

    w3.testing.timeTravel(time_travel_to)

    latest_block_time = w3.eth.get_block("pending")["timestamp"]
    assert latest_block_time >= time_travel_to
