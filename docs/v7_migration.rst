.. _migrating_v6_to_v7:

Migrating your code from v6 to v7
=================================

web3.py follows `Semantic Versioning <http://semver.org>`_, which means that
version 7 introduced backwards-incompatible changes. If you're upgrading from
web3.py ``v6`` or earlier, you can expect to need to make some changes. Refer
to this guide for a summary of breaking changes when updating from ``v6`` to
``v7``. If you are more than one major version behind, you should also review
the migration guides for the versions in between.


Provider Updates
~~~~~~~~~~~~~~~~


WebSocketProvider
`````````````````

``WebsocketProviderV2``, introduced in web3.py ``v6``, has taken priority over the
legacy ``WebsocketProvider``. The ``LegacyWebSocketProvider`` has been deprecated in
``v7`` and is slated for removal in the next major version of the library. In summary:

- ``WebsocketProvider`` -> ``LegacyWebSocketProvider`` (and deprecated)
- ``WebsocketProviderV2`` -> ``WebSocketProvider``

If migrating from ``WebSocketProviderV2`` to ``WebSocketProvider``, you can expect the
following changes:

- Instantiation no longer requires the ``persistant_websocket`` method:

  .. code-block:: python

      # WebsocketsProviderV2:
      AsyncWeb3.persistent_websocket(WebsocketProviderV2('...'))

      # WebSocketProvider:
      AsyncWeb3(WebSocketProvider('...'))

- Handling incoming subscription messages now occurs under a more flexible namespace:
  ``socket``. The ``AsyncIPCProvider`` uses the same API to listen for messages via
  an IPC socket.

  .. code-block:: python

    # WebsocketsProviderV2:
    async for message in w3.ws.process_subscriptions():
      ...

    # WebSocketProvider:
    async for message in w3.socket.process_subscriptions():
      ...


AsyncIPCProvider (non-breaking feature)
```````````````````````````````````````

An asynchronous IPC provider, ``AsyncIPCProvider``, is newly available in ``v7``.
This provider makes use of some of the same internals that the new ``WebSocketProvider``
introduced, allowing it to also support ``eth_subscription``.


EthereumTesterProvider
``````````````````````

``EthereumTesterProvider`` now returns ``input`` instead of ``data`` for ``eth_getTransaction*``
calls, as expected.


Middlewares -> Middleware
~~~~~~~~~~~~~~~~~~~~~~~~~

All references to ``middlewares`` have been replaced with the more grammatically
correct ``middleware``. Notably, this includes when a provider needs to be
instantiated with custom middleware.


Class-Based Middleware Model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The middleware model has been changed to a class-based model. Previously, middleware
were defined as functions that tightly wrapped the provider's ``make_request`` function,
where transformations could be conditionally applied before and after the request was made.

Now, middleware logic can be separated into ``request_processor`` and ``response_processor``
functions that enable pre-request and post-response logic, respectively. This change offers
a simpler, clearer interface for defining middleware, gives more flexibility for
asynchronous operations and also paves the way for supporting batch requests - included in
the roadmap for web3.py.

The new middleware model is documented in the :ref:`middleware_internals` section.


Middleware Renaming and Removals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following middleware have been renamed for generalization or clarity:

- ``name_to_address_middleware`` -> ``ENSNameToAddressMiddleware``
- ``geth_poa_middleware`` -> ``ExtraDataToPOAMiddleware``

The following middleware have been removed:


ABI Middleware
``````````````

``abi_middleware`` is no longer necessary and has been removed. All of the functionality
of the ``abi_middleware`` was already handled by web3.py's ABI formatters. For additional
context: a bug in the ENS name-to-address middleware would override the formatters. Fixing
this bug has removed the need for the ``abi_middleware``.


Caching Middleware
``````````````````

The following middleware have been removed:

- ``simple_cache_middleware``
- ``latest_block_based_cache_middleware``
- ``time_based_cache_middleware``

All caching middleware has been removed in favor of a decorator/wrapper around the
``make_request`` methods of providers with configuration options on the provider class.
The configuration options are outlined in the documentation in the
:ref:`request_caching` section.

If desired, the previous caching middleware can be re-created using the new class-based
middleware model overriding the ``wrap_make_request`` (or ``async_wrap_make_request``)
method in the middleware class.


Result Generating Middleware
````````````````````````````
The following middleware have been removed:

- ``fixture_middleware``
- ``result_generator_middleware``

The ``fixture_middleware`` and ``result_generator_middleware`` which were used for
testing/mocking purposes have been removed. These have been replaced internally by the
``RequestMocker`` class, utilized for testing via a ``request_mocker`` pytest fixture.


HTTP Retry Request Middleware
`````````````````````````````

The ``http_retry_request_middleware`` has been removed in favor of a configuration
option on the ``HTTPProvider`` and ``AsyncHTTPProvider`` classes. The configuration
options are outlined in the documentation in the :ref:`http_retry_requests` section.


Normalize Request Parameters Middleware
```````````````````````````````````````

The ``normalize_request_parameters`` middleware was not used anywhere internally and
has been removed.


Remaining camelCase -> snake_case Updates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following arguments have been renamed across the library from camelCase to
snake_case in all methods where they are passed in as a kwarg.

- ``fromBlock`` -> ``from_block``
- ``toBlock`` -> ``to_block``
- ``blockHash`` -> ``block_hash``

Note that if a dictionary is used instead, say to a call such as `eth_getLogs`, the
keys in the dictionary should be camelCase. This is because the dictionary is passed
directly to the JSON-RPC request, where the keys are expected to be in camelCase.


Changes to Exception Handling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All Python standard library exceptions that were raised from within web3.py have
been replaced with custom ``Web3Exception`` classes. This change allows for better
control over exception handling, being able to distinguish between exceptions raised
by web3.py and those raised from elsewhere in a codebase. The following exceptions
have been replaced:

- ``AssertionError`` -> ``Web3AssertionError``
- ``ValueError`` -> ``Web3ValueError``
- ``TypeError`` -> ``Web3TypeError``
- ``AttributeError`` -> ``Web3AttributeError``

A new ``MethodNotSupported`` exception is now raised when a method is not supported by
web3.py. This allows a user to distinguish between when a method is not available on
the current provider, ``MethodUnavailable``, and when a method is not supported by
web3.py under certain conditions, ``MethodNotSupported``.


JSON-RPC Error Handling
```````````````````````

Rather than a ``ValueError`` being replaced with a ``Web3ValueError`` when a JSON-RPC
response comes back with an ``error`` object, a new ``Web3RPCError`` exception is
now raised to provide more distinction for JSON-RPC error responses. Some previously
existing exceptions now extend from this class since they too are related to JSON-RPC
errors:

- ``MethodUnavailable``
- ``BlockNotFound``
- ``TransactionNotFound``
- ``TransactionIndexingInProgress``


End of Support and Feature Removals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python 3.7 Support Dropped
``````````````````````````

Python 3.7 support has been dropped in favor of Python 3.8+. Python 3.7 is no longer
supported by the Python core team, and we want to focus our efforts on supporting
the latest versions of Python.


EthPM Module Removed
````````````````````

The EthPM module has been removed from the library. It was not widely used and has not
been functional since around October 2022. It was deprecated in ``v6`` and has been
completely removed in ``v7``.


Geth Miner Namespace Removed
````````````````````````````

The ``geth.miner`` namespace, deprecated in ``v6``, has been removed in ``v7``.
The ``miner`` namespace was used for managing the concept of a miner in geth. This is
no longer a feature in geth and is planned for complete removal in the future, with
Ethereum having transitioned to proof-of-stake.


Geth Personal Namespace Removed
```````````````````````````````

The ``geth.personal`` namespace, deprecated in ``v6``, has been removed in ``v7``.
The ``personal`` namespace was used for managing accounts and keys and was deprecated
in geth in ``v1.11.0``. Geth has moved to using ``clef`` for account and key management.


Miscellaneous Changes
~~~~~~~~~~~~~~~~~~~~~

- ``LRU`` has been removed from the library and dependency on ``lru-dict`` library was
  dropped.
- ``CallOverride`` type was changed to ``StateOverride`` since more methods than
  ``eth_call`` utilize the state override params.
- ``User-Agent`` header was changed to a more readable format.
- ``BaseContractFunctions`` iterator now returns instances of ``ContractFunction`` rather
  than the function names.
- Beacon API filename change: ``beacon/main.py`` -> ``beacon/beacon.py``.
- The asynchronous version of ``w3.eth.wait_for_transaction_receipt()`` changes its
  signature to use ``Optional[float]`` instead of ``float`` since it may be ``None``.
- ``get_default_ipc_path()`` and ``get_dev_ipc_path()`` now return the path value
  without checking if the ``geth.ipc`` file exists.
- ``Web3.is_address()`` returns ``True`` for non-checksummed addresses.
- ``Contract.encodeABI()`` has been renamed to ``Contract.encode_abi()``.
- JSON-RPC responses are now more strictly validated against the JSON-RPC 2.0
  specification while providing more informative error messages for invalid responses.
