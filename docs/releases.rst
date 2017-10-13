Release Notes
=============

3.16.1
------

* Addition of ``ethereum-tester`` as a dependency


3.16.0
------

* Addition of *named* middlewares for easier manipulation of middleware stack.
* Provider middlewares can no longer be modified during runtime.
* Experimental custom ABI normalization API for Contract objects.


3.15.0
------

* Change docs to use RTD theme
* Experimental new ``EthereumTesterProvider`` for the ``ethereum-tester`` library.
* Bugfix for ``function`` type abi encoding via ``ethereum-abi-utils`` upgrade to ``v0.4.1``
* Bugfix for ``Web3.toHex`` to conform to RPC spec.


3.14.2
------

* Fix PyPi readme text.


3.14.1
------

* Fix PyPi readme text.

3.14.0
------

* New ``stalecheck_middleware``
* Improvements to ``Web3.toHex`` and ``Web3.toText``.
* Improvements to ``Web3.sha3`` signature.
* Bugfixes for ``Web3.eth.sign`` api


3.13.5
------

* Add experimental ``fixture_middleware``
* Various bugfixes introduced in middleware API introduction and migration to
  formatter middleware.


3.13.4
------

* Bugfix for formatter handling of contract creation transaction.



3.13.3
------

* Improved testing infrastructure.


3.13.2
------

* Bugfix for retrieving filter changes for both new block filters and pending
  transaction filters.


3.13.1
------

* Fix mispelled ``attrdict_middleware`` (was spelled ``attrdict_middlware``).


3.13.0
------

* New Middleware API
* Support for multiple providers
* New ``web3.soliditySha3``
* Remove multiple functions that were never implemented from the original web3.
* Deprecated ``web3.currentProvider`` accessor.  Use ``web3.provider`` now instead.
* Deprecated password prompt within ``web3.personal.newAccount``.


3.12.0
------

* Bugfix for abi filtering to correctly handle ``constructor`` and ``fallback`` type abi entries.

3.11.0
------

* All web3 apis which accept ``address`` parameters now enforce checksums if the address *looks* like it is checksummed.
* Improvements to error messaging with when calling a contract on a node that may not be fully synced
* Bugfix for ``web3.eth.syncing`` to correctly handle ``False``

3.10.0
------

* Web3 now returns ``web3.utils.datastructures.AttributeDict`` in places where it previously returned a normal ``dict``.
* ``web3.eth.contract`` now performs validation on the ``address`` parameter.
* Added ``web3.eth.getWork`` API

3.9.0
-----

* Add validation for the ``abi`` parameter of ``eth``
* Contract return values of ``bytes``, ``bytesXX`` and ``string`` are no longer converted to text types and will be returned in their raw byte-string format.

3.8.1
-----

* Bugfix for ``eth_sign`` double hashing input.
* Removed deprecated ``DelegatedSigningManager``
* Removed deprecate ``PrivateKeySigningManager``

3.8.0
-----

* Update pyrlp dependency to ``>=0.4.7``
* Update eth-testrpc dependency to ``>=1.2.0``
* Deprecate ``DelegatedSigningManager``
* Deprecate ``PrivateKeySigningManager``

3.7.1
-----

* upstream version bump for bugfix in eth-abi-utils

3.7.0
-----

* deprecate ``eth.defaultAccount`` defaulting to the coinbase account.

3.6.2
-----

* Fix error message from contract factory creation.
* Use ``ethereum-utils`` for utility functions.

3.6.1
-----

* Upgrade ``ethereum-abi-utils`` dependency for upstream bugfix.

3.6.0
-----

* Deprecate ``Contract.code``: replaced by ``Contract.bytecode``
* Deprecate ``Contract.code_runtime``: replaced by ``Contract.bytecode_runtime``
* Deprecate ``abi``, ``code``, ``code_runtime`` and ``source`` as arguments for the ``Contract`` object.
* Deprecate ``source`` as a property of the ``Contract`` object
* Add ``Contract.factory()`` API.
* Deprecate the ``construct_contract_factory`` helper function.

3.5.3
-----

* Bugfix for how ``requests`` library is used.  Now reuses session.

3.5.2
-----

* Bugfix for construction of ``request_kwargs`` within HTTPProvider

3.5.1
-----

* Allow ``HTTPProvider`` to be imported from ``web3`` module.
* make ``HTTPProvider`` accessible as a property of ``web3`` instances.

3.5.0
-----

* Deprecate ``web3.providers.rpc.RPCProvider``
* Deprecate ``web3.providers.rpc.KeepAliveRPCProvider``
* Add new ``web3.providers.rpc.HTTPProvider``
* Remove hard dependency on gevent.

3.4.4
-----

* Bugfix for ``web3.eth.getTransaction`` when the hash is unknown.

3.4.3
-----

* Bugfix for event log data decoding to properly handle dynamic sized values.
* New ``web3.tester`` module to access extra RPC functionality from ``eth-testrpc``

3.4.2
-----

* Fix package so that ``eth-testrpc`` is not required.

3.4.1
-----

* Force gevent<1.2.0 until this issue is fixed: https://github.com/gevent/gevent/issues/916

3.4.0
-----

* Bugfix for contract instances to respect ``web3.eth.defaultAccount``
* Better error reporting when ABI decoding fails for contract method response.

3.3.0
-----

* New ``EthereumTesterProvider`` now available.  Faster test runs than ``TestRPCProvider``
* Updated underlying eth-testrpc requirement.

3.2.0
-----

* ``web3.shh`` is now implemented.
* Introduced ``KeepAliveRPCProvider`` to correctly recycle HTTP connections and use HTTP keep alive

3.1.1
-----

* Bugfix for contract transaction sending not respecting the
  ``web3.eth.defaultAccount`` configuration.

3.1.0
-----

* New DelegatedSigningManager and PrivateKeySigningManager classes.

3.0.2
-----

* Bugfix or IPCProvider not handling large JSON responses well.

3.0.1
-----

* Better RPC compliance to be compatable with the Parity JSON-RPC server.

3.0.0
-----

* ``Filter`` objects now support controlling the interval through which they poll
  using the ``poll_interval`` property

2.9.0
-----

* Bugfix generation of event topics.
* Web3.Iban now allows access to Iban address tools.

2.8.1
-----

* Bugfix for ``geth.ipc`` path on linux systems.

2.8.0
-----

* Changes to the ``Contract`` API:
    * ``Contract.deploy()`` parameter arguments renamed to args
    * ``Contract.deploy()`` now takes args and kwargs parameters to allow
      constructing with keyword arguments or positional arguments.
    * ``Contract.pastEvents`` now allows you to specify a ``fromBlock or
      ``toBlock.`` Previously these were forced to be ``'earliest'`` and
      ``web3.eth.blockNumber`` respectively.
    * ``Contract.call``, ``Contract.transact`` and ``Contract.estimateGas`` are now
      callable as class methods as well as instance methods. When called this
      way, an address must be provided with the transaction parameter.
    * ``Contract.call``, ``Contract.transact`` and ``Contract.estimateGas`` now allow
      specifying an alternate address for the transaction.
* ``RPCProvider`` now supports the following constructor arguments.
    * ``ssl`` for enabling SSL
    * ``connection_timeout`` and ``network_timeout`` for controlling the timeouts
      for requests.

2.7.1
-----

* Bugfix: Fix KeyError in merge_args_and_kwargs helper fn.

2.7.0
-----

* Bugfix for usage of block identifiers 'latest', 'earliest', 'pending'
* Sphinx documentation
* Non-data transactions now default to 90000 gas.
* Web3 object now has helpers set as static methods rather than being set at
  initialization.
* RPCProvider now takes a ``path`` parameter to allow configuration for requests
  to go to paths other than ``/``.

2.6.0
-----

* TestRPCProvider no longer dumps logging output to stdout and stderr.
* Bugfix for return types of ``address[]``
* Bugfix for event data types of ``address``

2.5.0
-----

* All transactions which contain a ``data`` element will now have their gas
  automatically estimated with 100k additional buffer.  This was previously
  only true with transactions initiated from a ``Contract`` object.

2.4.0
-----

* Contract functions can now be called using keyword arguments.

2.3.0
-----

* Upstream fixes for filters
* Filter APIs ``on`` and ``pastEvents`` now callable as both instance and class methods.

2.2.0
-----

* The filters that come back from the contract ``on`` and ``pastEvents`` methods
  now call their callbacks with the same data format as ``web3.js``.

2.1.1
-----

* Cast RPCProvider port to an integer.

2.1.0
-----

* Remove all monkeypatching

2.0.0
-----

* Pull in downstream updates to proper gevent usage.
* Fix ``eth_sign``
* Bugfix with contract operations mutating the transaction object that is passed in.
* More explicit linting ignore statements.

1.9.0
-----

* BugFix: fix for python3 only ``json.JSONDecodeError`` handling.

1.8.0
-----

* BugFix: ``RPCProvider`` not sending a content-type header
* Bugfix: ``web3.toWei`` now returns an integer instead of a decimal.Decimal

1.7.1
-----

* ``TestRPCProvider`` can now be imported directly from ``web3``

1.7.0
-----

* Add ``eth.admin`` interface.
* Bugfix: Format the return value of ``web3.eth.syncing``
* Bugfix: IPCProvider socket interactions are now more robust.

1.6.0
-----

* Downstream package upgrades for ``eth-testrpc`` and ``ethereum-tester-client`` to
  handle configuration of the Homestead and DAO fork block numbers.

1.5.0
-----

* Rename ``web3.contract._Contract`` to ``web3.contract.Contract``
  to expose it for static analysis and auto completion tools
* Allow passing string parameters to functions
* Automatically compute gas requirements for contract deployment and
* transactions.
* Contract Filters
* Block, Transaction, and Log filters
* ``web3.eth.txpool`` interface
* ``web3.eth.mining`` interface
* Fixes for encoding.

1.4.0
-----

* Bugfix to allow address types in constructor arguments.

1.3.0
-----

* Partial implementation of the ``web3.eth.contract`` interface.

1.2.0
-----

* Restructure project modules to be more *flat*
* Add ability to run test suite without the *slow* tests.
* Breakup ``encoding`` utils into smaller modules.
* Basic pep8 formatting.
* Apply python naming conventions to internal APIs
* Lots of minor bugfixes.
* Removal of dead code left behing from ``1.0.0`` refactor.
* Removal of ``web3/solidity`` module.

1.1.0
-----

* Add missing ``isConnected()`` method.
* Add test coverage for ``setProvider()``

1.0.1
-----

* Specify missing ``pyrlp`` and ``gevent`` dependencies

1.0.0
-----

* Massive refactor to the majority of the app.

0.1.0
-----

* Initial release
