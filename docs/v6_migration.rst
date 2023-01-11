.. _migrating_v5_to_v6:

Migrating your code from v5 to v6
=================================

Web3.py follows `Semantic Versioning <http://semver.org>`_, which means
that version 6 introduced backwards-incompatible changes. If your
project depends on Web3.py v6, then you'll probably need to make some changes.

Breaking Changes:

Snake Case
~~~~~~~~~~

Web3.py v6 moved to the more Pythonic convention of snake_casing wherever
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

In v5, some Web3.py exceptions inherited from ``AttributeError``, namely:

- ``NoABIFunctionsFound``
- ``NoABIFound``
- ``NoABIEventsFound``

Others inherited from ValueError, namely:

- ``InvalidAddress``
- ``NameNotFound``
- ``LogTopicError``
- ``InvalidEventABI``

Now Web3.py exceptions inherit from the same base ``Web3Exception``.

As such, any code that was expecting a ``ValueError`` or an ``AttributeError`` from
Web3.py must update to expecting one of the exception listed above, or
``Web3Exception``.

Similarly, exceptions raised in the EthPM and ENS modules inherit from the base
``PyEthPMException`` and ``ENSException``, respectively.

Other Changes
-------------

- ``InfuraKeyNotFound`` exception has been changed to ``InfuraProjectIdNotFound``
- ``SolidityError`` has been removed in favor of ``ContractLogicError``

Removals
~~~~~~~~

- Removed unused IBAN module
- Removed ``WEB3_INFURA_API_KEY`` environment variable in favor of ``WEB3_INFURA_PROJECT_ID``
- Removed Kovan auto provider
- Removed deprecated ``sha3`` and ``soliditySha3`` methods in favor of ``keccak`` and ``solidityKeccak``
- Remove Parity Module and References


Other notable changes
~~~~~~~~~~~~~~~~~~~~~

- The ipfshttpclient library is now opt-in via a web3 install extra.
  This only affects the ethpm ipfs backends, which rely on the library.
