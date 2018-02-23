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

    * Delegates to ``net_version`` RPC Method

    Returns the current network chainId/version and is an alias of ``web3.net.version``.

    .. code-block:: python

        >>> web3.net.chainId
        1


.. py:method:: Net.version(self)

    * Delegates to ``net_version`` RPC Method

    Returns the current network chainId/version.

    .. code-block:: python

        >>> web3.net.version
        1

