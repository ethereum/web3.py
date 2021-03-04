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

Ethereum Addresses
------------------

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

Types by Example
----------------

Let's use a contrived contract to demonstrate input types in Web3.py:

.. code-block:: none

   contract ManyTypes {
       // booleans
       bool public b;

       // unsigned ints
       uint8 public u8;
       uint256 public u256;
       uint256[] public u256s;

       // signed ints
       int8 public i8;

       // addresses
       address public addr;
       address[] public addrs;

       // bytes
       bytes1 public b1;

       // structs
       struct S {
         address sa;
         bytes32 sb;
       }
       mapping(address => S) addrStructs;

       function updateBool(bool x) public { b = x; }
       function updateUint8(uint8 x) public { u8 = x; }
       function updateUint256(uint256 x) public { u256 = x; }
       function updateUintArray(uint256[] memory x) public { u256s = x; }
       function updateInt8(int8 x) public { i8 = x; }
       function updateAddr(address x) public { addr = x; }
       function updateBytes1(bytes1 x) public { b1 = x; }
       function updateMapping(S memory x) public { addrStructs[x.sa] = x; }
   }

Booleans
________

.. code-block:: python

   contract_instance.functions.updateBool(True).transact()

Unsigned Integers
_________________

.. code-block:: python

   contract_instance.functions.updateUint8(255).transact()
   contract_instance.functions.updateUint256(2**256 - 1).transact()
   contract_instance.functions.updateUintArray([1, 2, 3]).transact()

Signed Integers
_______________

.. code-block:: python

   contract_instance.functions.updateInt8(-128).transact()

Addresses
_________

.. code-block:: python

   contract_instance.functions.updateAddr("0x0000000000000000000000000000000000000000").transact()

Bytes
_____

.. code-block:: python

   contract_instance.functions.updateBytes1(HexBytes(255)).transact()

Structs
_______

.. code-block:: python

   contract_instance.functions.updateMapping({"sa": "0x0000000000000000000000000000000000000000", "sb": HexBytes(123)}).transact()
