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

* Any hexidecimal address with at least one capitalized letter will be validated using the EIP55 checksum spec.
