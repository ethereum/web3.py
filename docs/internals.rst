Web3 Internals
==============


.. warning:: This section of the documentation is for advanced users.  You should probably stay away from these APIs if you don't know what you are doing.

The Web3 library has multiple layers of abstraction betwwen the public api
exposed by the web3 object and the backend or node that web3 is connecting to.

* **Providers** are responsible for the actual communication with the
  blockchain such as sending JSON-RPC requests over HTTP or an IPC socket.
* **Middlewares** provide a hooks for monitoring and modifying requests and
  responses to and from the provider.
* **Managers** provide thread safety and primatives to allow for asyncronous usage of web3.

Here are some common things you might want to do with these APIs.

* Redirect certain RPC requests to different providers such as sending all
  *read* operations to a provider backed by Infura and all *write* operations
  to a go-ethereum node that you control.
* Transparently intercept transactions sent over ``eth_sendTransaction``, sign
  them locally, and then send them through ``eth_sendRawTransaction``.
* Modify the response from an RPC request so that it is returned in different
  format such as converting all integer values to their hexidecimal
  representation.
* Validate the inputs to RPC requests


Request Lifecycle
-----------------

Each web3 RPC call passes through these layers in the following manner.

.. code-block::

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
                 |     First  Middleware       |
                 +-----------------------------+
                       |                ^
                       v                |
                 +-----------------------------+
                 |             ...             |
                 +-----------------------------+
                       |                ^
                       v                |
                 +-----------------------------+
                 |      Last  Middleware       |
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
in-memory EVM to fulfil requests.

Web3 ships with the following providers which are appropriate for connecting to
local and remote JSON-RPC servers.


HTTPProvider
~~~~~~~~~~~~

.. py:class:: web3.providers.rpc.HTTPProvider(endpoint_uri[, request_kwargs])

    This provider handles interactions with an HTTP or HTTPS based JSON-RPC server.

    * ``endpoint_uri`` should be the full URI to the RPC endpoint such as
      ``'https://localhost:8545'``.  For RPC servers behind HTTP connections
      running on port 80 and HTTPS connections running on port 443 the port can
      be omitted from the URI.
    * ``request_kwargs`` this should be a dictionary of keyword arguments which
      will be passed onto the http/https request.

    .. code-block:: python

        >>> from web3 import Web3
        >>> web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545")

    Under the hood, the ``HTTPProvider`` uses the python requests library for
    making requests.  If you would like to modify how requests are made, you can
    use the ``request_kwargs`` to do so.  A common use case for this is increasing
    the timeout for each request.


    .. code-block:: python

        >>> from web3 import Web3
        >>> web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545", request_kwargs={'timeout': 60})


IPCProvider
~~~~~~~~~~~

.. py:class:: IPCProvider(ipc_path=None, testnet=False):

    This provider handles interaction with an IPC Socket based JSON-RPC
    server.

    *  ``ipc_path`` is the filesystem path to the IPC socket.:56

    .. code-block:: python

        >>> from web3 import Web3
        >>> web3 = Web3(Web3.IPCProvider("~/Library/Ethereum/geth.ipc")


.. py:currentmodule:: web3.providers.tester


EthereumTesterProvider
~~~~~~~~~~~~~~~~~~~~~~

.. warning:: Pending Deprecation:  This provider is being deprecated soon in favor of the newly created ethereum-tester library.

.. py:class:: EthereumTesterProvider():

    This provider can be used for testing.  It uses an ephemeral blockchain
    backed by the ``ethereum.tester`` module.


TestRPCProvider
~~~~~~~~~~~~~~~

.. warning:: Pending Deprecation:  This provider is being deprecated soon in favor of the newly created ethereum-tester library.

.. py:class:: TestRPCProvider():

    This provider can be used for testing.  It uses an ephemeral blockchain
    backed by the ``ethereum.tester`` module.  This provider will be slower
    than the ``EthereumTesterProvider`` since it uses an HTTP server for RPC
    interactions with.


Writing your own Provider
~~~~~~~~~~~~~~~~~~~~~~~~~

Writing your own provider requires implemented two required methods as well as
setting the middlewares the provider should use.


.. py:method:: BaseProvider.make_request(method, params)

    Each provider class **must** implement this method.  This method **should**
    return a JSON object with either a ``'result'`` key in the case of success,
    or an ``'error'`` key in the case of failure.


    * ``method``  This will be a string representing the JSON-RPC method that
      is being called such as ``'eth_sendTransaction'``.
    * ``params``  This will be a list or other iterable of the parameters for
      the JSON-RPC method being called.


.. py:method:: BaseProvider.isConnected()

    This function should return ``True`` or ``False`` depending on whether the
    provider should be considered *connected*.  For example, an IPC socket
    based provider should return ``True`` if the socket is open and ``False``
    if the socket is closed.


Setting middlewares is done one of two ways.

* Set the ``middleware_classes`` property to an iterable of classes that
  implement the middleware API.
* Implement a ``get_middleware_classes()`` method which returns an iterable of
  classes that implement the middleware API.



Middlewares
-----------

Middlewares provide a simple yet powerful api for implementing layers of
business logic for web3 requests.  Each middleware class **may** implement
any of the following APIs.

.. py:class:: BaseMiddleware.process_request(method, params, request_id)

    This will be called prior to issuing the request to the provider.  This
    method **must** return a 2-tuple of ``(method, params)``.  Each middleware
    is free to modify these parameters in any way.

    The ``request_id`` argument is a unique identifier for this request which
    can be used by any middleware which needs to maintain state between the
    request and response.


.. py:class:: BaseMiddleware.process_result(result, request_id)

    In the case that the Provider request is successful, this will be called
    with the value from the ``'result'`` key from the Provider response.

    The ``request_id`` argument is the same as from the ``process_request`` API.


.. py:class:: BaseMiddleware.process_error(error, request_id)

    In the case that the Provider request fails, this will be called
    with the value from the ``'error'`` key from the Provider response.

    The ``request_id`` argument is the same as from the ``process_request`` API.


.. py:property:: BaseMiddleware.provider

    Each middleware has access to the Provider that will ultimately handle the
    request.


Managers
--------

The Manager acts as a gatekeeper for the request/response lifecycle.  It is
unlikely that you will need to change the Manager as most functionality can be
implemented in the Middleware layer.
