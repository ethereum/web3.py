from eth_utils import (
    is_string,
    is_boolean,
    is_integer,
)


class NetModuleTest(object):
    def test_net_version(self, web3):
        version = web3.net.version

        assert is_string(version)
        assert version.isdigit()

    def test_net_listening(self, web3):
        listening = web3.net.listening

        assert is_boolean(listening)

    def test_net_peerCount(self, web3):
        peer_count = web3.net.peerCount

        assert is_integer(peer_count)
