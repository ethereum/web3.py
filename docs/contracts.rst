Contracts
=========

.. py:module:: web3.contract
.. py:currentmodule:: web3.contract


Contract Factories
------------------

.. py:class:: Contract(abi, address=None, code=None, code_runtime=None, source=None)

    The ``Contract`` class is not intended to be used or instantiated directly.
    Instead you should use the ``web3.eth.contract(...)`` method to generate
    the contract factory classes for your contracts.

    Contract Factories provide an interface for deploying and interacting with
    Ethereum smart contracts.


Properties
----------

    Each Contract Factory exposes the following properties.


.. py:attribute:: Contract.address

    The hexidecimal encoded 20 byte address of the contract.


.. py:attribute:: Contract.abi

    The contract ABI array.


.. py:attribute:: Contract.code

    The contract bytecode string.


.. py:attribute:: Contract.code_runtime

    The runtime part of the contract bytecode string.
