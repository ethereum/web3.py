Quickstart
==========

.. contents:: :local:

.. NOTE:: All code starting with a ``$`` is meant to run on your terminal.
    All code starting with a ``>>>`` is meant to run in a python interpreter,
    like `ipython <https://pypi.org/project/ipython/>`_.

Installation
------------

Web3.py can be installed (preferably in a virtualenv) using ``pip`` as follows:

.. code-block:: shell

   $ pip install web3


.. NOTE:: If you run into problems during installation, you might have a
    broken environment. See the troubleshooting guide to :ref:`setup-environment`.


Installation from source can be done from the root of the project with the
following command.

.. code-block:: shell

   $ pip install .


Using Web3
----------

To use the web3 library you will need to initialize the
:class:`~web3.Web3` class.

Use the ``auto`` module to guess at common node connection options.

.. code-block:: python

    >>> from web3.auto import w3
    >>> w3.eth.blockNumber
    4000000

.. NOTE:: If you get the result ``UnhandledRequest: No providers responded to the RPC request``
    then you are not connected to a node. See :ref:`why_need_connection` and
    :ref:`choosing_node`, and :ref:`choosing_provider`.

To peek under the hood, see: :ref:`automatic_provider_detection`

This ``w3`` instance will now allow you to interact with the Ethereum
blockchain.


Connecting to your Node
-----------------------

Sometimes, web3 cannot automatically detect where your node is.

You can connect to your Ethereum node (for example: geth or parity) using one of
the available :ref:`providers`, typically IPC or HTTP.

If your node is running locally, IPC will be faster and safer to expose.
If sharing the node across machines on a network, use HTTP instead.

IPC Provider
~~~~~~~~~~~~

.. code-block:: python

    >>> from web3 import Web3, IPCProvider

    # for an IPC based connection
    >>> w3 = Web3(IPCProvider('/path/to/node/rpc-json/file.ipc'))

    >>> w3.eth.blockNumber
    4000000


HTTP Provider
~~~~~~~~~~~~~

.. code-block:: python

    >>> from web3 import Web3, HTTPProvider

    # Note that you should create only one HTTPProvider per
    # process, as it recycles underlying TCP/IP network connections between
    # your process and Ethereum node
    >>> w3 = Web3(HTTPProvider('http://192.168.1.2:8545'))

    >>> w3.eth.blockNumber
    4000000

.. _provider_uri:

Provider via Environment Variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Alternatively, you can set the environment variable ``WEB3_PROVIDER_URI``
before starting your script, and web3 will look for that provider first.

Valid formats for the this environment variable are:

- ``file:///path/to/node/rpc-json/file.ipc``
- ``http://192.168.1.2:8545``

Simple Contract Example
-----------------------

.. code-block:: python

    import json
    import web3

    from web3 import Web3, TestRPCProvider
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
    contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

    # Get transaction hash from deployed contract
    tx_hash = contract.deploy(transaction={'from': w3.eth.accounts[0], 'gas': 410000})

    # Get tx receipt to get contract address
    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
    contract_address = tx_receipt['contractAddress']

    # Contract instance in concise mode
    contract_instance = w3.eth.contract(abi=contract_interface['abi'], address=contract_address, ContractFactoryClass=ConciseContract)

    # Getters + Setters for web3.eth.contract object
    print('Contract value: {}'.format(contract_instance.greet()))
    contract_instance.setGreeting('Nihao', transact={'from': w3.eth.accounts[0]})
    print('Setting value to: Nihao')
    print('Contract value: {}'.format(contract_instance.greet()))
