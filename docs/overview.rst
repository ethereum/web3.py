Overview
========

.. contents:: :local:

The common entrypoint for interacting with the Web3 library is the ``Web3``
object.  The web3 object provides APIs for interacting with the ethereum
blockchain, typically by connecting to a JSON-RPC server.


Providers
---------

*Providers* are how web3 connects to the blockchain.  The Web3 library comes
with a the following built-in providers that should be suitable for most normal
use cases.

- ``web3.HTTPProvider`` for connecting to http and https based JSON-RPC servers.
- ``web3.IPCProvider`` for connecting to ipc socket based JSON-RPC servers.
- ``web3.WebsocketProvider`` for connecting to ws and wss websocket based JSON-RPC servers.

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
    >>> web3 = Web3(HTTPProvider('http://localhost:8545'))

    # or for an IPC based connection
    >>> web3 = Web3(IPCProvider())

    # or for Websocket based connection
    >>> web3 = Web3(WebsocketProvider('ws://127.0.0.1:8546'))


Base API
--------

The ``Web3`` class exposes the following convenience APIs.


.. _overview_type_conversions:

Type Conversions
~~~~~~~~~~~~~~~~

.. py:method:: Web3.toHex(primitive=None, hexstr=None, text=None)

    Takes a variety of inputs and returns it in its hexadecimal representation.
    It follows the rules for converting to hex in the
    `JSON-RPC spec`_

    .. code-block:: python

        >>> Web3.toHex(0)
        '0x0'
        >>> Web3.toHex(1)
        '0x1'
        >>> Web3.toHex(0x0)
        '0x0'
        >>> Web3.toHex(0x000F)
        '0xf'
        >>> Web3.toHex(b'')
        '0x'
        >>> Web3.toHex(b'\x00\x0F')
        '0x000f'
        >>> Web3.toHex(False)
        '0x0'
        >>> Web3.toHex(True)
        '0x1'
        >>> Web3.toHex(hexstr='0x000F')
        '0x000f'
        >>> Web3.toHex(hexstr='000F')
        '0x000f'
        >>> Web3.toHex(text='')
        '0x'
        >>> Web3.toHex(text='cowmö')
        '0x636f776dc3b6'

.. _JSON-RPC spec: https://github.com/ethereum/wiki/wiki/JSON-RPC#hex-value-encoding

.. py:method:: Web3.toText(primitive=None, hexstr=None, text=None)

    Takes a variety of inputs and returns its string equivalent.
    Text gets decoded as UTF-8.


    .. code-block:: python

        >>> Web3.toText(0x636f776dc3b6)
        'cowmö'
        >>> Web3.toText(b'cowm\xc3\xb6')
        'cowmö'
        >>> Web3.toText(hexstr='0x636f776dc3b6')
        'cowmö'
        >>> Web3.toText(hexstr='636f776dc3b6')
        'cowmö'
        >>> Web3.toText(text='cowmö')
        'cowmö'


.. py:method:: Web3.toBytes(primitive=None, hexstr=None, text=None)

    Takes a variety of inputs and returns its bytes equivalent.
    Text gets encoded as UTF-8.


    .. code-block:: python

        >>> Web3.toBytes(0)
        b'\x00'
        >>> Web3.toBytes(0x000F)
        b'\x0f'
        >>> Web3.toBytes(b'')
        b''
        >>> Web3.toBytes(b'\x00\x0F')
        b'\x00\x0f'
        >>> Web3.toBytes(False)
        b'\x00'
        >>> Web3.toBytes(True)
        b'\x01'
        >>> Web3.toBytes(hexstr='0x000F')
        b'\x00\x0f'
        >>> Web3.toBytes(hexstr='000F')
        b'\x00\x0f'
        >>> Web3.toBytes(text='')
        b''
        >>> Web3.toBytes(text='cowmö')
        b'cowm\xc3\xb6'


.. py:method:: Web3.toInt(primitive=None, hexstr=None, text=None)

    Takes a variety of inputs and returns its integer equivalent.


    .. code-block:: python

        >>> Web3.toInt(0)
        0
        >>> Web3.toInt(0x000F)
        15
        >>> Web3.toInt(b'\x00\x0F')
        15
        >>> Web3.toInt(False)
        0
        >>> Web3.toInt(True)
        1
        >>> Web3.toInt(hexstr='0x000F')
        15
        >>> Web3.toInt(hexstr='000F')
        15

.. _overview_currency_conversions:

Currency Conversions
~~~~~~~~~~~~~~~~~~~~~

.. py:method:: Web3.toWei(value, currency)

    Returns the value in the denomination specified by the ``currency`` argument
    converted to wei.


    .. code-block:: python

        >>> Web3.toWei(1, 'ether')
        1000000000000000000


.. py:method:: Web3.fromWei(value, currency)

    Returns the value in wei converted to the given currency. The value is returned
    as a ``Decimal`` to ensure precision down to the wei.


    .. code-block:: python

        >>> web3.fromWei(1000000000000000000, 'ether')
        Decimal('1')


.. _overview_addresses:

Addresses
~~~~~~~~~~~~~~~~

.. py:method:: Web3.isAddress(value)

    Returns ``True`` if the value is one of the recognized address formats.

    * Allows for both ``0x`` prefixed and non-prefixed values.
    * If the address contains mixed upper and lower cased characters this function also
      checks if the address checksum is valid according to `EIP55`_

    .. code-block:: python

        >>> web3.isAddress('0xd3CdA913deB6f67967B99D67aCDFa1712C293601')
        True


.. py:method:: Web3.isChecksumAddress(value)

    Returns ``True`` if the value is a valid `EIP55`_ checksummed address


    .. code-block:: python

        >>> web3.isChecksumAddress('0xd3CdA913deB6f67967B99D67aCDFa1712C293601')
        True
        >>> web3.isChecksumAddress('0xd3cda913deb6f67967b99d67acdfa1712c293601')
        False


.. py:method:: Web3.toChecksumAddress(value)

    Returns the given address with an `EIP55`_ checksum.


    .. code-block:: python

        >>> Web3.toChecksumAddress('0xd3cda913deb6f67967b99d67acdfa1712c293601')
        '0xd3CdA913deB6f67967B99D67aCDFa1712C293601'

.. _EIP55: https://github.com/ethereum/EIPs/issues/55


.. _overview_hashing:

Cryptographic Hashing
~~~~~~~~~~~~~~~~~~~~~

.. py:classmethod:: Web3.sha3(primitive=None, hexstr=None, text=None)

    Returns the Keccak SHA256 of the given value. Text is encoded to UTF-8 before
    computing the hash, just like Solidity. Any of the following are
    valid and equivalent:

    .. code-block:: python

        >>> Web3.sha3(0x747874)
        >>> Web3.sha3(b'\x74\x78\x74')
        >>> Web3.sha3(hexstr='0x747874')
        >>> Web3.sha3(hexstr='747874')
        >>> Web3.sha3(text='txt')
        HexBytes('0xd7278090a36507640ea6b7a0034b69b0d240766fa3f98e3722be93c613b29d2e')

.. py:classmethod:: Web3.soliditySha3(abi_types, value)

    Returns the sha3 as it would be computed by the solidity ``sha3`` function
    on the provided ``value`` and ``abi_types``.  The ``abi_types`` value
    should be a list of solidity type strings which correspond to each of the
    provided values.


    .. code-block:: python

        >>> Web3.soliditySha3(['bool'], True)
        HexBytes("0x5fe7f977e71dba2ea1a68e21057beebb9be2ac30c6410aa38d4f3fbe41dcffd2")

        >>> Web3.soliditySha3(['uint8', 'uint8', 'uint8'], [97, 98, 99])
        HexBytes("0x4e03657aea45a94fc7d47ba826c8d667c0d1e6e33a64a036ec44f58fa12d6c45")

        >>> Web3.soliditySha3(['uint8[]'], [[97, 98, 99]])
        HexBytes("0x233002c671295529bcc50b76a2ef2b0de2dac2d93945fca745255de1a9e4017e")

        >>> Web3.soliditySha3(['address'], ["0x49eddd3769c0712032808d86597b84ac5c2f5614"])
        HexBytes("0x2ff37b5607484cd4eecf6d13292e22bd6e5401eaffcc07e279583bc742c68882")

        >>> Web3.soliditySha3(['address'], ["ethereumfoundation.eth"])
        HexBytes("0x913c99ea930c78868f1535d34cd705ab85929b2eaaf70fcd09677ecd6e5d75e9")

Modules
-------

The JSON-RPC functionality is split across multiple modules which *loosely*
correspond to the namespaces of the underlying JSON-RPC methods.
