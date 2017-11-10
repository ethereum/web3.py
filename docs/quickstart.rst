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
