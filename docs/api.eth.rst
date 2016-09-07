Eth API
=======

.. py:class:: Eth

The ``web3.eth`` object exposes methods to interact with the RPC APIs under the
``eth_`` namespace.


.. py:attribute:: Eth.defaultAccount

    The ethereum address that will be used as the default ``from`` address for
    all transactions.  This defaults to ``web3.eth.coinbase``.


.. py:attribute:: Eth.defaultBlock

    The default block number that will be used for any RPC methods that accept
    a block identifier.  Defaults to ``'latest'``.


.. py:attribute:: Eth.syncing

    * Delegates to ``eth_syncing`` RPC Method

    Returns either ``False`` if the node is not syncing or a dictionary
    showing sync status.

    .. code-block:: python

        >>> web3.eth.syncing
        {
            'currentBlock': 2177557,
            'highestBlock': 2211611,
            'knownStates': '0x0',
            'pulledStates': '0x0',
            'startingBlock': 2177365,
        }


.. py:attribute:: Eth.coinbase

    * Delegates to ``eth_coinbase`` RPC Method

    Returns the current *Coinbase* address.

    .. code-block:: python

        >>> web3.eth.coinbase
        '0xd3cda913deb6f67967b99d67acdfa1712c293601'


.. py:attribute:: Eth.mining

    * Delegates to ``eth_mining`` RPC Method

    Returns boolean as to whether the node is currently mining.

    .. code-block:: python

        >>> web3.eth.mining
        False


.. py:attribute:: Eth.hashrate

    * Delegates to ``eth_hashrate`` RPC Method

    Returns the current number of hashes per second the node is mining with.

    .. code-block:: python

        >>> web3.eth.hashrate
        906


.. py:attribute:: Eth.gasPrice

    * Delegates to ``eth_gasPrice`` RPC Method

    Returns the current gas price in Wei.

    .. code-block:: python

        >>> web3.eth.gasPrice
        20000000000


.. py:attribute:: Eth.accounts

    * Delegates to ``eth_accounts`` RPC Method

    Returns the list of known accounts.

    .. code-block:: python

        >>> web3.eth.accounts
        ['0xd3cda913deb6f67967b99d67acdfa1712c293601']


.. py:attribute:: Eth.blockNumber

    * Delegates to ``eth_blockNumber`` RPC Method

    Returns the number of the most recent block

    .. code-block:: python

        >>> web3.eth.blockNumber
        2206939


.. py:method:: Eth.getBalance(account, block_identifier=eth.defaultBlock)

    * Delegates to ``eth_getBalance`` RPC Method

    Returns the balance of the given ``account`` at the block specified by
    ``block_identifier``.

    .. code-block:: python

        >>> web3.eth.getBalance('0xd3cda913deb6f67967b99d67acdfa1712c293601')
        77320681768999138915


.. py:method:: Eth.getStorageAt(account, position, block_identifier=eth.defaultBlock)

    * Delegates to ``eth_getStorageAt`` RPC Method

    Returns the value from a storage position for the given ``account`` at the
    block specified by ``block_identifier``.

    .. code-block:: python

        >>> web3.eth.getStorageAt('0x6c8f2a135f6ed072de4503bd7c4999a1a17f824b', 0)
        '0x00000000000000000000000000000000000000000000000000120a0b063499d4'


.. py:method:: Eth.getCode(account, block_identifier=eth.defaultBlock)

    * Delegates to ``eth_getCode`` RPC Method

    Returns the bytecode for the given ``account`` at the block specified by
    ``block_identifier``.

    .. code-block:: python

        # For a contract address.
        >>> web3.eth.getCode('0x6c8f2a135f6ed072de4503bd7c4999a1a17f824b')
        '0x6060604052361561027c5760e060020a60003504630199.....'
        # For a private key address.
        >>> web3.eth.getCode('0xd3cda913deb6f67967b99d67acdfa1712c293601')
        '0x'


.. py:method:: Eth.getBlock(block_identifier=eth.defaultBlock, full_txns=False)

    * Delegates to ``eth_getBlockByNumber`` or ``eth_getBlockByHash`` RPC Methods

    Returns the block specified by ``block_identifier``.  Delegates to
    ``eth_getBlockByNumber`` if ``block_identifier`` is an integer or one of
    the predefined block parameters ``'latest', 'earliest', 'pending'``,
    otherwise delegates to ``eth_getBlockByHash``.

    If ``full_txns`` is ``True`` then the ``'transactions'`` key will contain
    full transactions objects.  Otherwise it will be an array of transaction
    hashes.

    .. code-block:: python

        >>> web3.eth.getBlock(2000000)
        {
            'difficulty': 49824742724615,
            'extraData': '0xe4b883e5bda9e7a59ee4bb99e9b1bc',
            'gasLimit': 4712388,
            'gasUsed': 21000,
            'hash': '0xc0f4906fea23cf6f3cce98cb44e8e1449e455b28d684dfa9ff65426495584de6',
            'logsBloom': '0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
            'miner': '0x61c808d82a3ac53231750dadc13c777b59310bd9',
            'nonce': '0x3b05c6d5524209f1',
            'number': 2000000,
            'parentHash': '0x57ebf07eb9ed1137d41447020a25e51d30a0c272b5896571499c82c33ecb7288',
            'receiptRoot': '0x84aea4a7aad5c5899bd5cfc7f309cc379009d30179316a2a7baa4a2ea4a438ac',
            'sha3Uncles': '0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347',
            'size': 650,
            'stateRoot': '0x96dbad955b166f5119793815c36f11ffa909859bbfeb64b735cca37cbf10bef1',
            'timestamp': 1470173578,
            'totalDifficulty': 44010101827705409388,
            'transactions': ['0xc55e2b90168af6972193c1f86fa4d7d7b31a29c156665d15b9cd48618b5177ef'],
            'transactionsRoot': '0xb31f174d27b99cdae8e746bd138a01ce60d8dd7b224f7c60845914def05ecc58',
            'uncles': [],
        }


.. py:method:: Eth.getBlockTransactionCount(block_identifier)

    * Delegates to ``eth_getBlockTransactionCountByNumber`` or
      ``eth_getBlockTransactionCountByHash`` RPC Methods

    Returns the number of transactions in the block specified by
    ``block_identifier``.  Delegates to
    ``eth_getBlockTransactionCountByNumber`` if ``block_identifier`` is an
    integer or one of the predefined block parameters ``'latest', 'earliest',
    'pending'``, otherwise delegates to ``eth_getBlockTransactionCountByHash``.

    .. code-block:: python

        >>> web3.eth.getBlockTransactionCount(46147)
        1
