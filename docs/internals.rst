Web3 Internals
==============


.. warning:: This section of the documentation is for advanced users.  You should probably stay away from these APIs if you don't know what you are doing.

The Web3 library has multiple layers of abstraction between the public api
exposed by the web3 object and the backend or node that web3 is connecting to.

* **Providers** are responsible for the actual communication with the
  blockchain such as sending JSON-RPC requests over HTTP or an IPC socket.
* **Middleware** provide hooks for monitoring and modifying requests and
  responses to and from the provider.
* **Managers** provide thread safety and primitives to allow for asynchronous usage of web3.

Here are some common things you might want to do with these APIs.

* Redirect certain RPC requests to different providers such as sending all
  *read* operations to a provider backed by a remote node and all *write* operations
  to a local node that you control.
* Transparently intercept transactions sent over ``eth_sendTransaction``, sign
  them locally, and then send them through ``eth_sendRawTransaction``.
* Modify the response from an RPC request so that it is returned in different
  format such as converting all integer values to their hexadecimal
  representation.
* Validate the inputs to RPC requests


Request Lifecycle
-----------------

Each web3 RPC call passes through these layers in the following manner.

.. code-block:: none

                   ***********    ************
                   | Request |    | Response |
                   ***********    ************
                       |                ^
                       v                |
                 +-----------------------------+
                 |           Manager           |
                 +-----------------------------+
                       |                ^
                       v                |
                 +-----------------------------+
                 |         Middleware          |
                 +-----------------------------+
                       |                ^
                       v                |
                 +-----------------------------+
                 |          Provider           |
                 +-----------------------------+


You can visualize this relationship like an onion, with the Provider at the
center. The request originates from the ``Manager``, outside of the onion, passing
down through each layer of the onion until it reaches the ``Provider`` at the
center. The ``Provider`` then handles the request, producing a response which will
then pass back out from the center of the onion, through each layer until it is
finally returned by the ``Manager``.


Providers
---------

A provider is responsible for all direct blockchain interactions.  In most
cases this means interacting with the JSON-RPC server for an ethereum node over
HTTP or an IPC socket.  There is however nothing which requires providers to be
RPC based, allowing for providers designed for testing purposes which use an
in-memory EVM to fulfill requests.


Writing your own Provider
~~~~~~~~~~~~~~~~~~~~~~~~~

Writing your own provider requires implementing two required methods as well as
setting the middleware the provider should use.


.. py:method:: BaseProvider.make_request(method, params)

    Each provider class **must** implement this method.  This method **should**
    return a JSON object with either a ``'result'`` key in the case of success,
    or an ``'error'`` key in the case of failure.


    * ``method``  This will be a string representing the JSON-RPC method that
      is being called such as ``'eth_sendTransaction'``.
    * ``params``  This will be a list or other iterable of the parameters for
      the JSON-RPC method being called.


.. py:method:: BaseProvider.is_connected(show_traceback=False)

    This function should return ``True`` or ``False`` depending on whether the
    provider should be considered *connected*.  For example, an IPC socket
    based provider should return ``True`` if the socket is open and ``False``
    if the socket is closed.

    If set to ``True``, the optional ``show_traceback`` boolean will raise a
    ``ProviderConnectionError`` and provide information on why the provider should
    not be considered *connected*.


.. py:attribute:: BaseProvider.middleware

    This should be an iterable of middleware.

You can set a new list of middleware by assigning to ``provider.middleware``,
with the first middleware that processes the request at the beginning of the list.


Provider Configurations
~~~~~~~~~~~~~~~~~~~~~~~

.. _request_caching:

Request Caching
```````````````

Request caching can be configured at the provider level via the following configuration
options on the provider instance:

- ``cache_allowed_requests: bool = False``
- ``cacheable_requests: Set[RPCEndpoint] = CACHEABLE_REQUESTS``

.. code-block:: python

    from web3 import Web3, HTTPProvider

    w3 = Web3(HTTPProvider(
        endpoint_uri="...",

        # optional flag to turn on cached requests, defaults to False
        cache_allowed_requests=True,

        # optional, defaults to an internal list of deemed-safe-to-cache endpoints
        cacheable_requests={"eth_chainId", "eth_getBlockByNumber"},
    ))

.. _http_retry_requests:

Retry Requests for HTTP Providers
`````````````````````````````````

``HTTPProvider`` and ``AsyncHTTPProvider`` instances retry certain requests by default
on exceptions. This can be configured via configuration options on the provider
instance. The retry mechanism employs an exponential backoff strategy, starting from
the initial value determined by the ``backoff_factor``, and doubling the delay with
each attempt, up to the ``retries`` value. Below is an example showing the default
options for the retry configuration and how to override them.

.. code-block:: python

    from web3 import Web3, HTTPProvider
    from web3.providers.rpc.utils import (
        REQUEST_RETRY_ALLOWLIST,
        ExceptionRetryConfiguration,
    )

    w3 = Web3(HTTPProvider(
        endpoint_uri="...",
        exception_retry_configuration=ExceptionRetryConfiguration(
            errors=DEFAULT_EXCEPTIONS,

            # number of retries to attempt
            retries=5,

            # initial delay multiplier, doubles with each retry attempt
            backoff_factor=0.125,

            # an in-house default list of retryable methods
            method_allowlist=REQUEST_RETRY_ALLOWLIST,
        ),
    ))

For the different http providers, ``DEFAULT_EXCEPTIONS`` is defined as:

- ``HTTPProvider``: ``(ConnectionError, requests.HTTPError, requests.Timeout)``
- ``AsyncHTTPProvider``: ``(ConnectionError, aiohttp.ClientError, asyncio.TimeoutError)``

Setting ``retry_configuration`` to ``None`` will disable retries on exceptions for the
provider instance.

.. code-block:: python

    from web3 import Web3, HTTPProvider

    w3 = Web3(HTTPProvider(endpoint_uri="...", retry_configuration=None)



Managers
--------

The Manager acts as a gatekeeper for the request/response lifecycle.  It is
unlikely that you will need to change the Manager as most functionality can be
implemented in the Middleware layer.

.. _internals__persistent_connection_providers:

Request Processing for Persistent Connection Providers
------------------------------------------------------

.. py:class:: web3.providers.persistent.request_processor.RequestProcessor

The ``RequestProcessor`` class is responsible for the storing and syncing up of
asynchronous requests to responses for a ``PersistentConnectionProvider``. The
:class:`~web3.providers.persistent.WebSocketProvider` and the
:class:`~web3.providers.persistent.AsyncIPCProvider` are two persistent connection
providers. In order to send a request and receive a response to that same request,
``PersistentConnectionProvider`` instances have to match request *id* values to
response *id* values coming back from the socket connection. Any provider that does
not adhere to the `JSON-RPC 2.0 specification <https://www.jsonrpc.org/specification>`_
in this way will not work with ``PersistentConnectionProvider`` instances. The specifics
of how the request processor handles this are outlined below.

Listening for Responses
~~~~~~~~~~~~~~~~~~~~~~~

Implementations of the ``PersistentConnectionProvider`` class have a message listener
background task that is called when the socket connection is established. This task
is responsible for listening for any and all messages coming in over the socket
connection and storing them in the ``RequestProcessor`` instance internal to the
``PersistentConnectionProvider`` instance. The ``RequestProcessor`` instance is
responsible for storing the messages in the correct cache, either the one-to-one cache
or the one-to-many (subscriptions) queue, depending on whether the message has a
JSON-RPC *id* value or not.


One-To-One Requests
~~~~~~~~~~~~~~~~~~~

One-to-one requests can be summarized as any request that expects only one response
back. An example is using the ``eth`` module API to request the latest block number.

.. code-block:: python

    >>> async def ws_one_to_one_example():
    ...     async with AsyncWeb3(WebSocketProvider(f"ws://127.0.0.1:8546")) as w3:
    ...         # make a request and expect a single response returned on the same line
    ...         latest_block_num = await w3.eth.block_number

    >>> asyncio.run(ws_one_to_one_example())

With persistent socket connections, we have to call ``send()`` and asynchronously
receive responses via another means, generally by calling ``recv()`` or by iterating
on the socket connection for messages. As outlined above, the
``PersistentConnectionProvider`` class has a message listener background task that
handles the receiving of messages.

Due to this asynchronous nature of sending and receiving, in order to make one-to-one
request-to-response calls work, we have to save the request information somewhere so
that, when the response is received, we can match it to the original request that was
made (i.e. the request with a matching *id* to the response that was received). The
stored request information is then used to process the response when it is received,
piping it through the response formatters and middleware internal to the *web3.py*
library.

In order to store the request information, the ``RequestProcessor`` class has an
internal ``RequestInformation`` cache. The ``RequestInformation`` class saves important
information about a request.

.. py:class:: web3._utils.caching.RequestInformation

    .. py:attribute:: method

        The name of the method - e.g. "eth_subscribe".

    .. py:attribute:: params

        The params used when the call was made - e.g. ("newPendingTransactions", True).

    .. py:attribute:: response_formatters

        The formatters that will be used to process the response.

    .. py:attribute:: middleware_response_processors

        Any middleware that processes responses that is present on the instance at the
        time of the request is appended here, in order, so the response may be piped
        through that logic when it comes in.

    .. py:attribute:: subscription_id

        If the request is an ``eth_subscribe`` request, rather than
        popping this information from the cache when the response to the subscription call
        comes in (i.e. the subscription *id*), we save the subscription id with the
        request information so that we can correctly process all subscription messages
        that come in with that subscription *id*. For one-to-one request-to-response
        calls, this value is always ``None``.

One-to-one responses, those that include a JSON-RPC *id* in the response object, are
stored in an internal ``SimpleCache`` class, isolated from any one-to-many responses.
When the ``PersistentConnectionProvider`` is looking for a response internally, it will
expect the message listener task to store the response in this cache. Since the request
*id* is used in the cache key generation, it will then look for a cache key that matches
the response *id* with that of the request *id*. If the cache key is found, the response
is processed and returned to the user. If the cache key is not found, the operation will
time out and raise a ``TimeExhausted`` exception. This timeout can be configured by the
user when instantiating the ``PersistentConnectionProvider`` instance via the
``response_timeout`` keyword argument.

One-To-Many Requests
~~~~~~~~~~~~~~~~~~~~

One-to-many requests can be summarized by any request that expects many responses as a
result of the initial request. The only current example is the ``eth_subscribe``
request. The initial ``eth_subscribe`` request expects only one response, the
subscription *id* value, but it also expects to receive many ``eth_subscription``
messages if and when the request is successful. For this reason, the original request
is considered a one-to-one request so that a subscription *id* can be returned to the
user on the same line, but the ``process_subscriptions()`` method on the
:class:`~web3.providers.persistent.PersistentConnection` class, the public API for
interacting with the active persistent socket connection, is set up to receive
``eth_subscription`` responses over an asynchronous interator pattern.

.. code-block:: python

    >>> async def ws_subscription_example():
    ...     async with AsyncWeb3(WebSocketProvider(f"ws://127.0.0.1:8546")) as w3:
    ...         # Subscribe to new block headers and receive the subscription_id.
    ...         # A one-to-one call with a trigger for many responses
    ...         subscription_id = await w3.eth.subscribe("newHeads")
    ...
    ...         # Listen to the socket for the many responses utilizing the
    ...         # ``w3.socket`` ``PersistentConnection`` public API method
    ...         # ``process_subscriptions()``
    ...         async for response in w3.socket.process_subscriptions():
    ...             # Receive only one-to-many responses here so that we don't
    ...             # accidentally return the response for a one-to-one request in this
    ...             # block
    ...
    ...             print(f"{response}\n")
    ...
    ...             if some_condition:
    ...                 # unsubscribe from new block headers, another one-to-one request
    ...                 is_unsubscribed = await w3.eth.unsubscribe(subscription_id)
    ...                 if is_unsubscribed:
    ...                     break

    >>> asyncio.run(ws_subscription_example())

One-to-many responses, those that do not include a JSON-RPC *id* in the response object,
are stored in an internal ``asyncio.Queue`` instance, isolated from any one-to-one
responses. When the ``PersistentConnectionProvider`` is looking for one-to-many
responses internally, it will expect the message listener task to store these messages
in this queue. Since the order of the messages is important, the queue is a FIFO queue.
The ``process_subscriptions()`` method on the ``PersistentConnection`` class is set up
to pop messages from this queue as FIFO over an asynchronous iterator pattern.

If the stream of messages from the socket is not being interrupted by any other
tasks, the queue will generally be in sync with the messages coming in over the
socket. That is, the message listener will put a message in the queue and the
``process_subscriptions()`` method will pop that message from the queue and yield
control of the loop back to the listener. This will continue until the socket
connection is closed or the user unsubscribes from the subscription. If the stream of
messages lags a bit, or the provider is not consuming messages but has subscribed to
a subscription, this internal queue may fill up with messages until it reaches its max
size and then trigger a waiting ``asyncio.Event`` until the provider begins consuming
messages from the queue again. For this reason, it's important to begin consuming
messages from the queue, via the ``process_subscriptions()`` method, as soon as a
subscription is made.
