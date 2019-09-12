ABI Types
=========

The Web3 library follows the following conventions.

Bytes vs Text
-------------

* The term *bytes* is used to refer to the binary representation of a string.
* The term *text* is used to refer to unicode representations of strings.

Hexadecimal Representations
---------------------------

* All hexadecimal values will be returned as text.
* All hexadecimal values will be ``0x`` prefixed.

Addresses
---------

All addresses must be supplied in one of three ways:

* While connected to mainnet, an Ethereum Name Service name (often in the form ``myname.eth``)
* A 20-byte hexadecimal that is checksummed using the `EIP-55
  <https://github.com/ethereum/EIPs/blob/master/EIPS/eip-55.md>`_ spec.
* A 20-byte binary address.

Strict Bytes Type Checking
--------------------------

.. note ::

  In version 6, this will be the default behavior

There is a method on web3 that will enable stricter bytes type checking.
The default is to allow Python strings, and to allow bytestrings less
than the specified byte size. To enable stricter checks, use
``w3.enable_strict_bytes_type_checking()``. This method will cause the web3
instance to raise an error if a Python string is passed in without a "0x"
prefix. It will also raise an error if the byte string or hex string is not
the exact number of bytes specified by the ABI type. See the
:ref:`enable-strict-byte-check` section
for an example and more details.
