.. _migrating_v5_to_v6:

Migrating your code from v5 to v6
=================================

web3.py follows `Semantic Versioning <http://semver.org>`_, which means
that version 6 introduced backwards-incompatible changes. If your
project depends on web3.py v6, then you'll probably need to make some changes.

Breaking Changes:

Strict Bytes Checking by Default
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

web3.py v6 moved to requiring strict bytes checking by default. This means that if an
ABI specifies a ``bytes4`` argument, web3.py will invalidate any entry that is not
encodable as a bytes type with length of 4. This means only 0x-prefixed hex strings with
a length of 4 and bytes types with a length of 4 will be considered valid. This removes
doubt that comes from inferring values and assuming they should be padded.

This behavior was previously available in via the ``w3.enable_strict_bytes_checking()``
method. This is now, however, a toggleable flag on the ``Web3`` instance via the
``w3.strict_bytes_type_checking`` property. As outlined above, this property is set to
``True`` by default but can be toggled on and off via the property's setter
(e.g. ``w3.strict_bytes_type_checking = False``).


Snake Case
~~~~~~~~~~

web3.py v6 moved to the more Pythonic convention of snake_casing wherever
possible. There are some exceptions to this pattern:

- Contract methods and events use whatever is listed in the ABI. If the smart contract
  convention is to use camelCase for method and event names, web3.py won't do
  any magic to convert it to snake_casing.
- Arguments to JSON-RPC methods. For example: transaction and filter
  parameters still use camelCasing. The reason for
  this is primarily due to error messaging. It would be confusing to pass in a
  snake_cased parameter and get an error message with a camelCased parameter.
- Data that is returned from JSON-RPC methods. For example:
  The keys in a transaction receipt will still be returned as camelCase.


Python 3.10 and 3.11 Support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Support for Python 3.10 and 3.11 is here. In order to support Python 3.10, we had to
update the Websockets dependency to v10+.

Exceptions
~~~~~~~~~~

Exceptions inherit from a base class
------------------------------------

In v5, some web3.py exceptions inherited from ``AttributeError``, namely:

- ``NoABIFunctionsFound``
- ``NoABIFound``
- ``NoABIEventsFound``

Others inherited from ``ValueError``, namely:

- ``InvalidAddress``
- ``NameNotFound``
- ``LogTopicError``
- ``InvalidEventABI``

Now web3.py exceptions inherit from the same base ``Web3Exception``.

As such, any code that was expecting a ``ValueError`` or an ``AttributeError`` from
web3.py must update to expecting one of the exceptions listed above, or
``Web3Exception``.

Similarly, exceptions raised in the EthPM and ENS modules inherit from the base
``EthPMException`` and ``ENSException``, respectively.

ValidationError
---------------

The Python dev tooling ecosystem is moving towards standardizing
``ValidationError``, so users know that they're catching the correct
``ValidationError``. The base ``ValidationError`` is imported from
``eth_utils``. However, we also wanted to empower users to catch all errors emitted
by a particular module. So we now have a ``Web3ValidationError``, ``EthPMValidationError``,
and an ``ENSValidationError`` that all inherit from the generic
``eth_utils.exceptions.ValidationError``.

Other Misc Changes
------------------

- ``InfuraKeyNotFound`` exception has been changed to ``InfuraProjectIdNotFound``
- ``SolidityError`` has been removed in favor of ``ContractLogicError``
- When a method is unavailable from a node provider (i.e. a response error
  code of -32601 is returned), a ``MethodUnavailable`` error is
  now raised instead of ``ValueError``

Removals
~~~~~~~~

- Removed unused IBAN module
- Removed ``WEB3_INFURA_API_KEY`` environment variable in favor of ``WEB3_INFURA_PROJECT_ID``
- Removed Kovan auto provider
- Removed deprecated ``sha3`` and ``soliditySha3`` methods in favor of ``keccak`` and ``solidityKeccak``
- Remove Parity Module and References


Other notable changes
~~~~~~~~~~~~~~~~~~~~~

- The ``ipfshttpclient`` library is now opt-in via a web3 install extra.
  This only affects the ethpm ipfs backends, which rely on the library.
