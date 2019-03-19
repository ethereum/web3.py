Geth API
========

.. py:module:: web3.geth

The ``web3.geth`` object exposes modules that enable you to interact with the JSON-RPC endpoints supported by `Geth <https://github.com/ethereum/go-ethereum/wiki/Management-APIs>`_ that are not defined in the standard set of Ethereum JSONRPC endpoints according to `EIP 1474 <https://github.com/ethereum/EIPs/pull/1474>`_.

GethAdmin API
~~~~~~~~~~~~~

The following methods are available on the ``web3.geth.admin`` namespace.

.. py:module:: web3.geth.admin

The ``web3.geth.admin`` object exposes methods to interact with the RPC APIs under the
``admin_`` namespace that are supported by the Geth client.

.. py:method:: datadir()

    * Delegates to ``admin_datadir`` RPC Method

    Returns the system path of the node's data directory.

    .. code-block:: python

        >>> web3.geth.admin.datadir()
        '/Users/piper/Library/Ethereum'


.. py:method:: nodeInfo()

    * Delegates to ``admin_nodeInfo`` RPC Method

    Returns information about the currently running node.

    .. code-block:: python

        >>> web3.geth.admin.nodeInfo()
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


.. py:method:: peers()

    * Delegates to ``admin_peers`` RPC Method

    Returns the current peers the node is connected to.

    .. code-block:: python

        >>> web3.geth.admin.peers()
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


.. py:method:: addPeer(node_url)

    * Delegates to ``admin_addPeer`` RPC Method

    Requests adding a new remote node to the list of tracked static nodes.

    .. code-block:: python

        >>> web3.geth.admin.addPeer('enode://e54eebad24dce1f6d246bea455ffa756d97801582420b9ed681a2ea84bf376d0bd87ae8dd6dc06cdb862a2ca89ecabe1be1050be35b4e70d62bc1a092cb7e2d3@52.71.255.237:30303')
        True


.. py:method:: setSolc(solc_path)

    * Delegates to ``admin_setSolc`` RPC Method

    Sets the system path to the ``solc`` binary for use with the
    ``eth_compileSolidity`` RPC method.  Returns the output reported by ``solc
    --version``.

    .. code-block:: python

        >>> web3.geth.admin.setSolc('/usr/local/bin/solc')
        "solc, the solidity compiler commandline interface\nVersion: 0.3.5-9da08ac3/Release-Darwin/appleclang/JIT"


.. py:method:: startRPC(host='localhost', port='8545', cors="", apis="eth,net,web3")

    * Delegates to ``admin_startRPC`` RPC Method

    Starts the HTTP based JSON RPC API webserver on the specified ``host`` and
    ``port``, with the ``rpccorsdomain`` set to the provided ``cors`` value and
    with the APIs specified by ``apis`` enabled.  Returns boolean as to whether
    the server was successfully started.

    .. code-block:: python

        >>> web3.geth.admin.startRPC()
        True


.. py:method:: startWS(host='localhost', port='8546', cors="", apis="eth,net,web3")

    * Delegates to ``admin_startWS`` RPC Method

    Starts the Websocket based JSON RPC API webserver on the specified ``host``
    and ``port``, with the ``rpccorsdomain`` set to the provided ``cors`` value
    and with the APIs specified by ``apis`` enabled.  Returns boolean as to
    whether the server was successfully started.

    .. code-block:: python

        >>> web3.geth.admin.startWS()
        True


.. py:method:: stopRPC()

    * Delegates to ``admin_stopRPC`` RPC Method

    Stops the HTTP based JSON RPC server.

    .. code-block:: python

        >>> web3.geth.admin.stopRPC()
        True


.. py:method:: stopWS()

    * Delegates to ``admin_stopWS`` RPC Method

    Stops the Websocket based JSON RPC server.

    .. code-block:: python

        >>> web3.geth.admin.stopWS()
        True


.. py:module:: web3.geth.personal

GethPersonal API
~~~~~~~~~~~~~~~~

The following methods are available on the ``web3.geth.personal`` namespace.

.. py:method:: listAccounts

    * Delegates to ``personal_listAccounts`` RPC Method

    Returns the list of known accounts.

    .. code-block:: python

        >>> web3.geth.personal.listAccounts()
        ['0xd3cda913deb6f67967b99d67acdfa1712c293601']


.. py:method:: importRawKey(self, private_key, passphrase)

    * Delegates to ``personal_importRawKey`` RPC Method

    Adds the given ``private_key`` to the node's keychain, encrypted with the
    given ``passphrase``.  Returns the address of the imported account.

    .. code-block:: python

        >>> web3.geth.personal.importRawKey(some_private_key, 'the-passphrase')
        '0xd3cda913deb6f67967b99d67acdfa1712c293601'


.. py:method:: newAccount(self, password)

    * Delegates to ``personal_newAccount`` RPC Method

    Generates a new account in the node's keychain encrypted with the
    given ``passphrase``.  Returns the address of the created account.

    .. code-block:: python

        >>> web3.geth.personal.newAccount('the-passphrase')
        '0xd3cda913deb6f67967b99d67acdfa1712c293601'


.. py:method:: lockAccount(self, account)

    * Delegates to ``personal_lockAccount`` RPC Method

    Locks the given ``account``.

    .. code-block:: python

        >>> web3.geth.personal.lockAccount('0xd3cda913deb6f67967b99d67acdfa1712c293601')


.. py:method:: unlockAccount(self, account, passphrase, duration=None)

    * Delegates to ``personal_unlockAccount`` RPC Method

    Unlocks the given ``account`` for ``duration`` seconds.  If ``duration`` is
    ``None`` then the account will remain unlocked indefinitely.  Returns
    boolean as to whether the account was successfully unlocked.

    .. code-block:: python

        >>> web3.geth.personal.unlockAccount('0xd3cda913deb6f67967b99d67acdfa1712c293601', 'wrong-passphrase')
        False
        >>> web3.geth.personal.unlockAccount('0xd3cda913deb6f67967b99d67acdfa1712c293601', 'the-passphrase')
        True

.. py:method:: sendTransaction(self, transaction, passphrase)

    * Delegates to ``personal_sendTransaction`` RPC Method

    Sends the transaction.


.. py:module:: web3.geth.txpool

GethTxPool API
~~~~~~~~~~~~~~

The ``web3.geth.txpool`` object exposes methods to interact with the RPC APIs under
the ``txpool_`` namespace. These methods are only exposed under the ``geth`` namespace
since they are not standard nor supported in Parity.

The following methods are available on the ``web3.geth.txpool`` namespace.

.. py:method:: TxPool.inspect()

    * Delegates to ``txpool_inspect`` RPC Method

    Returns a textual summary of all transactions currently pending for
    inclusing in the next block(s) as will as ones that are scheduled for
    future execution.

    .. code-block:: python

        >>> web3.geth.txpool.inspect()
        {
            'pending': {
                '0x26588a9301b0428d95e6fc3a5024fce8bec12d51': {
                  31813: ["0x3375ee30428b2a71c428afa5e89e427905f95f7e: 0 wei + 500000 × 20000000000 gas"]
                },
                '0x2a65aca4d5fc5b5c859090a6c34d164135398226': {
                  563662: ["0x958c1fa64b34db746925c6f8a3dd81128e40355e: 1051546810000000000 wei + 90000 × 20000000000 gas"],
                  563663: ["0x77517b1491a0299a44d668473411676f94e97e34: 1051190740000000000 wei + 90000 × 20000000000 gas"],
                  563664: ["0x3e2a7fe169c8f8eee251bb00d9fb6d304ce07d3a: 1050828950000000000 wei + 90000 × 20000000000 gas"],
                  563665: ["0xaf6c4695da477f8c663ea2d8b768ad82cb6a8522: 1050544770000000000 wei + 90000 × 20000000000 gas"],
                  563666: ["0x139b148094c50f4d20b01caf21b85edb711574db: 1048598530000000000 wei + 90000 × 20000000000 gas"],
                  563667: ["0x48b3bd66770b0d1eecefce090dafee36257538ae: 1048367260000000000 wei + 90000 × 20000000000 gas"],
                  563668: ["0x468569500925d53e06dd0993014ad166fd7dd381: 1048126690000000000 wei + 90000 × 20000000000 gas"],
                  563669: ["0x3dcb4c90477a4b8ff7190b79b524773cbe3be661: 1047965690000000000 wei + 90000 × 20000000000 gas"],
                  563670: ["0x6dfef5bc94b031407ffe71ae8076ca0fbf190963: 1047859050000000000 wei + 90000 × 20000000000 gas"]
                },
                '0x9174e688d7de157c5c0583df424eaab2676ac162': {
                  3: ["0xbb9bc244d798123fde783fcc1c72d3bb8c189413: 30000000000000000000 wei + 85000 × 21000000000 gas"]
                },
                '0xb18f9d01323e150096650ab989cfecd39d757aec': {
                  777: ["0xcd79c72690750f079ae6ab6ccd7e7aedc03c7720: 0 wei + 1000000 × 20000000000 gas"]
                },
                '0xb2916c870cf66967b6510b76c07e9d13a5d23514': {
                  2: ["0x576f25199d60982a8f31a8dff4da8acb982e6aba: 26000000000000000000 wei + 90000 × 20000000000 gas"]
                },
                '0xbc0ca4f217e052753614d6b019948824d0d8688b': {
                  0: ["0x2910543af39aba0cd09dbb2d50200b3e800a63d2: 1000000000000000000 wei + 50000 × 1171602790622 gas"]
                },
                '0xea674fdde714fd979de3edf0f56aa9716b898ec8': {
                  70148: ["0xe39c55ead9f997f7fa20ebe40fb4649943d7db66: 1000767667434026200 wei + 90000 × 20000000000 gas"]
                }
              },
              'queued': {
                '0x0f6000de1578619320aba5e392706b131fb1de6f': {
                  6: ["0x8383534d0bcd0186d326c993031311c0ac0d9b2d: 9000000000000000000 wei + 21000 × 20000000000 gas"]
                },
                '0x5b30608c678e1ac464a8994c3b33e5cdf3497112': {
                  6: ["0x9773547e27f8303c87089dc42d9288aa2b9d8f06: 50000000000000000000 wei + 90000 × 50000000000 gas"]
                },
                '0x976a3fc5d6f7d259ebfb4cc2ae75115475e9867c': {
                  3: ["0x346fb27de7e7370008f5da379f74dd49f5f2f80f: 140000000000000000 wei + 90000 × 20000000000 gas"]
                },
                '0x9b11bf0459b0c4b2f87f8cebca4cfc26f294b63a': {
                  2: ["0x24a461f25ee6a318bdef7f33de634a67bb67ac9d: 17000000000000000000 wei + 90000 × 50000000000 gas"],
                  6: ["0x6368f3f8c2b42435d6c136757382e4a59436a681: 17990000000000000000 wei + 90000 × 20000000000 gas", "0x8db7b4e0ecb095fbd01dffa62010801296a9ac78: 16998950000000000000 wei + 90000 × 20000000000 gas"],
                  7: ["0x6368f3f8c2b42435d6c136757382e4a59436a681: 17900000000000000000 wei + 90000 × 20000000000 gas"]
                }
              }
        }


.. py:method:: TxPool.status()

    * Delegates to ``txpool_status`` RPC Method

    Returns a textual summary of all transactions currently pending for
    inclusing in the next block(s) as will as ones that are scheduled for
    future execution.

    .. code-block:: python

        {
            pending: 10,
            queued: 7,
        }


.. py:method:: TxPool.content()

    * Delegates to ``txpool_content`` RPC Method

    Returns the exact details of all transactions that are pending or queued.

    .. code-block:: python

        >>> web3.geth.txpool.content()
        {
          'pending': {
            '0x0216d5032f356960cd3749c31ab34eeff21b3395': {
              806: [{
                'blockHash': "0x0000000000000000000000000000000000000000000000000000000000000000",
                'blockNumber': None,
                'from': "0x0216d5032f356960cd3749c31ab34eeff21b3395",
                'gas': "0x5208",
                'gasPrice': "0xba43b7400",
                'hash': "0xaf953a2d01f55cfe080c0c94150a60105e8ac3d51153058a1f03dd239dd08586",
                'input': "0x",
                'nonce': "0x326",
                'to': "0x7f69a91a3cf4be60020fb58b893b7cbb65376db8",
                'transactionIndex': None,
                'value': "0x19a99f0cf456000"
              }]
            },
            '0x24d407e5a0b506e1cb2fae163100b5de01f5193c': {
              34: [{
                'blockHash': "0x0000000000000000000000000000000000000000000000000000000000000000",
                'blockNumber': None,
                'from': "0x24d407e5a0b506e1cb2fae163100b5de01f5193c",
                'gas': "0x44c72",
                'gasPrice': "0x4a817c800",
                'hash': "0xb5b8b853af32226755a65ba0602f7ed0e8be2211516153b75e9ed640a7d359fe",
                'input': "0xb61d27f600000000000000000000000024d407e5a0b506e1cb2fae163100b5de01f5193c00000000000000000000000000000000000000000000000053444835ec580000000000000000000000000000000000000000000000000000000000000000006000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
                'nonce': "0x22",
                'to': "0x7320785200f74861b69c49e4ab32399a71b34f1a",
                'transactionIndex': None,
                'value': "0x0"
              }]
            }
          },
          'queued': {
            '0x976a3fc5d6f7d259ebfb4cc2ae75115475e9867c': {
              3: [{
                'blockHash': "0x0000000000000000000000000000000000000000000000000000000000000000",
                'blockNumber': None,
                'from': "0x976a3fc5d6f7d259ebfb4cc2ae75115475e9867c",
                'gas': "0x15f90",
                'gasPrice': "0x4a817c800",
                'hash': "0x57b30c59fc39a50e1cba90e3099286dfa5aaf60294a629240b5bbec6e2e66576",
                'input': "0x",
                'nonce': "0x3",
                'to': "0x346fb27de7e7370008f5da379f74dd49f5f2f80f",
                'transactionIndex': None,
                'value': "0x1f161421c8e0000"
              }]
            },
            '0x9b11bf0459b0c4b2f87f8cebca4cfc26f294b63a': {
              2: [{
                'blockHash': "0x0000000000000000000000000000000000000000000000000000000000000000",
                'blockNumber': None,
                'from': "0x9b11bf0459b0c4b2f87f8cebca4cfc26f294b63a",
                'gas': "0x15f90",
                'gasPrice': "0xba43b7400",
                'hash': "0x3a3c0698552eec2455ed3190eac3996feccc806970a4a056106deaf6ceb1e5e3",
                'input': "0x",
                'nonce': "0x2",
                'to': "0x24a461f25ee6a318bdef7f33de634a67bb67ac9d",
                'transactionIndex': None,
                'value': "0xebec21ee1da40000"
              }],
              6: [{
                'blockHash': "0x0000000000000000000000000000000000000000000000000000000000000000",
                'blockNumber': None,
                'from': "0x9b11bf0459b0c4b2f87f8cebca4cfc26f294b63a",
                'gas': "0x15f90",
                'gasPrice': "0x4a817c800",
                'hash': "0xbbcd1e45eae3b859203a04be7d6e1d7b03b222ec1d66dfcc8011dd39794b147e",
                'input': "0x",
                'nonce': "0x6",
                'to': "0x6368f3f8c2b42435d6c136757382e4a59436a681",
                'transactionIndex': None,
                'value': "0xf9a951af55470000"
              }, {
                'blockHash': "0x0000000000000000000000000000000000000000000000000000000000000000",
                'blockNumber': None,
                'from': "0x9b11bf0459b0c4b2f87f8cebca4cfc26f294b63a",
                'gas': "0x15f90",
                'gasPrice': "0x4a817c800",
                'hash': "0x60803251d43f072904dc3a2d6a084701cd35b4985790baaf8a8f76696041b272",
                'input': "0x",
                'nonce': "0x6",
                'to': "0x8db7b4e0ecb095fbd01dffa62010801296a9ac78",
                'transactionIndex': None,
                'value': "0xebe866f5f0a06000"
              }],
            }
          }
        }
