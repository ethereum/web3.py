import time

from hexbytes import (
    HexBytes,
)


def test_shh_sync_filter(web3, skip_if_testrpc):
    skip_if_testrpc(web3)

    sender = web3.shh.newKeyPair()
    sender_pub = web3.shh.getPublicKey(sender)

    receiver = web3.shh.newKeyPair()
    receiver_pub = web3.shh.getPublicKey(receiver)

    topic = '0x13370000'
    payloads = [web3.toHex(text="test message :)"), web3.toHex(text="2nd test message")]

    shh_filter = web3.shh.newMessageFilter({
        'privateKeyID': receiver,
        'sig': sender_pub,
        'topics': [topic]
    })

    web3.shh.post({
        'sig': sender,
        'powTarget': 2.5,
        'powTime': 2,
        'payload': payloads[0],
        'pubKey': receiver_pub
    })
    time.sleep(1)

    web3.shh.post({
        'sig': sender,
        'powTarget': 2.5,
        'powTime': 2,
        'payload': payloads[1],
        'topic': topic,
        'pubKey': receiver_pub
    })
    time.sleep(1)

    received_messages = shh_filter.get_new_entries()
    assert len(received_messages) == 1

    message = received_messages[0]

    assert message["payload"] == HexBytes(payloads[1])
    assert message["topic"] == HexBytes(topic)


def test_shh_async_filter(web3, skip_if_testrpc):
    skip_if_testrpc(web3)
    received_messages = []

    sender = web3.shh.newKeyPair()
    sender_pub = web3.shh.getPublicKey(sender)

    receiver = web3.shh.newKeyPair()
    receiver_pub = web3.shh.getPublicKey(receiver)

    topic = '0x13370000'
    payloads = [web3.toHex(text="test message :)"), web3.toHex(text="2nd test message")]

    shh_filter = web3.shh.newMessageFilter({
        'privateKeyID': receiver,
        'sig': sender_pub,
        'topics': [topic]
    }, poll_interval=0.5)
    watcher = shh_filter.watch(received_messages.extend)

    web3.shh.post({
        'sig': sender,
        'powTarget': 2.5,
        'powTime': 2,
        'payload': payloads[0],
        'topic': topic,
        'pubKey': receiver_pub
    })
    time.sleep(1)

    web3.shh.post({
        'sig': sender,
        'powTarget': 2.5,
        'powTime': 2,
        'payload': payloads[1],
        'pubKey': receiver_pub
    })
    time.sleep(1)

    assert len(received_messages) == 1

    message = received_messages[0]

    assert message["payload"] == HexBytes(payloads[0])
    assert message["topic"] == HexBytes(topic)

    watcher.stop()


def test_shh_remove_filter(web3, skip_if_testrpc):
    skip_if_testrpc(web3)

    receiver = web3.shh.newKeyPair()
    receiver_pub = web3.shh.getPublicKey(receiver)

    payload = web3.toHex(text="test message :)")
    shh_filter = web3.shh.newMessageFilter({'privateKeyID': receiver})

    web3.shh.post({
        'powTarget': 2.5,
        'powTime': 2,
        'payload': payload,
        'pubKey': receiver_pub
    })
    time.sleep(1)

    message = shh_filter.get_new_entries()[0]
    assert message["payload"] == HexBytes(payload)

    assert web3.shh.deleteMessageFilter(shh_filter.filter_id)

    try:
        web3.shh.getMessages(shh_filter.filter_id)
        assert False
    except:
        assert True
