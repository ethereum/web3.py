Filtering
=========


.. py:module:: web3.utils.filters


The :meth:`web3.eth.Eth.filter` method can be used to setup filters for:

* Pending Transactions: ``web3.eth.filter('pending')``

* New Blocks ``web3.eth.filter('latest')``

* Event Logs

    Through the contract instance api:

    .. code-block:: python

        event_filter = mycontract.events.myEvent.createFilter(fromBlock='latest', argument_filters={'arg1':10})

    Or built manually by supplying `valid filter params <https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_newfilter/>`_:

    .. code-block:: python

        event_filter = web3.eth.filter({"address": contract_address})

* Attaching to an existing filter

    .. code-block:: python

        from web3.auto import w3
        existing_filter = web3.eth.filter(filter_id="0x0")


Filter Class
------------

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


Block and Transaction Filter Classes
------------------------------------

.. py:class:: BlockFilter(...)
    
BlockFilter is a subclass of :class:``Filter``.

You can setup a filter for new blocks using ``web3.eth.filter('latest')`` which
will return a new :py:class:`BlockFilter` object.

    .. code-block:: python

        >>> new_block_filter = web.eth.filter('latest')
        >>> new_block_filter.get_new_entries()

.. py:class:: TransactionFilter(...)

TransactionFilter is a subclass of :class:``Filter``.

You can setup a filter for new blocks using ``web3.eth.filter('pending')`` which
will return a new :py:class:`BlockFilter` object.

    .. code-block:: python

        >>> new_transaction_filter = web.eth.filter('pending')
        >>> new_transaction_filter.get_new_entries()


Event Log Filters
-----------------

You can set up a filter for event logs using the web3.py contract api: 
:func:`web3.contract.Contract.events.<event_name>.createFilter`, which provides some conveniances for
creating event log filters. Refer to the following example:

    .. code-block:: python

        event_filter = myContract.events.<event_name>.createFilter(fromBlock="latest", argument_filters={'arg1':10})
        event_filter.get_new_entries()

See :meth:`web3.contract.Contract.events.<event_name>.createFilter` documentation for more information.

You can set up an event log filter like the one above with `web3.eth.filter` by supplying a
dictionary containing the standard filter parameters. Assuming that `arg1` is indexed, the
equivalent filter creation would look like:

    .. code-block:: python

        event_signature_hash = web3.sha3(text="eventName(uint32)").hex()
        event_filter = web3.eth.filter({
            "address": myContract_address,
            "topics": [event_signature_hash,
                       "0x000000000000000000000000000000000000000000000000000000000000000a"],
            })

The ``topics`` argument is order-dependent. For non-anonymous events, the first item in the topic list is always the keccack hash of the event signature. Subsequent topic items are the hex encoded values for indexed event arguments. In the above example, the second item is the ``arg1`` value ``10`` encoded to its hex string representation.

In addition to being order-dependent, there are a few more points to recognize when specifying topic filters:

    Given a transaction log with topics [A, B], the following topic filters will yield a match:

    - [] "anything"
    - [A] "A in first position (and anything after)"
    - [None, B] "anything in first position AND B in second position (and anything after)"
    - [A, B] "A in first position AND B in second position (and anything after)"
    - [[A, B], [A, B]] "(A OR B) in first position AND (A OR B) in second position (and anything after)"

See the JSON-RPC documentation for `eth_newFilter <https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_newfilter>`_ more information on the standard filter parameters.

Creating a log filter by either of the above methods will return a :class:`LogFilter` instance.

.. py:class:: LogFilter(web3, filter_id, log_entry_formatter=None, data_filter_set=None)

The :py:class:`LogFilter` class is a subclass of :class:`Filter`.  See the :class:`Filter`
documentation for inherited methods.

:class:`LogFilter` provides the following additional
methods:

.. py:method:: LogFilter.set_data_filters(data_filter_set)

Provides a means to filter on the log data, in other words the ability to filter on values from
un-indexed event arguments. The parameter ``data_filter_set`` should be a list or set of 32-byte hex encoded values.


Examples: Listening For Events
------------------------------

Synchronous
^^^^^^^^^^^

    .. code-block:: python

        from web3.auto import w3
        import time

        def handle_event(event):
            print(event)

        def log_loop(event_filter, poll_interval):
            while True:
                for event in event_filter.get_new_entries():
                    handle_event(event)
                time.sleep(poll_interval)

        def main():
            block_filter = w3.eth.filter('latest')
            log_loop(block_filter, 2)

        if __name__ == '__main__':
            main()

.. _asynchronous_filters:

Asynchronous Filter Polling
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Starting with web3 version 4, the ``watch`` method was taken out of the web3 filter objects.
There are many decisions to be made when designing a system regarding threading and concurrency.
Rather than force a decision, web3 leaves these choices up to the user. Below are some example 
implementations of asynchronous filter-event handling that can serve as starting points.

Single threaded concurrency with ``async`` and ``await``
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Beginning in python 3.5, the ``async`` and ``await`` built-in keywords were added.  These provide a
shared api for coroutines that can be utilized by modules such as the built-in asyncio_.  Below is 
an example event loop using asyncio_, that polls multiple web3 filter object, and passes new 
entries to a handler.

        .. code-block:: python

            from web3.auto import w3
            import asyncio


            def handle_event(event):
                print(event)
                # and whatever

            async def log_loop(event_filter, poll_interval):
                while True:
                    for event in event_filter.get_new_entries():
                        handle_event(event)
                    await asyncio.sleep(poll_interval)

            def main():
                block_filter = w3.eth.filter('latest')
                tx_filter = w3.eth.filter('pending')
                loop = asyncio.get_event_loop()
                try:
                    loop.run_until_complete(
                        asyncio.gather(
                            log_loop(block_filter, 2),
                            log_loop(tx_filter, 2)))
                finally:
                    loop.close()

            if __name__ == '__main__':
                main()

    Read the asyncio_ documentation for more information.

Running the event loop in a separate thread
"""""""""""""""""""""""""""""""""""""""""""

Here is an extended version of above example, where the event loop is run in a separate thread, 
releasing the ``main`` function for other tasks.

        .. code-block:: python

            from web3.auto import w3
            import sleep
            from threading import Thread


            def handle_event(event):
                print(event)
                # and whatever


            async def log_loop(event_filter, poll_interval):
                while True:
                    for event in event_filter.get_new_entries():
                        handle_event(event)
                    time.sleep(poll_interval)


            def main():
                loop = asyncio.new_event_loop()
                worker = Thread(target=log_loop, args=(block_filter, 5), daemon=True)
                worker.start()
                    # .. do some other stuff

            if __name__ == '__main__':
                main()

Here are some other libraries that provide frameworks for writing asynchronous python:

    * gevent_
    * twisted_
    * celery_

.. _asyncio: https://docs.python.org/3/library/asyncio.html
.. _gevent: https://www.gevent.org/
.. _twisted: https://twistedmatrix.com/
.. _celery: https://www.celeryproject.org/
