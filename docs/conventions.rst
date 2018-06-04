Conventions
===========

The Web3 library follows the following conventions.

Bytes vs Text
-------------

* The term *bytes* is used to refer to the binary representation of a string.
* The term *text* is used to refer to unicode representations of strings.

Hexidecimal Representations
---------------------------

* All hexidecimal values will be returned as text.
* All hexidecimal values will be ``0x`` prefixed.

Addresses
---------

All addresses must be supplied in one of two ways:

* A 20-byte hexidecimal that is checksummed using the `EIP-55
  <https://github.com/ethereum/EIPs/blob/master/EIPS/eip-55.md>`_ spec.
* An Ethereum Name Service name (often in the form ``myname.eth``)
