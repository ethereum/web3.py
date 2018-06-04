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
    
    
    def wait_for_receipt(w3, tx_hash, poll_interval):
       while True:
           tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
           if tx_receipt:
             return tx_receipt
           time.sleep(poll_interval)
    
    
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
      receipt = wait_for_receipt(w3, tx_hash, 1)
      print("Transaction receipt mined: \n")
      pprint.pprint(dict(receipt))
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
