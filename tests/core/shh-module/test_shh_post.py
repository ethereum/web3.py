import pytest


def test_shh_post_deprecated(web3, skip_if_testrpc):
    skip_if_testrpc(web3)

    with pytest.warns(DeprecationWarning) as warnings:
        receiver_pub = web3.shh.getPublicKey(web3.shh.newKeyPair())
        assert web3.shh.post({
            "topic": "0x12345678",
            "powTarget": 2.5,
            "powTime": 2,
            "payload": web3.toHex(text="testing shh on web3.py"),
            "pubKey": receiver_pub,
        })
        assert len(warnings) == 1


def test_shh_post(web3, skip_if_testrpc):
    skip_if_testrpc(web3)

    receiver_pub = web3.shh.get_public_key(web3.shh.new_key_pair())
    assert web3.shh.post({
        "topic": "0x12345678",
        "powTarget": 2.5,
        "powTime": 2,
        "payload": web3.toHex(text="testing shh on web3.py"),
        "pubKey": receiver_pub,
    })
