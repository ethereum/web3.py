.. _eth-account:

Working with Local Private Keys
==========================================

.. _local_vs_hosted:

Local vs Hosted Nodes
---------------------------------

Local Node
  A local node is started and controlled by you. It is as safe as you keep it.
  When you run ``geth`` or ``parity`` on your machine, you are running a local node.

Hosted Node
  A hosted node is controlled by someone else. When you connect to Infura, you are
  connected to a hosted node.

Local vs Hosted Keys
---------------------------------

Local Private Key
  A key is 32 :class:`bytes` of data that you can use to sign transactions and messages,
  before sending them to your node.
  You must use :meth:`~web3.eth.Eth.send_raw_transaction`
  when working with local keys, instead of
  :meth:`~web3.eth.Eth.send_transaction` .

Hosted Private Key
  This is a common way to use accounts with local nodes.
  Each account returned by :attr:`w3.eth.accounts <web3.eth.Eth.accounts>`
  has a hosted private key stored in your node.
  This allows you to use :meth:`~web3.eth.Eth.send_transaction`.


.. WARNING::
  It is unacceptable for a hosted node to offer hosted private keys. It
  gives other people complete control over your account. "Not your keys,
  not your Ether" in the wise words of Andreas Antonopoulos.

Some Common Uses for Local Private Keys
-------------------------------------------

A very common reason to work with local private keys is to interact
with a hosted node.

Some common things you might want to do with a `Local Private Key` are:

- `Sign a Transaction`_
- `Sign a Contract Transaction`_
- `Sign a Message`_
- `Verify a Message`_

Using private keys usually involves ``w3.eth.account`` in one way or another. Read on for more,
or see a full list of things you can do in the docs for
:class:`eth_account.Account <eth_account.account.Account>`.

.. _extract_geth_pk:

Extract private key from geth keyfile
---------------------------------------------

.. NOTE::
  The amount of available ram should be greater than 1GB.

.. code-block:: python

    with open('~/.ethereum/keystore/UTC--...--5ce9454909639D2D17A3F753ce7d93fa0b9aB12E') as keyfile:
        encrypted_key = keyfile.read()
        private_key = w3.eth.account.decrypt(encrypted_key, 'correcthorsebatterystaple')
        # tip: do not save the key or password anywhere, especially into a shared source file

Sign a Message
---------------

.. WARNING:: There is no single message format that is broadly adopted
    with community consensus. Keep an eye on several options,
    like `EIP-683 <https://github.com/ethereum/EIPs/pull/683>`_,
    `EIP-712 <https://github.com/ethereum/EIPs/pull/712>`_, and
    `EIP-719 <https://github.com/ethereum/EIPs/pull/719>`_. Consider
    the :meth:`w3.eth.sign() <web3.eth.Eth.sign>` approach be deprecated.

For this example, we will use the same message hashing mechanism that
is provided by :meth:`w3.eth.sign() <web3.eth.Eth.sign>`.

.. doctest::

    >>> from web3.auto import w3
    >>> from eth_account.messages import encode_defunct

    >>> msg = "I♥SF"
    >>> private_key = b"\xb2\\}\xb3\x1f\xee\xd9\x12''\xbf\t9\xdcv\x9a\x96VK-\xe4\xc4rm\x03[6\xec\xf1\xe5\xb3d"
    >>> message = encode_defunct(text=msg)
    >>> signed_message = w3.eth.account.sign_message(message, private_key=private_key)
    >>> signed_message
    SignedMessage(messageHash=HexBytes('0x1476abb745d423bf09273f1afd887d951181d25adc66c4834a70491911b7f750'),
     r=104389933075820307925104709181714897380569894203213074526835978196648170704563,
     s=28205917190874851400050446352651915501321657673772411533993420917949420456142,
     v=28,
     signature=HexBytes('0xe6ca9bba58c88611fad66a6ce8f996908195593807c4b38bd528d2cff09d4eb33e5bfbbf4d3e39b1a2fd816a7680c19ebebaf3a141b239934ad43cb33fcec8ce1c'))

Verify a Message
------------------------------------------------

With the original message text and a signature:

.. doctest::

    >>> message = encode_defunct(text="I♥SF")
    >>> w3.eth.account.recover_message(message, signature=signed_message.signature)
    '0x5ce9454909639D2D17A3F753ce7d93fa0b9aB12E'

Verify a Message from message hash
-----------------------------------------------------------

Sometimes, for historical reasons, you don't have the original message,
all you have is the prefixed & hashed message. To verify it, use:

.. CAUTION:: This method is deprecated, only having a hash typically indicates that
    you're using some old kind of mechanism. Expect this method to go away in the
    next major version upgrade.

.. doctest::

    >>> message_hash = '0x1476abb745d423bf09273f1afd887d951181d25adc66c4834a70491911b7f750'
    >>> signature = '0xe6ca9bba58c88611fad66a6ce8f996908195593807c4b38bd528d2cff09d4eb33e5bfbbf4d3e39b1a2fd816a7680c19ebebaf3a141b239934ad43cb33fcec8ce1c'
    >>> w3.eth.account.recoverHash(message_hash, signature=signature)
    '0x5ce9454909639D2D17A3F753ce7d93fa0b9aB12E'

Prepare message for ecrecover in Solidity
--------------------------------------------

Let's say you want a contract to validate a signed message,
like if you're making payment channels, and you want to
validate the value in Remix or web3.js.

You might have produced the signed_message locally, as in
`Sign a Message`_. If so, this will prepare it for Solidity:

.. doctest::

    >>> from web3 import Web3

    # ecrecover in Solidity expects v as a native uint8, but r and s as left-padded bytes32
    # Remix / web3.js expect r and s to be encoded to hex
    # This convenience method will do the pad & hex for us:
    >>> def to_32byte_hex(val):
    ...   return Web3.toHex(Web3.toBytes(val).rjust(32, b'\0'))

    >>> ec_recover_args = (msghash, v, r, s) = (
    ...   Web3.toHex(signed_message.messageHash),
    ...   signed_message.v,
    ...   to_32byte_hex(signed_message.r),
    ...   to_32byte_hex(signed_message.s),
    ... )
    >>> ec_recover_args
    ('0x1476abb745d423bf09273f1afd887d951181d25adc66c4834a70491911b7f750',
     28,
     '0xe6ca9bba58c88611fad66a6ce8f996908195593807c4b38bd528d2cff09d4eb3',
     '0x3e5bfbbf4d3e39b1a2fd816a7680c19ebebaf3a141b239934ad43cb33fcec8ce')

Instead, you might have received a message and a signature encoded to hex. Then
this will prepare it for Solidity:

.. doctest::

    >>> from web3 import Web3
    >>> from eth_account.messages import encode_defunct, _hash_eip191_message

    >>> hex_message = '0x49e299a55346'
    >>> hex_signature = '0xe6ca9bba58c88611fad66a6ce8f996908195593807c4b38bd528d2cff09d4eb33e5bfbbf4d3e39b1a2fd816a7680c19ebebaf3a141b239934ad43cb33fcec8ce1c'

    # ecrecover in Solidity expects an encoded version of the message

    # - encode the message
    >>> message = encode_defunct(hexstr=hex_message)

    # - hash the message explicitly
    >>> message_hash = _hash_eip191_message(message)

    # Remix / web3.js expect the message hash to be encoded to a hex string
    >>> hex_message_hash = Web3.toHex(message_hash)

    # ecrecover in Solidity expects the signature to be split into v as a uint8,
    #   and r, s as a bytes32
    # Remix / web3.js expect r and s to be encoded to hex
    >>> sig = Web3.toBytes(hexstr=hex_signature)
    >>> v, hex_r, hex_s = Web3.toInt(sig[-1]), Web3.toHex(sig[:32]), Web3.toHex(sig[32:64])

    # ecrecover in Solidity takes the arguments in order = (msghash, v, r, s)
    >>> ec_recover_args = (hex_message_hash, v, hex_r, hex_s)
    >>> ec_recover_args
    ('0x1476abb745d423bf09273f1afd887d951181d25adc66c4834a70491911b7f750',
     28,
     '0xe6ca9bba58c88611fad66a6ce8f996908195593807c4b38bd528d2cff09d4eb3',
     '0x3e5bfbbf4d3e39b1a2fd816a7680c19ebebaf3a141b239934ad43cb33fcec8ce')


Verify a message with ecrecover in Solidity
---------------------------------------------

Create a simple ecrecover contract in `Remix <https://remix.ethereum.org/>`_:

.. code-block:: none

    pragma solidity ^0.4.19;

    contract Recover {
      function ecr (bytes32 msgh, uint8 v, bytes32 r, bytes32 s) public pure
      returns (address sender) {
        return ecrecover(msgh, v, r, s);
      }
    }

Then call ecr with these arguments from `Prepare message for ecrecover in Solidity`_ in Remix,
``"0x1476abb745d423bf09273f1afd887d951181d25adc66c4834a70491911b7f750", 28, "0xe6ca9bba58c88611fad66a6ce8f996908195593807c4b38bd528d2cff09d4eb3", "0x3e5bfbbf4d3e39b1a2fd816a7680c19ebebaf3a141b239934ad43cb33fcec8ce"``

The message is verified, because we get the correct sender of
the message back in response: ``0x5ce9454909639d2d17a3f753ce7d93fa0b9ab12e``.

.. _local-sign-transaction:

Sign a Transaction
------------------------

Create a transaction, sign it locally, and then send it to your node for broadcasting,
with :meth:`~web3.eth.Eth.send_raw_transaction`.

.. doctest::

    >>> transaction = {
    ...     'to': '0xF0109fC8DF283027b6285cc889F5aA624EaC1F55',
    ...     'value': 1000000000,
    ...     'gas': 2000000,
    ...     'maxFeePerGas': 2000000000,
    ...     'maxPriorityFeePerGas': 1000000000,
    ...     'nonce': 0,
    ...     'chainId': 1,
    ...     'type': '0x2',  # the type is optional and, if omitted, will be interpreted based on the provided transaction parameters
    ...     'accessList': (  # accessList is optional for dynamic fee transactions
    ...         {
    ...             'address': '0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae',
    ...             'storageKeys': (
    ...                 '0x0000000000000000000000000000000000000000000000000000000000000003',
    ...                 '0x0000000000000000000000000000000000000000000000000000000000000007',
    ...             )
    ...         },
    ...         {
    ...             'address': '0xbb9bc244d798123fde783fcc1c72d3bb8c189413',
    ...             'storageKeys': ()
    ...         },
    ...     )
    ... }
    >>> key = '0x4c0883a69102937d6231471b5dbb6204fe5129617082792ae468d01a3f362318'
    >>> signed = w3.eth.account.sign_transaction(transaction, key)
    >>> signed.rawTransaction
    HexBytes('0x02f8e20180843b9aca008477359400831e848094f0109fc8df283027b6285cc889f5aa624eac1f55843b9aca0080f872f85994de0b295669a9fd93d5f28d9ec85e40f4cb697baef842a00000000000000000000000000000000000000000000000000000000000000003a00000000000000000000000000000000000000000000000000000000000000007d694bb9bc244d798123fde783fcc1c72d3bb8c189413c001a0b9ec671ccee417ff79e06e9e52bfa82b37cf1145affde486006072ca7a11cf8da0484a9beea46ff6a90ac76e7bbf3718db16a8b4b09cef477fb86cf4e123d98fde')
    >>> signed.hash
    HexBytes('0xe85ce7efa52c16cb5c469c7bde54fbd4911639fdfde08003f65525a85076d915')
    >>> signed.r
    84095564551732371065849105252408326384410939276686534847013731510862163857293
    >>> signed.s
    32698347985257114675470251181312399332782188326270244072370350491677872459742
    >>> signed.v
    1

    # When you run send_raw_transaction, you get back the hash of the transaction:
    >>> w3.eth.send_raw_transaction(signed.rawTransaction)  # doctest: +SKIP
    '0xe85ce7efa52c16cb5c469c7bde54fbd4911639fdfde08003f65525a85076d915'

Sign a Contract Transaction
-----------------------------------

To sign a transaction locally that will invoke a smart contract:

#. Initialize your :meth:`Contract <web3.eth.Eth.contract>` object
#. Build the transaction
#. Sign the transaction, with :meth:`w3.eth.account.sign_transaction()
   <eth_account.account.Account.sign_transaction>`
#. Broadcast the transaction with :meth:`~web3.eth.Eth.send_raw_transaction`

.. testsetup::

    import json

    nonce = 0

    EIP20_ABI = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]')  # noqa: 501


.. doctest::

    # When running locally, execute the statements found in the file linked below to load the EIP20_ABI variable.
    # See: https://github.com/carver/ethtoken.py/blob/v0.0.1-alpha.4/ethtoken/abi.py

    >>> from web3.auto import w3

    >>> unicorns = w3.eth.contract(address="0xfB6916095ca1df60bB79Ce92cE3Ea74c37c5d359", abi=EIP20_ABI)

    >>> nonce = w3.eth.get_transaction_count('0x5ce9454909639D2D17A3F753ce7d93fa0b9aB12E')  # doctest: +SKIP

    # Build a transaction that invokes this contract's function, called transfer
    >>> unicorn_txn = unicorns.functions.transfer(
    ...     '0xfB6916095ca1df60bB79Ce92cE3Ea74c37c5d359',
    ...     1,
    ... ).buildTransaction({
    ...     'chainId': 1,
    ...     'gas': 70000,
    ...     'maxFeePerGas': w3.toWei('2', 'gwei'),
    ...     'maxPriorityFeePerGas': w3.toWei('1', 'gwei'),
    ...     'nonce': nonce,
    ... })

    >>> unicorn_txn
    {'value': 0,
     'chainId': 1,
     'gas': 70000,
     'maxFeePerGas': 2000000000,
     'maxPriorityFeePerGas': 1000000000,
     'nonce': 0,
     'to': '0xfB6916095ca1df60bB79Ce92cE3Ea74c37c5d359',
     'data': '0xa9059cbb000000000000000000000000fb6916095ca1df60bb79ce92ce3ea74c37c5d3590000000000000000000000000000000000000000000000000000000000000001'}

    >>> private_key = b"\xb2\\}\xb3\x1f\xee\xd9\x12''\xbf\t9\xdcv\x9a\x96VK-\xe4\xc4rm\x03[6\xec\xf1\xe5\xb3d"
    >>> signed_txn = w3.eth.account.sign_transaction(unicorn_txn, private_key=private_key)
    >>> signed_txn.hash
    HexBytes('0x748db062639a45e519dba934fce09c367c92043867409160c9989673439dc817')
    >>> signed_txn.rawTransaction
    HexBytes('0x02f8b00180843b9aca0084773594008301117094fb6916095ca1df60bb79ce92ce3ea74c37c5d35980b844a9059cbb000000000000000000000000fb6916095ca1df60bb79ce92ce3ea74c37c5d3590000000000000000000000000000000000000000000000000000000000000001c001a0cec4150e52898cf1295cc4020ac0316cbf186071e7cdc5ec44eeb7cdda05afa2a06b0b3a09c7fb0112123c0bef1fd6334853a9dcf3cb5bab3ccd1f5baae926d449')
    >>> signed_txn.r
    93522894155654168208483453926995743737629589441154283159505514235904280342434
    >>> signed_txn.s
    48417310681110102814014302147799665717176259465062324746227758019974374282313
    >>> signed_txn.v
    1

    >>> w3.eth.send_raw_transaction(signed_txn.rawTransaction)  # doctest: +SKIP

    # When you run send_raw_transaction, you get the same result as the hash of the transaction:
    >>> w3.toHex(w3.keccak(signed_txn.rawTransaction))
    '0x748db062639a45e519dba934fce09c367c92043867409160c9989673439dc817'
