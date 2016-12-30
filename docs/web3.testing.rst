Testing API
===========

.. py:module:: web3.testing
.. py:currentmodule:: web3.testing

.. py:class:: Testing

The ``web3.testing`` object exposes methods to interact with non-standard RPC
APIs that are only available under the python ``eth-testrpc`` package.


Methods
-------

The following methods are available on the ``web3.testing`` namespace.


.. py:method:: Testing.timeTravel(timestamp)

    * Delegates to ``testing_timeTravel`` RPC Method

    Advances the test blockchain one block setting the new block's timestamp to
    the provided integer timestamp.


.. py:method:: Testing.mine(num_blocks=1)

    * Delegates to ``evm_mine`` RPC Method

    Mines ``num_blocks`` new blocks.


.. py:method:: Testing.snapshot()

    * Delegates to ``evm_snapshot`` RPC Method

    Takes a snapshot of the current EVM state and returns an integer that can
    be used with the ``revert`` method to restore the EVM to this state.


.. py:method:: Testing.revert(snapshot_idx=None)

    * Delegates to ``evm_revert`` RPC Method

    If no ``snapshot_idx`` is provided this will revert the EVM to the most
    recent snapshot.  Otherwise reverts the EVM to the snapshot indicated by
    the provided ``snapshot_idx``


.. py:method:: Testing.reset()

    * Delegates to ``evm_reset`` RPC Method

    Reset the EVM back to the genesis state.
