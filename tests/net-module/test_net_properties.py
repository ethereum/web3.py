def test_net_listening(web3):
    assert web3.net.listening is False


def test_net_peerCount(web3):
    assert web3.net.peerCount == 0
