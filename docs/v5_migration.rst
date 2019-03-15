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

JSON-RPC Updates
----------------

In v4, JSON-RPC calls that looked up transactions or blocks and
didn't find them, returned ``None``. Now if a transaction or
block is not found, an error will be thrown. This applies to
the following web3 methods:

- ``web3.eth.getTransaction``
- ``web3.eth.getTransactionReceipt``
- ``web3.eth.getTransactionFromBlock``
- ``web3.eth.replaceTransaction``
- ``web3.eth.getBlockTransactionCount``
- ``web3.eth.getBlock``
- ``web3.eth.getUncleCount``
- ``web3.eth.getUncleByBlock``


Changes to base API
-------------------

Removed Methods
~~~~~~~~~~~~~~~

- ``contract.buildTransaction`` was removed for ``contract.functions.buildTransaction.<method name>``
- ``contract.deploy`` was removed for ``contract.constructor.transact``
- ``contract.estimateGas`` was removed for ``contract.functions.<method name>.estimateGas``
- ``contract.call`` was removed for ``contract.<functions/events>.<method name>.call``
- ``contract.transact`` was removed for ``contract.<functions/events>.<method name>.transact``
- ``contract.eventFilter`` was removed for ``contract.events.<event name>.createFilter``
- ``middleware_stack`` was removed for ``Web3.middleware_onion``
- ``web3.sha3`` was removed for ``web3.keccak``
- ``web3.soliditySha3`` was removed for ``web3.solidity.keccak``
- ``web3.miner.hashrate`` was a duplicate of ``web3.eth.hashrate`` and was removed.
- ``web3.version.network`` was a duplicate of ``web3.net.version`` and was removed.
- check this one: ``web3.providers.tester.EthereumTesterProvider`` and ``web3.providers.tester.TestRPCProvider`` have been removed for ``web3.providers.eth_tester.EthereumTesterProvider``

Deprecated Methods
~~~~~~~~~~~~~~~~~~
- ``web3.sha3`` was deprecated for :meth:`~Web3.keccak`
- ``web3.soliditySha3`` was deprecated for :meth:`~Web3.solidityKeccak`

ENS
~~~

Web3.py has stopped inferring ``.eth`` TLD on domain names. If a domain name is used, you'll need to specify the TLD.

Manager Provider
~~~~~~~~~~~~~~~~

In v5, only a single provider will be allowed. Anywhere ``manager.providers`` was used, there is now a singular ``manager.provider``. Similarly, instances of ``web3.providers`` was changed to ``web3.provider``.

Testnet Changes
~~~~~~~~~~~~~~~

- Web3.py will no longer automatically look up a testnet connection
  in IPCProvider. Something like ``from web3.auto.ropsten import w3``
  should be used instead, if auto-detecting a testnet is desired.
- EthereumTesterProvider now validates the provided value is an
  instance of EthereumTester. For example, this will not work:

  .. code-block:: python

     >>> from web3 import Web3
     >>> from eth_tester import PyEVMBackend

     >>> w3 = Web3(Web3.EthereumTesterProvider(PyEVMBackend()))

Instead, you should use:

   .. doctest::

      >>> from web3 import Web3
      >>> from eth_tester import PyEVMBackend, EthereumTester

      >>> w3 = Web3(Web3.EthereumTesterProvider(EthereumTester(PyEVMBackend())))


