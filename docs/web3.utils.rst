Utils
=====

.. py:module:: web3.utils

The ``utils`` module houses public utility and helper functions.

ABI
---

.. py:method:: Utils.get_abi_input_names(abi)

    Return the ``input`` names for an ABI function or event.


.. py:method:: Utils.get_abi_output_names(abi)

    Return the ``output`` names an ABI function or event.


Exception Handling
------------------

.. py:method:: Utils.handle_offchain_lookup(offchain_lookup_payload, transaction)

    Handle ``OffchainLookup`` reverts on contract function calls manually. For an example, see :ref:`ccip-read-example`
    within the examples section.


.. py:method:: Utils.async_handle_offchain_lookup(offchain_lookup_payload, transaction)

    The async version of the ``handle_offchain_lookup()`` utility method described above.
