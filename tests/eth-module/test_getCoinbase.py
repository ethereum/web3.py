from web3 import Web3
from web3.web3.rpcprovider import TestRPCProvider


def test_getCoinbase(web3_tester):
    cb = web3_tester.eth.getCoinbase()
    assert cb == "0x82a978b3f5962a5b0957d9ee9eef472ee55b42f1"
