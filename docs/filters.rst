Filtering
=========


.. py:module:: web3.utils.filters


The :meth:`web3.eth.Eth.filter` method can be used to setup filter for:

* Pending Transactions
* New Blocks
* Event Logs


Filter API
----------

.. py:class:: Filter(web3, filter_id)

.. py:attribute:: Filter.filter_id

    The ``filter_id`` for this filter as returned by the ``eth_newFilter`` RPC
    method when this filter was created.


.. py:method:: Filter.get_new_entries()

    Retrieve new entries for this filter.

    Logs will be retrieved using the
    :func:`web3.eth.Eth.getFilterChanges` which returns only new entries since the last
    poll.


.. py:method:: Filter.get_all_entries()

    Retrieve all entries for this filter.

    Logs will be retrieved using the
    :func:`web3.eth.Eth.getFilterLogs` which returns all entries that match the given
    filter.


.. py:method:: Filter.format_entry(entry)

    Hook for subclasses to modify the format of the log entries this filter
    returns, or passes to it's callback functions.

    By default this returns the ``entry`` parameter umodified.


.. py:method:: Filter.is_valid_entry(entry)

    Hook for subclasses to add additional programatic filtering.  The default
    implementation always returns ``True``.


Block and Transaction Filters
-----------------------------

.. py:class:: BlockFilter(...)

    You can setup a filter for new blocks using ``web3.eth.filter('latest')`` which
    will return a new :py:class:`BlockFilter` object.

    .. code-block:: python

        >>> def new_block_callback(block_hash):
        ...     sys.stdout.write("New Block: {0}".format(block_hash))
        ...
        >>> new_block_filter = web3.eth.filter('latest')
        >>> new_block_filter.watch(new_block_callback)
        # each time the client receieves a new block the `new_block_callback`
        # function will be called with the block hash.


.. py:class:: TransactionFilter(...)

You can setup a filter for new blocks using ``web3.eth.filter('pending')`` which
will return a new :py:class:`BlockFilter` object.

    .. code-block:: python

        >>> def new_transaction_callback(transaction_hash):
        ...     sys.stdout.write("New Block: {0}".format(transaction_hash))
        ...
        >>> new_transaction_filter = web3.eth.filter('pending')
        >>> new_transaction_filter.watch(new_transaction_callback)
        # each time the client receieves a unmined transaction the
        # `new_transaction_filter` function will be called with the transaction
        # hash.


Event Log Filters
-----------------

.. py:class:: LogFilter(web3, filter_id, log_entry_formatter=None, data_filter_set=None)

The :py:class:`LogFilter` class is used for all filters pertaining to event
logs.  It exposes the following additional methods.


.. py:method:: LogFilter.get_new_entries()

    Retrieve new event logs for this filter.

    Logs will be retrieved using the
    :func:`web3.eth.Eth.getFilterChanges` which returns only new entries since the last
    poll.


.. py:method:: LogFilter.get_all_entries()

    Retrieve all event logs for this filter.

    Logs will be retrieved using the
    :func:`web3.eth.Eth.getFilterLogs` which returns all logs that match the given
    filter.


The :class:`LogFilter` class is returned from the
:func:`web3.contract.Contract.eventFilter` and will be configured to extract the
event data from the event logs.
