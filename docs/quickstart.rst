Quickstart
==========

.. contents:: :local:


Environment
------------

Web3.py prefers Python 3, and will soon require it. Often, the
best way to guarantee a clean Python 3 environment is with ``virtualenv``, like:

.. code-block:: shell

    # once:
    $ virtualenv -p python3 ~/.venv-py3

    # each session:
    $ source ~/.venv-py3/bin/activate

    # with virtualenv active, install...

Installation
------------

Web3.py can be installed using ``pip`` as follows.

.. code-block:: shell

   $ pip install web3

Or to install with support for the ``TestRPCProvider`` and
``EthereumTesterProvider`` you can use this install command.

.. code-block:: shell

   $ pip install web3[tester]


Installation from source can be done from the root of the project with the
following command.

.. code-block:: shell

   $ python setup.py install


Using Web3
----------

To use the web3 library you will need to instantiate an instance of the
``Web3`` object.

.. code-block:: python

    >>> from web3 import Web3, HTTPProvider, IPCProvider

    # Note that you should create only one RPCProvider per
    # process, as it recycles underlying TCP/IP network connections between
    # your process and Ethereum node
    >>> web3 = Web3(HTTPProvider('http://localhost:8545'))

    # or for an IPC based connection
    >>> web3 = Web3(IPCProvider())
    >>> web3.eth.blockNumber
    4000000


This ``web3`` instance will now allow you to interact with the Ethereum
blockchain.

Simple Example
--------------

.. code-block:: python

    import json
    import web3

    from web3 import Web3, HTTPProvider, TestRPCProvider
    from solc import compile_source
    from web3.contract import ConciseContract

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

    compiled_sol = compile_source(contract_source_code) # Compiled source code
    contract_interface = compiled_sol['<stdin>:Greeter']

    # web3.py instance
    w3 = Web3(TestRPCProvider())

    # Instantiate and deploy contract
    contract = w3.eth.contract(contract_interface['abi'], bytecode=contract_interface['bin'])

    # Get transaction hash from deployed contract
    tx_hash = contract.deploy(transaction={'from': w3.eth.accounts[0], 'gas': 410000})

    # Get tx receipt to get contract address
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    contract_address = tx_receipt['contractAddress']

    # Contract instance in concise mode
    contract_instance = w3.eth.contract(contract_interface['abi'], contract_address, ContractFactoryClass=ConciseContract)

    # Getters + Setters for web3.eth.contract object
    print('Contract value: {}'.format(contract_instance.greet()))
    contract_instance.setGreeting('Nihao', transact={'from': w3.eth.accounts[0]})
    print('Setting value to: Nihao')
    print('Contract value: {}'.format(contract_instance.greet()))
