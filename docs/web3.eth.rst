Eth API
=======

.. py:module:: web3.eth
.. py:currentmodule:: web3.eth

.. py:class:: Eth

The ``web3.eth`` object exposes the following properties and methods to
interact with the RPC APIs under the ``eth_`` namespace.


Properties
----------

The following properties are available on the ``web3.eth`` namespace.


.. py:attribute:: Eth.defaultAccount

    The ethereum address that will be used as the default ``from`` address for
    all transactions.


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


Methods
-------

The following methods are available on the ``web3.eth`` namespace.


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


.. py:method:: Eth.getBlock(block_identifier=eth.defaultBlock, full_transactions=False)

    * Delegates to ``eth_getBlockByNumber`` or ``eth_getBlockByHash`` RPC Methods

    Returns the block specified by ``block_identifier``.  Delegates to
    ``eth_getBlockByNumber`` if ``block_identifier`` is an integer or one of
    the predefined block parameters ``'latest', 'earliest', 'pending'``,
    otherwise delegates to ``eth_getBlockByHash``.

    If ``full_transactions`` is ``True`` then the ``'transactions'`` key will
    contain full transactions objects.  Otherwise it will be an array of
    transaction hashes.

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
        >>> web3.eth.getBlockTransactionCount('0x4e3a3754410177e6937ef1f84bba68ea139e8d1a2258c5f85db9f1cd715a1bdd')  # block 46147
        1


.. py:method:: Eth.getUncle(block_identifier)

    .. note:: Not Implemented


.. py:method:: Eth.getTransaction(transaction_hash)

    * Delegates to ``eth_getTransactionByHAsh`` RPC Method

    Returns the transaction specified by ``transaction_hash``

    .. code-block:: python

        >>> web3.eth.getTransaction('0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060')
        {
            'blockHash': '0x4e3a3754410177e6937ef1f84bba68ea139e8d1a2258c5f85db9f1cd715a1bdd',
            'blockNumber': 46147,
            'from': '0xa1e4380a3b1f749673e270229993ee55f35663b4',
            'gas': 21000,
            'gasPrice': 50000000000000,
            'hash': '0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060',
            'input': '0x',
            'nonce': 0,
            'to': '0x5df9b87991262f6ba471f09758cde1c0fc1de734',
            'transactionIndex': 0,
            'value': 31337,
        }


.. py:method:: Eth.getTransactionFromBlock(block_identifier, transaction_index)

    * Delegates to ``eth_getTransactionByBlockNumberAndIndex`` or
      ``eth_getTransactionByBlockHashAndIndex`` RPC Methods

    Returns the transaction at the index specified by ``transaction_index``
    from the block specified by ``block_identifier``.  Delegates to
    ``eth_getTransactionByBlockNumberAndIndex`` if ``block_identifier`` is an
    integer or one of the predefined block parameters ``'latest', 'earliest',
    'pending'``, otherwise delegates to
    ``eth_getTransactionByBlockHashAndIndex``.

    .. code-block:: python

        >>> web3.eth.getTransactionFromBlock(46147, 0)
        {
            'blockHash': '0x4e3a3754410177e6937ef1f84bba68ea139e8d1a2258c5f85db9f1cd715a1bdd',
            'blockNumber': 46147,
            'from': '0xa1e4380a3b1f749673e270229993ee55f35663b4',
            'gas': 21000,
            'gasPrice': 50000000000000,
            'hash': '0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060',
            'input': '0x',
            'nonce': 0,
            'to': '0x5df9b87991262f6ba471f09758cde1c0fc1de734',
            'transactionIndex': 0,
            'value': 31337,
        }
        >>> web3.eth.getTransactionFromBlock('0x4e3a3754410177e6937ef1f84bba68ea139e8d1a2258c5f85db9f1cd715a1bdd', 0)
        {
            'blockHash': '0x4e3a3754410177e6937ef1f84bba68ea139e8d1a2258c5f85db9f1cd715a1bdd',
            'blockNumber': 46147,
            'from': '0xa1e4380a3b1f749673e270229993ee55f35663b4',
            'gas': 21000,
            'gasPrice': 50000000000000,
            'hash': '0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060',
            'input': '0x',
            'nonce': 0,
            'to': '0x5df9b87991262f6ba471f09758cde1c0fc1de734',
            'transactionIndex': 0,
            'value': 31337,
        }


.. py:method:: Eth.getTransactionReceipt(transaction_hash)

    * Delegates to ``eth_getTransactionReceipt`` RPC Method

    Returns the transaction receipt specified by ``transaction_hash``.  If the transaction has not yet been mined returns ``None``

    .. code-block:: python

        >>> web3.eth.getTransactionReceipt('0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060')  # not yet mined
        None
        # wait for it to be mined....
        >>> web3.eth.getTransactionReceipt('0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060')
        {
            'blockHash': '0x4e3a3754410177e6937ef1f84bba68ea139e8d1a2258c5f85db9f1cd715a1bdd',
            'blockNumber': 46147,
            'contractAddress': None,
            'cumulativeGasUsed': 21000,
            'from': '0xa1e4380a3b1f749673e270229993ee55f35663b4',
            'gasUsed': 21000,
            'logs': [],
            'root': '96a8e009d2b88b1483e6941e6812e32263b05683fac202abc622a3e31aed1957',
            'to': '0x5df9b87991262f6ba471f09758cde1c0fc1de734',
            'transactionHash': '0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060',
            'transactionIndex': 0,
        }


.. py:method:: Eth.getTransactionCount(account, block_identifier=web3.eth.defaultBlock)

    * Delegates to ``eth_getTransactionCount`` RPC Method

    Returns the number of transactions that have been sent from ``account`` as
    of the block specified by ``block_identifier``.

    .. code-block:: python

        >>> web3.eth.getTransactionCount('0xd3cda913deb6f67967b99d67acdfa1712c293601')
        340


.. py:method:: Eth.sendTransaction(transaction)

    * Delegates to ``eth_sendTransaction`` RPC Method

    Signs and sends the given ``transaction``

    The ``transaction`` parameter should be a dictionary with the following fields.

    * ``from``: ``bytes or text``, 20 Bytes - (optional, default:
      ``web3.eth.defaultAccount``) The address the transaction is send from.
    * ``to``: ``bytes or text``, 20 Bytes - (optional when creating new
      contract) The address the transaction is directed to.
    * ``gas``: ``integer`` - (optional, default: 90000) Integer of the gas
      provided for the transaction execution. It will return unused gas.
    * ``gasPrice``: ``integer`` - (optional, default: To-Be-Determined) Integer
      of the gasPrice used for each paid gas
    * ``value``: ``integer`` - (optional) Integer of the value send with this
      transaction
    * ``data``: ``bytes or text`` - The compiled code of a contract OR the hash
      of the invoked method signature and encoded parameters. For details see
      Ethereum Contract ABI
    * ``nonce``: ``integer`` - (optional) Integer of a nonce. This allows to
      overwrite your own pending transactions that use the same nonce.

    If the ``transaction`` specifies a ``data`` value but does not specify
    ``gas`` then the ``gas`` value will be populated using the
    ``web3.eth.estimateGas()`` function with an additional buffer of ``100000``
    gas up to the ``gasLimit`` of the latest block.  In the event that the
    value returned by ``web3.eth.estimateGas()`` method is greater than the
    ``gasLimit`` a ``ValueError`` will be raised.


    .. code-block:: python

        >>> web3.eth.sendTransaction({'to': '0xd3cda913deb6f67967b99d67acdfa1712c293601', 'from': web3.eth.coinbase, 'value': 12345})
        '0xe670ec64341771606e55d6b4ca35a1a6b75ee3d5145a99d05921026d1527331'


.. py:method:: Eth.sendRawTransaction(raw_transaction)

    * Delegates to ``eth_sendRawTransaction`` RPC Method

    Sends a signed and serialized transaction.

    .. code-block:: python

        >>> import rlp
        >>> from ethereum.transactions import Transaction
        >>> tx = Transaction(
            nonce=web3.eth.getTransactionCount(web3.eth.coinbase),
            gasprice=web3.eth.gasPrice,
            startgas=100000,
            to='0xd3cda913deb6f67967b99d67acdfa1712c293601',
            value=12345,
            data='',
        )
        >>> tx.sign(the_private_key_for_the_from_account)
        >>> raw_tx = rlp.encode(tx)
        >>> raw_tx_hex = web3.toHex(raw_tx)
        >>> web3.eth.sendRawTransaction(raw_tx_hex)
        '0xe670ec64341771606e55d6b4ca35a1a6b75ee3d5145a99d05921026d1527331'


.. py:method:: Eth.sign(account, data)

    * Delegates to ``eth_sign`` RPC Method

    Signs the given ``data`` with the private key of the given ``account``.
    The account must be unlocked.

    .. code-block:: python

        >>> web3.eth.sign('0xd3cda913deb6f67967b99d67acdfa1712c293601', 'some-text-to-sign')
        '0x1a8bbe6eab8c72a219385681efefe565afd3accee35f516f8edf5ae82208fbd45a58f9f9116d8d88ba40fcd29076d6eada7027a3b412a9db55a0164547810cc401'


.. py:method:: Eth.call(transaction, block_identifier=web3.eth.defaultBlock)

    * Delegates to ``eth_call`` RPC Method

    Executes the given transaction locally without creating a new transaction
    on the blockchain.  Returns the return value of the executed contract.

    The ``transaction`` parameter is handled in the same manner as the
    ``web3.eth.sendTransaction()`` method.

    .. code-block:: python

        >>> web3.eth.sign('0xd3cda913deb6f67967b99d67acdfa1712c293601', 'some-text-to-sign')
        '0x1a8bbe6eab8c72a219385681efefe565afd3accee35f516f8edf5ae82208fbd45a58f9f9116d8d88ba40fcd29076d6eada7027a3b412a9db55a0164547810cc401'


.. py:method:: Eth.estimateGas(transaction)

    * Delegates to ``eth_estimateGas`` RPC Method

    Executes the given transaction locally without creating a new transaction
    on the blockchain.  Returns amount of gas consumed by execution which can
    be used as a gas estimate.

    .. code-block:: python

        >>> web3.eth.estimateGas({'to': '0xd3cda913deb6f67967b99d67acdfa1712c293601', 'from': web3.eth.coinbase, 'value': 12345})
        21000


Filters
-------

The following methods are available on the ``web3.eth`` object for interacting
with the filtering API.


.. py:method:: Eth.filter(filter_params)

    * Delegates to ``eth_newFilter``, ``eth_newBlockFilter``, and
      ``eth_newPendingTransactionFilter`` RPC Methods.

    This method delegates to one of three RPC methods depending on the value of
    ``filter_params``.

    * If ``filter_params`` is the string ``'pending'`` then a new filter is
      registered using the ``eth_newPendingTransactionFilter`` RPC method.
      This will create a new filter that will be called for each new unmined
      transaction that the node receives.
    * If ``filter_params`` is the string ``'latest'`` then a new filter is
      registered using the ``eth_newBlockFilter`` RPC method.  This will create
      a new filter that will be called each time the node receives a new block.
    * If ``filter_params`` is a dictionary then a new filter is registered
      using the ``eth_newFilter`` RPC method.  This will create a new filter
      that will be called for all log entries that match the provided
      ``filter_params``.

    This method returns a ``web3.utils.filters.Filter`` object which can then
    be used to either directly fetch the results of the filter or to register
    callbacks which will be called with each result of the filter.

    When creating a new log filter, the ``filter_params`` should be a
    dictionary with the following keys.

    * ``fromBlock``: ``integer/tag`` - (optional, default: "latest") Integer
      block number, or "latest" for the last mined block or "pending",
      "earliest" for not yet mined transactions.
    * ``toBlock``: ``integer/tag`` - (optional, default: "latest") Integer
      block number, or "latest" for the last mined block or "pending",
      "earliest" for not yet mined transactions.
    * ``address``: ``string`` or list of ``strings``, each 20 Bytes -
      (optional) Contract address or a list of addresses from which logs should
      originate.
    * ``topics``: list of 32 byte ``strings`` or ``null`` - (optional) Array of
      topics that should be used for filtering.  Topics are order-dependent.
      This parameter can also be a list of topic lists in which case filtering
      will match any of the provided topic arrays.


    See :doc:`./filters` for more information about filtering.

    .. code-block:: python

        >>> web3.eth.filter('latest')
        <BlockFilter at 0x10b72dc28>
        >>> web3.eth.filter('pending')
        <TransactionFilter at 0x10b780340>
        >>> web3.eth.filter({'fromBlock': 1000000, 'toBlock': 1000100, 'address': '0x6c8f2a135f6ed072de4503bd7c4999a1a17f824b'})
        <LogFilter at 0x10b7803d8>

.. py:method:: Eth.getFilterChanges(self, filter_id)

    * Delegates to ``eth_getFilterChanges`` RPC Method.

    Returns all new entries which occurred since the last call to this method
    for the given ``filter_id``

    .. code-block:: python

        >>> filter = web3.eth.filter()
        >>> web3.eth.getFilterChanges(filter.filter_id)
        [
            {
                'address': '0xdc3a9db694bcdd55ebae4a89b22ac6d12b3f0c24',
                'blockHash': '0xb72256286ca528e09022ffd408856a73ef90e7216ac560187c6e43b4c4efd2f0',
                'blockNumber': 2217196,
                'data': '0x0000000000000000000000000000000000000000000000000000000000000001',
                'logIndex': 0,
                'topics': ['0xe65b00b698ba37c614af350761c735c5f4a82b4ab365a1f1022d49d9dfc8e930',
                '0x000000000000000000000000754c50465885f1ed1fa1a55b95ee8ecf3f1f4324',
                '0x296c7fb6ccafa3e689950b947c2895b07357c95b066d5cdccd58c301f41359a3'],
                'transactionHash': '0xfe1289fd3915794b99702202f65eea2e424b2f083a12749d29b4dd51f6dce40d',
                'transactionIndex': 1,
            },
            ...
        ]


.. py:method:: Eth.getFilterLogs(self, filter_id)

    * Delegates to ``eth_getFilterLogs`` RPC Method.

    Returns all entries for the given ``filter_id``

    .. code-block:: python

        >>> filter = web3.eth.filter()
        >>> web3.eth.getFilterLogs(filter.filter_id)
        [
            {
                'address': '0xdc3a9db694bcdd55ebae4a89b22ac6d12b3f0c24',
                'blockHash': '0xb72256286ca528e09022ffd408856a73ef90e7216ac560187c6e43b4c4efd2f0',
                'blockNumber': 2217196,
                'data': '0x0000000000000000000000000000000000000000000000000000000000000001',
                'logIndex': 0,
                'topics': ['0xe65b00b698ba37c614af350761c735c5f4a82b4ab365a1f1022d49d9dfc8e930',
                '0x000000000000000000000000754c50465885f1ed1fa1a55b95ee8ecf3f1f4324',
                '0x296c7fb6ccafa3e689950b947c2895b07357c95b066d5cdccd58c301f41359a3'],
                'transactionHash': '0xfe1289fd3915794b99702202f65eea2e424b2f083a12749d29b4dd51f6dce40d',
                'transactionIndex': 1,
            },
            ...
        ]


.. py:method:: Eth.uninstallFilter(self, filter_id)

    * Delegates to ``eth_uninstallFilter`` RPC Method.

    Uninstalls the filter specified by the given ``filter_id``.  Returns
    boolean as to whether the filter was successfully uninstalled.

    .. code-block:: python

        >>> filter = web3.eth.filter()
        >>> web3.eth.uninstallFilter(filter.filter_id)
        True
        >>> web3.eth.uninstallFilter(filter.filter_id)
        False  # already uninstalled.


Contracts
---------

.. py:method:: Eth.contract(address=None, contract_name=None, ContractFactoryClass=Contract, **contract_factory_kwargs)

    If ``address`` is provided then this method will return an instance of the
    contract defined by ``abi``.  Otherwise the newly created contract class
    will be returned.

    ``contract_name`` will be used as the name of the contract class.  If
    ``None`` then the name of the ``ContractFactoryClass`` will be used.

    ``ContractFactoryClass`` will be used as the base Contract class.

    The following arguments are accepted for contract class creation.

    - ``abi``
    - ``asm``
    - ``ast``
    - ``bytecode``
    - ``bytecode_runtime``
    - ``clone_bin``
    - ``dev_doc``
    - ``interface``
    - ``metadata``
    - ``opcodes``
    - ``src_map``
    - ``src_map_runtime``
    - ``user_doc``

    See :doc:`./contracts` for more information about how to use contracts.
