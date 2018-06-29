Release Notes
=============

v4.4.1
--------

Released June 29, 2018

- Bugfixes

  - eth-pm package was renamed (old one deleted) which broke the web3 release.
    eth-pm was removed from the web3.py install until it's stable.

- Misc

  - :class:`~web3.providers.ipc.IPCProvider` now accepts a :class:`pathlib.Path`
    argument for the IPC path
  - Docs explaining the :ref:`new custom autoproviders in web3 <custom_auto_providers>`

v4.4.0
--------

Released June 21, 2018

- Features

  - Add support for https in WEB3_PROVIDER_URI environment variable
  - Can send websocket connection parameters in :class:`~web3.providers.websocket.WebsocketProvider`
  - Two new auto-initialization options:

    - ``from web3.auto.gethdev import w3``
    - ``from web3.auto.infura import w3``
      (After setting the ``INFURA_API_KEY`` environment variable)
  - Alpha support for a new package management tool based on ethpm-spec, see :doc:`web3.pm`
- Bugfixes

  - Can now receive large responses in :class:`~web3.providers.websocket.WebsocketProvider` by
    specifying a large ``max_size`` in the websocket connection parameters.
- Misc

  - Websockets dependency upgraded to v5
  - Raise deprecation warning on :meth:`~web3.eth.Eth.getTransactionFromBlock`
  - Fix docs for :meth:`~web3.eth.Eth.waitForTransactionReceipt`
  - Developer Dockerfile now installs testing dependencies

v4.3.0
--------

Released June 6, 2018

- Features

  - Support for the ABI types like: `fixedMxN
    <http://solidity.readthedocs.io/en/v0.4.24/abi-spec.html#types>`_
    which is used by Vyper.
  - In-flight transaction-signing middleware: Use local keys as if they were hosted keys
    using the new ``sign_and_send_raw_middleware``
  - New :meth:`~web3.eth.Eth.getUncleByBlock` API
  - New name :meth:`~web3.eth.Eth.getTransactionByBlock`, which replaces the deprecated
    :meth:`~web3.eth.Eth.getTransactionFromBlock`
  - Add several new Parity trace functions
  - New API to resolve ambiguous function calls, for example:

    - Two functions with the same name that accept similar argument types, like
      ``myfunc(uint8)`` and ``myfunc(int8)``, and you want to call
      ``contract.functions.myfunc(1).call()``
    - See how to use it at: :ref:`ambiguous-contract-functions`
- Bugfixes

  - Gas estimation doesn't crash, when 0 blocks are available. (ie~ on the genesis block)
  - Close out all HTTPProvider sessions, to squash warnings on exit
  - Stop adding Contract address twice to the filter. It was making some nodes unhappy
- Misc

  - Friendlier json encoding/decoding failure error messages
  - Performance improvements, when the responses from the node are large
    (by reducing the number of times we evaluate if the response is valid json)
  - Parity CI test fixes (ugh, environment setup hell, thanks to the
    community for cleaning this up!)
  - Don't crash when requesting a transaction that was created with the parity bug
    (which allowed an unsigned transaction to be included, so ``publicKey`` is ``None``)
  - Doc fixes: addresses must be checksummed (or ENS names on mainnet)
  - Enable local integration testing of parity on non-Debian OS
  - README:

    - Testing setup for devs
    - Change the build badge from Travis to Circle CI
  - Cache the parity binary in Circle CI, to reduce the impact of their binary API going down
  - Dropped the dot: ``py.test`` -> ``pytest``

v4.2.1
--------

Released May 9, 2018

- Bugfixes

  - When :meth:`getting a transaction <web3.eth.Eth.getTransaction>`
    with data attached and trying to :meth:`modify it <web3.eth.Eth.modifyTransaction>`
    (say, to increase the gas price), the data was not being reattached in
    the new transaction.
  - :meth:`web3.personal.sendTransaction` was crashing when using a transaction
    generated with ``buildTransaction()``
- Misc

  - Improved error message when connecting to a geth-style PoA network
  - Improved error message when address is not checksummed
  - Started in on support for ``fixedMxN`` ABI arguments
  - Lots of documentation upgrades, including:

    - Guide for understanding nodes/networks/connections
    - Simplified Quickstart with notes for common issues
    - A new Troubleshooting section
  - Potential pypy performance improvements (use toolz instead of cytoolz)
  - eth-tester upgraded to beta 24

v4.2.0
--------

Released Apr 25, 2018

- Removed audit warning and opt-in requirement for ``w3.eth.account``. See more in:
  :ref:`eth-account`
- Added an API to look up contract functions: ``fn = contract.functions['function_name_here']``
- Upgrade Whisper (shh) module to use v6 API
- Bugfix: set 'to' field of transaction to empty when using
  ``transaction = contract.constructor().buildTransaction()``
- You can now specify `nonce` in ``buildTransaction()``
- Distinguish between chain id and network id -- currently always return `None` for
  :attr:`~web3.net.Net.chainId`
- Better error message when trying to use a contract function that has 0 or >1 matches
- Better error message when trying to install on a python version <3.5
- Installs pypiwin32 during pip install, for a better Windows experience
- Cleaned up a lot of test warnings by upgrading from deprecated APIs, especially
  from the deprecated ``contract.deploy(txn_dict, args=contract_args)``
  to the new ``contract.constructor(*contract_args).transact(txn_dict)``
- Documentation typo fixes
- Better template for Pull Requests

v4.1.0
--------

Released Apr 9, 2018

- New :class:`~web3.providers.websocket.WebsocketProvider`.
  If you're looking for better performance than HTTP, check out websockets.
- New :meth:`w3.eth.waitForTransactionReceipt() <web3.eth.Eth.waitForTransactionReceipt>`
- Added name collision detection to ConciseContract and ImplicitContract
- Bugfix to allow fromBlock set to 0 in createFilter, like
  ``contract.events.MyEvent.createFilter(fromBlock=0, ...)``
- Bugfix of ENS automatic connection
- eth-tester support for Byzantium
- New migration guide for v3 -> v4 upgrade
- Various documentation updates
- Pinned eth-account to older version

v4.0.0
-----------------

Released Apr 2, 2018

- Marked beta.13 as stable
- Documentation tweaks

v4.0.0-beta.13
-----------------

Released Mar 27, 2018

*This is intended to be the final release before the stable v4 release.*

- Add support for geth 1.8 (fixed error on :meth:`~web3.eth.Eth.getTransactionReceipt`)
- You can now call a contract method at a specific block
  with the ``block_identifier`` keyword argument, see:
  :meth:`~web3.contract.ContractFunction.call`
- In preparation for stable release, disable ``w3.eth.account`` by default,
  until a third-party audit is complete & resolved.
- New API for contract deployment, which enables gas estimation, local signing, etc.
  See :meth:`~web3.contract.Contract.constructor`.
- Find contract events with :ref:`contract.events.$my_event.createFilter() <contract_createFilter>`
- Support auto-complete for contract methods.
- Upgrade most dependencies to stable

  - eth-abi
  - eth-utils
  - hexbytes
  - *not included: eth-tester and eth-account*
- Switch the default EthereumTesterProvider backend from eth-testrpc to eth-tester:
  :class:`web3.providers.eth_tester.EthereumTesterProvider`
- A lot of documentation improvements
- Test node integrations over a variety of providers
- geth 1.8 test suite


v4.0.0-beta.12
-----------------

A little hiccup on release. Skipped.

v4.0.0-beta.11
-----------------

Released Feb 28, 2018

- New methods to modify or replace pending transactions
- A compatibility option for connecting to ``geth --dev`` -- see :ref:`geth-poa`
- A new :attr:`web3.net.chainId`
- Create a filter object from an existing filter ID.
- eth-utils v1.0.1 (stable) compatibility


v4.0.0-beta.10
-----------------

Released Feb 21, 2018

- bugfix: Compatibility with eth-utils v1-beta2
  (the incompatibility was causing fresh web3.py installs to fail)
- bugfix: crash when sending the output of ``contract.functions.myFunction().buildTransaction()``
  to :meth:`~web3.eth.Eth.sendTransaction`. Now, having a chainID key does not crash
  sendTransaction.
- bugfix: a TypeError when estimating gas like:
  ``contract.functions.myFunction().estimateGas()`` is fixed
- Added parity integration tests to the continuous integration suite!
- Some py3 and docs cleanup

v4.0.0-beta.9
-------------

Released Feb 8, 2018

- Access event log parameters as attributes
- Support for specifying nonce in eth-tester
- `Bugfix <https://github.com/ethereum/web3.py/pull/616>`_
  dependency conflicts between eth-utils, eth-abi, and eth-tester
- Clearer error message when invalid keywords provided to contract constructor function
- New docs for working with private keys + set up doctests
- First parity integration tests
- replace internal implementation of w3.eth.account with
  :class:`eth_account.account.Account`

v4.0.0-beta.8
-------------

Released Feb 7, 2018, then recalled. It added 32MB of test data to git history,
so the tag was deleted, as well as the corresponding release.
(Although the release would not have contained that test data)

v4.0.0-beta.7
-------------

Released Jan 29, 2018

- Support for :meth:`web3.eth.Eth.getLogs` in eth-tester with py-evm
- Process transaction receipts with Event ABI, using
  `Contract.events.myEvent(*args, **kwargs).processReceipt(transaction_receipt)`
  see :ref:`event-log-object` for the new type.
- Add timeout parameter to :class:`web3.providers.ipc.IPCProvider`
- bugfix: make sure `idna` package is always installed
- Replace ethtestrpc with py-evm, in all tests
- Dockerfile fixup
- Test refactoring & cleanup
- Reduced warnings during tests

v4.0.0-beta.6
-------------

Released Jan 18, 2018

- New contract function call API: `my_contract.functions.my_func().call()` is preferred over the now
  deprecated `my_contract.call().my_func()` API.
- A new, sophisticated gas estimation algorithm, based on the https://ethgasstation.info approach.
  You must opt-in to the new approach, because it's quite slow. We recommend using the new caching middleware.
  See :meth:`web3.gas_strategies.time_based.construct_time_based_gas_price_strategy`
- New caching middleware that can cache based on time, block, or indefinitely.
- Automatically retry JSON-RPC requests over HTTP, a few times.
- ConciseContract now has the address directly
- Many eth-tester fixes. :class:`web3.providers.eth_tester.main.EthereumTesterProvider` is now a
  legitimate alternative to :class:`web3.providers.tester.EthereumTesterProvider`.
- ethtest-rpc removed from testing. Tests use eth-tester only, on pyethereum. Soon it will be
  eth-tester with py-evm.
- Bumped several dependencies, like eth-tester
- Documentation updates

v4.0.0-beta.5
-------------

Released Dec 28, 2017

* Improvements to working with eth-tester, using :class:`~web3.providers.eth_tester.EthereumTesterProvider`:

  * Bugfix the key names in event logging
  * Add support for :meth:`~web3.eth.Eth.sendRawTransaction`
* :class:`~web3.providers.ipc.IPCProvider` now automatically retries on a broken connection, like when you restart your node
* New gas price engine API, laying groundwork for more advanced gas pricing strategies

v4.0.0-beta.4
-------------

Released Dec 7, 2017

* New :meth:`~web3.contract.Contract.buildTransaction` method to prepare contract transactions, offline
* New automatic provider detection, for ``w3 = Web3()`` initialization
* Set environment variable `WEB3_PROVIDER_URI` to suggest a provider for automatic detection
* New API to set providers like: ``w3.providers = [IPCProvider()]``
* Crashfix: :meth:`web3.eth.Eth.filter` when retrieving logs with the argument 'latest'
* Bump eth-tester to v0.1.0-beta.5, with bugfix for filtering by topic
* Removed GPL lib ``pylru``, now believed to be in full MIT license compliance.

v4.0.0-beta.3
-------------

Released Dec 1, 2017

* Fix encoding of ABI types: ``bytes[]`` and ``string[]``
* Windows connection error bugfix
* Bugfix message signatures that were broken ~1% of the time (zero-pad ``r`` and ``s``)
* Autoinit web3 now produces None instead of raising an exception on ``from web3.auto import w3``
* Clearer errors on formatting failure (includes field name that failed)
* Python modernization, removing Py2 compatibility cruft
* Update dependencies with changed names, now:

  * ``eth-abi``
  * ``eth-keyfile``
  * ``eth-keys``
  * ``eth-tester``
  * ``eth-utils``
* Faster Travis CI builds, with cached geth binary

v4.0.0-beta.2
-------------

Released Nov 22, 2017

Bug Fixes:

* :meth:`~web3.eth.Eth.sendRawTransaction` accepts raw bytes
* :meth:`~web3.eth.Eth.contract` accepts an ENS name as contract address
* :meth:`~web3.account.Account.signTransaction` returns the expected hash (*after* signing the transaction)
* :class:`~web3.account.Account` methods can all be called statically, like: ``Account.sign(...)``
* :meth:`~web3.eth.Eth.getTransactionReceipt` returns the ``status`` field as an ``int``
* :meth:`Web3.soliditySha3` looks up ENS names if they are supplied with an "address" ABI
* If running multiple threads with the same w3 instance, ``ValueError: Recursively called ...`` is no longer raised

Plus, various python modernization code cleanups, and testing against geth 1.7.2.

v4.0.0-beta.1
-------------

* Python 3 is now required
* ENS names can be used anywhere that a hex address can
* Sign transactions and messages with local private keys
* New filter mechanism: :meth:`~web3.utils.filters.Filter.get_all_entries` and :meth:`~web3.utils.filters.Filter.get_new_entries`
* Quick automatic initialization with ``from web3.auto import w3``
* All addresses must be supplied with an EIP-55 checksum
* All addresses are returned with a checksum
* Renamed ``Web3.toDecimal()`` to ``toInt()``, see: :ref:`overview_type_conversions`
* All filter calls are synchronous, gevent integration dropped
* Contract :meth:`~web3.contract.Contract.eventFilter` has replaced both ``Contract.on()`` and ``Contract.pastEvents()``
* Contract arguments of ``bytes`` ABI type now accept hex strings.
* Contract arguments of ``string`` ABI type now accept python ``str``.
* Contract return values of ``string`` ABI type now return python ``str``.
* Many methods now return a ``bytes``-like object where they used to return a hex string, like in :meth:`Web3.sha3()`
* IPC connection left open and reused, rather than opened and closed on each call
* A number of deprecated methods from v3 were removed

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
