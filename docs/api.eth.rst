Eth API
=======

.. py:class:: Eth

The ``web3.eth`` object exposes methods to interact with the RPC APIs under the
``eth_`` namespace.

.. py::attribute:: Eth.defaultAccount

    The ethereum address that will be used as the default ``from`` address for
    all transactions.  This defaults to ``web3.eth.coinbase``.

.. py::attribute:: Eth.defaultBlock

    The default block number that will be used for any RPC methods that accept
    a block identifier.  Defaults to ``'latest'``.
