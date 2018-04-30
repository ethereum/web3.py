Quickstart
==========

.. contents:: :local:

.. NOTE:: All code starting with a ``$`` is meant to run on your terminal.
    All code starting with a ``>>>`` is meant to run in a python interpreter,
    like `ipython <https://pypi.org/project/ipython/>`_.

Installation
------------

Web3.py can be installed (preferably in a :ref:`virtualenv <setup_environment>`)
using ``pip`` as follows:

.. code-block:: shell

   $ pip install web3


.. NOTE:: If you run into problems during installation, you might have a
    broken environment. See the troubleshooting guide to :ref:`setup_environment`.


Installation from source can be done from the root of the project with the
following command.

.. code-block:: shell

   $ pip install .


Using Web3
----------

To use the web3 library you will need to initialize the
:class:`~web3.Web3` class.

Use the ``auto`` module to :ref:`guess at common node connection options
<automatic_provider_detection>`.

.. code-block:: python

    >>> from web3.auto import w3
    >>> w3.eth.blockNumber
    4000000

This ``w3`` instance will now allow you to interact with the Ethereum
blockchain.

.. NOTE:: If you get the result ``UnhandledRequest: No providers responded to the RPC request``
    then you are not connected to a node. See :ref:`why_need_connection` and
    :ref:`choosing_provider`

.. _first_w3_use:

Getting Blockchain Info
----------------------------------------

It's time to start using Web3.py! Try getting all the information about the latest block.

.. code-block:: python

    >>> w3.eth.getBlock('latest')
    {'difficulty': 1,
     'gasLimit': 6283185,
     'gasUsed': 0,
     'hash': HexBytes('0x53b983fe73e16f6ed8178f6c0e0b91f23dc9dad4cb30d0831f178291ffeb8750'),
     'logsBloom': HexBytes('0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'),
     'miner': '0x0000000000000000000000000000000000000000',
     'mixHash': HexBytes('0x0000000000000000000000000000000000000000000000000000000000000000'),
     'nonce': HexBytes('0x0000000000000000'),
     'number': 0,
     'parentHash': HexBytes('0x0000000000000000000000000000000000000000000000000000000000000000'),
     'proofOfAuthorityData': HexBytes('0x0000000000000000000000000000000000000000000000000000000000000000dddc391ab2bf6701c74d0c8698c2e13355b2e4150000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'),
     'receiptsRoot': HexBytes('0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421'),
     'sha3Uncles': HexBytes('0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347'),
     'size': 622,
     'stateRoot': HexBytes('0x1f5e460eb84dc0606ab74189dbcfe617300549f8f4778c3c9081c119b5b5d1c1'),
     'timestamp': 0,
     'totalDifficulty': 1,
     'transactions': [],
     'transactionsRoot': HexBytes('0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421'),
     'uncles': []}

Many of the typical things you'll want to do will be in the :class:`w3.eth <web3.eth.Eth>` API,
so that is a good place to start.

If you want to dive straight into contracts, check out the section on :ref:`contracts`,
including a :ref:`contract_example`, and how to create a contract instance using
:meth:`w3.eth.contract() <web3.eth.Eth.contract>`.
