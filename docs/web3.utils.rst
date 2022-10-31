Utils
=====

.. py:module:: web3.utils

The ``utils`` module houses public utility functions and classes.

ABI
---

.. py:method:: utils.get_abi_input_names(abi)

    Return the ``input`` names for an ABI function or event.


.. py:method:: utils.get_abi_output_names(abi)

    Return the ``output`` names an ABI function or event.


Caching
-------

.. py:class:: utils.SimpleCache

    The main cache class being used internally by web3.py. In some cases, it may prove
    useful to set your own cache size and pass in your own instance of this class where
    supported.


Exception Handling
------------------

.. py:method:: utils.handle_offchain_lookup(offchain_lookup_payload, transaction)

    Handle ``OffchainLookup`` reverts on contract function calls manually. For an example, see :ref:`ccip-read-example`
    within the examples section.


.. py:method:: utils.async_handle_offchain_lookup(offchain_lookup_payload, transaction)

    The async version of the ``handle_offchain_lookup()`` utility method described above.
