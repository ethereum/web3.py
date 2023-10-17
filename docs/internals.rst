Web3 Internals
==============


.. warning:: This section of the documentation is for advanced users.  You should probably stay away from these APIs if you don't know what you are doing.

The Web3 library has multiple layers of abstraction between the public api
exposed by the web3 object and the backend or node that web3 is connecting to.

* **Providers** are responsible for the actual communication with the
  blockchain such as sending JSON-RPC requests over HTTP or an IPC socket.
* **Middlewares** provide hooks for monitoring and modifying requests and
  responses to and from the provider.  These can be *global* operating on all
  providers or specific to one provider.
* **Managers** provide thread safety and primitives to allow for asynchronous usage of web3.

Here are some common things you might want to do with these APIs.

* Redirect certain RPC requests to different providers such as sending all
  *read* operations to a provider backed by Infura and all *write* operations
  to a go-ethereum node that you control.
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
                 |            Manager          |
                 +-----------------------------+
                       |                ^
                       v                |
                 +-----------------------------+
                 |     Global Middlewares      |
                 +-----------------------------+
                       |                ^
                       v                |
                 +-----------------------------+
                 |    Provider Middlewares     |
                 +-----------------------------+
                       |                ^
                       v                |
                 +-----------------------------+
                 |          Provider           |
                 +-----------------------------+


You can visualize this relationship like an onion, with the Provider at the
center.  The request originates from the Manager, outside of the onion, passing
down through each layer of the onion until it reaches the Provider at the
center.  The Provider then handles the request, producing a response which will
then pass back out from the center of the onion, through each layer until it is
finally returned by the Manager.


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
setting the middlewares the provider should use.


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


.. py:attribute:: BaseProvider.middlewares

    This should be an iterable of middlewares.

You can set a new list of middlewares by assigning to ``provider.middlewares``,
with the first middleware that processes the request at the beginning of the list.


.. _internals__middlewares:

Middlewares
-----------

.. note:: The Middleware API in web3 borrows heavily from the Django middleware API introduced in version 1.10.0

Middlewares provide a simple yet powerful api for implementing layers of
business logic for web3 requests.  Writing middleware is simple.

.. code-block:: python

    def simple_middleware(make_request, w3):
        # do one-time setup operations here

        def middleware(method, params):
            # do pre-processing here

            # perform the RPC request, getting the response
            response = make_request(method, params)

            # do post-processing here

            # finally return the response
            return response
        return middleware


It is also possible to implement middlewares as a class.


.. code-block:: python

    class SimpleMiddleware:
        def __init__(self, make_request, w3):
            self.w3 = w3
            self.make_request = make_request

        def __call__(self, method, params):
            # do pre-processing here

            # perform the RPC request, getting the response
            response = self.make_request(method, params)

            # do post-processing here

            # finally return the response
            return response


The ``make_request`` parameter is a callable which takes two
positional arguments, ``method`` and ``params`` which correspond to the RPC
method that is being called.  There is no requirement that the ``make_request``
function be called.  For example, if you were writing a middleware which cached
responses for certain methods your middleware would likely not call the
``make_request`` method, but instead get the response from some local cache.

The ``RequestManager`` object exposes the ``middleware_onion`` object to manage middlewares. It
is also exposed on the ``Web3`` object for convenience. That API is detailed in
:ref:`Modifying_Middleware`.


Managers
--------

The Manager acts as a gatekeeper for the request/response lifecycle.  It is
unlikely that you will need to change the Manager as most functionality can be
implemented in the Middleware layer.


Request Processing for Persistent Connection Providers
------------------------------------------------------

.. py:class:: web3.providers.websocket.request_processor.RequestProcessor

The ``RequestProcessor`` class is responsible for the storing and syncing up of
asynchronous requests to responses for a ``PersistentConnectionProvider``. The best
example of one such provider is the
:class:`~web3.providers.websocket.WebsocketProviderV2`. In order to send a websocket
message and receive a response to that particular request,
``PersistentConnectionProvider`` instances have to match request *id* values to
response *id* values coming back from the websocket connection. Any provider that does
not adhere to the `JSON-RPC 2.0 specification <https://www.jsonrpc.org/specification>`_
in this way will not work with ``PersistentConnectionProvider`` instances. The specifics
of how the request processor handles this are outlined below.

One-To-One Requests
~~~~~~~~~~~~~~~~~~~

One-to-one requests can be summarized as any request that expects only one response
back. An example is using the ``eth`` module API to request the latest block number.

.. code-block:: python

    >>> async def wsV2_one_to_one_example():
    ...     async with AsyncWeb3.persistent_websocket(
    ...         WebsocketProviderV2(f"ws://127.0.0.1:8546")
    ...     ) as w3:
    ...         # make a request and expect a single response returned on the same line
    ...         latest_block_num = await w3.eth.block_number

    >>> asyncio.run(wsV2_one_to_one_example())

With websockets we have to call ``send()`` and asynchronously receive responses via
``recv()``. In order to make the one-to-one request-to-response call work, we
have to save the request information somewhere so that when the response is received
we can match it to the original request that was made i.e. the request with a matching
*id* to the response that was received). The stored request information is then used to
process the response when it is received, piping it through the response formatters and
middlewares internal to the *web3.py* library.

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
cycle within a ``while`` loop, alternating between checking this cache (in case
somewhere else in the code our desired response was cached by another call) and calling
``recv()`` on the websocket connection to see if it is yet to come.

One-To-Many Requests
~~~~~~~~~~~~~~~~~~~~

One-to-many requests can be summarized by any request that expects many responses as a
result of the initial request. An example is the ``eth_subscribe`` request. The initial
``eth_subscribe`` request expects only one response, the subscription *id* value, but
it also expects to receive many ``eth_subscription`` messages if and when the request is
successful. For this reason, the original request is considered a one-to-one request
so that a subscription *id* can be returned to the user on the same line, but the
``listen_to_websocket()`` method on the
:class:`~web3.providers.websocket.WebsocketConnection` class, the public API for
interacting with the active websocket connection, is set up to receive
``eth_subscription`` responses over an asynchronous interator pattern.

.. code-block:: python

    >>> async def ws_v2_subscription_example():
    ...     async with AsyncWeb3.persistent_websocket(
    ...         WebsocketProviderV2(f"ws://127.0.0.1:8546")
    ...     ) as w3:
    ...         # Subscribe to new block headers and receive the subscription_id.
    ...         # A one-to-one call with a trigger for many responses
    ...         subscription_id = await w3.eth.subscribe("newHeads")
    ...
    ...         # Listen to the websocket for the many responses utilizing the ``w3.ws``
    ...         # ``WebsocketConnection`` public API method ``listen_to_websocket()``
    ...         async for response in w3.ws.listen_to_websocket():
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

    >>> asyncio.run(ws_v2_subscription_example())

One-to-many responses, those that do not include a JSON-RPC *id* in the response object,
are stored in an internal ``collections.deque`` instance, isolated from any one-to-one
responses. When the ``PersistentConnectionProvider`` is looking for a one-to-many
response internally, it will cycle within a ``while`` loop, alternating between
checking this deque (in case somewhere else in the code, subscriptions responses were
put in the deque by another call looking for another response type) and calling
``recv()`` on the websocket connection to see if the response is yet to be received.
With each iteration on this iterator, if the ``deque`` is non-empty, it will yield
messages from the ``deque`` as FIFO order until the deque is empty before receiving any
new messages from the websocket connection, guaranteeing the messages are yielded in the
order they were received.
