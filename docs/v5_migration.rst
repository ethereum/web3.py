.. _migrating_v4_to_v5:

Migrating your code from v4 to v5
=======================================

Web3.py follows `Semantic Versioning <http://semver.org>`_, which means
that version 5 introduced backwards-incompatible changes. If your
project depends on Web3.py v4, then you'll probably need to make some changes.

Here are the most common required updates:

Python 3.5 no longer supported
------------------------------

You will need to upgrade to either Python 3.6 or 3.7

``eth-abi`` v1 no longer supported
----------------------------------

You will need to upgrade the ``eth-abi`` dependency to v2

Changes to base API
-------------------

JSON-RPC Updates
~~~~~~~~~~~~~~~~

In v4, JSON-RPC calls that looked up transactions or blocks and
didn't find them, returned ``None``. Now if a transaction or
block is not found, a ``BlockNotFound`` or a ``TransactionNotFound``
error will be thrown as appropriate. This applies to the
following web3 methods:

- :meth:`~web3.eth.Eth.getTransaction` will throw a ``TransactionNotFound`` error
- :meth:`~web3.eth.Eth.getTransactionReceipt` will throw a ``TransactionNotFound`` error
- :meth:`~web3.eth.Eth.getTransactionByBlock` will throw a ``TransactionNotFound`` error
- :meth:`~web3.eth.Eth.getTransactionCount` will throw a ``BlockNotFound`` error
- :meth:`~web3.eth.Eth.getBlock` will throw a ``BlockNotFound`` error
- :meth:`~web3.eth.Eth.getUncleCount` will throw a ``BlockNotFound`` error
- :meth:`~web3.eth.Eth.getUncleByBlock` will throw a ``BlockNotFound`` error

Removed Methods
~~~~~~~~~~~~~~~

- ``contract.buildTransaction`` was removed for ``contract.functions.buildTransaction.<method name>``
- ``contract.deploy`` was removed for ``contract.constructor.transact``
- ``contract.estimateGas`` was removed for ``contract.functions.<method name>.estimateGas``
- ``contract.call`` was removed for ``contract.<functions/events>.<method name>.call``
- ``contract.transact`` was removed for ``contract.<functions/events>.<method name>.transact``
- ``contract.eventFilter`` was removed for ``contract.events.<event name>.createFilter``
- ``middleware_stack`` was renamed to :meth:`~Web3.middleware_onion`
- ``web3.miner.hashrate`` was a duplicate of :meth:`~web3.eth.Eth.hashrate` and was removed.
- ``web3.version.network`` was a duplicate of :meth:`~web3.net.Net.version` and was removed.
- ``web3.providers.tester.EthereumTesterProvider`` and ``web3.providers.tester.TestRPCProvider`` have been removed for :meth:`~web3.providers.eth_tester.EthereumTesterProvider`
- ``web3.eth.enableUnauditedFeatures`` was removed
- ``web3.txpool`` was moved to :meth:`~web3.geth.txpool`
- ``web3.version.node`` was removed for ``web3.clientVersion``
- ``web3.version.ethereum`` was removed for :meth:`~web3.eth.Eth.protocolVersion`
- Relocated personal RPC endpoints to reflect Parity and Geth implementations:

  - ``web3.personal.listAccounts`` was removed for :meth:`~web3.geth.personal.listAccounts` or :meth:`~web3.parity.personal.listAccounts`
  - ``web3.personal.importRawKey`` was removed for :meth:`~web3.geth.personal.importRawKey` or :meth:`~web3.parity.personal.importRawKey`
  - ``web3.personal.newAccount`` was removed for :meth:`~web3.geth.personal.newAccount` or :meth:`~web3.parity.personal.newAccount`
  - ``web3.personal.lockAccount`` was removed for :meth:`~web3.geth.personal.lockAccount`
  - ``web3.personal.unlockAccount`` was removed for :meth:`~web3.geth.personal.unlockAccount` or :meth:`~web3.parity.personal.unlockAccount`
  - ``web3.personal.sendTransaction`` was removed for :meth:`~web3.geth.personal.sendTransaction` or :meth:`~web3.parity.personal.sendTransaction`

- Relocated ``web3.admin`` module to ``web3.geth`` namespace
- Relocated ``web3.miner`` module to ``web3.geth`` namespace

Deprecated Methods
~~~~~~~~~~~~~~~~~~
Expect the following methods to be removed in v6:

- ``web3.sha3`` was deprecated for :meth:`~Web3.keccak`
- ``web3.soliditySha3`` was deprecated for :meth:`~Web3.solidityKeccak`
- :meth:`~web3.net.Net.chainId` was deprecated for :meth:`~web3.eth.Eth.chainId`.
  Follow issue `#1293 <https://github.com/ethereum/web3.py/issues/1293>`_ for details
- ``web3.eth.getCompilers()`` was deprecated and will not be replaced
- :meth:`~web3.eth.getTransactionFromBlock()` was deprecated for :meth:`~Web3.getTransactionByBlock`

Deprecated ConciseContract and ImplicitContract
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The ConciseContract and ImplicitContract have been deprecated and will be removed in v6.

ImplicitContract instances will need to use the verbose syntax. For example:

``contract.functions.<function name>.transact({})``

ConciseContract has been replaced with the ContractCaller API. Instead of using the ConciseContract factory, you can now use:

``contract.caller.<function_name>``

or the classic contract syntax:

``contract.functions.<function name>.call()``.

Some more concrete examples can be found in the `ContractCaller docs <https://web3py.readthedocs.io/en/latest/contracts.html?highlight=Caller#contractcaller>`_


Manager Provider
~~~~~~~~~~~~~~~~

In v5, only a single provider will be allowed. While allowing
multiple providers is a feature we'd like to support in the future,
the way that multiple providers was handled in v4 wasn't ideal.
The only thing they could do was fall back. There was no mechanism for any
round robin, nor was there any control around which provider
was chosen. Eventually, the idea is to expand the Manager API
to support injecting custom logic into the provider selection process.

For now, ``manager.providers`` has changed to ``manager.provider``.
Similarly, instances of ``web3.providers`` have been changed to
``web3.provider``.

Testnet Changes
~~~~~~~~~~~~~~~

Web3.py will no longer automatically look up a testnet connection
in IPCProvider. Something like ``from web3.auto.infura.ropsten import w3``
should be used instead.

ENS
---

Web3.py has stopped inferring the ``.eth`` TLD on domain names.
If a domain name is used instead of an address, you'll need
to specify the TLD. An ``InvalidTLD`` error will be thrown if
the TLD is missing.

Required Infura API Key
-----------------------

In order to interact with Infura after March 27, 2019, you'll need to set an
environment variable called ``WEB3_INFURA_PROJECT_ID``. You can get a
project id by visiting https://infura.io/register.
