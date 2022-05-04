.. _examples:

Examples
========

.. contents:: :local:

Here are some common things you might want to do with web3.

Looking up blocks
-----------------

Blocks can be looked up by either their number or hash using the
``web3.eth.get_block`` API.  Block hashes should be in their hexadecimal
representation.  Block numbers

.. code-block:: python

    # get a block by number
    >>> web3.eth.get_block(12345)
    {
        'author': '0xad5C1768e5974C231b2148169da064e61910f31a',
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
    >>> web3.eth.get_block('0x767c2bfb3bdee3f78676c1285cd757bcd5d8c272cef2eb30d9733800a78c0b6d')
    {...}


Getting the latest block
------------------------

You can also retrieve the latest block using the string ``'latest'`` in the
``web3.eth.get_block`` API.

.. code-block:: python

    >>> web3.eth.get_block('latest')
    {...}


If you want to know the latest block number you can use the
``web3.eth.block_number`` property.

.. code-block:: python

    >>> web3.eth.block_number
    4194803


Checking the balance of an account
----------------------------------

To find the amount of ether owned by an account, use the :meth:`~web3.eth.Eth.get_balance` method.
At the time of writing, the account with the `most ether <https://etherscan.io/accounts/1>`_
has a public address of 0x742d35Cc6634C0532925a3b844Bc454e4438f44e.

.. code-block:: python

   >>> web3.eth.get_balance('0x742d35Cc6634C0532925a3b844Bc454e4438f44e')
   3841357360894980500000001

Note that this number is not denominated in ether, but instead in the smallest unit of value in
Ethereum, wei. Read on to learn how to convert that number to ether.


Converting currency denominations
---------------------------------

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

Picking up from the previous example, the largest account contained
3841357360894980500000001 wei. You can use the :meth:`~web3.fromWei` method
to convert that balance to ether (or another denomination).

.. code-block:: python

    >>> web3.fromWei(3841357360894980500000001, 'ether')
    Decimal('3841357.360894980500000001')

To convert back to wei, you can use the inverse function, :meth:`~web3.toWei`.
Note that Python's default floating point precision is insufficient for this
use case, so it's necessary to cast the value to a
`Decimal <https://docs.python.org/3/library/decimal.html>`_ if it isn't already.

.. code-block:: python

    >>> from decimal import Decimal
    >>> web3.toWei(Decimal('3841357.360894980500000001'), 'ether')
    3841357360894980500000001

Best practice: If you need to work with multiple currency denominations, default
to wei. A typical workflow may require a conversion from some denomination to
wei, then from wei to whatever you need.

.. code-block:: python

    >>> web3.toWei(Decimal('0.000000005'), 'ether')
    5000000000
    >>> web3.fromWei(5000000000, 'gwei')
    Decimal('5')


Making transactions
-------------------

There are a few options for making transactions:

- :meth:`~web3.eth.Eth.send_transaction`

  Use this method if:
    - you want to send ether from one account to another.

- :meth:`~web3.eth.Eth.send_raw_transaction`

  Use this method if:
    - you want to sign the transaction elsewhere, e.g., a hardware wallet.
    - you want to broadcast a transaction through another provider, e.g., Infura.
    - you have some other advanced use case that requires more flexibility.

- :ref:`contract-functions`

  Use these methods if:
    - you want to interact with a contract. Web3.py parses the contract ABI and makes those functions available via the ``functions`` property.

- :meth:`~web3.middleware.construct_sign_and_send_raw_middleware`

  Use this middleware if:
    - you want to automate signing when using ``w3.eth.send_transaction`` or ``ContractFunctions``.

.. NOTE:: The location of your keys (e.g., local or hosted) will have implications on these methods. Read about the differences :ref:`here <eth-account>`.


Looking up transactions
-----------------------

You can look up transactions using the ``web3.eth.get_transaction`` function.

.. code-block:: python

    >>> web3.eth.get_transaction('0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060')
    {
        'blockHash': '0x4e3a3754410177e6937ef1f84bba68ea139e8d1a2258c5f85db9f1cd715a1bdd',
        'blockNumber': 46147,
        'condition': None,
        'creates': None,
        'from': '0xA1E4380A3B1f749673E270229993eE55F35663b4',
        'gas': 21000,
        'gasPrice': None,
        'hash': '0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060',
        'input': '0x',
        'maxFeePerGas': 2000000000,
        'maxPriorityFeePerGas': 1000000000,
        'networkId': None,
        'nonce': 0,
        'publicKey': '0x376fc429acc35e610f75b14bc96242b13623833569a5bb3d72c17be7e51da0bb58e48e2462a59897cead8ab88e78709f9d24fd6ec24d1456f43aae407a8970e4',
        'r': '0x88ff6cf0fefd94db46111149ae4bfc179e9b94721fffd821d38d16464b3f71d0',
        'raw': '0xf86780862d79883d2000825208945df9b87991262f6ba471f09758cde1c0fc1de734827a69801ca088ff6cf0fefd94db46111149ae4bfc179e9b94721fffd821d38d16464b3f71d0a045e0aff800961cfce805daef7016b9b675c137a6a41a548f7b60a3484c06a33a',
        's': '0x45e0aff800961cfce805daef7016b9b675c137a6a41a548f7b60a3484c06a33a',
        'standardV': '0x1',
        'to': '0x5DF9B87991262F6BA471F09758CDE1c0FC1De734',
        'transactionIndex': 0,
        'v': '0x1c',
        'value': 31337,
    }

If no transaction for the given hash can be found, then this function will
instead return ``None``.


Looking up receipts
-------------------

Transaction receipts can be retrieved using the ``web3.eth.get_transaction_receipt`` API.


.. code-block:: python

    >>> web3.eth.get_transaction_receipt('0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060')
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


If the transaction has not yet been mined then this method will raise a ``TransactionNotFound`` error.


Working with Contracts
----------------------


Interacting with existing contracts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In order to use an existing contract, you'll need its deployed address and its ABI.
Both can be found using block explorers, like Etherscan. Once you instantiate a contract
instance, you can read data and execute transactions.

.. code-block:: python

    # Configure w3, e.g., w3 = Web3(...)
    address = '0x1f9840a85d5aF5bf1D1762F925BDADdC4201F988'
    abi = '[{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"address","name":"minter_","type":"address"},...'
    contract_instance = w3.eth.contract(address=address, abi=abi)

    # read state:
    contract_instance.functions.storedValue().call()
    # 42

    # update state:
    tx_hash = contract_instance.functions.updateValue(43).transact()


Deploying new contracts
~~~~~~~~~~~~~~~~~~~~~~~

Given the following solidity source file stored at ``contract.sol``.

.. code-block:: javascript

    contract StoreVar {

        uint8 public _myVar;
        event MyEvent(uint indexed _var);

        function setVar(uint8 _var) public {
            _myVar = _var;
            emit MyEvent(_var);
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
    from eth_tester import PyEVMBackend
    from solcx import compile_source

    def compile_source_file(file_path):
       with open(file_path, 'r') as f:
          source = f.read()

       return compile_source(source)


    def deploy_contract(w3, contract_interface):
        tx_hash = w3.eth.contract(
            abi=contract_interface['abi'],
            bytecode=contract_interface['bin']).constructor().transact()

        address = w3.eth.get_transaction_receipt(tx_hash)['contractAddress']
        return address


    w3 = Web3(EthereumTesterProvider(PyEVMBackend()))

    contract_source_path = 'contract.sol'
    compiled_sol = compile_source_file('contract.sol')

    contract_id, contract_interface = compiled_sol.popitem()

    address = deploy_contract(w3, contract_interface)
    print(f'Deployed {contract_id} to: {address}\n')

    store_var_contract = w3.eth.contract(address=address, abi=contract_interface["abi"])

    gas_estimate = store_var_contract.functions.setVar(255).estimateGas()
    print(f'Gas estimate to transact with setVar: {gas_estimate}')

    if gas_estimate < 100000:
         print("Sending transaction to setVar(255)\n")
         tx_hash = store_var_contract.functions.setVar(255).transact()
         receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
         print("Transaction receipt mined:")
         pprint.pprint(dict(receipt))
         print("\nWas transaction successful?")
         pprint.pprint(receipt["status"])
    else:
         print("Gas cost exceeds 100000")



Output:

.. code-block:: none

    Deployed <stdin>:StoreVar to: 0xF2E246BB76DF876Cef8b38ae84130F4F55De395b

    Gas estimate to transact with setVar: 45535

    Sending transaction to setVar(255)

    Transaction receipt mined:
    {'blockHash': HexBytes('0x837609ad0a404718c131ac5157373662944b778250a507783349d4e78bd8ac84'),
     'blockNumber': 2,
     'contractAddress': None,
     'cumulativeGasUsed': 43488,
     'gasUsed': 43488,
     'logs': [AttributeDict({'type': 'mined', 'logIndex': 0, 'transactionIndex': 0, 'transactionHash': HexBytes('0x50aa3ba0673243f1e60f546a12ab364fc2f6603b1654052ebec2b83d4524c6d0'), 'blockHash': HexBytes('0x837609ad0a404718c131ac5157373662944b778250a507783349d4e78bd8ac84'), 'blockNumber': 2, 'address': '0xF2E246BB76DF876Cef8b38ae84130F4F55De395b', 'data': '0x', 'topics': [HexBytes('0x6c2b4666ba8da5a95717621d879a77de725f3d816709b9cbe9f059b8f875e284'), HexBytes('0x00000000000000000000000000000000000000000000000000000000000000ff')]})],
     'status': 1,
     'transactionHash': HexBytes('0x50aa3ba0673243f1e60f546a12ab364fc2f6603b1654052ebec2b83d4524c6d0'),
     'transactionIndex': 0}

     Was transaction successful?
     1


.. _ethpm_example:

Working with Contracts via ethPM
--------------------------------

`ethPM <http://www.ethpm.com/>`__ packages contain configured contracts ready for use. Web3's ``ethpm`` module (``web3.pm``)
extends Web3's native ``Contract`` module, with a few modifications for how you instantiate ``Contract`` factories and instances.

All you need is the package name, version and ethPM registry address for the package you wish to use.
An ethPM registry is an on-chain datastore for the release data associated with an ethPM package. You can find some sample registries to explore in the `ethPM registry <https://docs.ethpm.com/public-registry-directory>`__. Remember, you should only use packages from registries whose maintainer you trust not to inject malicious code!

In this example we will use the ``ethregistrar@3.0.0`` package sourced from the ``ens.snakecharmers.eth`` registry.

``web3.pm`` uses the ``Package`` class to represent an ethPM package. This object houses all of the contract assets
within a package, and exposes them via an API. So, before we can interact with our package, we need to generate
it as a ``Package`` instance.

.. code-block:: python3

    from web3.auto.infura import w3

    # Note. To use the web3.pm module, you will need to instantiate your w3 instance
    # with a web3 provider connected to the chain on which your registry lives.

    # The ethPM module is still experimental and subject to change,
    # so for now we need to enable it via a temporary flag.
    w3.enable_unstable_package_management_api()

    # Then we need to set the registry address that we want to use.
    # This should be an ENS address, but can also be a checksummed contract address.
    w3.pm.set_registry("ens.snakecharmers.eth")

    # This generates a Package instance of the target ethPM package.
    ens_package = w3.pm.get_package("ethregistrar", "3.0.0")


Now that we have a ``Package`` representation of our target ethPM package, we can generate contract factories
and instances from this ``Package``. However, it's important to note that some packages might be missing
the necessary contract assets needed to generate an instance or a factory. You can use the
`ethPM CLI <https://github.com/ethpm/ethpm-cli>`__ to figure out the available contract types and deployments
within an ethPM package.

.. code-block:: python3

    # To interact with a deployment located in an ethPM package.
    # Note. This will only expose deployments located on the
    # chain of the connected provider (in this example, mainnet)
    mainnet_registrar = ens_package.deployments.get_instance("BaseRegistrarImplementation")

    # Now you can treat mainnet_registrar like any other Web3 Contract instance!
    mainnet_registrar.caller.balanceOf("0x123...")
    > 0

    mainnet_registrar.functions.approve("0x123", 100000).transact()
    > 0x123abc...  # tx_hash

    # To create a contract factory from a contract type located in an ethPM package.
    registrar_factory = ens_package.get_contract_factory("BaseRegistrarImplementation")

    # Now you can treat registrar_factory like any other Web3 Contract factory to deploy new instances!
    # Note. This will deploy new instances to the chain of the connected provider (in this example, mainnet)
    registrar_factory.constructor(...).transact()
    > 0x456def...  # tx_hash

    # To connect your Package to a new chain - simply pass it a new Web3 instance
    # connected to your provider of choice. Now your factories will automatically
    # deploy to this new chain, and the deployments available on a package will
    # be automatically filtered to those located on the new chain.
    from web3.auto.infura.goerli import w3 as goerli_w3
    goerli_registrar = ens_package.update_w3(goerli_w3)


Working with an ERC20 Token Contract
------------------------------------

Most fungible tokens on the Ethereum blockchain conform to the `ERC20`_
standard.  This section of the guide covers interacting with an existing token
contract which conforms to this standard.

.. testsetup::

    from web3 import Web3
    from hexbytes import HexBytes
    w3 = Web3(Web3.EthereumTesterProvider())
    bytecode = '6060604052341561000c57fe5b604051602080610acb833981016040528080519060200190919050505b620f42408114151561003b5760006000fd5b670de0b6b3a76400008102600281905550600254600060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055505b505b610a27806100a46000396000f30060606040523615610097576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806306fdde0314610099578063095ea7b31461013257806318160ddd1461018957806323b872dd146101af578063313ce5671461022557806370a082311461025157806395d89b411461029b578063a9059cbb14610334578063dd62ed3e1461038b575bfe5b34156100a157fe5b6100a96103f4565b60405180806020018281038252838181518152602001915080519060200190808383600083146100f8575b8051825260208311156100f8576020820191506020810190506020830392506100d4565b505050905090810190601f1680156101245780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b341561013a57fe5b61016f600480803573ffffffffffffffffffffffffffffffffffffffff1690602001909190803590602001909190505061042e565b604051808215151515815260200191505060405180910390f35b341561019157fe5b610199610521565b6040518082815260200191505060405180910390f35b34156101b757fe5b61020b600480803573ffffffffffffffffffffffffffffffffffffffff1690602001909190803573ffffffffffffffffffffffffffffffffffffffff16906020019091908035906020019091905050610527565b604051808215151515815260200191505060405180910390f35b341561022d57fe5b610235610791565b604051808260ff1660ff16815260200191505060405180910390f35b341561025957fe5b610285600480803573ffffffffffffffffffffffffffffffffffffffff16906020019091905050610796565b6040518082815260200191505060405180910390f35b34156102a357fe5b6102ab6107e0565b60405180806020018281038252838181518152602001915080519060200190808383600083146102fa575b8051825260208311156102fa576020820191506020810190506020830392506102d6565b505050905090810190601f1680156103265780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b341561033c57fe5b610371600480803573ffffffffffffffffffffffffffffffffffffffff1690602001909190803590602001909190505061081a565b604051808215151515815260200191505060405180910390f35b341561039357fe5b6103de600480803573ffffffffffffffffffffffffffffffffffffffff1690602001909190803573ffffffffffffffffffffffffffffffffffffffff16906020019091905050610973565b6040518082815260200191505060405180910390f35b604060405190810160405280600981526020017f54657374546f6b656e000000000000000000000000000000000000000000000081525081565b600081600160003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020819055508273ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff167f8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925846040518082815260200191505060405180910390a3600190505b92915050565b60025481565b600081600060008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205410806105f1575081600160008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054105b156105fc5760006000fd5b81600060008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000828254019250508190555081600060008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000828254039250508190555081600160008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082825403925050819055508273ffffffffffffffffffffffffffffffffffffffff168473ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef846040518082815260200191505060405180910390a3600190505b9392505050565b601281565b6000600060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205490505b919050565b604060405190810160405280600481526020017f544553540000000000000000000000000000000000000000000000000000000081525081565b600081600060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205410156108695760006000fd5b81600060003373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000828254039250508190555081600060008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600082825401925050819055508273ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff167fddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef846040518082815260200191505060405180910390a3600190505b92915050565b6000600160008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205490505b929150505600a165627a7a723058205071371ee2a4a1be3c96e77d939cdc26161a256fdd638efc08bd33dfc65d3b850029'
    ABI = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function","stateMutability":"view"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function","stateMutability":"nonpayable"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function","stateMutability":"view"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function","stateMutability":"nonpayable"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"type":"function","stateMutability":"view"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function","stateMutability":"view"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function","stateMutability":"view"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function","stateMutability":"nonpayable"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function","stateMutability":"view"},{"inputs":[{"name":"_totalSupply","type":"uint256"}],"payable":false,"type":"constructor","stateMutability":"nonpayable"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"}]'
    factory = w3.eth.contract(abi=ABI, bytecode=bytecode)
    alice, bob = w3.eth.accounts[0], w3.eth.accounts[1]
    assert alice == '0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf', alice
    assert bob == '0x2B5AD5c4795c026514f8317c7a215E218DcCD6cF', bob
    tx_hash = factory.constructor(1000000).transact({'from': alice, 'gas': 899000, 'gasPrice': Web3.toWei(1, 'gwei')})
    assert tx_hash == HexBytes('0x49e3da72a95e4074a9eaea7b438c73ca154627d317e58abeae914e3769a15044'), tx_hash
    txn_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    assert txn_receipt['contractAddress'] == '0xF2E246BB76DF876Cef8b38ae84130F4F55De395b', txn_receipt['contractAddress']
    contract_address = txn_receipt['contractAddress']
    contract = w3.eth.contract(contract_address, abi=ABI)
    total_supply = contract.functions.totalSupply().call()
    decimals = 10 ** 18
    assert total_supply == 1000000 * decimals, total_supply


In this guide we will interact with an existing token contract that we have
already deployed to a local testing chain.  This guide assumes:

1. An existing token contract at a known address.
2. Access to the proper ``ABI`` for the given contract.
3. A ``web3.main.Web3`` instance connected to a provider with an unlocked account which can send transactions.


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
    >>> tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
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
    >>> tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
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
    >>> tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    >>> contract.functions.allowance(alice, bob).call()
    125
    >>> contract.functions.balanceOf(bob).call()
    175


.. _ERC20: https://github.com/ethereum/EIPs/blob/7f4f0377730f5fc266824084188cc17cf246932e/EIPS/eip-20.md


Contract Unit Tests in Python
-----------------------------

Here is an example of how one can use the `pytest`_ framework in python, Web3.py,
eth-tester, and PyEVM to perform unit tests entirely in python without any
additional need for a full featured ethereum node/client. To install needed
dependencies you can use the pinned extra for eth_tester in web3 and pytest:

.. _pytest: https://docs.pytest.org/en/latest/

.. code-block:: bash

    $ pip install web3[tester] pytest

Once you have an environment set up for testing, you can then write your tests
like so:

.. include::  ../tests/core/contracts/test_contract_example.py
    :code: python
    :start-line: 1

Using Infura Rinkeby Node
-------------------------
Import your required libraries

.. code-block:: python

    from web3 import Web3, HTTPProvider

Initialize a web3 instance with an Infura node

.. code-block:: python

    w3 = Web3(Web3.HTTPProvider("https://rinkeby.infura.io/v3/YOUR_INFURA_KEY"))


Inject the middleware into the middleware onion

.. code-block:: python

    from web3.middleware import geth_poa_middleware
    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

Just remember that you have to sign all transactions locally, as infura does not handle any keys from your wallet ( refer to `this`_  )


..  _this: https://web3py.readthedocs.io/en/stable/web3.eth.account.html#local-vs-hosted-nodes

.. code-block:: python

    transaction = contract.functions.function_Name(params).buildTransaction()
    transaction.update({ 'gas' : appropriate_gas_amount })
    transaction.update({ 'nonce' : w3.eth.get_transaction_count('Your_Wallet_Address') })
    signed_tx = w3.eth.account.sign_transaction(transaction, private_key)

P.S : the two updates are done to the transaction dictionary, since a raw transaction might not contain gas & nonce amounts, so you have to add them manually.

And finally, send the transaction

.. code-block:: python

    txn_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)

Tip : afterwards you can use the value stored in ``txn_hash``, in an explorer like `etherscan`_ to view the transaction's details

.. _etherscan: https://rinkeby.etherscan.io


Adjusting log levels
--------------------

Web3.py internally uses `Python logging subsystem <https://docs.python.org/3/library/logging.html>`_.

If you want to run your application logging in debug mode, below is an example of how to make some JSON-RPC traffic quieter.

.. code-block:: python

    import logging
    import coloredlogs

    def setup_logging(log_level=logging.DEBUG):
        """Setup root logger and quiet some levels."""
        logger = logging.getLogger()

        # Set log format to dislay the logger name to hunt down verbose logging modules
        fmt = "%(name)-25s %(levelname)-8s %(message)s"

        # Use colored logging output for console with the coloredlogs package
        # https://pypi.org/project/coloredlogs/
        coloredlogs.install(level=log_level, fmt=fmt, logger=logger)

        # Disable logging of JSON-RPC requests and replies
        logging.getLogger("web3.RequestManager").setLevel(logging.WARNING)
        logging.getLogger("web3.providers.HTTPProvider").setLevel(logging.WARNING)
        # logging.getLogger("web3.RequestManager").propagate = False

        # Disable all internal debug logging of requests and urllib3
        # E.g. HTTP traffic
        logging.getLogger("requests").setLevel(logging.WARNING)
        logging.getLogger("urllib3").setLevel(logging.WARNING)

        return logger


Advanced example: Fetching all token transfer events
----------------------------------------------------

In this example, we show how to fetch all events of a certain event type from the Ethereum blockchain. There are three challenges when working with a large set of events:

* How to incrementally update an existing database of fetched events

* How to deal with interruptions in long running processes

* How to deal with `eth_getLogs` JSON-RPC call query limitations

* How to handle Ethereum minor chain reorganisations in (near) real-time data


eth_getLogs limitations
~~~~~~~~~~~~~~~~~~~~~~~

Ethereum JSON-RPC API servers, like Geth, do not provide easy to paginate over events, only over blocks. There's no request that can find the first block with an event or how many events occur within a range of blocks. The only feedback the JSON-RPC service will give you is whether the `eth_getLogs` call failed.

In this example script, we provide two kinds of heurestics to deal with this issue. The script scans events in a chunk of blocks (start block number - end block number). Then it uses two methods to find how many events there are likely to be in a block window:

* Dynamically set the block range window size, while never exceeding a threshold (e.g., 10,000 blocks).

* In the case `eth_getLogs` JSON-PRC call gives a timeout error, decrease the end block number and try again with a smaller block range window.


Example code
~~~~~~~~~~~~

The following example code is divided into a reusable ``EventScanner`` class and then a demo script that:

* fetches all transfer events for `RCC token <https://etherscan.io/token/0x9b6443b0fb9c241a7fdac375595cea13e6b7807a>`_,

* can incrementally run again to check if there are new events,

* handles interruptions (e.g., CTRL+C abort) gracefully,

* writes all ``Transfer`` events in a single file JSON database, so that other process can consume them,

* uses the `tqdm <https://pypi.org/project/tqdm/>`_ library for progress bar output in a console,

* only supports ``HTTPS`` providers, because JSON-RPC retry logic depends on the implementation details of the underlying protocol,

* disables the standard ``http_retry_request_middleware`` because it does not know how to handle the shrinking block range window for ``eth_getLogs``, and

* consumes around 20k JSON-RPC API calls.

The script can be run with: ``python ./eventscanner.py <your JSON-RPC API URL>``.

.. code-block:: python

    """A stateful event scanner for Ethereum-based blockchains using Web3.py.

    With the stateful mechanism, you can do one batch scan or incremental scans,
    where events are added wherever the scanner left off.
    """

    import datetime
    import time
    import logging
    from abc import ABC, abstractmethod
    from typing import Tuple, Optional, Callable, List, Iterable

    from web3 import Web3
    from web3.contract import Contract
    from web3.datastructures import AttributeDict
    from web3.exceptions import BlockNotFound
    from eth_abi.codec import ABICodec

    # Currently this method is not exposed over official web3 API,
    # but we need it to construct eth_getLogs parameters
    from web3._utils.filters import construct_event_filter_params
    from web3._utils.events import get_event_data


    logger = logging.getLogger(__name__)


    class EventScannerState(ABC):
        """Application state that remembers what blocks we have scanned in the case of crash.
        """

        @abstractmethod
        def get_last_scanned_block(self) -> int:
            """Number of the last block we have scanned on the previous cycle.

            :return: 0 if no blocks scanned yet
            """

        @abstractmethod
        def start_chunk(self, block_number: int):
            """Scanner is about to ask data of multiple blocks over JSON-RPC.

            Start a database session if needed.
            """

        @abstractmethod
        def end_chunk(self, block_number: int):
            """Scanner finished a number of blocks.

            Persistent any data in your state now.
            """

        @abstractmethod
        def process_event(self, block_when: datetime.datetime, event: AttributeDict) -> object:
            """Process incoming events.

            This function takes raw events from Web3, transforms them to your application internal
            format, then saves them in a database or some other state.

            :param block_when: When this block was mined

            :param event: Symbolic dictionary of the event data

            :return: Internal state structure that is the result of event tranformation.
            """

        @abstractmethod
        def delete_data(self, since_block: int) -> int:
            """Delete any data since this block was scanned.

            Purges any potential minor reorg data.
            """


    class EventScanner:
        """Scan blockchain for events and try not to abuse JSON-RPC API too much.

        Can be used for real-time scans, as it detects minor chain reorganisation and rescans.
        Unlike the easy web3.contract.Contract, this scanner can scan events from multiple contracts at once.
        For example, you can get all transfers from all tokens in the same scan.

        You *should* disable the default `http_retry_request_middleware` on your provider for Web3,
        because it cannot correctly throttle and decrease the `eth_getLogs` block number range.
        """

        def __init__(self, w3: Web3, contract: Contract, state: EventScannerState, events: List, filters: {},
                     max_chunk_scan_size: int = 10000, max_request_retries: int = 30, request_retry_seconds: float = 3.0):
            """
            :param contract: Contract
            :param events: List of web3 Event we scan
            :param filters: Filters passed to getLogs
            :param max_chunk_scan_size: JSON-RPC API limit in the number of blocks we query. (Recommendation: 10,000 for mainnet, 500,000 for testnets)
            :param max_request_retries: How many times we try to reattempt a failed JSON-RPC call
            :param request_retry_seconds: Delay between failed requests to let JSON-RPC server to recover
            """

            self.logger = logger
            self.contract = contract
            self.w3 = w3
            self.state = state
            self.events = events
            self.filters = filters

            # Our JSON-RPC throttling parameters
            self.min_scan_chunk_size = 10  # 12 s/block = 120 seconds period
            self.max_scan_chunk_size = max_chunk_scan_size
            self.max_request_retries = max_request_retries
            self.request_retry_seconds = request_retry_seconds

            # Factor how fast we increase the chunk size if results are found
            # # (slow down scan after starting to get hits)
            self.chunk_size_decrease = 0.5

            # Factor how was we increase chunk size if no results found
            self.chunk_size_increase = 2.0

        @property
        def address(self):
            return self.token_address

        def get_block_timestamp(self, block_num) -> datetime.datetime:
            """Get Ethereum block timestamp"""
            try:
                block_info = self.w3.eth.getBlock(block_num)
            except BlockNotFound:
                # Block was not mined yet,
                # minor chain reorganisation?
                return None
            last_time = block_info["timestamp"]
            return datetime.datetime.utcfromtimestamp(last_time)

        def get_suggested_scan_start_block(self):
            """Get where we should start to scan for new token events.

            If there are no prior scans, start from block 1.
            Otherwise, start from the last end block minus ten blocks.
            We rescan the last ten scanned blocks in the case there were forks to avoid
            misaccounting due to minor single block works (happens once in a hour in Ethereum).
            These heurestics could be made more robust, but this is for the sake of simple reference implementation.
            """

            end_block = self.get_last_scanned_block()
            if end_block:
                return max(1, end_block - self.NUM_BLOCKS_RESCAN_FOR_FORKS)
            return 1

        def get_suggested_scan_end_block(self):
            """Get the last mined block on Ethereum chain we are following."""

            # Do not scan all the way to the final block, as this
            # block might not be mined yet
            return self.w3.eth.blockNumber - 1

        def get_last_scanned_block(self) -> int:
            return self.state.get_last_scanned_block()

        def delete_potentially_forked_block_data(self, after_block: int):
            """Purge old data in the case of blockchain reorganisation."""
            self.state.delete_data(after_block)

        def scan_chunk(self, start_block, end_block) -> Tuple[int, datetime.datetime, list]:
            """Read and process events between to block numbers.

            Dynamically decrease the size of the chunk if the case JSON-RPC server pukes out.

            :return: tuple(actual end block number, when this block was mined, processed events)
            """

            block_timestamps = {}
            get_block_timestamp = self.get_block_timestamp

            # Cache block timestamps to reduce some RPC overhead
            # Real solution might include smarter models around block
            def get_block_when(block_num):
                if block_num not in block_timestamps:
                    block_timestamps[block_num] = get_block_timestamp(block_num)
                return block_timestamps[block_num]

            all_processed = []

            for event_type in self.events:

                # Callable that takes care of the underlying web3 call
                def _fetch_events(_start_block, _end_block):
                    return _fetch_events_for_all_contracts(self.w3,
                                                           event_type,
                                                           self.filters,
                                                           from_block=_start_block,
                                                           to_block=_end_block)

                # Do `n` retries on `eth_getLogs`,
                # throttle down block range if needed
                end_block, events = _retry_web3_call(
                    _fetch_events,
                    start_block=start_block,
                    end_block=end_block,
                    retries=self.max_request_retries,
                    delay=self.request_retry_seconds)

                for evt in events:
                    idx = evt["logIndex"]  # Integer of the log index position in the block, null when its pending

                    # We cannot avoid minor chain reorganisations, but
                    # at least we must avoid blocks that are not mined yet
                    assert idx is not None, "Somehow tried to scan a pending block"

                    block_number = evt["blockNumber"]

                    # Get UTC time when this event happened (block mined timestamp)
                    # from our in-memory cache
                    block_when = get_block_when(block_number)

                    logger.debug(f"Processing event {evt["event"]}, block: {evt["blockNumber"]} count: {evt["blockNumber"]}")
                    processed = self.state.process_event(block_when, evt)
                    all_processed.append(processed)

            end_block_timestamp = get_block_when(end_block)
            return end_block, end_block_timestamp, all_processed

        def estimate_next_chunk_size(self, current_chuck_size: int, event_found_count: int):
            """Try to figure out optimal chunk size

            Our scanner might need to scan the whole blockchain for all events

            * We want to minimize API calls over empty blocks

            * We want to make sure that one scan chunk does not try to process too many entries once, as we try to control commit buffer size and potentially asynchronous busy loop

            * Do not overload node serving JSON-RPC API by asking data for too many events at a time

            Currently Ethereum JSON-API does not have an API to tell when a first event occurred in a blockchain
            and our heuristics try to accelerate block fetching (chunk size) until we see the first event.

            These heurestics exponentially increase the scan chunk size depending on if we are seeing events or not.
            When any transfers are encountered, we are back to scanning only a few blocks at a time.
            It does not make sense to do a full chain scan starting from block 1, doing one JSON-RPC call per 20 blocks.
            """

            if event_found_count > 0:
                # When we encounter first events, reset the chunk size window
                current_chuck_size = self.min_scan_chunk_size
            else:
                current_chuck_size *= self.chunk_size_increase

            current_chuck_size = max(self.min_scan_chunk_size, current_chuck_size)
            current_chuck_size = min(self.max_scan_chunk_size, current_chuck_size)
            return int(current_chuck_size)

        def scan(self, start_block, end_block, start_chunk_size=20, progress_callback=Optional[Callable]) -> Tuple[
            list, int]:
            """Perform a token balances scan.

            Assumes all balances in the database are valid before start_block (no forks sneaked in).

            :param start_block: The first block included in the scan

            :param end_block: The last block included in the scan

            :param start_chunk_size: How many blocks we try to fetch over JSON-RPC on the first attempt

            :param progress_callback: If this is an UI application, update the progress of the scan

            :return: [All processed events, number of chunks used]
            """

            assert start_block <= end_block

            current_block = start_block

            # Scan in chunks, commit between
            chunk_size = start_chunk_size
            last_scan_duration = last_logs_found = 0
            total_chunks_scanned = 0

            # All processed entries we got on this scan cycle
            all_processed = []

            while current_block <= end_block:

                self.state.start_chunk(current_block, chunk_size)

                # Print some diagnostics to logs to try to fiddle with real world JSON-RPC API performance
                estimated_end_block = current_block + chunk_size
                logger.debug(
                    f"Scanning token transfers for blocks: {current_block} - {estimated_end_block}, chunk size {chunk_size}, last chunk scan took {last_scan_duration}, last logs found {last_logs_found}"
                )

                start = time.time()
                actual_end_block, end_block_timestamp, new_entries = self.scan_chunk(current_block, estimated_end_block)

                # Where does our current chunk scan ends - are we out of chain yet?
                current_end = actual_end_block

                last_scan_duration = time.time() - start
                all_processed += new_entries

                # Print progress bar
                if progress_callback:
                    progress_callback(start_block, end_block, current_block, end_block_timestamp, chunk_size, len(new_entries))

                # Try to guess how many blocks to fetch over `eth_getLogs` API next time
                chunk_size = self.estimate_next_chunk_size(chunk_size, len(new_entries))

                # Set where the next chunk starts
                current_block = current_end + 1
                total_chunks_scanned += 1
                self.state.end_chunk(current_end)

            return all_processed, total_chunks_scanned


    def _retry_web3_call(func, start_block, end_block, retries, delay) -> Tuple[int, list]:
        """A custom retry loop to throttle down block range.

        If our JSON-RPC server cannot serve all incoming `eth_getLogs` in a single request,
        we retry and throttle down block range for every retry.

        For example, Go Ethereum does not indicate what is an acceptable response size.
        It just fails on the server-side with a "context was cancelled" warning.

        :param func: A callable that triggers Ethereum JSON-RPC, as func(start_block, end_block)
        :param start_block: The initial start block of the block range
        :param end_block: The initial start block of the block range
        :param retries: How many times we retry
        :param delay: Time to sleep between retries
        """
        for i in range(retries):
            try:
                return end_block, func(start_block, end_block)
            except Exception as e:
                # Assume this is HTTPConnectionPool(host='localhost', port=8545): Read timed out. (read timeout=10)
                # from Go Ethereum. This translates to the error "context was cancelled" on the server side:
                # https://github.com/ethereum/go-ethereum/issues/20426
                if i < retries - 1:
                    # Give some more verbose info than the default middleware
                    logger.warning(
                        f"Retrying events for block range {start_block} - {end_block} ({end_block-start_block}) failed with {e} , retrying in {delay} seconds")
                    # Decrease the `eth_getBlocks` range
                    end_block = start_block + ((end_block - start_block) // 2)
                    # Let the JSON-RPC to recover e.g. from restart
                    time.sleep(delay)
                    continue
                else:
                    logger.warning("Out of retries")
                    raise


    def _fetch_events_for_all_contracts(
            w3,
            event,
            argument_filters: dict,
            from_block: int,
            to_block: int) -> Iterable:
        """Get events using eth_getLogs API.

        This method is detached from any contract instance.

        This is a stateless method, as opposed to createFilter.
        It can be safely called against nodes which do not provide `eth_newFilter` API, like Infura.
        """

        if from_block is None:
            raise TypeError("Missing mandatory keyword argument to getLogs: fromBlock")

        # Currently no way to poke this using a public Web3.py API.
        # This will return raw underlying ABI JSON object for the event
        abi = event._get_event_abi()

        # Depending on the Solidity version used to compile
        # the contract that uses the ABI,
        # it might have Solidity ABI encoding v1 or v2.
        # We just assume the default that you set on Web3 object here.
        # More information here https://eth-abi.readthedocs.io/en/latest/index.html
        codec: ABICodec = w3.codec

        # Here we need to poke a bit into Web3 internals, as this
        # functionality is not exposed by default.
        # Construct JSON-RPC raw filter presentation based on human readable Python descriptions
        # Namely, convert event names to their keccak signatures
        # More information here:
        # https://github.com/ethereum/web3.py/blob/e176ce0793dafdd0573acc8d4b76425b6eb604ca/web3/_utils/filters.py#L71
        data_filter_set, event_filter_params = construct_event_filter_params(
            abi,
            codec,
            address=argument_filters.get("address"),
            argument_filters=argument_filters,
            fromBlock=from_block,
            toBlock=to_block
        )

        logger.debug(f"Querying eth_getLogs with the following parameters: {event_filter_params}")

        # Call JSON-RPC API on your Ethereum node.
        # get_logs() returns raw AttributedDict entries
        logs = w3.eth.get_logs(event_filter_params)

        # Convert raw binary data to Python proxy objects as described by ABI
        all_events = []
        for log in logs:
            # Convert raw JSON-RPC log result to human readable event by using ABI data
            # More information how processLog works here
            # https://github.com/ethereum/web3.py/blob/fbaf1ad11b0c7fac09ba34baff2c256cffe0a148/web3/_utils/events.py#L200
            evt = get_event_data(codec, abi, log)
            # Note: This was originally yield,
            # but deferring the timeout exception caused the throttle logic not to work
            all_events.append(evt)
        return all_events


    if __name__ == "__main__":
        # Simple demo that scans all the token transfers of RCC token (11k).
        # The demo supports persistant state by using a JSON file.
        # You will need an Ethereum node for this.
        # Running this script will consume around 20k JSON-RPC calls.
        # With locally running Geth, the script takes 10 minutes.
        # The resulting JSON state file is 2.9 MB.
        import sys
        import json
        from web3.providers.rpc import HTTPProvider

        # We use tqdm library to render a nice progress bar in the console
        # https://pypi.org/project/tqdm/
        from tqdm import tqdm

        # RCC has around 11k Transfer events
        # https://etherscan.io/token/0x9b6443b0fb9c241a7fdac375595cea13e6b7807a
        RCC_ADDRESS = "0x9b6443b0fB9C241A7fdAC375595cEa13e6B7807A"

        # Reduced ERC-20 ABI, only Transfer event
        ABI = """[
            {
                "anonymous": false,
                "inputs": [
                    {
                        "indexed": true,
                        "name": "from",
                        "type": "address"
                    },
                    {
                        "indexed": true,
                        "name": "to",
                        "type": "address"
                    },
                    {
                        "indexed": false,
                        "name": "value",
                        "type": "uint256"
                    }
                ],
                "name": "Transfer",
                "type": "event"
            }
        ]
        """

        class JSONifiedState(EventScannerState):
            """Store the state of scanned blocks and all events.

            All state is an in-memory dict.
            Simple load/store massive JSON on start up.
            """

            def __init__(self):
                self.state = None
                self.fname = "test-state.json"
                # How many second ago we saved the JSON file
                self.last_save = 0

            def reset(self):
                """Create initial state of nothing scanned."""
                self.state = {
                    "last_scanned_block": 0,
                    "blocks": {},
                }

            def restore(self):
                """Restore the last scan state from a file."""
                try:
                    self.state = json.load(open(self.fname, "rt"))
                    print(f"Restored the state, previously {self.state['last_scanned_block']} blocks have been scanned")
                except (IOError, json.decoder.JSONDecodeError):
                    print("State starting from scratch")
                    self.reset()

            def save(self):
                """Save everything we have scanned so far in a file."""
                with open(self.fname, "wt") as f:
                    json.dump(self.state, f)
                self.last_save = time.time()

            #
            # EventScannerState methods implemented below
            #

            def get_last_scanned_block(self):
                """The number of the last block we have stored."""
                return self.state["last_scanned_block"]

            def delete_data(self, since_block):
                """Remove potentially reorganised blocks from the scan data."""
                for block_num in range(since_block, self.get_last_scanned_block()):
                    if block_num in self.state["blocks"]:
                        del self.state["blocks"][block_num]

            def start_chunk(self, block_number, chunk_size):
                pass

            def end_chunk(self, block_number):
                """Save at the end of each block, so we can resume in the case of a crash or CTRL+C"""
                # Next time the scanner is started we will resume from this block
                self.state["last_scanned_block"] = block_number

                # Save the database file for every minute
                if time.time() - self.last_save > 60:
                    self.save()

            def process_event(self, block_when: datetime.datetime, event: AttributeDict) -> str:
                """Record a ERC-20 transfer in our database."""
                # Events are keyed by their transaction hash and log index
                # One transaction may contain multiple events
                # and each one of those gets their own log index

                # event_name = event.event # "Transfer"
                log_index = event.logIndex  # Log index within the block
                # transaction_index = event.transactionIndex  # Transaction index within the block
                txhash = event.transactionHash.hex()  # Transaction hash
                block_number = event.blockNumber

                # Convert ERC-20 Transfer event to our internal format
                args = event["args"]
                transfer = {
                    "from": args["from"],
                    "to": args.to,
                    "value": args.value,
                    "timestamp": block_when.isoformat(),
                }

                # Create empty dict as the block that contains all transactions by txhash
                if block_number not in self.state["blocks"]:
                    self.state["blocks"][block_number] = {}

                block = self.state["blocks"][block_number]
                if txhash not in block:
                    # We have not yet recorded any transfers in this transaction
                    # (One transaction may contain multiple events if executed by a smart contract).
                    # Create a tx entry that contains all events by a log index
                    self.state["blocks"][block_number][txhash] = {}

                # Record ERC-20 transfer in our database
                self.state["blocks"][block_number][txhash][log_index] = transfer

                # Return a pointer that allows us to look up this event later if needed
                return f"{block_number}-{txhash}-{log_index}"

        def run():

            if len(sys.argv) < 2:
                print("Usage: eventscanner.py http://your-node-url")
                sys.exit(1)

            api_url = sys.argv[1]

            # Enable logs to the stdout.
            # DEBUG is very verbose level
            logging.basicConfig(level=logging.INFO)

            provider = HTTPProvider(api_url)

            # Remove the default JSON-RPC retry middleware
            # as it correctly cannot handle eth_getLogs block range
            # throttle down.
            provider.middlewares.clear()

            w3 = Web3(provider)

            # Prepare stub ERC-20 contract object
            abi = json.loads(ABI)
            ERC20 = w3.eth.contract(abi=abi)

            # Restore/create our persistent state
            state = JSONifiedState()
            state.restore()

            # chain_id: int, w3: Web3, abi: dict, state: EventScannerState, events: List, filters: {}, max_chunk_scan_size: int=10000
            scanner = EventScanner(
                w3=w3,
                contract=ERC20,
                state=state,
                events=[ERC20.events.Transfer],
                filters={"address": RCC_ADDRESS},
                # How many maximum blocks at the time we request from JSON-RPC
                # and we are unlikely to exceed the response size limit of the JSON-RPC server
                max_chunk_scan_size=10000
            )

            # Assume we might have scanned the blocks all the way to the last Ethereum block
            # that mined a few seconds before the previous scan run ended.
            # Because there might have been a minor Etherueum chain reorganisations
            # since the last scan ended, we need to discard
            # the last few blocks from the previous scan results.
            chain_reorg_safety_blocks = 10
            scanner.delete_potentially_forked_block_data(state.get_last_scanned_block() - chain_reorg_safety_blocks)

            # Scan from [last block scanned] - [latest ethereum block]
            # Note that our chain reorg safety blocks cannot go negative
            start_block = max(state.get_last_scanned_block() - chain_reorg_safety_blocks, 0)
            end_block = scanner.get_suggested_scan_end_block()
            blocks_to_scan = end_block - start_block

            print(f"Scanning events from blocks {start_block} - {end_block}")

            # Render a progress bar in the console
            start = time.time()
            with tqdm(total=blocks_to_scan) as progress_bar:
                def _update_progress(start, end, current, current_block_timestamp, chunk_size, events_count):
                    if current_block_timestamp:
                        formatted_time = current_block_timestamp.strftime("%d-%m-%Y")
                    else:
                        formatted_time = "no block time available"
                    progress_bar.set_description(f"Current block: {current} ({formatted_time}), blocks in a scan batch: {chunk_size}, events processed in a batch {events_count}")
                    progress_bar.update(chunk_size)

                # Run the scan
                result, total_chunks_scanned = scanner.scan(start_block, end_block, progress_callback=_update_progress)

            state.save()
            duration = time.time() - start
            print(f"Scanned total {len(result)} Transfer events, in {duration} seconds, total {total_chunks_scanned} chunk scans performed")

        run()


