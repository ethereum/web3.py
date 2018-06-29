Conventions
===========

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
