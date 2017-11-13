import time


def test_shh_sync_filter(web3, skip_if_testrpc):
    skip_if_testrpc(web3)
    topic = web3.toHex(text="test")
    shh_filter = web3.shh.filter({"topics": [topic]})

    payloads = []
    payloads.append(str.encode("payload1"))
    web3.shh.post({
        "topics": [topic],
        "payload": web3.toHex(text=payloads[-1]),
    })
    time.sleep(1)

    payloads.append(str.encode("payload2"))
    web3.shh.post({
        "topics": [topic],
        "payload": web3.toHex(text=payloads[-1]),
    })
    time.sleep(1)
    received_messages = shh_filter.get_new_entries()
    assert len(received_messages) > 1

    for message in received_messages:
        assert message["payload"] in payloads


def test_shh_async_filter(web3, skip_if_testrpc):
    skip_if_testrpc(web3)
    received_messages = []
    topic = web3.toHex(text="test")
    shh_filter = web3.shh.filter({"topics": [topic]})
    shh_filter.watch(received_messages.append)

    payloads = []
    payloads.append(str.encode("payload1"))
    web3.shh.post({
        "topics": [topic],
        "payload": web3.toHex(text=payloads[-1]),
    })
    time.sleep(1)

    payloads.append(str.encode("payload2"))
    web3.shh.post({
        "topics": [topic],
        "payload": web3.toHex(text=payloads[-1]),
    })
    time.sleep(1)
    assert len(received_messages) > 1

    for message in received_messages:
        assert message["payload"] in payloads
