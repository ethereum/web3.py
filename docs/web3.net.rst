Net API
===========

.. py:module:: web3.net
.. py:currentmodule:: web3.net

.. py:class:: Net

The ``web3.net`` object exposes methods to interact with the RPC APIs under
the ``net_`` namespace.


Properties
----------

The following properties are available on the ``web3.net`` namespace.

.. py:method:: Net.chainId(self)

    This method is not implemented. You must manually determine your chain ID for now.

    It will always return `None`, which is a valid chainId to specify in the transaction.
    It means the transaction (may be) replayable on other forks of the network.

    .. code-block:: python

        >>> web3.net.chainId
        None

.. py:method:: Net.version(self)

    * Delegates to ``net_version`` RPC Method

    Returns the current network chainId/version.

    .. code-block:: python

        >>> web3.net.version
        1

