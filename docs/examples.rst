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
``web3.eth.blockNumber`` property.

.. code-block:: python

    >>> web3.eth.blockNumber
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

- :meth:`~web3.eth.Eth.sendTransaction`

  Use this method if:
    - you want to send ether from one account to another.

- :meth:`~web3.eth.Eth.sendRawTransaction`

  Use this method if:
    - you want to sign the transaction elsewhere, e.g., a hardware wallet.
    - you want to broadcast a transaction through another provider, e.g., Infura.
    - you have some other advanced use case that requires more flexibility.

- :ref:`contract-functions`

  Use these methods if:
    - you want to interact with a contract. Web3.py parses the contract ABI and makes those functions available via the ``functions`` property.

- :meth:`~web3.middleware.construct_sign_and_send_raw_middleware`

  Use this middleware if:
    - you want to automate signing when using ``w3.eth.sendTransaction`` or ``ContractFunctions``.

.. NOTE:: The location of your keys (e.g., local or hosted) will have implications on these methods. Read about the differences :ref:`here <eth-account>`.


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
        'from': '0xA1E4380A3B1f749673E270229993eE55F35663b4',
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
        'to': '0x5DF9B87991262F6BA471F09758CDE1c0FC1De734',
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

        address = w3.eth.getTransactionReceipt(tx_hash)['contractAddress']
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
         receipt = w3.eth.waitForTransactionReceipt(tx_hash)
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
    tx_hash = factory.constructor(1000000).transact({'from': alice, 'gas': 899000, 'gasPrice': 320000})
    assert tx_hash == HexBytes('0x611aa2d5c3e51f08d0665c4529c5520ed32520d8a48ba2cf2aff3f2fce3f26e4'), tx_hash
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
    transaction.update({ 'nonce' : w3.eth.getTransactionCount('Your_Wallet_Address') })
    signed_tx = w3.eth.account.signTransaction(transaction, private_key)

P.S : the two updates are done to the transaction dictionary, since a raw transaction might not contain gas & nonce amounts, so you have to add them manually.

And finally, send the transaction

.. code-block:: python

    txn_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    txn_receipt = w3.eth.waitForTransactionReceipt(txn_hash)

Tip : afterwards you can use the value stored in ``txn_hash``, in an explorer like `etherscan`_ to view the transaction's details

.. _etherscan: https://rinkeby.etherscan.io
