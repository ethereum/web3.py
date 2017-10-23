from web3.utils.compat import sleep


def test_shh_filter(web3, skip_if_testrpc):
    skip_if_testrpc(web3)
    recieved_messages = []
    topic = web3.toHex(text="test")
    shh_filter = web3.shh.filter({"topics": [topic]})
    shh_filter.watch(recieved_messages.append)

    payloads = []
    payloads.append(str.encode("payload1"))
    web3.shh.post({
        "topics": [topic],
        "payload": web3.toHex(text=payloads[-1]),
    })
    sleep(1)

    payloads.append(str.encode("payload2"))
    web3.shh.post({
        "topics": [topic],
        "payload": web3.toHex(text=payloads[-1]),
    })
    sleep(1)
    assert len(recieved_messages) > 1

    for message in recieved_messages:
        assert web3.toBytes(message["payload"]) in payloads
