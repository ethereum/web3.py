.. py:module:: web3.account
    :synopsis: Validate signatures, and work with local private keys

web3.eth.account API
=====================

.. py:class:: Account

The ``w3.eth.account`` object exposes the following methods to
interact with locally managed keys. It can be used for signing without connecting
to an Ethereum client.

``w3.eth.account`` roughly follows the API of the web3js v1.0
`eth.accounts module <https://web3js.readthedocs.io/en/1.0/web3-eth-accounts.html>`_ .

.. NOTE::
   There is a subtle difference in the naming here:
   web3.py uses ``account`` where web3.js uses ``accounts``. web3.py continues to
   return the list of available accounts in your client when calling ``web3.eth.accounts``


Methods
-------

The following methods are available on the ``w3.eth.account`` namespace. They can all
be called statically, like ``Account.create()``.


.. py:method:: Account.create(extra_entropy="")

    Creates a new private key, and returns it with some :ref:`eth-account-key-convenience`.

    :param extra_entropy: Add extra randomness to whatever randomness your OS can provide
    :type extra_entropy: str or bytes or int
    :return: an object with private key and convenience methods

    .. code-block:: python

        >>> from web3.auto import w3
        >>> acct = w3.eth.account.create('KEYSMASH FJAFJKLDSKF7JKFDJ 1530')
        >>> acct.address
        '0x5ce9454909639D2D17A3F753ce7d93fa0b9aB12E'
        >>> acct.privateKey
        b"\xb2\\}\xb3\x1f\xee\xd9\x12''\xbf\t9\xdcv\x9a\x96VK-\xe4\xc4rm\x03[6\xec\xf1\xe5\xb3d"

        # These methods are also available: sign(), signTransaction(), encrypt()
        # They correspond to the same-named methods in w3.eth.account.*
        # but without the private key argument


.. py:method:: Account.privateKeyToAccount(private_key)

    Returns some :ref:`eth-account-key-convenience`.

    :param private_key: The raw private key
    :type private_key: hex str or bytes or int
    :return: an object with private key and convenience methods

    .. code-block:: python

        >>> acct = w3.eth.account.privateKeyToAccount(
          b"\xb2\\}\xb3\x1f\xee\xd9\x12''\xbf\t9\xdcv\x9a\x96VK-\xe4\xc4rm\x03[6\xec\xf1\xe5\xb3d")
        >>> acct.address
        '0x5ce9454909639D2D17A3F753ce7d93fa0b9aB12E'
        >>> acct.privateKey
        b"\xb2\\}\xb3\x1f\xee\xd9\x12''\xbf\t9\xdcv\x9a\x96VK-\xe4\xc4rm\x03[6\xec\xf1\xe5\xb3d"

        # These methods are also available: sign(), signTransaction(), encrypt()
        # They correspond to the same-named methods in w3.eth.account.*
        # but without the private key argument


.. py:method:: Account.encrypt(private_key, password)

    Creates a dictionary containing your private key, encrypted by the supplied password.
    If you want to create a keyfile recognized by Ethereum clients like geth and parity:
    encode this dictionary with :func:`json.dumps` and save it to disk where your
    client keeps key files.

    :param private_key: The raw private key
    :type private_key: hex str or bytes or int
    :param str password: The password which you will need to unlock the account in your client
    :returns dict: The data to use in your encrypted file

    .. code-block:: python

        >>> encrypted = w3.eth.account.encrypt(
                b"\xb2\\}\xb3\x1f\xee\xd9\x12''\xbf\t9\xdcv\x9a\x96VK-\xe4\xc4rm\x03[6\xec\xf1\xe5\xb3d",
                'correcthorsebatterystaple' )

        {'address': '5ce9454909639d2d17a3f753ce7d93fa0b9ab12e',
         'crypto': {'cipher': 'aes-128-ctr',
          'cipherparams': {'iv': '78f214584844e0b241b433d7c3bb8d5f'},
          'ciphertext': 'd6dbb56e4f54ba6db2e8dc14df17cb7352fdce03681dd3f90ce4b6c1d5af2c4f',
          'kdf': 'pbkdf2',
          'kdfparams': {'c': 1000000,
           'dklen': 32,
           'prf': 'hmac-sha256',
           'salt': '45cf943b4de2c05c2c440ef96af914a2'},
          'mac': 'f5e1af09df5ded25c96fcf075ada313fb6f79735a914adc8cb02e8ddee7813c3'},
         'id': 'b812f3f9-78cc-462a-9e89-74418aa27cb0',
         'version': 3}

         >>> with open('my-keyfile', 'w') as f:
                 f.write(json.dumps(encrypted))


.. py:method:: Account.decrypt(keyfile_json, password)

    Decrypts the private key encrypted using an Ethereum client or :meth:`~Account.encrypt`.

    :param keyfile_json: The encrypted key
    :type keyfile_json: dict or str
    :param str password: The password that was used to encrypt the key
    :returns bytes: the raw private key

    .. code-block:: python

        >>> encrypted = {
         'address': '5ce9454909639d2d17a3f753ce7d93fa0b9ab12e',
         'crypto': {'cipher': 'aes-128-ctr',
          'cipherparams': {'iv': '78f214584844e0b241b433d7c3bb8d5f'},
          'ciphertext': 'd6dbb56e4f54ba6db2e8dc14df17cb7352fdce03681dd3f90ce4b6c1d5af2c4f',
          'kdf': 'pbkdf2',
          'kdfparams': {'c': 1000000,
           'dklen': 32,
           'prf': 'hmac-sha256',
           'salt': '45cf943b4de2c05c2c440ef96af914a2'},
          'mac': 'f5e1af09df5ded25c96fcf075ada313fb6f79735a914adc8cb02e8ddee7813c3'},
         'id': 'b812f3f9-78cc-462a-9e89-74418aa27cb0',
         'version': 3}

        >>> w3.eth.account.decrypt(encrypted, 'correcthorsebatterystaple')
        b"\xb2\\}\xb3\x1f\xee\xd9\x12''\xbf\t9\xdcv\x9a\x96VK-\xe4\xc4rm\x03[6\xec\xf1\xe5\xb3d"


.. py:method:: Account.sign(message=None, private_key=None, message_hexstr=None, message_text=None)

    Sign the message provided. This is equivalent to :meth:`eth.sign() <web3.eth.Eth.sign>` but with
    a local private key instead of an account in a connected client.
    
    Caller must supply exactly one of the message types:
    in bytes, a hex string, or a unicode string. The message will automatically
    be prepended with the text indicating that it is a message (preventing it
    from being used to sign a transaction). The prefix is: ``b'\x19Ethereum Signed Message:\n'``

    :param message: the message message to be signed
    :type message: bytes or int
    :param private_key: the key to sign the message with
    :type private_key: hex str, bytes or int
    :param str message_hexstr: the message encoded as hex
    :param str message_text: the message as a series of unicode characters (a normal Py3 str)
    :returns AttributeDict: Various details about the signature - most
      importantly the fields: v, r, and s

    .. code-block:: python

        >>> msg = "I♥SF"
        >>> key = b"\xb2\\}\xb3\x1f\xee\xd9\x12''\xbf\t9\xdcv\x9a\x96VK-\xe4\xc4rm\x03[6\xec\xf1\xe5\xb3d"
        >>> w3.eth.account.sign(message_text=msg, private_key=key)
        {'message': b'I\xe2\x99\xa5SF',
         'messageHash': HexBytes('0x1476abb745d423bf09273f1afd887d951181d25adc66c4834a70491911b7f750'),
         'r': HexBytes('0xe6ca9bba58c88611fad66a6ce8f996908195593807c4b38bd528d2cff09d4eb3'),
         's': HexBytes('0x3e5bfbbf4d3e39b1a2fd816a7680c19ebebaf3a141b239934ad43cb33fcec8ce'),
         'signature': HexBytes('0xe6ca9bba58c88611fad66a6ce8f996908195593807c4b38bd528d2cff09d4eb33e5bfbbf4d3e39b1a2fd816a7680c19ebebaf3a141b239934ad43cb33fcec8ce1c'),
         'v': 28}

        # these are all equivalent:
        >>> w3.eth.account.sign(w3.toBytes(text=msg), key)
        >>> w3.eth.account.sign(bytes(msg, encoding='utf-8'), key)

        >>> Web3.toHex(text=msg)
        '0x49e299a55346'
        >>> w3.eth.account.sign(message_hexstr='0x49e299a55346', private_key=key)
        >>> w3.eth.account.sign(0x49e299a55346, key)


.. py:method:: Account.recoverMessage(data=None, hexstr=None, text=None, vrs=None, signature=None)

    Get the address of the account that signed the given message.

    * You must specify exactly one of: data, hexstr, or text
    * You must specify exactly one of: vrs or signature

    :param data: the raw message, before it was hashed or signed
    :type data: bytes or int 
    :param str hexstr: the raw message, before it was hashed or signed, as a hex string
    :param str text: the raw message, before it was hashed or signed, as unicode text
    :param vrs: the three pieces generated by an elliptic curve signature
    :type vrs: tuple(v, r, s), each element is hex str, bytes or int
    :param signature: signature bytes concatenated as r+s+v
    :type signature: hex str or bytes or int 
    :returns str: address of signer, hex-encoded & checksummed

    .. code-block:: python

        >>> msg = "I♥SF"
        >>> vrs = (
              28,
              '0xe6ca9bba58c88611fad66a6ce8f996908195593807c4b38bd528d2cff09d4eb3',
              '0x3e5bfbbf4d3e39b1a2fd816a7680c19ebebaf3a141b239934ad43cb33fcec8ce')
        >>> w3.eth.account.recoverMessage(text=msg, vrs=vrs)
        '0x5ce9454909639D2D17A3F753ce7d93fa0b9aB12E'

        # All of these recover calls are equivalent:

        # variations on msg
        >>> msg_raw = b'I\xe2\x99\xa5SF'
        >>> w3.eth.account.recoverMessage(msg_raw, vrs=vrs)
        >>> w3.eth.account.recoverMessage(data=msg_raw, vrs=vrs)

        >>> msg_hex = '0x49e299a55346'
        >>> w3.eth.account.recover(hexstr=msg_hex, vrs=vrs)

        >>> msg_int = 0x49e299a55346
        >>> w3.eth.account.recoverMessage(msg_int, vrs=vrs)
        >>> w3.eth.account.recoverMessage(data=msg_int, vrs=vrs)


.. py:method:: Account.recover(msghash, vrs=None, signature=None)

    Get the address of the account that signed the message with the given hash.
    You must specify exactly one of: vrs or signature

    :param msghash: the hash of the message that you want to verify
    :type msghash: hex str or bytes or int 
    :param vrs: the three pieces generated by an elliptic curve signature
    :type vrs: tuple(v, r, s), each element is hex str, bytes or int
    :param signature: signature bytes concatenated as r+s+v
    :type signature: hex str or bytes or int 
    :returns str: address of signer, hex-encoded & checksummed

    .. code-block:: python

        >>> msg = "I♥SF"
        >>> msghash = '0x1476abb745d423bf09273f1afd887d951181d25adc66c4834a70491911b7f750'
        >>> vrs = (
              28,
              '0xe6ca9bba58c88611fad66a6ce8f996908195593807c4b38bd528d2cff09d4eb3',
              '0x3e5bfbbf4d3e39b1a2fd816a7680c19ebebaf3a141b239934ad43cb33fcec8ce')
        >>> w3.eth.account.recover(msghash, vrs=vrs)
        '0x5ce9454909639D2D17A3F753ce7d93fa0b9aB12E'

        # All of these recover calls are equivalent:
        
        # variations on msghash
        >>> msghash = b"\x14v\xab\xb7E\xd4#\xbf\t'?\x1a\xfd\x88}\x95\x11\x81\xd2Z\xdcf\xc4\x83JpI\x19\x11\xb7\xf7P"
        >>> w3.eth.account.recover(msghash, vrs=vrs)
        >>> msghash = 0x1476abb745d423bf09273f1afd887d951181d25adc66c4834a70491911b7f750
        >>> w3.eth.account.recover(msghash, vrs=vrs)

        # variations on vrs
        >>> vrs = (
              '0x1c',
              '0xe6ca9bba58c88611fad66a6ce8f996908195593807c4b38bd528d2cff09d4eb3',
              '0x3e5bfbbf4d3e39b1a2fd816a7680c19ebebaf3a141b239934ad43cb33fcec8ce')
        >>> w3.eth.account.recover(msghash, vrs=vrs)
        >>> vrs = (
              b'\x1c',
              b'\xe6\xca\x9b\xbaX\xc8\x86\x11\xfa\xd6jl\xe8\xf9\x96\x90\x81\x95Y8\x07\xc4\xb3\x8b\xd5(\xd2\xcf\xf0\x9dN\xb3',
              b'>[\xfb\xbfM>9\xb1\xa2\xfd\x81jv\x80\xc1\x9e\xbe\xba\xf3\xa1A\xb29\x93J\xd4<\xb3?\xce\xc8\xce')
        >>> w3.eth.account.recover(msghash, vrs=vrs)
        >>> vrs = (
              0x1c,
              0xe6ca9bba58c88611fad66a6ce8f996908195593807c4b38bd528d2cff09d4eb3,
              0x3e5bfbbf4d3e39b1a2fd816a7680c19ebebaf3a141b239934ad43cb33fcec8ce)
        >>> w3.eth.account.recover(msghash, vrs=vrs)

        # variations on signature
        >>> signature = '0xe6ca9bba58c88611fad66a6ce8f996908195593807c4b38bd528d2cff09d4eb33e5bfbbf4d3e39b1a2fd816a7680c19ebebaf3a141b239934ad43cb33fcec8ce1c'
        >>> w3.eth.account.recover(msghash, signature=signature)
        >>> signature = b'\xe6\xca\x9b\xbaX\xc8\x86\x11\xfa\xd6jl\xe8\xf9\x96\x90\x81\x95Y8\x07\xc4\xb3\x8b\xd5(\xd2\xcf\xf0\x9dN\xb3>[\xfb\xbfM>9\xb1\xa2\xfd\x81jv\x80\xc1\x9e\xbe\xba\xf3\xa1A\xb29\x93J\xd4<\xb3?\xce\xc8\xce\x1c'
        >>> w3.eth.account.recover(msghash, signature=signature)
        >>> signature = 0xe6ca9bba58c88611fad66a6ce8f996908195593807c4b38bd528d2cff09d4eb33e5bfbbf4d3e39b1a2fd816a7680c19ebebaf3a141b239934ad43cb33fcec8ce1c
        >>> w3.eth.account.recover(msghash, signature=signature)


.. py:method:: Account.hashMessage(data=None, hexstr=None, text=None)

    Generate the message hash, including the prefix. See :meth:`~Account.sign`
    for more about the prefix. Supply exactly one of the three arguments.

    :param data: the message to sign, in primitive form
    :type data: bytes or int
    :param str hexstr: the message to sign, as a hex-encoded string
    :param str data: the message to sign, as a series of unicode points
    :returns str: the hex-encoded hash of the message

    .. code-block:: python

        >>> msg = "I♥SF"
        >>> w3.eth.account.hashMessage(text=msg)
        HexBytes('0x1476abb745d423bf09273f1afd887d951181d25adc66c4834a70491911b7f750')


.. py:method:: Account.signTransaction(transaction_dict, private_key)

    Sign a transaction using a local private key. Produces signature details
    and the hex-encoded transaction suitable for broadcast using
    :meth:`~web3.eth.Eth.sendRawTransaction`.

    The transaction dict for executing contract methods may be created using 
    :meth:`~web3.contract.Contract.buildTransaction`.

    :param dict transaction_dict: the transaction with keys:
      nonce, chainId, to, data, value, gas, and gasPrice.
    :param private_key: the private key to sign the data with
    :type private_key: hex str, bytes or int
    :returns AttributeDict: Various details about the signature - most
      importantly the fields: v, r, and s

    .. code-block:: python

        >>> transaction = {
                'to': '0xF0109fC8DF283027b6285cc889F5aA624EaC1F55',
                'value': 1000000000,
                'gas': 2000000,
                'gasPrice': 234567897654321,
                'nonce': 0,
                'chainId': 1
            }
        >>> key = '0x4c0883a69102937d6231471b5dbb6204fe5129617082792ae468d01a3f362318'
        >>> signed = w3.eth.account.signTransaction(transaction, key)
        {'hash': HexBytes('0x6893a6ee8df79b0f5d64a180cd1ef35d030f3e296a5361cf04d02ce720d32ec5'),
         'r': HexBytes('0x09ebb6ca057a0535d6186462bc0b465b561c94a295bdb0621fc19208ab149a9c'),
         'rawTransaction': HexBytes('0xf86a8086d55698372431831e848094f0109fc8df283027b6285cc889f5aa624eac1f55843b9aca008025a009ebb6ca057a0535d6186462bc0b465b561c94a295bdb0621fc19208ab149a9ca0440ffd775ce91a833ab410777204d5341a6f9fa91216a6f3ee2c051fea6a0428'),
         's': HexBytes('0x440ffd775ce91a833ab410777204d5341a6f9fa91216a6f3ee2c051fea6a0428'),
         'v': 37}
        >>> w3.eth.sendRawTransaction(signed.rawTransaction)


.. py:method:: Account.recoverTransaction(serialized_transaction)

    Get the address of the account that signed this transaction.

    :param serialized_transaction: the complete signed transaction
    :type serialized_transaction: hex str, bytes or int
    :returns str: address of signer, hex-encoded & checksummed

    .. code-block:: python

        >>> raw_transaction = '0xf86a8086d55698372431831e848094f0109fc8df283027b6285cc889f5aa624eac1f55843b9aca008025a009ebb6ca057a0535d6186462bc0b465b561c94a295bdb0621fc19208ab149a9ca0440ffd775ce91a833ab410777204d5341a6f9fa91216a6f3ee2c051fea6a0428',
        >>> w3.eth.account.recoverTransaction(raw_transaction)
        '0x2c7536E3605D9C16a7a3D7b1898e529396a65c23'


.. _eth-account-key-convenience:

Private Key Convenience Methods
---------------------------------

The following are a set of methods that mirror :class:`Account` methods, but
with a prefilled private key. They are accessible as a result of the :meth:`~Account.create` and
:meth:`~Account.privateKeyToAccount` calls.


.. py:method:: web3.utils.signing.LocalAccount.encrypt(password)

    Just like :meth:`Account.encrypt`, but prefilling the private key parameter.

.. py:method:: web3.utils.signing.LocalAccount.sign(message=None, message_hexstr=None, message_text=None)

    Just like :meth:`Account.sign`, but prefilling the private key parameter.

.. py:method:: web3.utils.signing.LocalAccount.signTransaction(transaction_dict)

    Just like :meth:`Account.signTransaction`, but prefilling the private key parameter.
