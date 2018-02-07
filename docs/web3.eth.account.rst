Working with Local Private Keys
==========================================

Local Private Key
  A key is 32 :class:`bytes` of data that you can use to sign transactions and messages,
  before sending them to your node. That node can be local (like Geth or Parity),
  or remote (like Infura). You must use :meth:`~web3.eth.Eth.sendRawTransaction`
  when working with local keys, instead of
  :meth:`~web3.eth.Eth.sendTransaction` .

Managed Private Key
  A managed key is like a `Local Private Key`, but managed by your local node.
  This allows you to use
  :meth:`~web3.eth.Eth.sendTransaction`.
  Each account returned by :attr:`w3.eth.accounts <web3.eth.Eth.accounts>`
  has a key associated
  with it, which is managed by your node.

.. WARNING::
  It is unnacceptable for a remote
  node to manage your private keys, because of the likelihood of theft.
  Any reputable 3rd-party node (like Infura) will not offer a `Managed Private Key`.

Some Common Uses for Local Private Keys
-------------------------------------------

Some common things you might want to do with Local Private Keys are:

- `Sign a Transaction`_
- `Sign a Contract Transaction`_
- `Sign a Message`_
- `Verify a Message`_

Using private keys usually involves ``w3.eth.account`` in one way or another. Read on for more,
or see a full list of things you can do in the docs for
:class:`eth_account.Account <eth_account.account.Account>`.

Extract private key from geth keyfile
---------------------------------------------

.. code-block:: python

    with open('~/.ethereum/keystore/UTC--...--5ce9454909639D2D17A3F753ce7d93fa0b9aB12E') as keyfile:
        encrypted_key = keyfile.read()
        private_key = w3.eth.account.decrypt(encrypted_key, 'correcthorsebatterystaple')
        # tip: do not save the key or password anywhere, especially into a shared source file

Sign a Message
---------------

.. doctest::

    >>> from web3.auto import w3

    >>> msg = "I♥SF"
    >>> private_key = b"\xb2\\}\xb3\x1f\xee\xd9\x12''\xbf\t9\xdcv\x9a\x96VK-\xe4\xc4rm\x03[6\xec\xf1\xe5\xb3d"
    >>> signed_message = w3.eth.account.sign(message_text=msg, private_key=private_key)
    >>> signed_message
    AttrDict({'message': HexBytes('0x49e299a55346'),
     'messageHash': HexBytes('0x1476abb745d423bf09273f1afd887d951181d25adc66c4834a70491911b7f750'),
     'r': 104389933075820307925104709181714897380569894203213074526835978196648170704563,
     's': 28205917190874851400050446352651915501321657673772411533993420917949420456142,
     'v': 28,
     'signature': HexBytes('0xe6ca9bba58c88611fad66a6ce8f996908195593807c4b38bd528d2cff09d4eb33e5bfbbf4d3e39b1a2fd816a7680c19ebebaf3a141b239934ad43cb33fcec8ce1c')})

Verify a Message
------------------------------------------------

With the original message text and a signature:

.. doctest::

    >>> w3.eth.account.recoverMessage(text="I♥SF", signature=signed_message.signature)
    '0x5ce9454909639D2D17A3F753ce7d93fa0b9aB12E'

Verify a message from message hash
-----------------------------------------------------------

Sometimes you don't have the original message, all you have is the
prefixed & hashed message. To verify it, use:

.. doctest::

    >>> message_hash = '0x1476abb745d423bf09273f1afd887d951181d25adc66c4834a70491911b7f750'
    >>> signature = '0xe6ca9bba58c88611fad66a6ce8f996908195593807c4b38bd528d2cff09d4eb33e5bfbbf4d3e39b1a2fd816a7680c19ebebaf3a141b239934ad43cb33fcec8ce1c'
    >>> w3.eth.account.recover(message_hash, signature=signature)
    '0x5ce9454909639D2D17A3F753ce7d93fa0b9aB12E'

.. NOTE::

    Note the usage of :meth:`~eth_account.account.Account.recover`, **not**
    :meth:`~eth_account.account.Account.recoverMessage`.
    If you try to use a prefixed & hashed message instead of the original message,
    then :meth:`~eth_account.account.Account.recoverMessage`
    will give you the wrong result.

Prepare message for ecrecover in Solidity
--------------------------------------------

Produce a signed_message as in `Sign a Message`_, then...

.. doctest::

    >>> from web3 import Web3

    >>> def to_32byte_hex(val):
    ...   return Web3.toHex(Web3.toBytes(val).rjust(32, b'\0'))

    >>> ec_recover_args = (msghash, v, r, s) = (
    ...   signed_message.messageHash,
    ...   signed_message.v,
    ...   to_32byte_hex(signed_message.r),
    ...   to_32byte_hex(signed_message.s),
    ... )
    >>> ec_recover_args
    (HexBytes('0x1476abb745d423bf09273f1afd887d951181d25adc66c4834a70491911b7f750'),
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

Sign a Transaction
------------------------

Create a transaction, sign it locally, and then send it to your node for broadcasting,
with :meth:`~web3.eth.Eth.sendRawTransaction`.

.. doctest::

    >>> transaction = {
    ...     'to': '0xF0109fC8DF283027b6285cc889F5aA624EaC1F55',
    ...     'value': 1000000000,
    ...     'gas': 2000000,
    ...     'gasPrice': 234567897654321,
    ...     'nonce': 0,
    ...     'chainId': 1
    ... }
    >>> key = '0x4c0883a69102937d6231471b5dbb6204fe5129617082792ae468d01a3f362318'
    >>> signed = w3.eth.account.signTransaction(transaction, key)
    >>> signed.rawTransaction
    HexBytes('0xf86a8086d55698372431831e848094f0109fc8df283027b6285cc889f5aa624eac1f55843b9aca008025a009ebb6ca057a0535d6186462bc0b465b561c94a295bdb0621fc19208ab149a9ca0440ffd775ce91a833ab410777204d5341a6f9fa91216a6f3ee2c051fea6a0428')
    >>> signed.hash
    HexBytes('0xd8f64a42b57be0d565f385378db2f6bf324ce14a594afc05de90436e9ce01f60')
    >>> signed.r
    4487286261793418179817841024889747115779324305375823110249149479905075174044
    >>> signed.s
    30785525769477805655994251009256770582792548537338581640010273753578382951464
    >>> signed.v
    37

    # When you run sendRawTransaction, you get back the hash of the transaction:
    >>> w3.eth.sendRawTransaction(signed.rawTransaction)  # doctest: +SKIP
    '0xd8f64a42b57be0d565f385378db2f6bf324ce14a594afc05de90436e9ce01f60'

Sign a Contract Transaction
-----------------------------------

To sign a transaction locally that will invoke a smart contract:

#. Initialize your :meth:`Contract <web3.eth.Eth.contract>` object
#. Build the transaction
#. Sign the transaction, with :meth:`w3.eth.account.signTransaction()
   <eth_account.account.Account.signTransaction>`
#. Broadcast the transaction with :meth:`~web3.eth.Eth.sendRawTransaction`

.. testsetup::

    nonce = 0

.. doctest::

    >>> from ethtoken.abi import EIP20_ABI
    >>> from web3.auto import w3

    >>> unicorns = w3.eth.contract(address="0xfB6916095ca1df60bB79Ce92cE3Ea74c37c5d359", abi=EIP20_ABI)

    >>> nonce = w3.eth.getTransactionCount('0x5ce9454909639D2D17A3F753ce7d93fa0b9aB12E')  # doctest: +SKIP

    >>> unicorn_txn = unicorns.functions.transfer(
    ...     '0xfB6916095ca1df60bB79Ce92cE3Ea74c37c5d359',
    ...     1,
    ... ).buildTransaction({
    ...     'chainId': 1,
    ...     'gas': 70000,
    ...     'gasPrice': w3.toWei('1', 'gwei'),
    ...     'nonce': nonce,
    ... })

    >>> unicorn_txn
    {'value': 0,
     'chainId': 1,
     'gas': 70000,
     'gasPrice': 1000000000,
     'nonce': 0,
     'to': '0xfB6916095ca1df60bB79Ce92cE3Ea74c37c5d359',
     'data': '0xa9059cbb000000000000000000000000fb6916095ca1df60bb79ce92ce3ea74c37c5d3590000000000000000000000000000000000000000000000000000000000000001'}

    >>> private_key = b"\xb2\\}\xb3\x1f\xee\xd9\x12''\xbf\t9\xdcv\x9a\x96VK-\xe4\xc4rm\x03[6\xec\xf1\xe5\xb3d"
    >>> signed_txn = w3.eth.account.signTransaction(unicorn_txn, private_key=private_key)
    >>> signed_txn.hash
    HexBytes('0x4795adc6a719fa64fa21822630c0218c04996e2689ded114b6553cef1ae36618')
    >>> signed_txn.rawTransaction
    HexBytes('0xf8a980843b9aca008301117094fb6916095ca1df60bb79ce92ce3ea74c37c5d35980b844a9059cbb000000000000000000000000fb6916095ca1df60bb79ce92ce3ea74c37c5d359000000000000000000000000000000000000000000000000000000000000000125a00fb532eea06b8f17d858d82ad61986efd0647124406be65d359e96cac3e004f0a02e5d7ffcfb7a6073a723be38e6733f353cf9367743ae94e2ccd6f1eba37116f4')
    >>> signed_txn.r
    7104843568152743554992057394334744036860247658813231830421570918634460546288
    >>> signed_txn.s
    20971591154030974221209741174186570949918731455961098911091818811306894497524
    >>> signed_txn.v
    37

    >>> w3.eth.sendRawTransaction(signed_txn.rawTransaction)  # doctest: +SKIP

    # When you run sendRawTransaction, you get the same result as the hash of the transaction:
    >>> w3.toHex(w3.sha3(signed_txn.rawTransaction))
    '0x4795adc6a719fa64fa21822630c0218c04996e2689ded114b6553cef1ae36618'
