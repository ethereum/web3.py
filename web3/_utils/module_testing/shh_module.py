import pytest
import time
from typing import (  # noqa: F401
    TYPE_CHECKING,
    List,
)

from eth_typing import (
    HexStr,
)
from eth_utils import (
    is_integer,
)
from hexbytes import (
    HexBytes,
)

from web3._utils.filters import (
    ShhFilter,
)
from web3.types import (  # noqa: F401
    ShhMessage,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401


class GoEthereumShhModuleTest():
    #
    # shh_filter
    #
    def test_shh_sync_filter(self, web3: "Web3") -> None:

        info = web3.geth.shh.info()
        sender = web3.geth.shh.new_key_pair()
        sender_pub = web3.geth.shh.get_public_key(sender)

        receiver = web3.geth.shh.new_key_pair()
        receiver_pub = web3.geth.shh.get_public_key(receiver)

        topic = HexStr('0x13370000')
        payloads = [web3.toHex(text="test message :)"), web3.toHex(text="2nd test message")]

        shh_filter_id = web3.geth.shh.new_message_filter({
            'privateKeyID': receiver,
            'sig': sender_pub,
            'topics': [topic]
        })

        shh_filter = ShhFilter(web3, shh_filter_id)

        web3.geth.shh.post({
            'sig': sender,
            'powTarget': info['minPow'],
            'powTime': 2,
            'payload': payloads[0],
            'pubKey': receiver_pub
        })
        time.sleep(1)

        web3.geth.shh.post({
            'sig': sender,
            'powTarget': info['minPow'],
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

    def test_shh_sync_filter_deprecated(self, web3: "Web3") -> None:
        with pytest.warns(DeprecationWarning):
            info = web3.geth.shh.info()
            sender = web3.geth.shh.newKeyPair()
            sender_pub = web3.geth.shh.getPublicKey(sender)
            receiver = web3.geth.shh.newKeyPair()
            receiver_pub = web3.geth.shh.getPublicKey(receiver)

            topic = HexStr('0x13370000')
            payloads = [web3.toHex(text="test message :)"), web3.toHex(text="2nd test message")]

            shh_filter_id = web3.geth.shh.newMessageFilter({
                'privateKeyID': receiver,
                'sig': sender_pub,
                'topics': [topic]
            })

            shh_filter = ShhFilter(web3, shh_filter_id)

            web3.geth.shh.post({
                'sig': sender,
                'powTarget': info['minPow'],
                'powTime': 2,
                'payload': payloads[0],
                'pubKey': receiver_pub
            })
            time.sleep(1)

            web3.geth.shh.post({
                'sig': sender,
                'powTarget': info['minPow'],
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

    def test_shh_async_filter(self, web3: "Web3") -> None:
        received_messages: List[ShhMessage] = []

        info = web3.geth.shh.info()
        sender = web3.geth.shh.new_key_pair()
        sender_pub = web3.geth.shh.get_public_key(sender)
        receiver = web3.geth.shh.new_key_pair()
        receiver_pub = web3.geth.shh.get_public_key(receiver)

        topic = HexStr('0x13370000')
        payloads = [web3.toHex(text="test message :)"), web3.toHex(text="2nd test message")]

        shh_filter_id = web3.geth.shh.new_message_filter({
            'privateKeyID': receiver,
            'sig': sender_pub,
            'topics': [topic]
        })

        shh_filter = ShhFilter(web3, shh_filter_id, poll_interval=0.5)
        watcher = shh_filter.watch(received_messages.extend)

        web3.geth.shh.post({
            'sig': sender,
            'powTarget': info['minPow'],
            'powTime': 2,
            'payload': payloads[0],
            'topic': topic,
            'pubKey': receiver_pub
        })
        time.sleep(1)

        web3.geth.shh.post({
            'sig': sender,
            'powTarget': info['minPow'],
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

    def test_shh_async_filter_deprecated(self, web3: "Web3") -> None:
        received_messages: List[ShhMessage] = []

        with pytest.warns(DeprecationWarning) as warnings:
            info = web3.geth.shh.info()
            sender = web3.geth.shh.newKeyPair()
            sender_pub = web3.geth.shh.getPublicKey(sender)

            receiver = web3.geth.shh.newKeyPair()
            receiver_pub = web3.geth.shh.getPublicKey(receiver)

            topic = HexStr('0x13370000')
            payloads = [web3.toHex(text="test message :)"), web3.toHex(text="2nd test message")]

            shh_filter_id = web3.geth.shh.newMessageFilter({
                'privateKeyID': receiver,
                'sig': sender_pub,
                'topics': [topic]
            })

            shh_filter = ShhFilter(web3, shh_filter_id, poll_interval=0.5)
            watcher = shh_filter.watch(received_messages.extend)

            web3.geth.shh.post({
                'sig': sender,
                'powTarget': info['minPow'],
                'powTime': 2,
                'payload': payloads[0],
                'topic': topic,
                'pubKey': receiver_pub
            })
            time.sleep(1)

            web3.geth.shh.post({
                'sig': sender,
                'powTarget': info['minPow'],
                'powTime': 2,
                'payload': payloads[1],
                'pubKey': receiver_pub
            })
            time.sleep(1)

            assert len(received_messages) == 1
            assert len(warnings) == 5

            message = received_messages[0]

            assert message["payload"] == HexBytes(payloads[0])
            assert message["topic"] == HexBytes(topic)

            watcher.stop()

    def test_shh_remove_filter_deprecated(self, web3: "Web3") -> None:
        with pytest.warns(DeprecationWarning):
            info = web3.geth.shh.info()
            receiver = web3.geth.shh.newKeyPair()
            receiver_pub = web3.geth.shh.getPublicKey(receiver)
            payload = web3.toHex(text="test message :)")
            shh_filter_id = web3.geth.shh.newMessageFilter({'privateKeyID': receiver})
            shh_filter = ShhFilter(web3, shh_filter_id)

            web3.geth.shh.post({
                'powTarget': info['minPow'],
                'powTime': 2,
                'payload': payload,
                'pubKey': receiver_pub
            })
            time.sleep(1)

            message = shh_filter.get_new_entries()[0]
            assert message["payload"] == HexBytes(payload)

            assert web3.geth.shh.deleteMessageFilter(shh_filter.filter_id)

            try:
                web3.geth.shh.getMessages(shh_filter.filter_id)
                assert False
            except BaseException:
                assert True

    def test_shh_remove_filter(self, web3: "Web3") -> None:

        info = web3.geth.shh.info()
        receiver = web3.geth.shh.new_key_pair()
        receiver_pub = web3.geth.shh.get_public_key(receiver)
        payload = web3.toHex(text="test message :)")
        shh_filter_id = web3.geth.shh.new_message_filter({'privateKeyID': receiver})
        shh_filter = ShhFilter(web3, shh_filter_id)

        web3.geth.shh.post({
            'powTarget': info['minPow'],
            'powTime': 2,
            'payload': payload,
            'pubKey': receiver_pub
        })
        time.sleep(1)

        message = shh_filter.get_new_entries()[0]
        assert message["payload"] == HexBytes(payload)

        assert web3.geth.shh.delete_message_filter(shh_filter.filter_id)

        try:
            web3.geth.shh.get_filter_messages(shh_filter.filter_id)
            assert False
        except BaseException:
            assert True

    #
    # shh_key_pair
    #
    def test_shh_asymmetric_key_pair(self, web3: "Web3") -> None:
        # Test generating key

        key_id = web3.geth.shh.new_key_pair()
        assert web3.geth.shh.has_key_pair(key_id)
        assert len(web3.geth.shh.get_public_key(key_id)) == 132
        private_key = web3.geth.shh.get_private_key(key_id)
        assert len(private_key) == 66
        assert web3.geth.shh.delete_key_pair(key_id)

        # Test adding a key
        assert not web3.geth.shh.has_key_pair(key_id)
        key_id = web3.geth.shh.add_private_key(private_key)
        assert web3.geth.shh.has_key_pair(key_id)
        assert web3.geth.shh.delete_key_pair(key_id)

    def test_shh_asymmetric_key_pair_deprecated(self, web3: "Web3") -> None:
        # Test generating key
        with pytest.warns(DeprecationWarning):
            key_id = web3.geth.shh.newKeyPair()
            assert web3.geth.shh.hasKeyPair(key_id)
            assert len(web3.geth.shh.getPublicKey(key_id)) == 132
            private_key = web3.geth.shh.getPrivateKey(key_id)
            assert len(private_key) == 66
            assert web3.geth.shh.deleteKeyPair(key_id)

        # Test adding a key
            assert not web3.geth.shh.hasKeyPair(key_id)
            key_id = web3.geth.shh.addPrivateKey(private_key)
            assert web3.geth.shh.hasKeyPair(key_id)
            assert web3.geth.shh.deleteKeyPair(key_id)

    def test_shh_symmetric_key_pair(self, web3: "Web3") -> None:
        # Test generating key
        key_id = web3.geth.shh.new_sym_key()
        assert web3.geth.shh.has_sym_key(key_id)

        key = web3.geth.shh.get_sym_key(key_id)
        assert len(key) == 66
        assert web3.geth.shh.delete_sym_key(key_id)

        # Test adding a key
        assert not web3.geth.shh.has_sym_key(key_id)
        key_id = web3.geth.shh.add_sym_key(key)
        assert web3.geth.shh.has_sym_key(key_id)
        assert web3.geth.shh.delete_sym_key(key_id)

    def test_shh_symmetric_key_pair_deprecated(self, web3: "Web3") -> None:
        with pytest.warns(DeprecationWarning):
            # Test generating key
            key_id = web3.geth.shh.newSymKey()
            assert web3.geth.shh.hasSymKey(key_id)

            key = web3.geth.shh.getSymKey(key_id)
            assert len(key) == 66
            assert web3.geth.shh.deleteSymKey(key_id)

        # Test adding a key
            assert not web3.geth.shh.hasSymKey(key_id)
            key_id = web3.geth.shh.addSymKey(key)
            assert web3.geth.shh.hasSymKey(key_id)
            assert web3.geth.shh.deleteSymKey(key_id)

    def test_shh_symmetric_key_pair_from_password_deprecated(self, web3: "Web3") -> None:
        with pytest.warns(DeprecationWarning):
            key_id = web3.geth.shh.generateSymKeyFromPassword('shh be quiet')

            assert web3.geth.shh.hasSymKey(key_id)
            assert len(web3.geth.shh.getSymKey(key_id)) == 66
            assert web3.geth.shh.deleteSymKey(key_id)

    def test_shh_symmetric_key_pair_from_password(self, web3: "Web3") -> None:

        key_id = web3.geth.shh.generate_sym_key_from_password('shh be quiet')

        assert web3.geth.shh.has_sym_key(key_id)
        assert len(web3.geth.shh.get_sym_key(key_id)) == 66
        assert web3.geth.shh.delete_sym_key(key_id)

    #
    # shh_post
    #
    def test_shh_post(self, web3: "Web3") -> None:
        info = web3.geth.shh.info()
        receiver_pub = web3.geth.shh.get_public_key(web3.geth.shh.new_key_pair())
        assert web3.geth.shh.post({
            "topic": HexStr("0x12345678"),
            "powTarget": info['minPow'],
            "powTime": 2,
            "payload": web3.toHex(text="testing shh on web3.py"),
            "pubKey": receiver_pub,
        })

    def test_shh_post_deprecated(self, web3: "Web3") -> None:
        with pytest.warns(DeprecationWarning):
            info = web3.geth.shh.info()
            receiver_pub = web3.geth.shh.getPublicKey(web3.geth.shh.newKeyPair())
            assert web3.geth.shh.post({
                "topic": HexStr("0x12345678"),
                "powTarget": info['minPow'],
                "powTime": 2,
                "payload": web3.toHex(text="testing shh on web3.py"),
                "pubKey": receiver_pub,
            })

    #
    # shh_properties
    #
    def test_shh_version(self, web3: "Web3") -> None:
        version = web3.geth.shh.version()
        assert version == '6.0'

    def test_shh_info(self, web3: "Web3") -> None:
        pre_info = web3.geth.shh.info()
        assert pre_info["maxMessageSize"] != 2048
        assert pre_info["minPow"] != 0.6

        web3.geth.shh.set_max_message_size(2048)
        web3.geth.shh.set_min_pow(0.6)

        info = web3.geth.shh.info()

        assert len(info) == 4
        assert info["maxMessageSize"] == 2048
        assert info["minPow"] == 0.6

    def test_shh_info_deprecated(self, web3: "Web3") -> None:
        with pytest.warns(DeprecationWarning):
            pre_info = web3.geth.shh.info()
            assert pre_info["maxMessageSize"] != 1024
            assert pre_info["minPow"] != 0.5

            web3.geth.shh.setMaxMessageSize(1024)
            web3.geth.shh.setMinPoW(0.5)

            info = web3.geth.shh.info()

            assert len(info) == 4
            assert info["maxMessageSize"] == 1024
            assert info["minPow"] == 0.5


class ParityShhModuleTest():
    #
    # shh_filter
    #
    def test_shh_sync_filter(self, web3: "Web3") -> None:
        sender = web3.parity.shh.new_key_pair()
        sender_pub = web3.parity.shh.get_public_key(sender)

        receiver = web3.parity.shh.new_key_pair()
        receiver_pub = web3.parity.shh.get_public_key(receiver)

        topic = HexStr('0x13370000')
        payloads = [web3.toHex(text="test message :)"), web3.toHex(text="2nd test message")]

        shh_filter_id = web3.parity.shh.new_message_filter({
            'decryptWith': receiver,
            'from': sender_pub,
            'topics': [topic],
        })

        shh_filter = ShhFilter(web3, shh_filter_id)
        time.sleep(1)

        assert web3.parity.shh.post({
            'from': sender,
            'payload': payloads[0],
            'to': {'public': receiver_pub},
            'topics': [topic],
            'priority': 1000,
            'ttl': 100,
        })
        time.sleep(1)

        assert web3.parity.shh.post({
            'from': receiver,
            'payload': payloads[1],
            'topics': [topic],
            'priority': 1000,
            'ttl': 100,
        })
        time.sleep(1)
        received_messages = shh_filter.get_new_entries()
        assert len(received_messages) == 1

        message = received_messages[0]

        assert message["payload"] == HexBytes(payloads[1])
        assert message["topic"] == HexBytes(topic)

    def test_shh_async_filter(self, web3: "Web3") -> None:
        received_messages: List[ShhMessage] = []

        sender = web3.parity.shh.new_key_pair()
        sender_pub = web3.parity.shh.get_public_key(sender)

        receiver = web3.parity.shh.new_key_pair()
        receiver_pub = web3.parity.shh.get_public_key(receiver)

        topic = HexStr('0x13370000')
        payloads = [web3.toHex(text="test message :)"), web3.toHex(text="2nd test message")]

        shh_filter_id = web3.parity.shh.new_message_filter({
            'decryptWith': receiver,
            'from': sender_pub,
            'topics': [topic]
        })
        shh_filter = ShhFilter(web3, shh_filter_id, poll_interval=0.5)
        watcher = shh_filter.watch(received_messages.extend)

        web3.parity.shh.post({
            'from': sender,
            'payload': payloads[0],
            'topics': [topic],
            'to': {'public': receiver_pub},
            'priority': 1000,
            'ttl': 100,
        })
        time.sleep(1)

        web3.parity.shh.post({
            'from': sender,
            'payload': payloads[1],
            'topics': [topic],
            'to': {'identity': receiver},
            'priority': 1000,
            'ttl': 100,
        })
        time.sleep(1)

        assert len(received_messages) == 1

        message = received_messages[0]

        assert message["payload"] == HexBytes(payloads[0])
        assert message["topic"] == HexBytes(topic)

        watcher.stop()

    # Sometimes the post fails because PoW is too low.
    # We don't care if an error or a True response comes back,
    # we only care that we're interfacing correctly with Parity
    @pytest.mark.xfail(strict=False, raises=ValueError)
    def test_shh_remove_filter(self, web3: "Web3") -> None:
        receiver = web3.parity.shh.new_key_pair()
        receiver_pub = web3.parity.shh.get_public_key(receiver)

        payload = web3.toHex(text="test message :)")
        topic = HexStr('0x13370000')
        shh_filter = web3.parity.shh.new_message_filter({'decryptWith': None, 'topics': [topic]})

        assert web3.parity.shh.post({
            'payload': payload,
            'topics': [topic],
            'to': {'public': receiver_pub},
            'priority': 500,
            'ttl': 400,
        })
        time.sleep(1)

        # Commented out until parity filter bug is resolved
        # https://github.com/paritytech/parity-ethereum/issues/10565
        # message = ShhFilter(web3, shh_filter).get_new_entries()
        # assert message["payload"] == HexBytes(payload)

        assert web3.parity.shh.delete_message_filter(shh_filter)

        try:
            web3.parity.shh.get_filter_messages(shh_filter)
            assert False
        except BaseException:
            assert True

    #
    # shh_key_pair
    #
    def test_shh_asymmetric_key_pair(self, web3: "Web3") -> None:
        # Test generating key
        key_id = web3.parity.shh.new_key_pair()
        assert len(web3.parity.shh.get_public_key(key_id)) == 130

        private_key = web3.parity.shh.get_private_key(key_id)
        assert len(private_key) == 66
        assert web3.parity.shh.delete_key(key_id)

        # Test adding a key
        assert not web3.parity.shh.delete_key(key_id)
        key_id = web3.parity.shh.add_private_key(private_key)
        assert web3.parity.shh.delete_key(key_id)

    def test_shh_symmetric_key_pair(self, web3: "Web3") -> None:
        # Test generating key
        key_id = web3.parity.shh.new_sym_key()

        key = web3.parity.shh.get_sym_key(key_id)
        assert len(key) == 66
        assert web3.parity.shh.delete_key(key_id)

        # Test adding a key
        assert not web3.parity.shh.delete_key(key_id)
        key_id = web3.parity.shh.add_sym_key(key)
        assert web3.parity.shh.delete_key(key_id)

    #
    # shh_post
    #

    # Sometimes the post fails because PoW is too low.
    # We don't care if an error or a True response comes back,
    # we only care that we're interfacing correctly with Parity
    @pytest.mark.xfail(strict=False, raises=ValueError)
    def test_shh_post(self, web3: "Web3") -> None:
        sender = web3.parity.shh.new_key_pair()
        assert web3.parity.shh.post({
            "topics": [HexStr("0x12345678")],
            "payload": web3.toHex(text="testing shh on web3.py"),
            "from": sender,
            "priority": 40,
            "ttl": 400,
        })

    def test_shh_info(self, web3: "Web3") -> None:
        info = web3.parity.shh.info()

        assert len(info) == 3
        assert is_integer(info["memory"])
        assert is_integer(info["messages"])
        assert is_integer(info["targetMemory"])
