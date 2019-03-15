Migrating your code from v4 to v5
=======================================

Web3.py follows `Semantic Versioning <http://semver.org>`_, which means
that version 5 introduced backwards-incompatible changes. If your
project depends on Web3.py v4, then you'll probably need to make some changes.

Here are the most common required updates:

Python 3.5 no longer supported.
-------------------------------

You will need to upgrade to either Python 3.6 or 3.7

``eth-abi`` v1 no longer supported
----------------------------------

You will need to upgrade the ``eth-abi`` dependency to v2 or higher.

Changes to base API
-------------------

JSON-RPC Updates
~~~~~~~~~~~~~~~~

In v4, JSON-RPC calls that looked up transactions or blocks and
didn't find them, returned ``None``. Now if a transaction or
block is not found, an error will be thrown. This applies to
the following web3 methods:

- :meth:`~web3.eth.Eth.getTransaction`
- :meth:`~web3.eth.Eth.getTransactionReceipt`
- :meth:`~web3.eth.Eth.getTransactionFromBlock`
- :meth:`~web3.eth.Eth.getTransactionCount`
- :meth:`~web3.eth.Eth.getBlock`
- :meth:`~web3.eth.Eth.getUncleCount`
- :meth:`~web3.eth.Eth.getUncleByBlock`

Removed Methods
~~~~~~~~~~~~~~~

- ``contract.buildTransaction`` was removed for ``contract.functions.buildTransaction.<method name>``
- ``contract.deploy`` was removed for ``contract.constructor.transact``
- ``contract.estimateGas`` was removed for ``contract.functions.<method name>.estimateGas``
- ``contract.call`` was removed for ``contract.<functions/events>.<method name>.call``
- ``contract.transact`` was removed for ``contract.<functions/events>.<method name>.transact``
- ``contract.eventFilter`` was removed for ``contract.events.<event name>.createFilter``
- ``middleware_stack`` was removed for :meth:`~Web3.middleware_onion`
- ``web3.miner.hashrate`` was a duplicate of :meth:`~web3.eth.Eth.hashrate` and was removed.
- ``web3.version.network`` was a duplicate of :meth:`~web3.net.Net.version` and was removed.
- ``web3.providers.tester.EthereumTesterProvider`` and ``web3.providers.tester.TestRPCProvider`` have been removed for :meth:`~web3.providers.eth_tester.EthereumTesterProvider`

Deprecated Methods
~~~~~~~~~~~~~~~~~~
- ``web3.sha3`` was deprecated for :meth:`~Web3.keccak`
- ``web3.soliditySha3`` was deprecated for :meth:`~Web3.solidityKeccak`

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

- Web3.py will no longer automatically look up a testnet connection
  in IPCProvider. Something like ``from web3.auto.ropsten import w3``
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
