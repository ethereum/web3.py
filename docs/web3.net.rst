Net API
=======

.. py:module:: web3.net

The ``web3.net`` object exposes methods to interact with the RPC APIs under
the ``net_`` namespace.


Properties
----------

The following properties are available on the ``web3.net`` namespace.

.. py:method:: chainId
  :property:

    .. warning:: Deprecated: This property is deprecated as of EIP 1474.

.. py:method:: listening
  :property:

    * Delegates to ``net_listening`` RPC method

    Returns true if client is actively listening for network connections.

    .. code-block:: python

        >>> web3.net.listening
        True

.. py:method:: peer_count
  :property:

    * Delegates to ``net_peerCount`` RPC method

    Returns number of peers currently connected to the client.

    .. code-block:: python

        >>> web3.net.peer_count
        1

.. py:method:: peerCount
  :property:

    .. warning:: Deprecated: This property is deprecated in favor of
      :attr:`~web3.geth.admin.peer_count`

.. py:method:: version
  :property:

    * Delegates to ``net_version`` RPC Method

    Returns the current network id.

    .. code-block:: python

        >>> web3.net.version
        '8996'
