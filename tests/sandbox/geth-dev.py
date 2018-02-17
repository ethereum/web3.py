""" Demonstration / Test Code For "geth --dev" compatibility

Adopts the example from the web3.py manual.

This code demonstrates the activation of the "geth -dev" / Rinkeby compatibility

Usage:

    geth --dev --ipc
    python tests/sandbox/geth-dev.py

"""

from solc import (
    compile_source,
)
from web3 import (
    HTTPProvider,
    Web3,
)
from web3.contract import (
    ConciseContract,
)
from web3.middleware.geth_dev import (
    geth_dev_middleware,
)

# w3 = Web3(IPCProvider('/tmp/geth.ipc'))
w3 = Web3(HTTPProvider('http://127.0.0.1:8545'))

# ========================== MIDDLEWARE WORKAROUND =============================

# from web3.middleware.geth_dev import geth_dev_middleware
w3.manager.middleware_stack.add_bottom(geth_dev_middleware, 'addedspec')

# disable above line and enable the below will trigger error on dev-nets
# w3.manager.middleware_stack.add(geth_dev_middleware, 'addedspec')

# ==============================================================================

# Solidity source code
contract_source_code = '''
pragma solidity ^0.4.0;

contract Greeter {
    string public greeting;

    function Greeter() {
        greeting = 'Hello';
    }

    function setGreeting(string _greeting) public {
        greeting = _greeting;
    }

    function greet() constant returns (string) {
        return greeting;
    }
}
'''

compiled_sol = compile_source(contract_source_code)
contract_interface = compiled_sol['<stdin>:Greeter']

# Instantiate and deploy contract
contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

# Get transaction hash from deployed contract
tx_hash = contract.deploy(transaction={'from': w3.eth.accounts[0], 'gas': 410000})
print('hash:', tx_hash)

# Get tx receipt to get contract address
tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
print('txreceipt ', tx_receipt)

contract_address = tx_receipt['contractAddress']

# Contract instance in concise mode
contract_instance = w3.eth.contract(
    contract_address, abi=contract_interface['abi'], ContractFactoryClass=ConciseContract
)

# Getters + Setters for web3.eth.contract object
print('Contract value: {}'.format(contract_instance.greet()))
contract_instance.setGreeting('Nihao', transact={'from': w3.eth.accounts[0]})
print('Setting value to: Nihao')
print('Contract value: {}'.format(contract_instance.greet()))
