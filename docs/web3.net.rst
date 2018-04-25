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

    This method is trivially implemented.
    It will always return `None`, which is a valid chainId to specify in the transaction.

    If you want the real chainId of your node, you must manually determine it for now.

    Note that your transactions (may be) replayable on forks of the network you intend, if
    :ref:`eth-account` and using a chainId of `None`.

    .. code-block:: python

        >>> web3.net.chainId
        None

.. py:method:: Net.version(self)

    * Delegates to ``net_version`` RPC Method

    Returns the current network chainId/version.

    .. code-block:: python

        >>> web3.net.version
        1

