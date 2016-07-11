import web3 as web3_module
import testrpc


def test_api_property(web3):
    assert web3.version.api == web3_module.__version__


def test_node_property(web3):
    client_name, client_version, platform_name, platform_version = web3.version.node.split('/')

    assert client_name in {"Geth", "TestRPC"}
    assert platform_name in {"darwin", "linux", "linux2", "linux3"}


def test_network_property(web3):
    assert web3.version.network in {1, 2, 3, 1234}


def test_ethereum_property(web3):
    assert web3.version.ethereum == 63
