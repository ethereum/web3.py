.. _web3_base:

Web3 API
========

.. contents:: :local:

.. py:module:: web3
.. py:currentmodule:: web3


.. py:class:: Web3(provider)

Each ``web3`` instance exposes the following APIs.

Providers
~~~~~~~~~

.. py:attribute:: Web3.HTTPProvider

    Convenience API to access :py:class:`web3.providers.rpc.HTTPProvider`

.. py:attribute:: Web3.IPCProvider

    Convenience API to access :py:class:`web3.providers.ipc.IPCProvider`


Attributes
~~~~~~~~~~

.. py:attribute:: Web3.api

    Returns the current Web3 version.

    .. code-block:: python
     
       >>> web3.api
       "4.7.0"

.. py:attribute:: Web3.clientVersion

    * Delegates to ``web3_clientVersion`` RPC Method

    Returns the current client version.

    .. code-block:: python

       >>> web3.clientVersion
       'Geth/v1.4.11-stable-fed692f6/darwin/go1.7'


.. _overview_type_conversions:

Encoding and Decoding Helpers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

.. py:method:: Web3.toJSON(obj)

    Takes a variety of inputs and returns its JSON equivalent.


    .. code-block:: python

        >>> Web3.toJSON(3)
        '3'
        >>> Web3.toJSON({'one': 1})
        '{"one": 1}'


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

        >>> Web3.fromWei(1000000000000000000, 'ether')
        Decimal('1')


.. _overview_addresses:

Addresses
~~~~~~~~~

.. py:method:: Web3.isAddress(value)

    Returns ``True`` if the value is one of the recognized address formats.

    * Allows for both ``0x`` prefixed and non-prefixed values.
    * If the address contains mixed upper and lower cased characters this function also
      checks if the address checksum is valid according to `EIP55`_

    .. code-block:: python

        >>> Web3.isAddress('0xd3CdA913deB6f67967B99D67aCDFa1712C293601')
        True


.. py:method:: Web3.isChecksumAddress(value)

    Returns ``True`` if the value is a valid `EIP55`_ checksummed address


    .. code-block:: python

        >>> Web3.isChecksumAddress('0xd3CdA913deB6f67967B99D67aCDFa1712C293601')
        True
        >>> Web3.isChecksumAddress('0xd3cda913deb6f67967b99d67acdfa1712c293601')
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

.. py:classmethod:: Web3.keccak(primitive=None, hexstr=None, text=None)

    Returns the Keccak-256 of the given value. Text is encoded to UTF-8 before
    computing the hash, just like Solidity. Any of the following are
    valid and equivalent:

    .. code-block:: python

        >>> Web3.keccak(0x747874)
        >>> Web3.keccak(b'\x74\x78\x74')
        >>> Web3.keccak(hexstr='0x747874')
        >>> Web3.keccak(hexstr='747874')
        >>> Web3.keccak(text='txt')
        HexBytes('0xd7278090a36507640ea6b7a0034b69b0d240766fa3f98e3722be93c613b29d2e')

.. py:classmethod:: Web3.solidityKeccak(abi_types, value)

    Returns the Keccak-256 as it would be computed by the solidity ``keccak``
    function on the provided ``value`` and ``abi_types``.  The ``abi_types``
    value should be a list of solidity type strings which correspond to each
    of the provided values.


    .. code-block:: python

        >>> Web3.solidityKeccak(['bool'], [True])
        HexBytes("0x5fe7f977e71dba2ea1a68e21057beebb9be2ac30c6410aa38d4f3fbe41dcffd2")

        >>> Web3.solidityKeccak(['uint8', 'uint8', 'uint8'], [97, 98, 99])
        HexBytes("0x4e03657aea45a94fc7d47ba826c8d667c0d1e6e33a64a036ec44f58fa12d6c45")

        >>> Web3.solidityKeccak(['uint8[]'], [[97, 98, 99]])
        HexBytes("0x233002c671295529bcc50b76a2ef2b0de2dac2d93945fca745255de1a9e4017e")

        >>> Web3.solidityKeccak(['address'], ["0x49EdDD3769c0712032808D86597B84ac5c2F5614"])
        HexBytes("0x2ff37b5607484cd4eecf6d13292e22bd6e5401eaffcc07e279583bc742c68882")

        >>> Web3.solidityKeccak(['address'], ["ethereumfoundation.eth"])
        HexBytes("0x913c99ea930c78868f1535d34cd705ab85929b2eaaf70fcd09677ecd6e5d75e9")

.. py:classmethod:: Web3.sha3(primitive=None, hexstr=None, text=None)

    .. WARNING::
      This method has been deprecated for :meth:`~Web3.keccak`

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

    .. WARNING::
      This method has been deprecated for :meth:`~Web3.solidityKeccak`


    Returns the sha3 as it would be computed by the solidity ``sha3`` function
    on the provided ``value`` and ``abi_types``.  The ``abi_types`` value
    should be a list of solidity type strings which correspond to each of the
    provided values.


    .. code-block:: python

        >>> Web3.soliditySha3(['bool'], [True])
        HexBytes("0x5fe7f977e71dba2ea1a68e21057beebb9be2ac30c6410aa38d4f3fbe41dcffd2")

        >>> Web3.soliditySha3(['uint8', 'uint8', 'uint8'], [97, 98, 99])
        HexBytes("0x4e03657aea45a94fc7d47ba826c8d667c0d1e6e33a64a036ec44f58fa12d6c45")

        >>> Web3.soliditySha3(['uint8[]'], [[97, 98, 99]])
        HexBytes("0x233002c671295529bcc50b76a2ef2b0de2dac2d93945fca745255de1a9e4017e")

        >>> Web3.soliditySha3(['address'], ["0x49EdDD3769c0712032808D86597B84ac5c2F5614"])
        HexBytes("0x2ff37b5607484cd4eecf6d13292e22bd6e5401eaffcc07e279583bc742c68882")

        >>> Web3.soliditySha3(['address'], ["ethereumfoundation.eth"])
        HexBytes("0x913c99ea930c78868f1535d34cd705ab85929b2eaaf70fcd09677ecd6e5d75e9")


Check Encodability
~~~~~~~~~~~~~~~~~~~~

.. py:method:: w3.is_encodable(_type, value)

  Returns ``True`` if a value can be encoded as the given type. Otherwise returns ``False``.

   .. code-block:: python

        >>> from web3.auto.gethdev import w3
        >>> w3.is_encodable('bytes2', b'12')
        True
        >>> w3.is_encodable('bytes2', b'1')
        True
        >>> w3.is_encodable('bytes2', '0x1234')
        True
        >>> w3.is_encodable('bytes2', b'123')
        False

.. py:method:: w3.enable_strict_bytes_type_checking()

   Enables stricter bytes type checking. For more examples see :ref:`enable-strict-byte-check`

    .. doctest::

        >>> from web3.auto.gethdev import w3
        >>> w3.enable_strict_bytes_type_checking()
        >>> w3.is_encodable('bytes2', b'12')
        True
        >>> w3.is_encodable('bytes2', b'1')
        False


RPC APIS
~~~~~~~~

Each ``web3`` instance also exposes these namespaced APIs.


.. py:attribute:: Web3.eth

    See :doc:`./web3.eth`

.. py:attribute:: Web3.miner

    See :doc:`./web3.miner`

.. py:attribute:: Web3.pm

    See :doc:`./web3.pm`

.. py:attribute:: Web3.geth

    See :doc:`./web3.geth`

.. py:attribute:: Web3.parity

    See :doc:`./web3.parity`
