web3.eth API
=============

.. py:module:: web3.eth

.. py:class:: Eth

The ``web3.eth`` object exposes the following properties and methods to
interact with the RPC APIs under the ``eth_`` namespace.

Often, when a property or method returns a mapping of keys to values, it
will return an ``AttributeDict`` which acts like a ``dict`` but you can
access the keys as attributes and cannot modify its fields. For example,
you can find the latest block number in these two ways:

    .. code-block:: python

        >>> block = web3.eth.getBlock('latest')
        AttributeDict({
          'hash': '0xe8ad537a261e6fff80d551d8d087ee0f2202da9b09b64d172a5f45e818eb472a',
          'number': 4022281,
          # ... etc ...
        })

        >>> block['number']
        4022281
        >>> block.number
        4022281

        >>> block.number = 4022282
        Traceback # ... etc ...
        TypeError: This data is immutable -- create a copy instead of modifying


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
        AttributeDict({
            'currentBlock': 2177557,
            'highestBlock': 2211611,
            'knownStates': 0,
            'pulledStates': 0,
            'startingBlock': 2177365,
        })


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

    ``account`` may be a hex address or an ENS name

    .. code-block:: python

        >>> web3.eth.getBalance('0xd3cda913deb6f67967b99d67acdfa1712c293601')
        77320681768999138915


.. py:method:: Eth.getStorageAt(account, position, block_identifier=eth.defaultBlock)

    * Delegates to ``eth_getStorageAt`` RPC Method

    Returns the value from a storage position for the given ``account`` at the
    block specified by ``block_identifier``.

    ``account`` may be a hex address or an ENS name

    .. code-block:: python

        >>> web3.eth.getStorageAt('0x6c8f2a135f6ed072de4503bd7c4999a1a17f824b', 0)
        '0x00000000000000000000000000000000000000000000000000120a0b063499d4'


.. py:method:: Eth.getCode(account, block_identifier=eth.defaultBlock)

    * Delegates to ``eth_getCode`` RPC Method

    Returns the bytecode for the given ``account`` at the block specified by
    ``block_identifier``.

    ``account`` may be a hex address or an ENS name

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
        AttributeDict({
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
        })


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

    .. note:: Method to get an Uncle from its hash is not available through
      RPC, a possible substitute is the method ``Eth.getUncleByBlock``


.. py:method:: Eth.getUncleByBlock(block_identifier, uncle_index)

    * Delegates to ``eth_getUncleByBlockHashAndIndex`` or
      ``eth_getUncleByBlockNumberAndIndex`` RPC methods

    Returns the uncle at the index specified by ``uncle_index``
    from the block specified by ``block_identifier``.  Delegates to
    ``eth_getUncleByBlockNumberAndIndex`` if ``block_identifier`` is an
    integer or one of the predefined block parameters ``'latest', 'earliest',
    'pending'``, otherwise delegates to
    ``eth_getUncleByBlockHashAndIndex``.

    .. code-block:: python

        >>> web3.eth.getUncleByBlock(56160, 0)
        AttributeDict({
          'author': '0xbe4532e1b1db5c913cf553be76180c1777055403',
          'difficulty': '0x17dd9ca0afe',
          'extraData': '0x476574682f686261722f76312e302e312f6c696e75782f676f312e342e32',
          'gasLimit': '0x2fefd8',
          'gasUsed': '0x0',
          'hash': '0xc78c35720d930f9ef34b4e6fb9d02ffec936f9b02a8f0fa858456e4afd4d5614',
          'logsBloom':'0x000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
          'miner': '0xbe4532e1b1db5c913cf553be76180c1777055403',
          'mixHash': '0x041e14603f35a82f6023802fec96ef760433292434a39787514f140950597e5e',
          'nonce': '0x5d2b7e3f1af09995',
          'number': '0xdb5e',
          'parentHash': '0xcc30e8a9b15c548d5bf113c834143a8f0e1909fbfea96b2a208dc154293a78cf',
          'receiptsRoot': '0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421',
          'sealFields': ['0xa0041e14603f35a82f6023802fec96ef760433292434a39787514f140950597e5e', '0x885d2b7e3f1af09995'],
          'sha3Uncles': '0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347',
          'size': None, 'stateRoot': '0x8ce2b1bf8e25a06a8ca34c647ff5fd0fa48ac725cc07f657ae1645ab8ef68c91',
          'timestamp': '0x55c6a972',
          'totalDifficulty': '0xce4c4f0a0b810b',
          'transactions': [],
          'transactionsRoot': '0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421',
          'uncles': []
        })

        # You can also refer to the block by hash:
        >>> web3.eth.getUncleByBlock('0x685b2226cbf6e1f890211010aa192bf16f0a0cba9534264a033b023d7367b845', 0)
        AttributeDict({
            ...
        })


.. py:method:: Eth.getTransaction(transaction_hash)

    * Delegates to ``eth_getTransactionByHAsh`` RPC Method

    Returns the transaction specified by ``transaction_hash``

    .. code-block:: python

        >>> web3.eth.getTransaction('0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060')
        AttributeDict({
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
        })


.. py:method:: Eth.getTransactionFromBlock(block_identifier, transaction_index)

  .. note:: This method is deprecated and replaced by
    ``Eth.getTransactionByBlock``


.. py:method:: Eth.getTransactionByBlock(block_identifier, transaction_index)

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
        AttributeDict({
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
        })
        >>> web3.eth.getTransactionFromBlock('0x4e3a3754410177e6937ef1f84bba68ea139e8d1a2258c5f85db9f1cd715a1bdd', 0)
        AttributeDict({
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
        })


.. py:method:: Eth.waitForTransactionReceipt(transaction_hash, timeout=120)

    Waits for the transaction specified by ``transaction_hash`` to be included in a block, then
    returns its transaction receipt.

    Optionally, specify a ``timeout`` in seconds. If timeout elapses before the transaction
    is added to a block, then :meth:`~Eth.waitForTransactionReceipt` raises a
    :class:`web3.exceptions.TimeExhausted` exception.

    .. code-block:: python

        >>> web3.eth.waitForTransactionReceipt('0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060')
        # If transaction is not yet in a block, time passes, while the thread sleeps...
        # ...
        # Then when the transaction is added to a block, its receipt is returned:
        AttributeDict({
            'blockHash': '0x4e3a3754410177e6937ef1f84bba68ea139e8d1a2258c5f85db9f1cd715a1bdd',
            'blockNumber': 46147,
            'contractAddress': None,
            'cumulativeGasUsed': 21000,
            'from': '0xa1e4380a3b1f749673e270229993ee55f35663b4',
            'gasUsed': 21000,
            'logs': [],
            'logsBloom': '0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
            'status': 1,
            'to': '0x5df9b87991262f6ba471f09758cde1c0fc1de734',
            'transactionHash': '0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060',
            'transactionIndex': 0,
        })


.. py:method:: Eth.getTransactionReceipt(transaction_hash)

    * Delegates to ``eth_getTransactionReceipt`` RPC Method

    Returns the transaction receipt specified by ``transaction_hash``.  If the transaction has not yet been mined returns ``None``

    .. code-block:: python

        >>> web3.eth.getTransactionReceipt('0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060')  # not yet mined
        None
        # wait for it to be mined....
        >>> web3.eth.getTransactionReceipt('0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060')
        AttributeDict({
            'blockHash': '0x4e3a3754410177e6937ef1f84bba68ea139e8d1a2258c5f85db9f1cd715a1bdd',
            'blockNumber': 46147,
            'contractAddress': None,
            'cumulativeGasUsed': 21000,
            'from': '0xa1e4380a3b1f749673e270229993ee55f35663b4',
            'gasUsed': 21000,
            'logs': [],
            'logsBloom': '0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000,
            'status': 1,
            'to': '0x5df9b87991262f6ba471f09758cde1c0fc1de734',
            'transactionHash': '0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060',
            'transactionIndex': 0,
        })


.. py:method:: Eth.getTransactionCount(account, block_identifier=web3.eth.defaultBlock)

    * Delegates to ``eth_getTransactionCount`` RPC Method

    Returns the number of transactions that have been sent from ``account`` as
    of the block specified by ``block_identifier``.

    ``account`` may be a hex address or an ENS name

    .. code-block:: python

        >>> web3.eth.getTransactionCount('0xd3cda913deb6f67967b99d67acdfa1712c293601')
        340


.. py:method:: Eth.sendTransaction(transaction)

    * Delegates to ``eth_sendTransaction`` RPC Method

    Signs and sends the given ``transaction``

    The ``transaction`` parameter should be a dictionary with the following fields.

    * ``from``: ``bytes or text``, hex address or ENS name - (optional, default:
      ``web3.eth.defaultAccount``) The address the transaction is send from.
    * ``to``: ``bytes or text``, hex address or ENS name - (optional when creating new
      contract) The address the transaction is directed to.
    * ``gas``: ``integer`` - (optional, default: 90000) Integer of the gas
      provided for the transaction execution. It will return unused gas.
    * ``gasPrice``: ``integer`` - (optional, default: To-Be-Determined) Integer
      of the gasPrice used for each paid gas
    * ``value``: ``integer`` - (optional) Integer of the value send with this
      transaction
    * ``data``: ``bytes or text`` - The compiled code of a contract OR the hash
      of the invoked method signature and encoded parameters. For details see
      `Ethereum Contract ABI <https://github.com/ethereum/wiki/wiki/Ethereum-Contract-ABI>`_.
    * ``nonce``: ``integer`` - (optional) Integer of a nonce. This allows to
      overwrite your own pending transactions that use the same nonce.

    If the ``transaction`` specifies a ``data`` value but does not specify
    ``gas`` then the ``gas`` value will be populated using the
    :meth:`~web3.eth.Eth.estimateGas()` function with an additional buffer of ``100000``
    gas up to the ``gasLimit`` of the latest block.  In the event that the
    value returned by :meth:`~web3.eth.Eth.estimateGas()` method is greater than the
    ``gasLimit`` a ``ValueError`` will be raised.


    .. code-block:: python

        >>> web3.eth.sendTransaction({'to': '0xd3cda913deb6f67967b99d67acdfa1712c293601', 'from': web3.eth.coinbase, 'value': 12345})
        '0xe670ec64341771606e55d6b4ca35a1a6b75ee3d5145a99d05921026d1527331'


.. py:method:: Eth.sendRawTransaction(raw_transaction)

    * Delegates to ``eth_sendRawTransaction`` RPC Method

    Sends a signed and serialized transaction. Returns the transaction hash.

    .. code-block:: python

        >>> signed_txn = w3.eth.account.signTransaction(dict(
            nonce=w3.eth.getTransactionCount(w3.eth.coinbase),
            gasPrice=w3.eth.gasPrice,
            gas=100000,
            to='0xd3cda913deb6f67967b99d67acdfa1712c293601',
            value=12345,
            data=b'',
          ),
          private_key_for_senders_account,
        )
        >>> w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        '0xe670ec64341771606e55d6b4ca35a1a6b75ee3d5145a99d05921026d1527331'


.. py:method:: Eth.replaceTransaction(transaction_hash, new_transaction)

    * Delegates to ``eth_sendTransaction`` RPC Method

    Sends a transaction that replaces the transaction with ``transaction_hash``.

    The ``transaction_hash`` must be the hash of a pending transaction.

    The ``new_transaction`` parameter should be a dictionary with transaction fields
    as required by :meth:`~web3.eth.Eth.sendTransaction`. It will be used to entirely
    replace the transaction of ``transaction_hash`` without using any of the pending
    transaction's values.

    If the ``new_transaction`` specifies a ``nonce`` value, it must match the pending
    transaction's nonce.

    If the ``new_transaction`` specifies a ``gasPrice`` value, it must be greater than
    the pending transaction's ``gasPrice``.

    If the ``new_transaction`` does not specify a ``gasPrice`` value, the highest of the
    following 2 values will be used:

    * The pending transaction's ``gasPrice`` * 1.1 - This is typically the minimum
      ``gasPrice`` increase a node requires before it accepts a replacement transaction.
    * The ``gasPrice`` as calculated by the current gas price strategy(See :ref:`Gas_Price`).

    This method returns the transaction hash of the replacement transaction.

    .. code-block:: python

        >>> tx = web3.eth.sendTransaction({
                'to': '0xd3cda913deb6f67967b99d67acdfa1712c293601',
                'from': web3.eth.coinbase,
                'value': 1000
            })
        '0xe670ec64341771606e55d6b4ca35a1a6b75ee3d5145a99d05921026d1527331'
        >>> web3.eth.replaceTransaction('0xe670ec64341771606e55d6b4ca35a1a6b75ee3d5145a99d05921026d1527331', {
                'to': '0xd3cda913deb6f67967b99d67acdfa1712c293601',
                'from': web3.eth.coinbase,
                'value': 2000
            })


.. py:method:: Eth.modifyTransaction(transaction_hash, **transaction_params)

    * Delegates to ``eth_sendTransaction`` RPC Method

    Sends a transaction that modifies the transaction with ``transaction_hash``.

    ``transaction_params`` are keyword arguments that correspond to valid transaction
    parameters as required by :meth:`~web3.eth.Eth.sendTransaction`. The parameter values
    will override the pending transaction's values to create the replacement transaction
    to send.

    The same validation and defaulting rules of :meth:`~web3.eth.Eth.replaceTransaction` apply.

    This method returns the transaction hash of the newly modified transaction.

    .. code-block:: python

        >>> tx = web3.eth.sendTransaction({
                'to': '0xd3cda913deb6f67967b99d67acdfa1712c293601',
                'from': web3.eth.coinbase,
                'value': 1000
            })
        '0xe670ec64341771606e55d6b4ca35a1a6b75ee3d5145a99d05921026d1527331'
        >>> web3.eth.modifyTransaction('0xe670ec64341771606e55d6b4ca35a1a6b75ee3d5145a99d05921026d1527331', value=2000)


.. py:method:: Eth.sign(account, data=None, hexstr=None, text=None)

    * Delegates to ``eth_sign`` RPC Method

    Caller must specify exactly one of: ``data``, ``hexstr``, or ``text``.

    Signs the given data with the private key of the given ``account``.
    The account must be unlocked.

    ``account`` may be a hex address or an ENS name

    .. code-block:: python

        >>> web3.eth.sign(
              '0xd3cda913deb6f67967b99d67acdfa1712c293601',
              text='some-text-tö-sign')
        '0x1a8bbe6eab8c72a219385681efefe565afd3accee35f516f8edf5ae82208fbd45a58f9f9116d8d88ba40fcd29076d6eada7027a3b412a9db55a0164547810cc401'

        >>> web3.eth.sign(
              '0xd3cda913deb6f67967b99d67acdfa1712c293601',
              data=b'some-text-t\xc3\xb6-sign')
        '0x1a8bbe6eab8c72a219385681efefe565afd3accee35f516f8edf5ae82208fbd45a58f9f9116d8d88ba40fcd29076d6eada7027a3b412a9db55a0164547810cc401'

        >>> web3.eth.sign(
              '0xd3cda913deb6f67967b99d67acdfa1712c293601',
              hexstr='0x736f6d652d746578742d74c3b62d7369676e')
        '0x1a8bbe6eab8c72a219385681efefe565afd3accee35f516f8edf5ae82208fbd45a58f9f9116d8d88ba40fcd29076d6eada7027a3b412a9db55a0164547810cc401'


.. py:method:: Eth.call(transaction, block_identifier=web3.eth.defaultBlock)

    * Delegates to ``eth_call`` RPC Method

    Executes the given transaction locally without creating a new transaction
    on the blockchain.  Returns the return value of the executed contract.

    The ``transaction`` parameter is handled in the same manner as the
    :meth:`~web3.eth.Eth.sendTransaction()` method.

    .. code-block:: python

        >>> myContract.functions.setVar(1).transact()
        HexBytes('0x79af0c7688afba7588c32a61565fd488c422da7b5773f95b242ea66d3d20afda')
        >>> myContract.functions.getVar().call()
        1
        # The above call equivalent to the raw call:
        >>> we3.eth.call({'value': 0, 'gas': 21736, 'gasPrice': 1, 'to': '0xc305c901078781C232A2a521C2aF7980f8385ee9', 'data': '0x477a5c98'})
        HexBytes('0x0000000000000000000000000000000000000000000000000000000000000001')

    In most cases it is better to make contract function call through the :py:class:`web3.contract.Contract` interface.


.. py:method:: Eth.estimateGas(transaction, block_identifier=None)

    * Delegates to ``eth_estimateGas`` RPC Method

    Executes the given transaction locally without creating a new transaction
    on the blockchain.  Returns amount of gas consumed by execution which can
    be used as a gas estimate.

    The ``transaction`` and ``block_identifier`` parameters are handled in the
    same manner as the :meth:`~web3.eth.call()` method.

    .. code-block:: python

        >>> web3.eth.estimateGas({'to': '0xd3cda913deb6f67967b99d67acdfa1712c293601', 'from': web3.eth.coinbase, 'value': 12345})
        21000

    .. note::
        The parameter ``block_identifier`` is not enabled in geth nodes,
        hence passing a value of ``block_identifier`` when connected to a geth
        nodes would result in an error like:  ``ValueError: {'code': -32602, 'message': 'too many arguments, want at most 1'}``


.. py:method:: Eth.generateGasPrice(transaction_params=None)

    Uses the selected gas price strategy to calculate a gas price. This method
    returns the gas price denominated in wei.

    The `transaction_params` argument is optional however some gas price strategies
    may require it to be able to produce a gas price.

    .. code-block:: python

        >>> Web3.eth.generateGasPrice()
        20000000000

    .. note::
        For information about how gas price can be customized in web3 see
        :ref:`Gas_Price`.

.. py:method:: Eth.setGasPriceStrategy(gas_price_strategy)

    Set the selected gas price strategy. It must be a method of the signature
    ``(web3, transaction_params)`` and return a gas price denominated in wei.

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

        >>> filt = web3.eth.filter()
        >>> web3.eth.getFilterChanges(filt.filter_id)
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

        >>> filt = web3.eth.filter()
        >>> web3.eth.getFilterLogs(filt.filter_id)
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

        >>> filt = web3.eth.filter()
        >>> web3.eth.uninstallFilter(filt.filter_id)
        True
        >>> web3.eth.uninstallFilter(filt.filter_id)
        False  # already uninstalled.


.. py:method:: Eth.getLogs(filter_params)

    This is the equivalent of: creating a new
    filter, running :meth:`~Eth.getFilterLogs`, and then uninstalling the filter. See
    :meth:`~Eth.filter` for details on allowed filter parameters.


Contracts
---------

.. py:method:: Eth.contract(address=None, contract_name=None, ContractFactoryClass=Contract, **contract_factory_kwargs)

    If ``address`` is provided, then this method will return an instance of the
    contract defined by ``abi``. The address may be a hex string,
    or an ENS name like ``'mycontract.eth'``.

    .. code-block:: python

        from web3 import Web3

        w3 = Web3(...)

        contract = w3.eth.contract(address='0x000000000000000000000000000000000000dead', abi=...)

        # alternatively:
        contract = w3.eth.contract(address='mycontract.eth', abi=...)

    .. note::

        If you use an ENS name to initialize a contract, the contract will be looked up by
        name on each use. If the name could ever change maliciously, first
        :ref:`ens_get_address`, and then create the contract with the hex address.


    If ``address`` is *not* provided, the newly created contract class will be returned. That
    class will then be initialized by supplying the address.

    .. code-block:: python

        from web3 import Web3

        w3 = Web3(...)

        Contract = w3.eth.contract(abi=...)

        # later, initialize contracts with the same metadata at different addresses:
        contract1 = Contract(address='0x000000000000000000000000000000000000dead')
        contract2 = Contract(address='mycontract.eth')

    ``contract_name`` will be used as the name of the contract class.  If it is
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

.. py:method:: Eth.setContractFactory(contractFactoryClass)

    Modify the default contract factory from ``Contract`` to ``contractFactoryClass``.
    Future calls to ``Eth.contract()`` will then default to ``contractFactoryClass``.

    An example of an alternative Contract Factory is ``ConciseContract``.
