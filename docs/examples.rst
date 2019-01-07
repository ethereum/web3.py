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

Creation of the contract factory from the ERC20 ABI
---------------------------------------------------

Using this command, you can create a contract factory from the ERC20 ABI. You need to specify the contract address

.. testsetup::

    from web3 import Web3
    import json
    w3 = Web3(Web3.EthereumTesterProvider())
    bytecode='60606040526040516108ee3803806108ee83398101604052805160805160a05160c05160e0519394928301939192019060008054600160a060020a03191633179055600160a060020a0381166000146100655760008054600160a060020a031916821790555b600160a060020a033316600090815260056020908152604082208790558551600180549381905292600281851615610100026000190190911604601f9081018390047fb10e2d527612073b26eecdfd717e6a320cf44b4afac2b0732d9fcbe2b7fa0cf69081019390919089019083901061010257805160ff19168380011785555b506101329291505b8082111561018b57600081556001016100ee565b828001600101855582156100e6579182015b828111156100e6578251826000505591602001919060010190610114565b50508160026000509080519060200190828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061018f57805160ff19168380011785555b506101bf9291506100ee565b5090565b8280016001018555821561017f579182015b8281111561017f5782518260005055916020019190600101906101a1565b50506003805460ff19169390931790925550505060045561070a806101e46000396000f3606060405236156100b95760e060020a600035046306fdde0381146100c1578063095ea7b31461011d57806318160ddd1461015857806323b872dd14610161578063313ce5671461019357806370a082311461019f57806379c65068146101b75780638da5cb5b146101db57806395d89b41146101ed578063a9059cbb14610246578063b414d4b614610275578063dc3080f214610290578063dd62ed3e146102b5578063e724529c146102da578063f2fde38b146102fe575b61031f610002565b610321600180546020600282841615610100026000190190921691909104601f810182900490910260809081016040526060828152929190828280156103dc5780601f106103b1576101008083540402835291602001916103dc565b600160a060020a03338116600090815260076020908152604080832060043594909416835292905290812060243590555b6060908152602090f35b61014e60045481565b61014e600435602435604435600160a060020a0383166000908152600560205260408120548290101561058a57610002565b61014e60035460ff1681565b61014e60043560056020526000908152604090205481565b61031f60043560243560005433600160a060020a039081169116146104d957610002565b61014e600054600160a060020a031681565b610321600280546020601f600019600184161561010002019092168390049182018190040260809081016040526060828152929190828280156103dc5780601f106103b1576101008083540402835291602001916103dc565b61031f60043560243533600160a060020a0316600090815260056020526040902054819010156103e457610002565b61014e60043560066020526000908152604090205460ff1681565b60086020908152600435600090815260408082209092526024358152205461014e9081565b60076020908152600435600090815260408082209092526024358152205461014e9081565b61031f60043560243560005433600160a060020a0390811691161461053557610002565b61031f60043560005433600160a060020a0390811691161461038f57610002565b005b60405180806020018281038252838181518152602001915080519060200190808383829060006004602084601f0104600f02600301f150905090810190601f1680156103815780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b6000805473ffffffffffffffffffffffffffffffffffffffff19168217905550565b820191906000526020600020905b8154815290600101906020018083116103bf57829003601f168201915b505050505081565b600160a060020a03821660009081526040902054808201101561040657610002565b33600160a060020a031660009081526006602052604090205460ff161561042c57610002565b806005600050600033600160a060020a03168152602001908152602001600020600082828250540392505081905550806005600050600084600160a060020a0316815260200190815260200160002060008282825054019250508190555081600160a060020a031633600160a060020a03167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef836040518082815260200191505060405180910390a35050565b600160a060020a0380831660008181526005602090815260408220805486019055600480548601905590546060858152929316917fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef9190a35050565b600160a060020a03821660008181526006602052604090819020805460ff191684179055606091825260808390527f48335238b4855f35377ed80f164e8c6f3c366e54ac00b96a6402d4a9814a03a591a15050565b600160a060020a0383168152604081205482810110156105a957610002565b600160a060020a03841681526006602052604081205460ff16156105cc57610002565b600760209081526040808320600160a060020a033381168086529184528285205490881685526008845282852091855292528220548301111561060e57610002565b816005600050600086600160a060020a03168152602001908152602001600020600082828250540392505081905550816005600050600085600160a060020a03168152602001908152602001600020600082828250540192505081905550816008600050600086600160a060020a03168152602001908152602001600020600050600033600160a060020a0316815260200190815260200160002060008282825054019250508190555082600160a060020a031633600160a060020a03167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef846040518082815260200191505060405180910390a3939250505056000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000a0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000e0000000000000000000000000fb6916095ca1df60bb79ce92ce3ea74c37c5d3590000000000000000000000000000000000000000000000000000000000000008556e69636f726e730000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004f09fa68400000000000000000000000000000000000000000000000000000000'
    abi='[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]'

.. doctest::

    >>> factory=w3.eth.contract(abi=json.loads(abi), bytecode=bytecode)
    >>> tx_hash = factory.constructor(1000000, 'DEM', 18, 'DE', 1).transact()
    >>> print(tx_hash)
    b'\xe9K\xcfz\xfc9*-+\x17|\xd4at.\xe32t\x13\xf4\\\xe8\x8b\x9e6?\x08\xa1\xb4\xe6[\xd3'
    >>> txn_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

Instantiate a contract pointing at a specific address
-----------------------------------------------------

.. doctest::

    >>> new_contract = w3.eth.contract(address='0x89205A3A3b2A69De6Dbf7f01ED13B2108B2c43e7', abi=json.loads(abi))
    >>> balance = new_contract.functions.balanceOf('0x89205A3A3b2A69De6Dbf7f01ED13B2108B2c43e7')

Query account balance
---------------------

.. doctest::

    >>> new_contract = w3.eth.contract(address=w3.eth.accounts[0], abi=json.loads(abi))
    >>> w3.eth.getBalance(w3.eth.accounts[0])
    999999999999999999350633

Querying the approved spending balance for external transfers
-------------------------------------------------------------

.. doctest::

    >>> new_contract = w3.eth.contract(address=w3.eth.accounts[0], abi=json.loads(abi))
    >>> alice, bob = w3.eth.accounts[:2]
    >>> txn_hash = new_contract.functions.transferFrom(alice, bob, 12345).transact()
    >>> txn_receipt = w3.eth.waitForTransactionReceipt(txn_hash)

Creating an approval for external transfers
-------------------------------------------

.. doctest::

    >>> new_contract = w3.eth.contract(address=w3.eth.accounts[0], abi=json.loads(abi))
    >>> w3.eth.getBalance(w3.eth.accounts[0])
    999999999999999999326289
    >>> txn_hash = new_contract.functions.approve(w3.eth.accounts[0], 12345).transact()
    >>> txn_receipt = w3.eth.waitForTransactionReceipt(txn_hash)

Perform direct transfer call
----------------------------

.. doctest::

    >>> new_contract = w3.eth.contract(address=w3.eth.accounts[0], abi=json.loads(abi))
    >>> w3.eth.getBalance(w3.eth.accounts[0])
    999999999999999999303353
    >>> txn_hash = new_contract.functions.transfer(w3.eth.accounts[1], 12345).transact()
    >>> txn_receipt = w3.eth.waitForTransactionReceipt(txn_hash)


Performing a transferFrom call with an approved transfer.
---------------------------------------------------------

.. doctest::

    >>> new_contract = w3.eth.contract(address=w3.eth.accounts[0], abi=json.loads(abi))
    >>> w3.eth.getBalance(w3.eth.accounts[0])
    999999999999999999280417
    >>> alice, bob = w3.eth.accounts[:2]
    >>> txn_hash = new_contract.functions.transferFrom(alice, bob, 12345).transact()
    >>> txn_receipt = w3.eth.waitForTransactionReceipt(txn_hash)
    >>> w3.eth.getBalance(w3.eth.accounts[0])
    999999999999999999256073

Interacting with an ERC20 Contract
----------------------------------

The ERC20 (formally `EIP20 <https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20.md>`_) token standard is the most widely used standard in Ethereum. Here's how to check the current state of an ERC20 token contract.

First, create your Python object representing the ERC20 contract.
For this example, we'll be inspecting the `Unicorns <https://etherscan.io/token/0x89205a3a3b2a69de6dbf7f01ed13b2108b2c43e7>`_ token contract.

.. testsetup::
    
    import os
    # Please play nice and don't use this key for any shenanigans, thanks!!
    os.environ['INFURA_API_KEY'] = "b2679bb624354d1b9a2586154651b51f"

.. doctest::

    >>> import json
    >>> from web3.auto.infura import w3

    >>> ERC20_ABI = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]')  # noqa: 501

    # Address field should be the checksum address at which the ERC20 contract was deployed
    >>> erc20 = w3.eth.contract(address='0x89205A3A3b2A69De6Dbf7f01ED13B2108B2c43e7', abi=ERC20_ABI)

Fetch various data about the current state of the ERC20 contract.

.. doctest::

    >>> erc20.functions.name().call()
    'Unicorns'
    >>> erc20.functions.symbol().call()
    '🦄'
    >>> erc20.functions.decimals().call()
    0
    >>> total_supply = erc20.functions.totalSupply().call()
    >>> assert total_supply > 2040

Get the balance of an account address. 

.. doctest::

    >>> erc20.functions.balanceOf('0xD1220A0cf47c7B9Be7A2E6BA89F429762e7b9aDb').call()
    1

Calculate the token count from the token balance of an account address.

.. doctest::
   
    >>> from decimal import Decimal
    
    # Most applications expect *exact* results, so using the Decimal library,
    # with default precision of 28, is usually sufficient to avoid any rounding error.
    >>> decimals = erc20.functions.decimals().call()
    >>> balance = erc20.functions.balanceOf('0xD1220A0cf47c7B9Be7A2E6BA89F429762e7b9aDb').call()
    >>> balance / Decimal(10 ** decimals)
    Decimal('1')

Balance is *always* an integer in the currency's smallest natural unit (equivalent to 'wei' for ether). Token balance is typically used only for backend calculations.

Token count *may* be a integer or fraction in the currency's primary unit (equivalent to 'eth' for ether). Token count is typically displayed to the user on the front-end since it is more readable.


