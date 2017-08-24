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


.. method:: Web3.toHex(value)

Takes a string or numeric value and returns it in its hexidecimal representation.


.. code-block:: python

    >>> x.toHex(0)
    '0x0'
    >>> x.toHex(1)
    '0x1'
    >>> x.toHex('abcd')
    '0x61626364'


.. method:: Web3.toAscii(value)

Takes a hexidecimal encoded string and returns its ascii equivalent.


.. code-block:: python

    >>> x.toAscii('0x61626364)
    b'abcd'


.. method:: Web3.toUtf8(value)

Takes a hexidecimal encoded string and returns the UTF8 encoded equivalent.


.. code-block:: python

    >>> x.toUtf8('0x61626364)
    'abcd'


.. method:: Web3.fromAscii(value)

Takes an ascii string and returns it in its hexidecimal representation


.. code-block:: python

    >>> x.fromAscii(b'abcd')
    '0x61626364'


.. method:: Web3.fromUtf8(value)

Takes a utf8 encoded string and returns it in its hexidecimal representation


.. code-block:: python

    >>> x.fromUtf8('abcd')
    '0x61626364'


.. method:: Web3.toDecimal(value)

Takes a hexidecimal encoded value and returns its numeric representation.


.. code-block:: python

    >>> x.toDecimal('0x1')
    1
    >>> x.toDecimal('0xf')
    15


.. method:: Web3.fromDecimal(value)

Takes a numeric value and returns its hexidecimal equivalent.


.. code-block:: python

    >>> x.fromDecimal(1)
    '0x1'
    >>> x.fromDecimal(15)
    '0xf'


.. method:: Web3.toWei(value, currency)

Returns the value in the denomination specified by the ``currency`` argument
converted to wei.


.. code-block:: python

    >>> x.toWei(1, 'ether')
    1000000000000000000


.. method:: Web3.fromWei(value, currency)

Returns the value in wei converted to the given currency.


.. code-block:: python

    >>> x.fromWei(1000000000000000000, 'ether')
    1


.. method:: Web3.isAddress(value)

Returns ``True`` if the value is one of the recognized address formats.


.. code-block:: python

    >>> x.isAddress('0xd3CDA913deB6f67967B99D67aCDFa1712C293601')
    True


.. method:: Web3.isChecksumAddress(value)

Returns ``True`` if the value is a valid ERC55 checksummed address


.. code-block:: python

    >>> x.isChecksumAddress('0xd3CDA913deB6f67967B99D67aCDFa1712C293601')
    True
    >>> x.isChecksumAddress('0xd3cda913deb6f67967b99d67acdfa1712c293601')
    False


.. method:: Web3.toChecksumAddress(value)

Returns the given address with an ERC55 checksum.


.. code-block:: python

    >>> x.toChecksumAddress('0xd3cda913deb6f67967b99d67acdfa1712c293601')
    '0xd3CDA913deB6f67967B99D67aCDFa1712C293601'


Modules
-------

The JSON-RPC functionality is split across multiple modules which *loosely*
correspond to the namespaces of the underlying JSON-RPC methods.
