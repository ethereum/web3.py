Web3 API
========

.. contents:: :local:

.. py:module:: web3
.. py:currentmodule:: web3


.. py:class:: Web3(provider)

Each ``web3`` instance exposes the following APIs.

Providers
~~~~~~~~~

.. py:attribute:: Web3.RPCProvider

    Convenience API to access :py:class:`web3.providers.rpc.RPCProvider`

.. py:attribute:: Web3.KeepAliveRPCProvider

    Convenience API to access :py:class:`web3.providers.rpc.KeepAliveRPCProvider`

.. py:attribute:: Web3.IPCProvider

    Convenience API to access :py:class:`web3.providers.rpc.IPCProvider`

.. py:attribute:: Web3.TestRPCProvider

    Convenience API to access :py:class:`web3.providers.rpc.TestRPCProvider`

.. py:method:: Web3.setProvider(provider)

    Updates the current web3 instance with the new provider.

.. py:method:: Web3.sha3(value, encoding='hex')

    Returns the Keccak Sha3 of the given value.


Encoding and Decoding Helpers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. py:staticmethod:: Web3.toHex(value)

    Returns the unpadded hexidecimal representation for the given
    ``value``.  This function supports the following types.

    * Booleans: Returns ``0x0`` or ``0x1``
    * Strings: Returns the string bytes in their hexidecimal representation.
    * Integers: Returns the integer value in it's hexidecimal representation.
    * Dictionaries: Returns the hexidecimal representation of the
      dictionary converted to a JSON string.

.. py:staticmethod:: Web3.toAscii(hex_value)

    Takes a hexidecimal value and returns it in its bytes representation.
    
.. py:staticmethod:: Web3.toUtf8(value)

    Takes a hexidecimal value and returns it in its text representation.

.. py:staticmethod:: Web3.fromAscii(value)

    Takes a byte string and returns its hexidecimal representation.

.. py:staticmethod:: Web3.fromUtf8(value)

    Takes a text string and returns its hexidecimal representation.

.. py:staticmethod:: Web3.toDecimal(value)

    Takes a hexidecimal value and returns it as its integer representation.

.. py:staticmethod:: Web3.fromDecimal(value)

    Takes an integer value and returns its hexidecimal representation.


Currency Converstions
~~~~~~~~~~~~~~~~~~~~~

.. py:staticmethod:: Web3.toWei(value, unit)

    Takes a value in the given ``unit`` and returns it converted to Wei.

.. py:staticmethod:: Web3.fromWei(value, unit)

    Takes a value in Wei and converts it to the given unit.

    .. note::
    
        The return type of this function is a very high precision
        ``decimal.Decimal`` value to ensure there are no rounding errors.


Addresses
~~~~~~~~~

.. py:staticmethod:: Web3.isAddress(value)

    Return boolean indicating whether the value passed in is a valid
    hexidecimal encoded Ethereum address.

    * Allows for both ``0x`` prefixed and non-prefixed values.
    * If the address contains mixed upper and lower cased characters this function also checks if the the address checksum is valid according to `EIP55`_

    
.. py:staticmethod:: Web3.isChecksumAddress(address)

    Returns boolean as to whether the given address is checksummed according to
    `EIP55`_

.. py:staticmethod:: Web3.toChecksumAddress(address)

    Returns the given address checksummed according to `EIP55`_


RPC APIS
--------

Each ``web3`` instance also exposes these namespaced APIs.



.. py:attribute:: Web3.eth

    See :doc:`./web3.eth`

.. py:attribute:: Web3.shh

    See :doc:`./web3.shh`

.. py:attribute:: Web3.personal

    See :doc:`./web3.personal`

.. py:attribute:: Web3.version

    See :doc:`./web3.version`

.. py:attribute:: Web3.txpool

    See :doc:`./web3.txpool`

.. py:attribute:: Web3.miner

    See :doc:`./web3.miner`

.. py:attribute:: Web3.admin

    See :doc:`./web3.admin`


.. _EIP55: https://github.com/ethereum/EIPs/issues/55
