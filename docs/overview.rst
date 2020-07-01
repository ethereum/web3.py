Overview
========

.. contents:: :local:

The common entrypoint for interacting with the Web3 library is the ``Web3``
object.  The web3 object provides APIs for interacting with the ethereum
blockchain, typically by connecting to a JSON-RPC server.


Providers
---------

*Providers* are how web3 connects to the blockchain.  The Web3 library comes
with the following built-in providers that should be suitable for most normal
use cases.

- ``Web3.HTTPProvider`` for connecting to http and https based JSON-RPC servers.
- ``Web3.IPCProvider`` for connecting to ipc socket based JSON-RPC servers.
- ``Web3.WebsocketProvider`` for connecting to ws and wss websocket based JSON-RPC servers.

The ``HTTPProvider`` takes the full URI where the server can be found.  For
local development this would be something like ``http://localhost:8545``.

The ``IPCProvider`` takes the filesystem path where the IPC socket can be
found.  If no argument is provided it will use the *default* path for your
operating system.

The ``WebsocketProvider`` takes the full URI where the server can be found.  For
local development this would be something like ``ws://127.0.0.1:8546``.

.. code-block:: python

    >>> from web3 import Web3, HTTPProvider, IPCProvider, WebsocketProvider

    # Note that you should create only one RPCProvider per
    # process, as it recycles underlying TCP/IP network connections between
    # your process and Ethereum node
    >>> w3 = Web3(HTTPProvider('http://localhost:8545'))

    # or for an IPC based connection
    >>> w3 = Web3(IPCProvider())

    # or for Websocket based connection
    >>> w3 = Web3(WebsocketProvider('ws://127.0.0.1:8546'))


Base API
--------

The ``Web3`` class exposes the following convenient APIs.
