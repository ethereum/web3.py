def test_net_listening(web3_tester):
    assert web3_tester.net.listening is False


def test_net_peerCount(web3_tester):
    assert web3_tester.net.peerCount == 0
