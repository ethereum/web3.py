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


.. py:method:: node_info()

    * Delegates to ``admin_nodeInfo`` RPC Method

    Returns information about the currently running node.

    .. code-block:: python

        >>> web3.geth.admin.node_info()
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


.. py:method:: nodeInfo()

    .. warning:: Deprecated: This method is deprecated in favor of
      :meth:`~web3.geth.admin.node_info()`


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


.. py:method:: add_peer(node_url)

    * Delegates to ``admin_addPeer`` RPC Method

    Requests adding a new remote node to the list of tracked static nodes.

    .. code-block:: python

        >>> web3.geth.admin.add_peer('enode://e54eebad24dce1f6d246bea455ffa756d97801582420b9ed681a2ea84bf376d0bd87ae8dd6dc06cdb862a2ca89ecabe1be1050be35b4e70d62bc1a092cb7e2d3@52.71.255.237:30303')
        True


.. py:method:: addPeer(node_url)

    .. warning:: Deprecated: This method is deprecated in favor of :meth:`~web3.geth.admin.add_peer()`

.. py:method:: setSolc(solc_path)

    .. Warning:: This method has been removed from Geth

.. py:method:: start_rpc(host='localhost', port='8545', cors="", apis="eth,net,web3")

    * Delegates to ``admin_startRPC`` RPC Method

    Starts the HTTP based JSON RPC API webserver on the specified ``host`` and
    ``port``, with the ``rpccorsdomain`` set to the provided ``cors`` value and
    with the APIs specified by ``apis`` enabled.  Returns boolean as to whether
    the server was successfully started.

    .. code-block:: python

        >>> web3.geth.admin.start_rpc()
        True


.. py:method:: startRPC(host='localhost', port='8545', cors="", apis="eth,net,web3")

    .. warning:: Deprecated: This method is deprecated in favor of
       :meth:`~web3.geth.admin.start_rpc()`


.. py:method:: start_ws(host='localhost', port='8546', cors="", apis="eth,net,web3")

    * Delegates to ``admin_startWS`` RPC Method

    Starts the Websocket based JSON RPC API webserver on the specified ``host``
    and ``port``, with the ``rpccorsdomain`` set to the provided ``cors`` value
    and with the APIs specified by ``apis`` enabled.  Returns boolean as to
    whether the server was successfully started.

    .. code-block:: python

        >>> web3.geth.admin.start_ws()
        True


.. py:method:: startWS(host='localhost', port='8546', cors="", apis="eth,net,web3")

    .. warning:: Deprecated: This method is deprecated in favor of
       :meth:`~web3.geth.admin.start_ws()`


.. py:method:: stop_rpc()

    * Delegates to ``admin_stopRPC`` RPC Method

    Stops the HTTP based JSON RPC server.

    .. code-block:: python

        >>> web3.geth.admin.stop_rpc()
        True


.. py:method:: stopRPC()

    .. warning:: Deprecated: This method is deprecated in favor of
       :meth:`~web3.geth.admin.stop_rpc()`


.. py:method:: stop_ws()

    * Delegates to ``admin_stopWS`` RPC Method

    Stops the Websocket based JSON RPC server.

    .. code-block:: python

        >>> web3.geth.admin.stop_ws()
        True


.. py:method:: stopWS()

    .. warning:: Deprecated: This method is deprecated in favor of
       :meth:`~web3.geth.admin.stop_ws()`


.. py:module:: web3.geth.personal

GethPersonal API
~~~~~~~~~~~~~~~~

The following methods are available on the ``web3.geth.personal`` namespace.

.. py:method:: listAccounts

    * Delegates to ``personal_listAccounts`` RPC Method

    Returns the list of known accounts.

    .. code-block:: python

        >>> web3.geth.personal.listAccounts()
        ['0xd3CdA913deB6f67967B99D67aCDFa1712C293601']


.. py:method:: importRawKey(self, private_key, passphrase)

    * Delegates to ``personal_importRawKey`` RPC Method

    Adds the given ``private_key`` to the node's keychain, encrypted with the
    given ``passphrase``.  Returns the address of the imported account.

    .. code-block:: python

        >>> web3.geth.personal.importRawKey(some_private_key, 'the-passphrase')
        '0xd3CdA913deB6f67967B99D67aCDFa1712C293601'


.. py:method:: newAccount(self, password)

    * Delegates to ``personal_newAccount`` RPC Method

    Generates a new account in the node's keychain encrypted with the
    given ``passphrase``.  Returns the address of the created account.

    .. code-block:: python

        >>> web3.geth.personal.newAccount('the-passphrase')
        '0xd3CdA913deB6f67967B99D67aCDFa1712C293601'


.. py:method:: lockAccount(self, account)

    * Delegates to ``personal_lockAccount`` RPC Method

    Locks the given ``account``.

    .. code-block:: python

        >>> web3.geth.personal.lockAccount('0xd3CdA913deB6f67967B99D67aCDFa1712C293601')


.. py:method:: unlockAccount(self, account, passphrase, duration=None)

    * Delegates to ``personal_unlockAccount`` RPC Method

    Unlocks the given ``account`` for ``duration`` seconds.  If ``duration`` is
    ``None`` then the account will remain unlocked indefinitely.  Returns
    boolean as to whether the account was successfully unlocked.

    .. code-block:: python

        >>> web3.geth.personal.unlockAccount('0xd3CdA913deB6f67967B99D67aCDFa1712C293601', 'wrong-passphrase')
        False
        >>> web3.geth.personal.unlockAccount('0xd3CdA913deB6f67967B99D67aCDFa1712C293601', 'the-passphrase')
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
                '0x26588a9301b0428d95e6Fc3A5024fcE8BEc12D51': {
                  31813: ["0x3375Ee30428b2A71c428afa5E89e427905F95F7e: 0 wei + 500000 × 20000000000 gas"]
                },
                '0x2a65Aca4D5fC5B5C859090a6c34d164135398226': {
                  563662: ["0x958c1Fa64B34db746925c6F8a3Dd81128e40355E: 1051546810000000000 wei + 90000 × 20000000000 gas"],
                  563663: ["0x77517B1491a0299A44d668473411676f94e97E34: 1051190740000000000 wei + 90000 × 20000000000 gas"],
                  563664: ["0x3E2A7Fe169c8F8eee251BB00d9fb6d304cE07d3A: 1050828950000000000 wei + 90000 × 20000000000 gas"],
                  563665: ["0xAF6c4695da477F8C663eA2D8B768Ad82Cb6A8522: 1050544770000000000 wei + 90000 × 20000000000 gas"],
                  563666: ["0x139B148094C50F4d20b01cAf21B85eDb711574dB: 1048598530000000000 wei + 90000 × 20000000000 gas"],
                  563667: ["0x48B3Bd66770b0D1EeceFCe090daFeE36257538aE: 1048367260000000000 wei + 90000 × 20000000000 gas"],
                  563668: ["0x468569500925D53e06Dd0993014aD166fD7Dd381: 1048126690000000000 wei + 90000 × 20000000000 gas"],
                  563669: ["0x3DcB4C90477a4b8Ff7190b79b524773CbE3bE661: 1047965690000000000 wei + 90000 × 20000000000 gas"],
                  563670: ["0x6DfeF5BC94b031407FFe71ae8076CA0FbF190963: 1047859050000000000 wei + 90000 × 20000000000 gas"]
                },
                '0x9174E688d7dE157C5C0583Df424EAAB2676aC162': {
                  3: ["0xBB9bc244D798123fDe783fCc1C72d3Bb8C189413: 30000000000000000000 wei + 85000 × 21000000000 gas"]
                },
                '0xb18F9d01323e150096650ab989CfecD39D757Aec': {
                  777: ["0xcD79c72690750F079ae6AB6ccd7e7aEDC03c7720: 0 wei + 1000000 × 20000000000 gas"]
                },
                '0xB2916C870Cf66967B6510B76c07E9d13a5D23514': {
                  2: ["0x576f25199D60982A8f31A8DfF4da8aCB982e6ABa: 26000000000000000000 wei + 90000 × 20000000000 gas"]
                },
                '0xBc0CA4f217E052753614d6B019948824d0d8688B': {
                  0: ["0x2910543Af39abA0Cd09dBb2D50200b3E800A63D2: 1000000000000000000 wei + 50000 × 1171602790622 gas"]
                },
                '0xea674fdde714fd979de3edf0f56aa9716b898ec8': {
                  70148: ["0xe39c55ead9f997f7fa20ebe40fb4649943d7db66: 1000767667434026200 wei + 90000 × 20000000000 gas"]
                }
              },
              'queued': {
                '0x0F6000De1578619320aBA5e392706b131FB1dE6f': {
                  6: ["0x8383534d0bcd0186d326C993031311c0Ac0D9B2d: 9000000000000000000 wei + 21000 × 20000000000 gas"]
                },
                '0x5b30608c678e1ac464A8994C3B33E5CdF3497112': {
                  6: ["0x9773547e27f8303C87089dc42D9288aa2B9d8F06: 50000000000000000000 wei + 90000 × 50000000000 gas"]
                },
                '0x976A3Fc5d6f7d259EBfb4cc2Ae75115475E9867C': {
                  3: ["0x346FB27dE7E7370008f5da379f74dd49F5f2F80F: 140000000000000000 wei + 90000 × 20000000000 gas"]
                },
                '0x9B11bF0459b0c4b2f87f8CEBca4cfc26f294B63A': {
                  2: ["0x24a461f25eE6a318BDef7F33De634A67bb67Ac9D: 17000000000000000000 wei + 90000 × 50000000000 gas"],
                  6: ["0x6368f3f8c2B42435D6C136757382E4A59436a681: 17990000000000000000 wei + 90000 × 20000000000 gas", "0x8db7b4e0ecb095fbd01dffa62010801296a9ac78: 16998950000000000000 wei + 90000 × 20000000000 gas"],
                  7: ["0x6368f3f8c2B42435D6C136757382E4A59436a681: 17900000000000000000 wei + 90000 × 20000000000 gas"]
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
            '0x0216D5032f356960Cd3749C31Ab34eEFF21B3395': {
              806: [{
                'blockHash': "0x0000000000000000000000000000000000000000000000000000000000000000",
                'blockNumber': None,
                'from': "0x0216D5032f356960Cd3749C31Ab34eEFF21B3395",
                'gas': "0x5208",
                'gasPrice': "0xba43b7400",
                'hash': "0xaf953a2d01f55cfe080c0c94150a60105e8ac3d51153058a1f03dd239dd08586",
                'input': "0x",
                'nonce': "0x326",
                'to': "0x7f69a91A3CF4bE60020fB58B893b7cbb65376db8",
                'transactionIndex': None,
                'value': "0x19a99f0cf456000"
              }]
            },
            '0x24d407e5A0B506E1Cb2fae163100B5DE01F5193C': {
              34: [{
                'blockHash': "0x0000000000000000000000000000000000000000000000000000000000000000",
                'blockNumber': None,
                'from': "0x24d407e5A0B506E1Cb2fae163100B5DE01F5193C",
                'gas': "0x44c72",
                'gasPrice': "0x4a817c800",
                'hash': "0xb5b8b853af32226755a65ba0602f7ed0e8be2211516153b75e9ed640a7d359fe",
                'input': "0xb61d27f600000000000000000000000024d407e5a0b506e1cb2fae163100b5de01f5193c00000000000000000000000000000000000000000000000053444835ec580000000000000000000000000000000000000000000000000000000000000000006000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
                'nonce': "0x22",
                'to': "0x7320785200f74861B69C49e4ab32399a71b34f1a",
                'transactionIndex': None,
                'value': "0x0"
              }]
            }
          },
          'queued': {
            '0x976A3Fc5d6f7d259EBfb4cc2Ae75115475E9867C': {
              3: [{
                'blockHash': "0x0000000000000000000000000000000000000000000000000000000000000000",
                'blockNumber': None,
                'from': "0x976A3Fc5d6f7d259EBfb4cc2Ae75115475E9867C",
                'gas': "0x15f90",
                'gasPrice': "0x4a817c800",
                'hash': "0x57b30c59fc39a50e1cba90e3099286dfa5aaf60294a629240b5bbec6e2e66576",
                'input': "0x",
                'nonce': "0x3",
                'to': "0x346FB27dE7E7370008f5da379f74dd49F5f2F80F",
                'transactionIndex': None,
                'value': "0x1f161421c8e0000"
              }]
            },
            '0x9B11bF0459b0c4b2f87f8CEBca4cfc26f294B63A': {
              2: [{
                'blockHash': "0x0000000000000000000000000000000000000000000000000000000000000000",
                'blockNumber': None,
                'from': "0x9B11bF0459b0c4b2f87f8CEBca4cfc26f294B63A",
                'gas': "0x15f90",
                'gasPrice': "0xba43b7400",
                'hash': "0x3a3c0698552eec2455ed3190eac3996feccc806970a4a056106deaf6ceb1e5e3",
                'input': "0x",
                'nonce': "0x2",
                'to': "0x24a461f25eE6a318BDef7F33De634A67bb67Ac9D",
                'transactionIndex': None,
                'value': "0xebec21ee1da40000"
              }],
              6: [{
                'blockHash': "0x0000000000000000000000000000000000000000000000000000000000000000",
                'blockNumber': None,
                'from': "0x9B11bF0459b0c4b2f87f8CEBca4cfc26f294B63A",
                'gas': "0x15f90",
                'gasPrice': "0x4a817c800",
                'hash': "0xbbcd1e45eae3b859203a04be7d6e1d7b03b222ec1d66dfcc8011dd39794b147e",
                'input': "0x",
                'nonce': "0x6",
                'to': "0x6368f3f8c2B42435D6C136757382E4A59436a681",
                'transactionIndex': None,
                'value': "0xf9a951af55470000"
              }, {
                'blockHash': "0x0000000000000000000000000000000000000000000000000000000000000000",
                'blockNumber': None,
                'from': "0x9B11bF0459b0c4b2f87f8CEBca4cfc26f294B63A",
                'gas': "0x15f90",
                'gasPrice': "0x4a817c800",
                'hash': "0x60803251d43f072904dc3a2d6a084701cd35b4985790baaf8a8f76696041b272",
                'input': "0x",
                'nonce': "0x6",
                'to': "0x8DB7b4e0ECB095FBD01Dffa62010801296a9ac78",
                'transactionIndex': None,
                'value': "0xebe866f5f0a06000"
              }],
            }
          }
        }

GethShh
~~~~~~~

The ``web3.geth.shh`` object exposes methods to interact with the RPC APIs under the
``shh_`` namespace.

Full documentation for Geth-supported endpoints can be found `here <https://github.com/ethereum/go-ethereum/wiki/Whisper-v6-RPC-API>`_.

.. warning:: The Whisper protocol is in flux, with incompatible versions supported
    by different major clients.

.. py:method:: Shh.version()

    Returns the Whisper version this node offers.

    .. code-block:: python

        >>>web3.geth.shh.version()
        6.0

.. py:method:: Shh.info()

    Returns the Whisper statistics for diagnostics.

    .. code-block:: python

        >>>web3.geth.shh.info()
        {'maxMessageSize': 1024, 'memory': 240, 'messages': 0, 'minPow': 0.2}

.. py:method:: Shh.post(self, message)

    * Creates a whisper message and injects it into the network for distribution.

    * Parameters:
        * ``symKeyID``: When using symmetric key encryption, holds the symmetric key ID.
        * ``pubKey``: When using asymmetric key encryption, holds the public key.
        * ``ttl``: Time-to-live in seconds.
        * ``sig (optional)``: ID of the signing key.
        * ``topic``: Message topic (four bytes of arbitrary data).
        * ``payload``: Payload to be encrypted.
        * ``padding (optional)``: Padding (byte array of arbitrary length).
        * ``powTime``: Maximal time in seconds to be spent on prrof of work.
        * ``powTarget``: Minimal PoW target required for this message.
        * ``targetPeer (optional)``: Peer ID (for peer-to-peer message only).

    * Returns ``True`` if the message was succesfully sent, otherwise ``False``

    .. code-block:: python

        >>>web3.geth.shh.post({'payload': web3.toHex(text="test_payload"), 'pubKey': recipient_public, 'topic': '0x12340000', 'powTarget': 2.5, 'powTime': 2})
        True

.. py:method:: Shh.new_message_filter(self, criteria)

    * Create a new filter id. This filter id can be used with ``ShhFilter`` to poll for new messages that match the set of criteria.

    * Parameters:
        * ``symKeyID``: When using symmetric key encryption, holds the symmetric key ID.
        * ``privateKeyID``: When using asymmetric key encryption, holds the private key ID.
        * ``sig``: Public key of the signature.
        * ``minPoW``: Minimal PoW requirement for incoming messages.
        * ``topics``: Array of possible topics (or partial topics).
        * ``allowP2P``: Indicates if this filter allows processing of direct peer-to-peer messages.


    .. code-block:: python

        >>>web3.geth.shh.new_message_filter({'topic': '0x12340000', 'privateKeyID': recipient_private})
        'b37c3106cfb683e8f01b5019342399e0d1d74e9160f69b27625faba7a6738554'

.. py:method:: Shh.deleteMessageFilter(self, filter_id)

    * Deletes a message filter in the node.

    * Returns ``True`` if the filter was sucesfully uninstalled, otherwise ``False``

    .. code-block:: python

        >>>web3.geth.shh.deleteMessageFilter('b37c3106cfb683e8f01b5019342399e0d1d74e9160f69b27625faba7a6738554')
        True

.. py:method:: Shh.getMessages(self, filter_id)

    * Retrieve messages that match the filter criteria and are received between the last time this function was called and now.

    * Returns all new messages since the last invocation

    .. code-block:: python

        >>>web3.geth.shh.get_messages('b37c3106cfb683e8f01b5019342399e0d1d74e9160f69b27625faba7a6738554')
        [{
            'ttl': 50,
            'timestamp': 1524497850,
            'topic': HexBytes('0x13370000'),
            'payload': HexBytes('0x74657374206d657373616765203a29'),
            'padding': HexBytes('0x50ab643f1b23bc6df1b1532bb6704ad947c2453366754aade3e3597553eeb96119f4f4299834d9989dc4ecc67e6b6470317bb3f7396ace0417fc0d6d2023900d3'),
            'pow': 6.73892030848329,
            'hash': HexBytes('0x7418f8f0989655ed2f4f9b496e6b1d9be51ef9f0f5ad89f6f750b0eee268b02f'),
            'recipientPublicKey': HexBytes('0x047d36c9e45fa82fcd27d35bc7d2fd41a2e41e512feec9e4b90ee4293ab12dc2cfc98250a6f5689b07650f8a5ca3a6e0fa8808cd0ce1a1962f2551354487a8fc79')
        }]

.. py:method:: Shh.set_max_message_size(self, size)

    * Sets the maximal message size allowed by this node. Incoming and outgoing messages with a larger size will be rejected. Whisper message size can never exceed the limit imposed by the underlying P2P protocol (10 Mb).

    * Returns ``True`` if the filter was sucesfully uninstalled, otherwise ``False``

    .. code-block:: python

        >>>web3.geth.shh.set_max_message_size(1024)
        True

.. py:method:: Shh.set_min_pow(self, min_pow)

    * Sets the minimal PoW required by this node.

    * Returns ``True`` if the filter was sucesfully uninstalled, otherwise ``False``

    .. code-block:: python

        >>>web3.geth.shh.set_min_pow(0.4)
        True

.. py:method:: Shh.mark_trusted_peer(self, enode)

    * Marks specific peer trusted, which will allow it to send historic (expired) messages.

    * Returns ``True`` if the filter was sucesfully uninstalled, otherwise ``False``

    .. code-block:: python

        >>>web3.geth.shh.mark_trusted_peer('enode://d25474361659861e9e651bc728a17e807a3359ca0d344afd544ed0f11a31faecaf4d74b55db53c6670fd624f08d5c79adfc8da5dd4a11b9213db49a3b750845e@52.178.209.125:30379')
        True

---------------
Asymmetric Keys
---------------

.. py:method:: Shh.new_key_pair(self)

    * Generates a new cryptographic identity for the client, and injects it into the known identities for message decryption

    * Returns the new key pair's identity

    .. code-block:: python

        >>>web3.geth.shh.new_key_pair()
        '86e658cbc6da63120b79b5eec0c67d5dcfb6865a8f983eff08932477282b77bb'

.. py:method:: Shh.add_private_key(self, key)

    * Stores a key pair derived from a private key, and returns its ID.

    * Returns the added key pair's ID

    .. code-block:: python

        >>>web3.geth.shh.addPrivateKey('0x7b8190d96cd061a102e551ee36d08d4f3ca1f56fb0008ef5d70c56271d8c46d0')
        '86e658cbc6da63120b79b5eec0c67d5dcfb6865a8f983eff08932477282b77bb'

.. py:method:: Shh.delete_key_pair(self, id)

    * Deletes the specified key if it exists.

    * Returns ``True`` if the key pair was deleted, otherwise ``False``

    .. code-block:: python

        >>>web3.geth.shh.deleteKeyPair('86e658cbc6da63120b79b5eec0c67d5dcfb6865a8f983eff08932477282b77bb')
        True

.. py:method:: Shh.has_key_pair(self, id)

    * Checks if the whisper node has a private key of a key pair matching the given ID.

    * Returns ``True`` if the key pair exists, otherwise ``False``

    .. code-block:: python

        >>>web3.geth.shh.has_key_pair('86e658cbc6da63120b79b5eec0c67d5dcfb6865a8f983eff08932477282b77bb')
        False

.. py:method:: Shh.get_public_key(self, id)

    * Returns the public key associated with the key pair.

    .. code-block:: python

        >>>web3.geth.shh.get_public_key('86e658cbc6da63120b79b5eec0c67d5dcfb6865a8f983eff08932477282b77bb')
        '0x041b0777ceb8cf8748fe0bba5e55039d650a03eb0239a909f9ee345bbbad249f2aa236a4b8f41f51bd0a97d87c08e69e67c51f154d634ba51a224195212fc31e4e'

.. py:method:: Shh.get_private_key(self, id)

    * Returns the private key associated with the key pair.

    .. code-block:: python

        >>>web3.geth.shh.get_private_key('86e658cbc6da63120b79b5eec0c67d5dcfb6865a8f983eff08932477282b77bb')
        '0x7b8190d96cd061a102e551ee36d08d4f3ca1f56fb0008ef5d70c56271d8c46d0'

---------------
Symmetric Keys
---------------

.. py:method:: Shh.new_sym_key(self)

    * Generates a random symmetric key and stores it under id, which is then returned. Will be used in the future for session key exchange

    * Returns the new key pair's identity

    .. code-block:: python

        >>>web3.geth.shh.new_sym_key()
        '6c388d63003deb378700c9dad87f67df0247e660647d6ba1d04321bbc2f6ce0c'

.. py:method:: Shh.addSymKey(self, key)

    * Stores the key, and returns its ID.

    * Returns the new key pair's identity

    .. code-block:: python

        >>>web3.geth.shh.addSymKey('0x58f6556e56a0d41b464a083161377c8a9c2e95156921f954f99ef97d41cebaa2')
        '6c388d63003deb378700c9dad87f67df0247e660647d6ba1d04321bbc2f6ce0c'

.. py:method:: Shh.generate_sym_key_from_password(self)

    * Generates the key from password, stores it, and returns its ID.

    * Returns the new key pair's identity

    .. code-block:: python

        >>>web3.geth.shh.generate_sym_key_from_password('shh secret pwd')
        '6c388d63003deb378700c9dad87f67df0247e660647d6ba1d04321bbc2f6ce0c'

.. py:method:: Shh.has_sym_key(self, id)

    * Checks if there is a symmetric key stored with the given ID.

    * Returns ``True`` if the key exists, otherwise ``False``

    .. code-block:: python

        >>>web3.geth.shh.has_sym_key('6c388d63003deb378700c9dad87f67df0247e660647d6ba1d04321bbc2f6ce0c')
        False

.. py:method:: Shh.get_sym_key(self, id)

    * Returns the symmetric key associated with the given ID.

    * Returns the public key associated with the key pair

    .. code-block:: python

        >>>web3.geth.shh.get_sym_key('6c388d63003deb378700c9dad87f67df0247e660647d6ba1d04321bbc2f6ce0c')
        '0x58f6556e56a0d41b464a083161377c8a9c2e95156921f954f99ef97d41cebaa2'

.. py:method:: Shh.delete_sym_key(self, id)

    * Deletes the symmetric key associated with the given ID.

    * Returns ``True`` if the key pair was deleted, otherwise ``False``

    .. code-block:: python

        >>>web3.geth.shh.delete_sym_key('6c388d63003deb378700c9dad87f67df0247e660647d6ba1d04321bbc2f6ce0c')
        True
