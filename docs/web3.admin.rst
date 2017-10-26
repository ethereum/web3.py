Admin API
==========

.. py:module:: web3.admin
.. py:currentmodule:: web3.admin

.. py:class:: Admin

The ``web3.admin`` object exposes methods to interact with the RPC APIs under the
``admin_`` namespace.


Properties
----------

The following properties are available on the ``web3.admin`` namespace.

.. py:attribute:: datadir

    * Delegates to ``admin_datadir`` RPC Method

    Returns the system path of the node's data directory.

    .. code-block:: python

        >>> web3.admin.datadir
        '/Users/piper/Library/Ethereum'


.. py:attribute:: nodeInfo

    * Delegates to ``admin_nodeInfo`` RPC Method

    Returns information about the currently running node.

    .. code-block:: python

        >>> web3.admin.nodeInfo
        {
            'enode': 'enode://e54eebad24dce1f6d246bea455ffa756d97801582420b9ed681a2ea84bf376d0bd87ae8dd6dc06cdb862a2ca89ecabe1be1050be35b4e70d62bc1a092cb7e2d3@[::]:30303',
            'id': 'e54eebad24dce1f6d246bea455ffa756d97801582420b9ed681a2ea84bf376d0bd87ae8dd6dc06cdb862a2ca89ecabe1be1050be35b4e70d62bc1a092cb7e2d3',
            'ip': '::',
            'listenAddr': '[::]:30303',
            'name': 'Geth/v1.4.11-stable-fed692f6/darwin/go1.7',
            'ports': {'discovery': 30303, 'listener': 30303},
            'protocols': {
                'eth': {
                    'difficulty': 57631175724744612603,
                    'genesis': '0xd4e56740f876aef8c010b86a40d5f56745a118d0906a34e69aec8c0db1cb8fa3',
                    'head': '0xaaef6b9dd0d34088915f4c62b6c166379da2ad250a88f76955508f7cc81fb796',
                    'network': 1,
                },
            },
        }


.. py:attribute:: peers

    * Delegates to ``admin_peers`` RPC Method

    Returns the current peers the node is connected to.

    .. code-block:: python

        >>> web3.admin.peers
        [
            {
                'caps': ['eth/63'],
                'id': '146e8e3e2460f1e18939a5da37c4a79f149c8b9837240d49c7d94c122f30064e07e4a42ae2c2992d0f8e7e6f68a30e7e9ad31d524349ec9d17effd2426a37b40',
                'name': 'Geth/v1.4.10-stable/windows/go1.6.2',
                'network': {
                    'localAddress': '10.0.3.115:64478',
                    'remoteAddress': '72.208.167.127:30303',
                },
                'protocols': {
                    'eth': {
                        'difficulty': 17179869184,
                        'head': '0xd4e56740f876aef8c010b86a40d5f56745a118d0906a34e69aec8c0db1cb8fa3',
                        'version': 63,
                    },
                }
            },
            {
                'caps': ['eth/62', 'eth/63'],
                'id': '76cb6cd3354be081923a90dfd4cda40aa78b307cc3cf4d5733dc32cc171d00f7c08356e9eb2ea47eab5aad7a15a3419b859139e3f762e1e1ebf5a04f530dcef7',
                'name': 'Geth/v1.4.10-stable-5f55d95a/linux/go1.5.1',
                'network': {
                    'localAddress': '10.0.3.115:64784',
                    'remoteAddress': '60.205.92.119:30303',
                },
                'protocols': {
                    'eth': {
                        'difficulty': 57631175724744612603,
                        'head': '0xaaef6b9dd0d34088915f4c62b6c166379da2ad250a88f76955508f7cc81fb796',
                        'version': 63,
                    },
                },
            },
            ...
        ]

Methods
-------

The following methods are available on the ``web3.admin`` namespace.


.. py:method:: addPeer(node_url)

    * Delegates to ``admin_addPeer`` RPC Method

    Requests adding a new remote node to the list of tracked static nodes.

    .. code-block:: python

        >>> web3.admin.addPeer('enode://e54eebad24dce1f6d246bea455ffa756d97801582420b9ed681a2ea84bf376d0bd87ae8dd6dc06cdb862a2ca89ecabe1be1050be35b4e70d62bc1a092cb7e2d3@52.71.255.237:30303')
        True


.. py:method:: setSolc(solc_path)

    * Delegates to ``admin_setSolc`` RPC Method

    Sets the system path to the ``solc`` binary for use with the
    ``eth_compileSolidity`` RPC method.  Returns the output reported by ``solc
    --version``.

    .. code-block:: python

        >>> web3.admin.setSolc('/usr/local/bin/solc')
        "solc, the solidity compiler commandline interface\nVersion: 0.3.5-9da08ac3/Release-Darwin/appleclang/JIT"


.. py:method:: startRPC(host='localhost', port='8545', cors="", apis="eth,net,web3")

    * Delegates to ``admin_startRPC`` RPC Method

    Starts the HTTP based JSON RPC API webserver on the specified ``host`` and
    ``port``, with the ``rpccorsdomain`` set to the provided ``cors`` value and
    with the APIs specified by ``apis`` enabled.  Returns boolean as to whether
    the server was successfully started.

    .. code-block:: python

        >>> web3.admin.startRPC()
        True


.. py:method:: startWS(host='localhost', port='8546', cors="", apis="eth,net,web3")

    * Delegates to ``admin_startWS`` RPC Method

    Starts the Websocket based JSON RPC API webserver on the specified ``host``
    and ``port``, with the ``rpccorsdomain`` set to the provided ``cors`` value
    and with the APIs specified by ``apis`` enabled.  Returns boolean as to
    whether the server was successfully started.

    .. code-block:: python

        >>> web3.admin.startWS()
        True


.. py:method:: stopRPC()

    * Delegates to ``admin_stopRPC`` RPC Method

    Stops the HTTP based JSON RPC server.

    .. code-block:: python

        >>> web3.admin.stopRPC()
        True


.. py:method:: stopWS()

    * Delegates to ``admin_stopWS`` RPC Method

    Stops the Websocket based JSON RPC server.

    .. code-block:: python

        >>> web3.admin.stopWS()
        True
