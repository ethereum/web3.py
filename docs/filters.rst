Filtering
=========


.. py:module:: web3.utils.filters


The :meth:`web3.eth.Eth.filter` method can be used to setup filters for:

* Pending Transactions: ``web3.eth.filter('pending')``

* New Blocks ``web3.eth.filter('latest')``

* Event Logs

    Through the contract instance api:

    .. code-block:: python

        event_filter = myContract.eventFilter('eventName', {'filter': {'arg1':10}})

    Or built manually by supplying `valid filter params <http://https://github.com/ethereum/wiki/wiki/JSON-RPC#eth_newfilter/>`_:

    .. code-block:: python

        event_filter = web3.eth.filter({"address": contract_address})

* Attaching to an existing filter

    .. code-block:: python

        from web3.auto import w3
        existing_filter = web3.utils.filters.Filter(w3, "0x0")


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

        >>> new_block_filter = web.eth.filter('latest')
        >>> new_block_filter.get_new_entries()

.. py:class:: TransactionFilter(...)

You can setup a filter for new blocks using ``web3.eth.filter('pending')`` which
will return a new :py:class:`BlockFilter` object.

    .. code-block:: python

        >>> new_transaction_filter = web.eth.filter('pending')
        >>> new_transaction_filter.get_new_entries()


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

    .. code-block:: python

        event_filter = myContract.eventFilter('eventName', {'filter': {'arg1':10}})
        event_filter.get_new_entries()

Listening For Events
--------------------

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


Asynchronous
^^^^^^^^^^^^

Starting with web3 version 4, the ``watch`` method was taken out of the web3 filter objects.
There are many decisions to be made when designing a system regarding threading and concurrency.
Rather than force a decision, web3 leaves these choices up to the user. Below are some example implementations of asynchronous filter-event handling that can serve as starting points.

Single threaded concurrency with ``async`` and ``await``
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    Beginning in python 3.5, the ``async`` and ``await`` built-in keywords were added.  These provide a shared api for coroutines that can be utilized by modules such as the built-in asyncio_.  Below is an example event loop using asyncio_, that polls multiple web3 filter object, and passes new entries to a handler.

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
                            log_loop(tx_filter, 2))
                finally:
                    loop.close()

            if __name__ == '__main__':
                main()

    Read the asyncio_ documentation for more information.

Running the event loop in a separate thread
"""""""""""""""""""""""""""""""""""""""""""

    Here is an extended version of above example, where the event loop is run in a separate thread, releasing the ``main`` function for other tasks.

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
