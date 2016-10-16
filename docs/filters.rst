Filtering
=========

.. py:module:: web3.utils.filters
.. py:currentmodule:: web3.utils.filters


The ``web3.eth.filter`` method can be used to setup filter for:

* Pending Transactions
* New Blocks
* Event Logs


Filter API
----------

.. py:class:: Filter(web3, filter_id)

The :py:class::`Filter` object is a subclass of the
:py:class::`gevent.Greenlet` object.  It exposes these additional properties
and methods.


.. py:attribute:: Filter.filter_id

    The ``filter_id`` for this filter as returned by the ``eth_newFilter`` RPC
    method when this filter was created.


.. py:attribute:: Filter.callbacks

    A list of callbacks that this filter will call with new entries.


.. py:attribute:: Filter.running

    Boolean as to whether this filter is currently polling.


.. py:attribute:: Filter.stopped

    Boolean as to whether this filter has been stopped.  Will be set to
    ``None`` if the filter has not yet been started.


.. py:method:: Filter.format_entry(entry)

    Hook for subclasses to modify the format of the log entries this filter
    returns, or passes to it's callback functions.

    By default this returns the ``entry`` parameter umodified.


.. py:method:: Filter.is_valid_entry(entry)

    Hook for subclasses to add additional programatic filtering.  The default
    implementation always returns ``True``.


.. py:method:: Filter.watch(*callbacks)

    Registers the provided ``callbacks`` to be called with each new entry this
    filter encounters and starts the filter polling for changes.

    Can only be called once on each filter.  Cannot be called on a filter that
    has already been started.

.. py:method:: Filter.stop_watching(self, timeout=0)

    Stops the filter from polling and uninstalls the filter.  Blocks until all
    events that are currently being processed have been processed.


Block and Transaction Filters
-----------------------------

.. py:class:: BlockFilter(...)

    You can setup a filter for new blocks using ``web3.eth.filter('latest')`` which
    will return a new :py:class::`BlockFilter` object.

    .. code-block:: python

        >>> def new_block_callback(block_hash):
        ...     sys.stdout.write("New Block: {0}".format(block_hash))
        ...
        >>> new_block_filter = web3.eth.filter('latest')
        >>> new_block_filter.watch(new_block_filter)
        # each time the client receieves a new block the `new_block_callback`
        # function will be called with the block hash.


.. py:class:: TransactionFilter(...)

You can setup a filter for new blocks using ``web3.eth.filter('pending')`` which
will return a new :py:class::`BlockFilter` object.

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

The :py:class::`LogFilter` class is used for all filters pertaining to even
logs.  It exposes the following additional methods.


.. py:method:: LogFilter.get(only_changes=True)

    Synchronously retrieve the event logs for this filter.

    If ``only_changes`` is ``True`` then logs will be retrieved using the
    ``web3.eth.getFilterChanges`` which returns only new entries since the last
    poll.

    If ``only_changes`` is ``False`` then the logs will be retrieved using the
    ``web3.eth.getFilterLogs`` which returns all logs that match the given
    filter.

    This method will raise a ``ValueError`` if called on a filter that is
    currently polling.


The :py:class::`LogFilter` class is returned from the
:py:method::`web3.contract.Contract.on` and will be configured to extract the
event data from the event logs.


.. py:class:: PastLogFilter(...)

The :py:class::`PastLogFilter` is a subclass of :py:class::`LogFilter` that is
configured specially to return historical event logs.  It conforms to the same
API as the ``LogFilter`` class.


Shh Filter
----------

.. py:class:: ShhFilter(web3, filter_id)

The :py:class:: `ShhFilter` class is used for filtering Shh messages.
You can setup a callback function for Whipser messages matching the topics subscribed using ``web3.shh.filter(filter_params)``,which
will return a :py:class::`ShhFilter` object

    .. code-block:: python
   
        >>>def filter_callback(new_message):
        ...     sys.stdout.write("New Shh Message: {0}".format(new_message))
        ...
        >>>shh_filter = web3.shh.filter({"topics":[web3.fromAscii("topic_to_subscribe")]})
        >>>shh_filter.watch(filter_callback)
        #each time client recieves a Shh messages matching the topics subscibed,
        #filter_callback is called
