Examples
========

.. contents:: :local:

Here are some common things you might want to do with web3.

Looking up blocks
-----------------

Blocks can be looked up by either their number or hash using the
``web3.eth.getBlock`` API.  Block hashes should be in their hexadecimal
representation.  Block numbers

.. code-block:: python

    # get a block by number
    >>> web3.eth.getBlock(12345)
    {
        'author': '0xad5c1768e5974c231b2148169da064e61910f31a',
        'difficulty': 735512610763,
        'extraData': '0x476574682f76312e302e302f6c696e75782f676f312e342e32',
        'gasLimit': 5000,
        'gasUsed': 0,
        'hash': '0x767c2bfb3bdee3f78676c1285cd757bcd5d8c272cef2eb30d9733800a78c0b6d',
        'logsBloom': '0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
        'miner': '0xad5c1768e5974c231b2148169da064e61910f31a',
        'mixHash': '0x31d9ec7e3855aeba37fd92aa1639845e70b360a60f77f12eff530429ef8cfcba',
        'nonce': '0x549f882c5f356f85',
        'number': 12345,
        'parentHash': '0x4b3c1d7e65a507b62734feca1ee9f27a5379e318bd52ae62de7ba67dbeac66a3',
        'receiptsRoot': '0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421',
        'sealFields': ['0x31d9ec7e3855aeba37fd92aa1639845e70b360a60f77f12eff530429ef8cfcba',
        '0x549f882c5f356f85'],
        'sha3Uncles': '0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347',
        'size': 539,
        'stateRoot': '0xca495e22ed6b88c61714d129dbc8c94f5bf966ac581c09a57c0a72d0e55e7286',
        'timestamp': 1438367030,
        'totalDifficulty': 3862140487204603,
        'transactions': [],
        'transactionsRoot': '0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421',
        'uncles': [],
    }
    # get a block by it's hash
    >>> web3.eth.getBlock('0x767c2bfb3bdee3f78676c1285cd757bcd5d8c272cef2eb30d9733800a78c0b6d')
    {...}


Getting the latest block
------------------------

You can also retrieve the latest block using the string ``'latest'`` in the
``web3.eth.getBlock`` API.

.. code-block:: python

    >>> web3.eth.getBlock('latest')
    {...}


If you want to know the latest block number you can use the
``web3.eth.blockNumber`` property.

.. code-block:: python

    >>> web3.eth.blockNumber
    4194803


Currency conversions
--------------------

Web3 can help you convert between denominations.  The following denominations are supported.

+--------------+---------------------------------+
| denomination | amount in wei                   |
+--------------+---------------------------------+
| wei          | 1                               |
+--------------+---------------------------------+
| kwei         | 1000                            |
+--------------+---------------------------------+
| babbage      | 1000                            |
+--------------+---------------------------------+
| femtoether   | 1000                            |
+--------------+---------------------------------+
| mwei         | 1000000                         |
+--------------+---------------------------------+
| lovelace     | 1000000                         |
+--------------+---------------------------------+
| picoether    | 1000000                         |
+--------------+---------------------------------+
| gwei         | 1000000000                      |
+--------------+---------------------------------+
| shannon      | 1000000000                      |
+--------------+---------------------------------+
| nanoether    | 1000000000                      |
+--------------+---------------------------------+
| nano         | 1000000000                      |
+--------------+---------------------------------+
| szabo        | 1000000000000                   |
+--------------+---------------------------------+
| microether   | 1000000000000                   |
+--------------+---------------------------------+
| micro        | 1000000000000                   |
+--------------+---------------------------------+
| finney       | 1000000000000000                |
+--------------+---------------------------------+
| milliether   | 1000000000000000                |
+--------------+---------------------------------+
| milli        | 1000000000000000                |
+--------------+---------------------------------+
| ether        | 1000000000000000000             |
+--------------+---------------------------------+
| kether       | 1000000000000000000000          |
+--------------+---------------------------------+
| grand        | 1000000000000000000000          |
+--------------+---------------------------------+
| mether       | 1000000000000000000000000       |
+--------------+---------------------------------+
| gether       | 1000000000000000000000000000    |
+--------------+---------------------------------+
| tether       | 1000000000000000000000000000000 |
+--------------+---------------------------------+


.. code-block:: python

    >>> web3.toWei('1', 'ether')
    1000000000000000000
    >>> web3.fromWei('1000000000000000000', 'ether')
    Decimal('1')
    >>> from_wei(123456789, 'ether')
    Decimal('1.23456789E-10')


Looking up transactions
-----------------------

You can look up transactions using the ``web3.eth.getTransaction`` function.

.. code-block:: python

    >>> web3.eth.getTransaction('0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060')
    {
        'blockHash': '0x4e3a3754410177e6937ef1f84bba68ea139e8d1a2258c5f85db9f1cd715a1bdd',
        'blockNumber': 46147,
        'condition': None,
        'creates': None,
        'from': '0xa1e4380a3b1f749673e270229993ee55f35663b4',
        'gas': 21000,
        'gasPrice': 50000000000000,
        'hash': '0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060',
        'input': '0x',
        'networkId': None,
        'nonce': 0,
        'publicKey': '0x376fc429acc35e610f75b14bc96242b13623833569a5bb3d72c17be7e51da0bb58e48e2462a59897cead8ab88e78709f9d24fd6ec24d1456f43aae407a8970e4',
        'r': '0x88ff6cf0fefd94db46111149ae4bfc179e9b94721fffd821d38d16464b3f71d0',
        'raw': '0xf86780862d79883d2000825208945df9b87991262f6ba471f09758cde1c0fc1de734827a69801ca088ff6cf0fefd94db46111149ae4bfc179e9b94721fffd821d38d16464b3f71d0a045e0aff800961cfce805daef7016b9b675c137a6a41a548f7b60a3484c06a33a',
        's': '0x45e0aff800961cfce805daef7016b9b675c137a6a41a548f7b60a3484c06a33a',
        'standardV': '0x1',
        'to': '0x5df9b87991262f6ba471f09758cde1c0fc1de734',
        'transactionIndex': 0,
        'v': '0x1c',
        'value': 31337,
    }

If no transaction for the given hash can be found, then this function will
instead return ``None``.


Looking up receipts
-------------------

Transaction receipts can be retrieved using the ``web3.eth.getTransactionReceipt`` API.


.. code-block:: python

    >>> web3.eth.getTransactionReceipt('0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060')
    {
        'blockHash': '0x4e3a3754410177e6937ef1f84bba68ea139e8d1a2258c5f85db9f1cd715a1bdd',
        'blockNumber': 46147,
        'contractAddress': None,
        'cumulativeGasUsed': 21000,
        'gasUsed': 21000,
        'logs': [],
        'logsBloom': '0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
        'root': '0x96a8e009d2b88b1483e6941e6812e32263b05683fac202abc622a3e31aed1957',
        'transactionHash': '0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060',
        'transactionIndex': 0,
    }


If the transaction has not yet been mined then this method will return ``None``.


Working with Contracts
----------------------

Given the following solidity source file stored at ``contract.sol``.

.. code-block:: javascript

    contract StoreVar {
    
        uint8 public _myVar;
        event MyEvent(uint indexed _var);
    
        function setVar(uint8 _var) public {
            _myVar = _var;
            MyEvent(_var);
        }
    
        function getVar() public view returns (uint8) {
            return _myVar;
        }
    
    }

The following example demonstrates a few things:

* Compiling a contract from a sol file.
* Estimating gas costs of a transaction.
* Transacting with a contract function.
* Waiting for a transaction receipt to be mined.

.. code-block:: python

    import sys
    import time
    import pprint
    
    from web3.providers.eth_tester import EthereumTesterProvider
    from web3 import Web3
    from solc import compile_source
    

    def compile_source_file(file_path):
       with open(file_path, 'r') as f:
          source = f.read()
    
       return compile_source(source)
    
    
    def deploy_contract(w3, contract_interface):
        tx_hash = w3.eth.contract(
            abi=contract_interface['abi'],
            bytecode=contract_interface['bin']).deploy()
    
        address = w3.eth.getTransactionReceipt(tx_hash)['contractAddress']
        return address
    
    
    w3 = Web3(EthereumTesterProvider())
    
    contract_source_path = 'contract.sol'
    compiled_sol = compile_source_file('contract.sol')
    
    contract_id, contract_interface = compiled_sol.popitem()
    
    address = deploy_contract(w3, contract_interface)
    print("Deployed {0} to: {1}\n".format(contract_id, address))
    
    store_var_contract = w3.eth.contract(
       address=address,
       abi=contract_interface['abi'])
    
    gas_estimate = store_var_contract.functions.setVar(255).estimateGas()
    print("Gas estimate to transact with setVar: {0}\n".format(gas_estimate))
    
    if gas_estimate < 100000:
      print("Sending transaction to setVar(255)\n")
      tx_hash = store_var_contract.functions.setVar(255).transact()
      receipt = w3.eth.waitForTransactionReceipt(tx_hash)
      print("Transaction receipt mined: \n")
      pprint.pprint(dict(receipt))
      print("Was transaction successful? \n")
      pprint.pprint(receipt['status'])
    else:
      print("Gas cost exceeds 100000")


Output:

.. code-block:: none

    Deployed <stdin>:StoreVar to: 0xF2E246BB76DF876Cef8b38ae84130F4F55De395b
    
    Gas estimate to transact with setVar: 32463
    
    Sending transaction to setVar(255)
    
    Transaction receipt mined: 
    
    {'blockHash': HexBytes('0x94e07b0b88667da284e914fa44b87d4e7fec39761be51245ef94632a3b5ab9f0'),
     'blockNumber': 2,
     'contractAddress': None,
     'cumulativeGasUsed': 43106,
     'gasUsed': 43106,
     'logs': [AttributeDict({'type': 'mined', 'logIndex': 0, 'transactionIndex': 0, 'transactionHash': HexBytes('0x3ac3518cc59d1698aa03a0bab7fb8191a4ef017aeda7429b11e8c6462b20a62a'), 'blockHash': HexBytes('0x94e07b0b88667da284e914fa44b87d4e7fec39761be51245ef94632a3b5ab9f0'), 'blockNumber': 2, 'address': '0xF2E246BB76DF876Cef8b38ae84130F4F55De395b', 'data': '0x', 'topics': [HexBytes('0x6c2b4666ba8da5a95717621d879a77de725f3d816709b9cbe9f059b8f875e284'), HexBytes('0x00000000000000000000000000000000000000000000000000000000000000ff')]})],
     'transactionHash': HexBytes('0x3ac3518cc59d1698aa03a0bab7fb8191a4ef017aeda7429b11e8c6462b20a62a'),
     'transactionIndex': 0}


Working with an ERC20 Token Contract
------------------------------------

Most fungible tokens on the Ethereum blockchain conform to the `ERC20`_
standard.  This section of the guide covers interacting with an existing token
contract which conforms to this standard.

.. testsetup::

    from web3 import Web3
    w3 = Web3(Web3.EthereumTesterProvider())
    bytecode = '6060604052341561000c57fe5b604051602080610acb833981016040528080519060200190919050505b620f42408114151561003b5760006000fd5b670de0b6b3a76400008102600281905550600254600060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055505b505b610a27806100a46000396000f30060606040523615610097576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806306fdde0314610099578063095ea7b31461013257806318160ddd1461018957806323b872dd146101af578063313ce5671461022557806370a082311461025157806395d89b411461029b578063a9059cbb14610334578063dd62ed3e1461038b575bfe5b34156100a157fe5b6100a96103f4565b60405180806020018281038252838181518152602001915080519060200190808383600083146100f8575b8051825260208311156100f8576020820191506020810190506020830392506100d4565b505050905090810190601f1680156101245780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b341561013a57fe5b61016f600480803573ffffffffffffffffffffffffffffffffffffffff1690602001909190803590602001909190505061042e565b604051808215151515815260200191505060405180910390f35b341561019157fe5b610199610521565b6040518082815260200191505060405180910390f35b34156101b757fe5b61020b600480803573ffffffffffffffffffffffffffffffffffffffff1690602001909190803573ffffffffffffffffffffffffffffffffffffffff16906020019091908035906020019091905050610527565b604051808215151515815260200191505060405180910390f35b341561022d57fe5b610235610791565b604051808260ff1660ff16815260200191505060405180910390f35b341561025957fe5b610285600480803573ffffffffffffffffffffffffffffffffffffffff16906020019091905050610796565b6040518082815260200191505060405180910390f35b34156102a357fe5b6102ab6107e0565b60405180806020018281038252838181518152602001915080519060200190808383600083146102fa575b8051825260208311156102fa576020820191506020810190506020830392506102d6565b505050905090810190601f1680156103265780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b341561033c57fe5b610371600480803573ffffffffffffffffffffffffffffffffffffffff1690602001909190803590602001909190505061081a565b604051808215151515815260200191505060405180910390f35b341561039357fe5b6103de600480803573ffffffffffffffffffffffffffffffffffffffff1690602001909190803573ffffffffffffffffffffffffffffffffffffffff16906020019091905050610973565b6040518082815260200191505060405180910390f35b604060405190810160405280600981526020017f54657374546f6b656e000000000000000000000000000000000000000000000081525081565b600081600160003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055508273ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff167f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925846040518082815260200191505060405180910390a3600190505b92915050565b60025481565b600081600060008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205410806105f1575081600160008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054105b156105fc5760006000fd5b81600060008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000828254019250508190555081600060008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000828254039250508190555081600160008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082825403925050819055508273ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef846040518082815260200191505060405180910390a3600190505b9392505050565b601281565b6000600060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205490505b919050565b604060405190810160405280600481526020017f544553540000000000000000000000000000000000000000000000000000000081525081565b600081600060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205410156108695760006000fd5b81600060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000828254039250508190555081600060008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082825401925050819055508273ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef846040518082815260200191505060405180910390a3600190505b92915050565b6000600160008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205490505b929150505600a165627a7a723058205071371ee2a4a1be3c96e77d939cdc26161a256fdd638efc08bd33dfc65d3b850029'
    ABI = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function","stateMutability":"view"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function","stateMutability":"nonpayable"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function","stateMutability":"view"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function","stateMutability":"nonpayable"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function","stateMutability":"view"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function","stateMutability":"view"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function","stateMutability":"view"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function","stateMutability":"nonpayable"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function","stateMutability":"view"},{"inputs":[{"name":"_totalSupply","type":"uint256"}],"payable":false,"type":"constructor","stateMutability":"nonpayable"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"}]'
    factory = w3.eth.contract(abi=ABI, bytecode=bytecode)
    alice, bob = w3.eth.accounts[0], w3.eth.accounts[1]
    assert alice == '0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf', alice
    assert bob == '0x2B5AD5c4795c026514f8317c7a215E218DcCD6cF', bob
    tx_hash = factory.constructor(1000000).transact({'from': alice})
    assert tx_hash == b'h9\xeb\xdb4\x07\x03y\x92RP`X\xf6\xf7\x9f\xfaT\xed&e\xee*\xc2\rx\xb3\xab\x8c4\xc9\x1f', tx_hash
    txn_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    assert txn_receipt['contractAddress'] == '0xF2E246BB76DF876Cef8b38ae84130F4F55De395b', txn_receipt['contractAddress']
    contract_address = txn_receipt['contractAddress']
    contract = w3.eth.contract(contract_address, abi=ABI)
    total_supply = contract.functions.totalSupply().call()
    decimals = 10 ** 18
    assert total_supply == 1000000 * decimals, total_supply


In this guide we will interact with an existing token contract that we have
already deployed to a local testing chain.  This guide assumes:

1. An existing token contract at a known address.
1. Access to the proper ``ABI`` for the given contract.
1. A `~web3.main.Web3` instance connected to a provider with an unlocked account which can send transactions.


Creating the contract factory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First we need to create a contract instance with the address of our token
contract and the ``ERC20`` ABI.

.. doctest::

    >>> contract = w3.eth.contract(contract_address, abi=ABI)
    >>> contract.address
    '0xF2E246BB76DF876Cef8b38ae84130F4F55De395b'


Querying token metadata
~~~~~~~~~~~~~~~~~~~~~~~

Each token will have a total supply which represents the total number of tokens
in circulation.  In this example we've initialized the token contract to have 1
million tokens.  Since this token contract is setup to have 18 decimal places,
the raw total supply returned by the contract is going to have 18 additional
decimal places.

.. doctest::

    >>> contract.functions.name().call()
    'TestToken'
    >>> contract.functions.symbol().call()
    'TEST'
    >>> decimals = contract.functions.decimals().call()
    >>> decimals
    18
    >>> DECIMALS = 10 ** decimals
    >>> contract.functions.totalSupply().call() // DECIMALS
    1000000


Query account balances
~~~~~~~~~~~~~~~~~~~~~~

Next we can query some account balances using the contract's ``balanceOf``
function.  The token contract we are using starts with a single account which
we'll refer to as ``alice`` holding all of the tokens.

.. doctest::

    >>> alice = '0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf'
    >>> bob = '0x2B5AD5c4795c026514f8317c7a215E218DcCD6cF'
    >>> raw_balance = contract.functions.balanceOf(alice).call()
    >>> raw_balance
    1000000000000000000000000
    >>> raw_balance // DECIMALS
    1000000
    >>> contract.functions.balanceOf(bob).call()
    0


Sending tokens
~~~~~~~~~~~~~~

Next we can transfer some tokens from ``alice`` to ``bob`` using the contract's
``transfer`` function.


.. doctest::

    >>> tx_hash = contract.functions.transfer(bob, 100).transact({'from': alice})
    >>> tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    >>> contract.functions.balanceOf(alice).call()
    999999999999999999999900
    >>> contract.functions.balanceOf(bob).call()
    100


Creating an approval for external transfers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Alice could also *approve* someone else to spend tokens from her account using
the ``approve`` function.  We can also query how many tokens we're approved to
spend using the ``allowance`` function.

.. doctest::

    >>> contract.functions.allowance(alice, bob).call()
    0
    >>> tx_hash = contract.functions.approve(bob, 200).transact({'from': alice})
    >>> tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    >>> contract.functions.allowance(alice, bob).call()
    200


Performing an external transfer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When someone has an allowance they can transfer those tokens using the
``transferFrom`` function.

.. doctest::

    >>> contract.functions.allowance(alice, bob).call()
    200
    >>> contract.functions.balanceOf(bob).call()
    100
    >>> tx_hash = contract.functions.transferFrom(alice, bob, 75).transact({'from': bob})
    >>> tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    >>> contract.functions.allowance(alice, bob).call()
    125
    >>> contract.functions.balanceOf(bob).call()
    175


.. _ERC20: https://github.com/ethereum/EIPs/blob/7f4f0377730f5fc266824084188cc17cf246932e/EIPS/eip-20.md
