Utils
=====

.. py:module:: web3.utils

The ``utils`` module houses public utility and helper functions.


.. py:method:: Utils.handle_offchain_lookup(offchain_lookup_payload, transaction)

    Handle ``OffchainLookup`` reverts on contract function calls manually. For an example, see :ref:`ccip-read-example`
    within the examples section.


.. py:method:: Utils.async_handle_offchain_lookup(offchain_lookup_payload, transaction)

    The async version of the ``handle_offchain_lookup()`` utility method described above.
