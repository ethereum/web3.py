Quickstart
==========

.. contents:: :local:


Installation
------------

Web3.py can be installed using ``pip`` as follows.

.. code-block:: shell

   $ pip install web3

Installation from source can be done from the root of the project with the
following command.

.. code-block:: shell

   $ python setup.py install


The ``Web3`` object
-------------------

The common entrypoint for interacting with the Web3 library is the ``Web3``
class.  You will need to instantiate a web3 instance.

.. code-block:: python

    >>> from web3 import Web, RPCProvider, IPCProvider
    >>> web3 = Web3(RPCProvider(host='localhost', port='8545'))
    # or for an IPC based connection
    >>> web3 = Web3(IPCProvider())

This ``web3`` instance will now allow you to interact with the Ethereum
blockchain.
