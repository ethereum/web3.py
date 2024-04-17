.. _filtering:

Monitoring Events
=================

If you're on this page, you're likely looking for an answer to this question:
**How do I know when a specific contract is used?** You have at least three options:

1. Query blocks for transactions that include the contract address in the ``"to"`` field.
   This contrived example is searching the latest block for any transactions sent to the
   WETH_ contract.

.. code-block:: python

   WETH_ADDRESS = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'

   block = w3.eth.get_block('latest')
   for tx_hash in block.transactions:
       tx = w3.eth.get_transaction(tx_hash)
       if tx['to'] == WETH_ADDRESS:
           print(f'Found interaction with WETH contract! {tx}')

2. Query for logs emitted by a contract. After instantiating a web3.py Contract object,
   you can :ref:`fetch logs <contract_get_logs>` for any event listed in the ABI.  In this
   example, we query for ``Transfer`` events in the latest block and log out the results.

.. code-block:: python

   WETH_ADDRESS = '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2'
   WETH_ABI = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"guy","type":"address"},{"name":"wad","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"src","type":"address"},{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"wad","type":"uint256"}],"name":"withdraw","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"deposit","outputs":[],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"},{"name":"","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"payable":true,"stateMutability":"payable","type":"fallback"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"guy","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"dst","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Deposit","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"src","type":"address"},{"indexed":false,"name":"wad","type":"uint256"}],"name":"Withdrawal","type":"event"}]'

   weth_contract = w3.eth.contract(address=WETH_ADDRESS, abi=WETH_ABI)

   # fetch transfer events in the last block
   logs = weth_contract.events.Transfer().get_logs(from_block=w3.eth.block_number)

   for log in logs:
      print(f"Transfer of {w3.from_wei(log.args.wad, 'ether')} WETH from {log.args.src} to {log.args.dst}")

See an advanced example of fetching log history :ref:`here <advanced_token_fetch>`.

3. Use a filter.

.. warning ::

  While filters can be a very convenient way to monitor for blocks, transactions, or
  events, they are notoriously unreliable. Both remote and locally hosted nodes have
  a reputation for occasionally dropping filters, and some remote node providers don't
  support filter-related RPC calls at all.

.. py:module:: web3.utils.filters

The :meth:`web3.eth.Eth.filter` method can be used to set up filters for:

* Pending Transactions: ``w3.eth.filter("pending")``

* New Blocks ``w3.eth.filter("latest")``

* Event Logs

    Through the contract instance api:

    .. code-block:: python

        event_filter = my_contract.events.myEvent.create_filter(from_block='latest', argument_filters={'arg1':10})

    Or built manually by supplying `valid filter params <https://github.com/ethereum/execution-apis/blob/bea0266c42919a2fb3ee524fb91e624a23bc17c5/src/schemas/filter.json#L28>`_:

    .. code-block:: python

        event_filter = w3.eth.filter({"address": contract_address})

* Attaching to an existing filter

    .. code-block:: python

        existing_filter = w3.eth.filter(filter_id="0x0")

.. note ::

    Creating event filters requires that your Ethereum node has an API support enabled for filters.
    Note that Infura support for filters does not offer access to `pending` filters.
    To get event logs on other stateless nodes please see :class:`web3.contract.ContractEvents`.



Filter Class
------------

.. py:class:: Filter(web3, filter_id)

.. py:attribute:: Filter.filter_id

    The ``filter_id`` for this filter as returned by the ``eth_newFilter`` RPC
    method when this filter was created.


.. py:method:: Filter.get_new_entries()

    Retrieve new entries for this filter.

    Logs will be retrieved using the
    :func:`web3.eth.Eth.get_filter_changes` which returns only new entries since the last
    poll.


.. py:method:: Filter.get_all_entries()

    Retrieve all entries for this filter.

    Logs will be retrieved using the
    :func:`web3.eth.Eth.get_filter_logs` which returns all entries that match the given
    filter.


.. py:method:: Filter.format_entry(entry)

    Hook for subclasses to modify the format of the log entries this filter
    returns, or passes to its callback functions.

    By default this returns the ``entry`` parameter umodified.


.. py:method:: Filter.is_valid_entry(entry)

    Hook for subclasses to add additional programmatic filtering.  The default
    implementation always returns ``True``.


Block and Transaction Filter Classes
------------------------------------

.. py:class:: BlockFilter(...)

``BlockFilter`` is a subclass of :class:`Filter`.

You can setup a filter for new blocks using ``web3.eth.filter('latest')`` which
will return a new :class:`BlockFilter` object.

    .. code-block:: python

        new_block_filter = w3.eth.filter('latest')
        new_block_filter.get_new_entries()

    .. note::

        ``"safe"`` and ``"finalized"`` block identifiers are not yet supported for
        ``eth_newBlockFilter``.

.. py:class:: TransactionFilter(...)

``TransactionFilter`` is a subclass of :class:`Filter`.

You can setup a filter for new blocks using ``web3.eth.filter('pending')`` which
will return a new :class:`TransactionFilter` object.

    .. code-block:: python

        new_transaction_filter = w3.eth.filter('pending')
        new_transaction_filter.get_new_entries()


Event Log Filters
-----------------

You can set up a filter for event logs using the web3.py contract api:
:meth:`web3.contract.Contract.events.your_event_name.create_filter`, which provides some conveniences for
creating event log filters. Refer to the following example:

    .. code-block:: python

        event_filter = my_contract.events.<event_name>.create_filter(from_block="latest", argument_filters={'arg1':10})
        event_filter.get_new_entries()

See :meth:`web3.contract.Contract.events.your_event_name.create_filter()` documentation for more information.

You can set up an event log filter like the one above with ``web3.eth.filter`` by supplying a
dictionary containing the standard filter parameters. Assuming that ``arg1`` is indexed, the
equivalent filter creation would look like:

    .. code-block:: python

        event_signature_hash = web3.keccak(text="eventName(uint32)").hex()
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

See the JSON-RPC documentation for `eth_newFilter <https://ethereum.org/en/developers/docs/apis/json-rpc/#eth_newfilter>`_ more information on the standard filter parameters.

    .. note::

        Though ``"finalized"`` and ``"safe"`` block identifiers are not yet part of the
        specifications for ``eth_newFilter``, they are supported by web3.py and may or
        may not yield expected results depending on the node being accessed.

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

        from web3 import Web3, IPCProvider
        import time

        # instantiate Web3 instance
        w3 = Web3(IPCProvider(...))

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
^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

            from web3 import Web3, IPCProvider
            import asyncio

            # instantiate Web3 instance
            w3 = Web3(IPCProvider(...))

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

            from web3 import Web3, IPCProvider
            from threading import Thread
            import time

            # instantiate Web3 instance
            w3 = Web3(IPCProvider(...))

            def handle_event(event):
                print(event)
                # and whatever


            def log_loop(event_filter, poll_interval):
                while True:
                    for event in event_filter.get_new_entries():
                        handle_event(event)
                    time.sleep(poll_interval)


            def main():
                block_filter = w3.eth.filter('latest')
                worker = Thread(target=log_loop, args=(block_filter, 5), daemon=True)
                worker.start()
                    # .. do some other stuff

            if __name__ == '__main__':
                main()

Here are some other libraries that provide frameworks for writing asynchronous python:

    * gevent_
    * twisted_
    * celery_

.. _WETH: https://etherscan.io/token/0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2#code
.. _asyncio: https://docs.python.org/3/library/asyncio.html
.. _gevent: https://www.gevent.org/
.. _twisted: https://twistedmatrix.com/
.. _celery: https://www.celeryproject.org/
