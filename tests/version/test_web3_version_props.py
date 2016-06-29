import web3 as web3_module
import testrpc


def test_api_property(web3):
    assert web3.version.api == web3_module.__version__


def test_node_property(web3):
    assert web3.version.node == testrpc.testrpc.web3_clientVersion()


def test_network_property(web3):
    assert web3.version.network == testrpc.testrpc.net_version()


def test_ethereum_property(web3):
    assert web3.version.ethereum == testrpc.testrpc.eth_protocolVersion()
