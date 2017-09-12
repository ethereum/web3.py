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

The ``HTTPProvider`` takes the full URI where the server can be found.  For
local development this would be something like ``http://localhost:8545``.

The ``IPCProvider`` takes the filesystem path where the IPC socket can be
found.  If no argument is provided it will use the *default* path for your
operating system.


.. code-block:: python

    >>> from web3 import Web3, HTTPProvider, IPCProvider

    # Note that you should create only one RPCProvider per
    # process, as it recycles underlying TCP/IP network connections between
    # your process and Ethereum node
    >>> web3 = Web3(HTTPProvider('http://localhost:8545'))

    # or for an IPC based connection
    >>> web3 = Web3(IPCProvider())


Base API
--------

The ``web3`` object itself exposes the following convenience APIs.


.. py:method:: Web3.toHex(value)

    Takes a string or numeric value and returns it in its hexidecimal representation.


    .. code-block:: python

        >>> web3.toHex(0)
        '0x0'
        >>> web3.toHex(1)
        '0x1'
        >>> web3.toHex('abcd')
        '0x61626364'


.. py:method:: Web3.toAscii(value)

    Takes a hexidecimal encoded string and returns its ascii equivalent.


    .. code-block:: python

        >>> web3.toAscii('0x61626364')
        b'abcd'


.. py:method:: Web3.toUtf8(value)

    Takes a hexidecimal encoded string and returns the UTF8 encoded equivalent.


    .. code-block:: python

        >>> web3.toUtf8('0x61626364')
        'abcd'


.. py:method:: Web3.fromAscii(value)

    Takes an ascii string and returns it in its hexidecimal representation


    .. code-block:: python

        >>> web3.fromAscii(b'abcd')
        '0x61626364'


.. py:method:: Web3.fromUtf8(value)

    Takes a utf8 encoded string and returns it in its hexidecimal representation


    .. code-block:: python

        >>> web3.fromUtf8('abcd')
        '0x61626364'


.. py:method:: Web3.toDecimal(value)

    Takes a hexidecimal encoded value and returns its numeric representation.


    .. code-block:: python

        >>> web3.toDecimal('0x1')
        1
        >>> web3.toDecimal('0xf')
        15


.. py:method:: Web3.fromDecimal(value)

    Takes a numeric value and returns its hexidecimal equivalent.


    .. code-block:: python

        >>> web3.fromDecimal(1)
        '0x1'
        >>> web3.fromDecimal(15)
        '0xf'


.. py:method:: Web3.toWei(value, currency)

    Returns the value in the denomination specified by the ``currency`` argument
    converted to wei.


    .. code-block:: python

        >>> web3.toWei(1, 'ether')
        1000000000000000000


.. py:method:: Web3.fromWei(value, currency)

    Returns the value in wei converted to the given currency.


    .. code-block:: python

        >>> web3.fromWei(1000000000000000000, 'ether')
        1


.. py:method:: Web3.isAddress(value)

    Returns ``True`` if the value is one of the recognized address formats.


    .. code-block:: python

        >>> web3.isAddress('0xd3CDA913deB6f67967B99D67aCDFa1712C293601')
        True


.. py:method:: Web3.isChecksumAddress(value)

    Returns ``True`` if the value is a valid ERC55 checksummed address


    .. code-block:: python

        >>> web3.isChecksumAddress('0xd3CDA913deB6f67967B99D67aCDFa1712C293601')
        True
        >>> web3.isChecksumAddress('0xd3cda913deb6f67967b99d67acdfa1712c293601')
        False


.. py:method:: Web3.toChecksumAddress(value)

    Returns the given address with an ERC55 checksum.


    .. code-block:: python

        >>> web3.toChecksumAddress('0xd3cda913deb6f67967b99d67acdfa1712c293601')
        '0xd3CDA913deB6f67967B99D67aCDFa1712C293601'


.. py:method:: Web3.sha3(primitive=None, hexstr=None, text=None)

    Returns the Keccak SHA256 of the given value. Text is encoded to UTF-8 before
    computing the hash, just like Solidity. Any of the following are
    valid and equivalent:

    .. code-block:: python

        web3.sha3(0x747874)
        web3.sha3(b'\x74\x78\x74')
        web3.sha3(hexstr='0x747874')
        web3.sha3(hexstr='747874')
        web3.sha3(text='txt')

.. py:method:: Web3.soliditySha3(abi_types, value)

    Returns the sha3 as it would be computed by the solidity ``sha3`` function
    on the provided ``value`` and ``abi_types``.  The ``abi_types`` value
    should be a list of solidity type strings which correspond to each of the
    provided values.


    .. code-block:: python

        >>> web3.soliditySha3(['bool'], True)
        "0x5fe7f977e71dba2ea1a68e21057beebb9be2ac30c6410aa38d4f3fbe41dcffd2"
        >>> web3.soliditySha3(['uint8', 'uint8', 'uint8'], [97, 98, 99])
        "0x4e03657aea45a94fc7d47ba826c8d667c0d1e6e33a64a036ec44f58fa12d6c45"
        >>> web3.soliditySha3(['address'], ["0x49eddd3769c0712032808d86597b84ac5c2f5614"])
        "0x2ff37b5607484cd4eecf6d13292e22bd6e5401eaffcc07e279583bc742c68882"


Modules
-------

The JSON-RPC functionality is split across multiple modules which *loosely*
correspond to the namespaces of the underlying JSON-RPC methods.
