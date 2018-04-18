Miner API
=========

.. py:module:: web3.miner

.. py:class:: Miner

The ``web3.miner`` object exposes methods to interact with the RPC APIs under
the ``miner_`` namespace.


Properties
----------

The following properties are available on the ``web3.miner`` namespace.

.. py:attribute:: Miner.hashrate

    * Delegates to ``eth_hashrate`` RPC Method

    Returns the current number of hashes per second the node is mining with.

    .. code-block:: python

        >>> web3.eth.hashrate
        906


    .. note:: This property is an alias to ``web3.eth.hashrate``.


Methods
-------

The following methods are available on the ``web3.miner`` namespace.


.. py:method:: Miner.makeDAG(number)

    * Delegates to ``miner_makeDag`` RPC Method

    Generate the DAG for the given block number.

    .. code-block:: python

        >>> web3.miner.makeDag(10000)


.. py:method:: Miner.setExtra(extra)

    * Delegates to ``miner_setExtra`` RPC Method

    Set the 32 byte value ``extra`` as the extra data that will be included
    when this node mines a block.

    .. code-block:: python

        >>> web3.miner.setExtra('abcdefghijklmnopqrstuvwxyzABCDEF')


.. py:method:: Miner.setGasPrice(gas_price)

    * Delegates to ``miner_setGasPrice`` RPC Method

    Sets the minimum accepted gas price that this node will accept when mining
    transactions.  Any transactions with a gas price below this value will be
    ignored.

    .. code-block:: python

        >>> web3.miner.setGasPrice(19999999999)


.. py:method:: Miner.start(num_threads)

    * Delegates to ``miner_start`` RPC Method

    Start the CPU mining process using the given number of threads.

    .. code-block:: python

        >>> web3.miner.start(2)


.. py:method:: Miner.stop()

    * Delegates to ``miner_stop`` RPC Method

    Stop the CPU mining operation

    .. code-block:: python

        >>> web3.miner.stop()


.. py:method:: Miner.startAutoDAG()

    * Delegates to ``miner_startAutoDag`` RPC Method

    Enable automatic DAG generation.

    .. code-block:: python

        >>> web3.miner.startAutoDAG()


.. py:method:: Miner.stopAutoDAG()

    * Delegates to ``miner_stopAutoDag`` RPC Method

    Disable automatic DAG generation.

    .. code-block:: python

        >>> web3.miner.stopAutoDAG()
