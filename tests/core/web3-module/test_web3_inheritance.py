from web3 import (
    EthereumTesterProvider,
    Web3,
)


def test_classes_may_inherit_from_web3():
    class InheritsFromWeb3(Web3):
        pass

    inherited_w3 = InheritsFromWeb3(EthereumTesterProvider())
    assert inherited_w3.eth.chain_id == inherited_w3.provider.eth_tester.chain_id
