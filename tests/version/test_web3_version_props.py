import web3
import testrpc


def test_api_property(web3_tester):
    assert web3_tester.version.api == web3.__version__


def test_node_property(web3_tester):
    assert web3_tester.version.node == testrpc.testrpc.web3_clientVersion()


def test_network_property(web3_tester):
    assert web3_tester.version.network == testrpc.testrpc.net_version()


def test_ethereum_property(web3_tester):
    assert web3_tester.version.ethereum == testrpc.testrpc.eth_protocolVersion()
