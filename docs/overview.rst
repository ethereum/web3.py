.. _overview:

Overview
========

The purpose of this page is to give you a sense of everything Web3.py can do
and to serve as a quick reference guide. You'll find a summary of each feature
with links to learn more. You may also be interested in the
:ref:`Examples <examples>` page, which demonstrates some of these features in
greater detail.


Configuration
~~~~~~~~~~~~~

After installing Web3.py (via ``pip install web3``), you'll need to specify the
provider and any middleware you want to use beyond the defaults.


Providers
---------

Providers are how Web3.py connects to the blockchain. The library comes with the
following built-in providers:

- ``Web3.IPCProvider`` for connecting to ipc socket based JSON-RPC servers.
- ``Web3.HTTPProvider`` for connecting to http and https based JSON-RPC servers.
- ``Web3.WebsocketProvider`` for connecting to ws and wss websocket based JSON-RPC servers.

.. code-block:: python

   >>> from web3 import Web3

   # IPCProvider:
   >>> w3 = Web3(Web3.IPCProvider('./path/to/geth.ipc'))

   # HTTPProvider:
   >>> w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

   # WebsocketProvider:
   >>> w3 = Web3(Web3.WebsocketProvider('ws://127.0.0.1:8546'))

   >>> w3.isConnected()
   True

For more information, (e.g., connecting to remote nodes, provider auto-detection,
using a test provider) see the :ref:`Providers <providers>` documentation.


Middleware
----------

Your Web3.py instance may be further configured via middleware.

Web3.py middleware is described using an onion metaphor, where each layer of
middleware may affect both the incoming request and outgoing response from your
provider. The documentation includes a :ref:`visualization <Modifying_Middleware>`
of this idea.

Several middleware are :ref:`included by default <default_middleware>`. You may add to
(:meth:`add <Web3.middleware_onion.add>`, :meth:`inject <Web3.middleware_onion.inject>`,
:meth:`replace <Web3.middleware_onion.replace>`) or disable
(:meth:`remove <Web3.middleware_onion.remove>`,
:meth:`clear <Web3.middleware_onion.clear>`) any of these middleware.


Your Keys
~~~~~~~~~

Private keys are required to approve any transaction made on your behalf. The manner in
which your key is secured will determine how you create and send transactions in Web3.py.

A local node, like `Geth <https://geth.ethereum.org/>`_, may manage your keys for you.
You can reference those keys using the :attr:`web3.eth.accounts <web3.eth.Eth.accounts>`
property.

A hosted node, like `Infura <https://infura.io/>`_, will have no knowledge of your keys.
In this case, you'll need to have your private key available locally for signing
transactions.

Full documentation on the distinction between keys can be found :ref:`here <eth-account>`.


Base API
~~~~~~~~

The :ref:`Web3 <web3_base>` class includes a number of convenient utility functions:


Encoding and Decoding Helpers
-----------------------------

- :meth:`Web3.is_encodable() <web3.w3.is_encodable>`
- :meth:`Web3.toBytes() <web3.Web3.toBytes>`
- :meth:`Web3.toHex() <web3.Web3.toHex>`
- :meth:`Web3.toInt() <web3.Web3.toInt>`
- :meth:`Web3.toJSON() <web3.Web3.toJSON>`
- :meth:`Web3.toText() <web3.Web3.toText>`


Address Helpers
---------------

- :meth:`Web3.isAddress() <web3.Web3.isAddress>`
- :meth:`Web3.isChecksumAddress() <web3.Web3.isChecksumAddress>`
- :meth:`Web3.toChecksumAddress() <web3.Web3.toChecksumAddress>`


Currency Conversions
--------------------

- :meth:`Web3.fromWei() <web3.Web3.fromWei>`
- :meth:`Web3.toWei() <web3.Web3.toWei>`


Cryptographic Hashing
---------------------

- :meth:`Web3.keccak() <web3.Web3.keccak>`
- :meth:`Web3.solidityKeccak() <web3.Web3.solidityKeccak>`


web3.eth API
~~~~~~~~~~~~

The most commonly used APIs for interacting with Ethereum can be found under the
``web3.eth`` namespace.  As a reminder, the :ref:`Examples <examples>` page will
demonstrate how to use several of these methods.


Fetching Data
-------------

Viewing account balances (:meth:`get_balance <web3.eth.Eth.get_balance>`), transactions
(:meth:`getTransaction <web3.eth.Eth.getTransaction>`), and block data
(:meth:`get_block <web3.eth.Eth.get_block>`) are some of the most common starting
points in Web3.py.


API
^^^

- :meth:`web3.eth.get_balance() <web3.eth.Eth.get_balance>`
- :meth:`web3.eth.get_block() <web3.eth.Eth.get_block>`
- :meth:`web3.eth.get_block_transaction_count() <web3.eth.Eth.get_block_transaction_count>`
- :meth:`web3.eth.getCode() <web3.eth.Eth.getCode>`
- :meth:`web3.eth.getProof() <web3.eth.Eth.getProof>`
- :meth:`web3.eth.get_storage_at() <web3.eth.Eth.get_storage_at>`
- :meth:`web3.eth.getTransaction() <web3.eth.Eth.getTransaction>`
- :meth:`web3.eth.getTransactionByBlock() <web3.eth.Eth.getTransactionByBlock>`
- :meth:`web3.eth.getTransactionCount() <web3.eth.Eth.getTransactionCount>`
- :meth:`web3.eth.getUncleByBlock() <web3.eth.Eth.getUncleByBlock>`
- :meth:`web3.eth.getUncleCount() <web3.eth.Eth.getUncleCount>`


Making Transactions
-------------------

The most common use cases will be satisfied with
:meth:`sendTransaction <web3.eth.Eth.sendTransaction>` or the combination of
:meth:`signTransaction <web3.eth.Eth.signTransaction>` and
:meth:`sendRawTransaction <web3.eth.Eth.sendRawTransaction>`.

.. note::

   If interacting with a smart contract, a dedicated API exists. See the next
   section, :ref:`Contracts <overview_contracts>`.


API
^^^

- :meth:`web3.eth.sendTransaction() <web3.eth.Eth.sendTransaction>`
- :meth:`web3.eth.signTransaction() <web3.eth.Eth.signTransaction>`
- :meth:`web3.eth.sendRawTransaction() <web3.eth.Eth.sendRawTransaction>`
- :meth:`web3.eth.replaceTransaction() <web3.eth.Eth.replaceTransaction>`
- :meth:`web3.eth.modifyTransaction() <web3.eth.Eth.modifyTransaction>`
- :meth:`web3.eth.waitForTransactionReceipt() <web3.eth.Eth.waitForTransactionReceipt>`
- :meth:`web3.eth.getTransactionReceipt() <web3.eth.Eth.getTransactionReceipt>`
- :meth:`web3.eth.sign() <web3.eth.Eth.sign>`
- :meth:`web3.eth.signTypedData() <web3.eth.Eth.signTypedData>`
- :meth:`web3.eth.estimateGas() <web3.eth.Eth.estimateGas>`
- :meth:`web3.eth.generateGasPrice() <web3.eth.Eth.generateGasPrice>`
- :meth:`web3.eth.setGasPriceStrategy() <web3.eth.Eth.setGasPriceStrategy>`


.. _overview_contracts:

Contracts
---------

The two most common use cases involving smart contracts are deploying and executing
functions on a deployed contract.

Deployment requires that the contract already be compiled, with its bytecode and ABI
available. This compilation step can done within
`Remix <http://remix.ethereum.org/>`_ or one of the many contract development
frameworks, such as `Brownie <https://eth-brownie.readthedocs.io/>`_.

Once the contract object is instantiated, calling ``transact`` on the
:meth:`constructor <web3.contract.Contract.constructor>` method will deploy an
instance of the contract:

.. code-block:: python

   >>> ExampleContract = w3.eth.contract(abi=abi, bytecode=bytecode)
   >>> tx_hash = ExampleContract.constructor().transact()
   >>> tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
   >>> tx_receipt.contractAddress
   '0x8a22225eD7eD460D7ee3842bce2402B9deaD23D3'

Once loaded into a Contract object, the functions of a deployed contract are available
on the ``functions`` namespace:

.. code-block:: python

   >>> deployed_contract = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)
   >>> deployed_contract.functions.myFunction(42).transact()

If you want to read data from a contract (or see the result of transaction locally,
without executing it on the network), you can use the
:meth:`ContractFunction.call <web3.contract.ContractFunction.call>` method, or the
more concise :attr:`ContractCaller <web3.contract.ContractCaller>` syntax:

.. code-block:: python

   # Using ContractFunction.call
   >>> deployed_contract.functions.getMyValue().call()
   42

   # Using ContractCaller
   >>> deployed_contract.caller().getMyValue()
   42

For more, see the full :ref:`Contracts` documentation.


API
^^^

- :meth:`web3.eth.contract() <web3.eth.Eth.contract>`
- :attr:`Contract.address <web3.contract.Contract.address>`
- :attr:`Contract.abi <web3.contract.Contract.abi>`
- :attr:`Contract.bytecode <web3.contract.Contract.bytecode>`
- :attr:`Contract.bytecode_runtime <web3.contract.Contract.bytecode_runtime>`
- :attr:`Contract.functions <web3.contract.Contract.functions>`
- :attr:`Contract.events <web3.contract.Contract.events>`
- :attr:`Contract.fallback <web3.contract.Contract.fallback.call>`
- :meth:`Contract.constructor() <web3.contract.Contract.constructor>`
- :meth:`Contract.encodeABI() <web3.contract.Contract.encodeABI>`
- :attr:`web3.contract.ContractFunction <web3.contract.ContractFunction>`
- :attr:`web3.contract.ContractEvents <web3.contract.ContractEvents>`


Logs and Filters
----------------

If you want to react to new blocks being mined or specific events being emitted by
a contract, you can leverage Web3.py filters.

.. code-block:: python

   # Use case: filter for new blocks
   >>> new_filter = web3.eth.filter('latest')

   # Use case: filter for contract event "MyEvent"
   >>> new_filter = deployed_contract.events.MyEvent.createFilter(fromBlock='latest')

   # retrieve filter results:
   >>> new_filter.get_all_entries()
   >>> new_filter.get_new_entries()

More complex patterns for creating filters and polling for logs can be found in the
:ref:`Filtering <filtering>` documentation.


API
^^^

- :meth:`web3.eth.filter() <web3.eth.Eth.filter>`
- :meth:`web3.eth.getFilterChanges() <web3.eth.Eth.getFilterChanges>`
- :meth:`web3.eth.getFilterLogs() <web3.eth.Eth.getFilterLogs>`
- :meth:`web3.eth.uninstallFilter() <web3.eth.Eth.uninstallFilter>`
- :meth:`web3.eth.getLogs() <web3.eth.Eth.getLogs>`
- :meth:`Contract.events.your_event_name.createFilter() <web3.contract.Contract.events.your_event_name.createFilter>`
- :meth:`Contract.events.your_event_name.build_filter() <web3.contract.Contract.events.your_event_name.build_filter>`
- :meth:`Filter.get_new_entries() <web3.utils.filters.Filter.get_new_entries>`
- :meth:`Filter.get_all_entries() <web3.utils.filters.Filter.get_all_entries>`
- :meth:`Filter.format_entry() <web3.utils.filters.Filter.format_entry>`
- :meth:`Filter.is_valid_entry() <web3.utils.filters.Filter.is_valid_entry>`


Net API
~~~~~~~

Some basic network properties are available on the ``web3.net`` object:

- :attr:`web3.net.listening`
- :attr:`web3.net.peer_count`
- :attr:`web3.net.version`


ethPM
~~~~~

ethPM allows you to package up your contracts for reuse or use contracts from
another trusted registry. See the full details :ref:`here <ethpm>`.


ENS
~~~

`Ethereum Name Service (ENS) <https://ens.domains/>`_ provides the infrastructure
for human-readable addresses. As an example, instead of
``0xfB6916095ca1df60bB79Ce92cE3Ea74c37c5d359``, you can send funds to
``ethereumfoundation.eth``. Web3.py has support for ENS, documented
:ref:`here <ens_overview>`.
