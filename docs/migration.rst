Migration Guide
===============

.. _migrating_v6_to_v7:

Migrating from v6 to v7
-----------------------

Ready for the future? web3.py
`v7 beta versions <https://web3py.readthedocs.io/en/latest/migration.html#migrating-from-v6-to-v7>`_
are now available! The API is stable, and we're looking for feedback.


.. _migrating_v5_to_v6:

Migrating from v5 to v6
-----------------------

web3.py follows `Semantic Versioning <http://semver.org>`_, which means
that version 6 introduced backwards-incompatible changes. If your
project depends on web3.py v6, then you'll probably need to make some changes.

Breaking Changes:

Strict Bytes Checking by Default
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

web3.py v6 moved to requiring strict bytes checking by default. This means that if an
ABI specifies a ``bytes4`` argument, web3.py will invalidate any entry that is not
encodable as a bytes type with length of 4. This means only 0x-prefixed hex strings with
a length of 4 and bytes types with a length of 4 will be considered valid. This removes
doubt that comes from inferring values and assuming they should be padded.

This behavior was previously available in via the ``w3.enable_strict_bytes_checking()``
method. This is now, however, a toggleable flag on the ``Web3`` instance via the
``w3.strict_bytes_type_checking`` property. As outlined above, this property is set to
``True`` by default but can be toggled on and off via the property's setter
(e.g. ``w3.strict_bytes_type_checking = False``).


Snake Case
~~~~~~~~~~

web3.py v6 moved to the more Pythonic convention of snake_casing wherever
possible. There are some exceptions to this pattern:

- Contract methods and events use whatever is listed in the ABI. If the smart contract
  convention is to use camelCase for method and event names, web3.py won't do
  any magic to convert it to snake_casing.
- Arguments to JSON-RPC methods. For example: transaction and filter
  parameters still use camelCasing. The reason for
  this is primarily due to error messaging. It would be confusing to pass in a
  snake_cased parameter and get an error message with a camelCased parameter.
- Data that is returned from JSON-RPC methods. For example:
  The keys in a transaction receipt will still be returned as camelCase.


Python 3.10 and 3.11 Support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Support for Python 3.10 and 3.11 is here. In order to support Python 3.10, we had to
update the ``websockets`` dependency to v10+.

Exceptions
~~~~~~~~~~

Exceptions inherit from a base class
````````````````````````````````````

In v5, some web3.py exceptions inherited from ``AttributeError``, namely:

- ``NoABIFunctionsFound``
- ``NoABIFound``
- ``NoABIEventsFound``

Others inherited from ``ValueError``, namely:

- ``InvalidAddress``
- ``NameNotFound``
- ``LogTopicError``
- ``InvalidEventABI``

Now web3.py exceptions inherit from the same base ``Web3Exception``.

As such, any code that was expecting a ``ValueError`` or an ``AttributeError`` from
web3.py must update to expecting one of the exceptions listed above, or
``Web3Exception``.

Similarly, exceptions raised in the EthPM and ENS modules inherit from the base
``EthPMException`` and ``ENSException``, respectively.

ValidationError
```````````````

The Python dev tooling ecosystem is moving towards standardizing
``ValidationError``, so users know that they're catching the correct
``ValidationError``. The base ``ValidationError`` is imported from
``eth_utils``. However, we also wanted to empower users to catch all errors emitted
by a particular module. So we now have a ``Web3ValidationError``, ``EthPMValidationError``,
and an ``ENSValidationError`` that all inherit from the generic
``eth_utils.exceptions.ValidationError``.

Web3 class split into Web3 and AsyncWeb3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `Web3` class previously contained both sync and async methods. We've separated
`Web3` and `AsyncWeb3` functionality to tighten up typing. For example:

.. code-block:: python

    from web3 import Web3, AsyncWeb3

    w3 = Web3(Web3.HTTPProvider(<provider.url>))
    async_w3 = AsyncWeb3(AsyncWeb3.AsyncHTTPProvider(<provider.url>))

`dict` to `AttributeDict` conversion moved to middleware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Eth` module data returned as key-value pairs was previously automatically converted to
an `AttributeDict` by result formatters, which could cause problems with typing. This
conversion has been moved to a default `attrdict_middleware` where it can be easily
removed if necessary. See the `Eth module <web3.eth.html#web3.eth.Eth>`_ docs for more detail.

Other Misc Changes
~~~~~~~~~~~~~~~~~~

- ``InfuraKeyNotFound`` exception has been changed to ``InfuraProjectIdNotFound``
- ``SolidityError`` has been removed in favor of ``ContractLogicError``
- When a method is unavailable from a node provider (i.e. a response error
  code of -32601 is returned), a ``MethodUnavailable`` error is
  now raised instead of ``ValueError``
- Logs' `data` field was previously formatted with `to_ascii_if_bytes`, now formatted to `HexBytes`
- Receipts' `type` field was previously not formatted, now formatted with `to_integer_if_hex`

Removals
~~~~~~~~

- Removed unused IBAN module
- Removed ``WEB3_INFURA_API_KEY`` environment variable in favor of ``WEB3_INFURA_PROJECT_ID``
- Removed Kovan auto provider
- Removed deprecated ``sha3`` and ``soliditySha3`` methods in favor of ``keccak`` and ``solidityKeccak``
- Remove Parity Module and References


Other notable changes
~~~~~~~~~~~~~~~~~~~~~

- The ``ipfshttpclient`` library is now opt-in via a web3 install extra.
  This only affects the ethpm ipfs backends, which rely on the library.


.. _migrating_v4_to_v5:

Migrating from v4 to v5
-----------------------

Web3.py follows `Semantic Versioning <http://semver.org>`_, which means
that version 5 introduced backwards-incompatible changes. If your
project depends on Web3.py v4, then you'll probably need to make some changes.

Here are the most common required updates:

Python 3.5 no longer supported
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You will need to upgrade to either Python 3.6 or 3.7

``eth-abi`` v1 no longer supported
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You will need to upgrade the ``eth-abi`` dependency to v2

Changes to base API
~~~~~~~~~~~~~~~~~~~

JSON-RPC Updates
````````````````

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
```````````````

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
``````````````````

Expect the following methods to be removed in v6:

- ``web3.sha3`` was deprecated for :meth:`~Web3.keccak`
- ``web3.soliditySha3`` was deprecated for :meth:`~Web3.solidityKeccak`
- :meth:`~web3.net.Net.chainId` was deprecated for :meth:`~web3.eth.Eth.chainId`.
  Follow issue `#1293 <https://github.com/ethereum/web3.py/issues/1293>`_ for details
- ``web3.eth.getCompilers()`` was deprecated and will not be replaced
- :meth:`~web3.eth.getTransactionFromBlock()` was deprecated for :meth:`~Web3.getTransactionByBlock`

Deprecated ConciseContract and ImplicitContract
```````````````````````````````````````````````
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
in IPCProvider.

ENS
~~~

Web3.py has stopped inferring the ``.eth`` TLD on domain names.
If a domain name is used instead of an address, you'll need
to specify the TLD. An ``InvalidTLD`` error will be thrown if
the TLD is missing.

Required Infura API Key
~~~~~~~~~~~~~~~~~~~~~~~

In order to interact with Infura after March 27, 2019, you'll need to set an
environment variable called ``WEB3_INFURA_PROJECT_ID``. You can get a
project id by visiting https://infura.io/register.


Migrating from v3 to v4
-----------------------

Web3.py follows `Semantic Versioning <http://semver.org>`_, which means
that version 4 introduced backwards-incompatible changes. If your
project depends on Web3.py v3, then you'll probably need to make some changes.

Here are the most common required updates:

Python 2 to Python 3
~~~~~~~~~~~~~~~~~~~~

Only Python 3 is supported in v4. If you are running in Python 2,
it's time to upgrade. We recommend using `2to3` which can make
most of your code compatible with Python 3, automatically.

The most important update, relevant to Web3.py, is the new :class:`bytes`
type. It is used regularly, throughout the library, whenever dealing with data
that is not guaranteed to be text.

Many different methods in Web3.py accept text or binary data, like contract methods,
transaction details, and cryptographic functions. The following example
uses :meth:`~Web3.sha3`, but the same pattern applies elsewhere.

In v3 & Python 2, you might have calculated the hash of binary data this way:

.. code-block:: python

    >>> Web3.sha3('I\xe2\x99\xa5SF')
    '0x50a826df121f4d076a3686d74558f40082a8e70b3469d8e9a16ceb2a79102e5e'

Or, you might have calculated the hash of text data this way:

.. code-block:: python

    >>> Web3.sha3(text=u'I♥SF')
    '0x50a826df121f4d076a3686d74558f40082a8e70b3469d8e9a16ceb2a79102e5e'

After switching to Python 3, these would instead be executed as:

.. code-block:: python

    >>> Web3.sha3(b'I\xe2\x99\xa5SF')
    HexBytes('0x50a826df121f4d076a3686d74558f40082a8e70b3469d8e9a16ceb2a79102e5e')

    >>> Web3.sha3(text='I♥SF')
    HexBytes('0x50a826df121f4d076a3686d74558f40082a8e70b3469d8e9a16ceb2a79102e5e')

Note that the return value is different too: you can treat :class:`hexbytes.main.HexBytes`
like any other bytes value, but the representation on the console shows you the hex encoding of
those bytes, for easier visual comparison.

It takes a little getting used to, but the new py3 types are much better. We promise.

Filters
~~~~~~~

Filters usually don't work quite the way that people want them to.

The first step toward fixing them was to simplify them by removing the polling
logic. Now, you must request an update on your filters explicitly. That
means that any exceptions during the request will bubble up into your code.

In v3, those exceptions (like "filter is not found") were swallowed silently
in the automated polling logic. Here was the invocation for
printing out new block hashes as they appear:

.. code-block:: python

    >>> def new_block_callback(block_hash):
    ...     print(f"New Block: {block_hash}")
    ...
    >>> new_block_filter = web3.eth.filter('latest')
    >>> new_block_filter.watch(new_block_callback)

In v4, that same logic:

.. code-block:: python

    >>> new_block_filter = web3.eth.filter('latest')
    >>> for block_hash in new_block_filter.get_new_entries():
    ...     print(f"New Block: {block_hash}")

The caller is responsible for polling the results from ``get_new_entries()``.
See :ref:`asynchronous_filters` for examples of filter-event handling with web3 v4.

TestRPCProvider and EthereumTesterProvider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These providers are fairly uncommon. If you don't recognize the names,
you can probably skip the section.

However, if you were using web3.py for testing contracts,
you might have been using TestRPCProvider or EthereumTesterProvider.

In v4 there is a new :class:`EthereumTesterProvider`, and the old v3 implementation has been
removed. Web3.py v4 uses :class:`eth_tester.main.EthereumTester` under the hood, instead
of eth-testrpc. While ``eth-tester`` is still in beta, many parts are
already in better shape than testrpc, so we decided to replace it in v4.

If you were using TestRPC, or were explicitly importing EthereumTesterProvider, like:
``from web3.providers.tester import EthereumTesterProvider``, then you will need to update.

With v4 you should import with ``from web3 import EthereumTesterProvider``. As before, you'll
need to install Web3.py with the ``tester`` extra to get these features, like:

.. code-block:: bash

    $ pip install web3[tester]


Changes to base API convenience methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Web3.toDecimal()
````````````````

In v4 ``Web3.toDecimal()`` is renamed: :meth:`~Web3.toInt` for improved clarity. It does not return a :class:`decimal.Decimal`, it returns an :class:`int`.


Removed Methods
```````````````

- ``Web3.toUtf8`` was removed for :meth:`~Web3.toText`.
- ``Web3.fromUtf8`` was removed for :meth:`~Web3.toHex`.
- ``Web3.toAscii`` was removed for :meth:`~Web3.toBytes`.
- ``Web3.fromAscii`` was removed for :meth:`~Web3.toHex`.
- ``Web3.fromDecimal`` was removed for :meth:`~Web3.toHex`.

Provider Access
~~~~~~~~~~~~~~~~~

In v4, ``w3.currentProvider`` was removed, in favor of ``w3.providers``.

Disambiguating String Inputs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are a number of places where an arbitrary string input might be either
a byte-string that has been hex-encoded, or unicode characters in text.
These are named ``hexstr`` and ``text`` in Web3.py.
You specify which kind of :class:`str` you have by using the appropriate
keyword argument. See examples in :ref:`overview_type_conversions`.

In v3, some methods accepted a :class:`str` as the first positional argument.
In v4, you must pass strings as one of ``hexstr`` or ``text`` keyword arguments.

Notable methods that no longer accept ambiguous strings:

- :meth:`~Web3.sha3`
- :meth:`~Web3.toBytes`

Contracts
~~~~~~~~~

- When a contract returns the ABI type ``string``, Web3.py v4 now returns a :class:`str`
  value by decoding the underlying bytes using UTF-8.
- When a contract returns the ABI type ``bytes`` (of any length),
  Web3.py v4 now returns a :class:`bytes` value

Personal API
~~~~~~~~~~~~

``w3.personal.signAndSendTransaction`` is no longer available. Use
:meth:`w3.personal.sendTransaction() <web3.personal.sendTransaction>` instead.
