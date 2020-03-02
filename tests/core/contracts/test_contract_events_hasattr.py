import pytest 
import json 

CONTRACT_ABI = json.loads('[{"constant":false,"inputs":[],"name":"return13","outputs":[{"name":"result","type":"int256"}],"type":"function"},{"constant":true,"inputs":[],"name":"counter","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"amt","type":"uint256"}],"name":"increment","outputs":[{"name":"result","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"a","type":"int256"},{"name":"b","type":"int256"}],"name":"add","outputs":[{"name":"result","type":"int256"}],"type":"function"},{"constant":false,"inputs":[],"name":"increment","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"a","type":"int256"}],"name":"multiply7","outputs":[{"name":"result","type":"int256"}],"type":"function"},{"anonymous":false,"inputs":[{"indexed":false,"name":"value","type":"uint256"}],"name":"Increased","type":"event"}]')  # noqa: E501

def test_contract_event_hasattr(Web3, EthereumTesterProvider, event_name, expected):
    web3 = Web3(EthereumTesterProvider)
    contract = web3.eth.contract(abi=CONTRACT_ABI)
    if hasattr(contract.events, event_name) == expected:
        return True 
    return False 
