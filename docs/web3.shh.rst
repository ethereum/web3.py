SHH API
=======

.. py:module:: web3.shh
.. py:class:: Shh

The ``web3.shh`` object exposes methods to interact with the RPC APIs under the
``shh_`` namespace.

.. warning:: The Whisper protocol is in flux, with incompatible versions supported
    by different major clients. So it is not currently included by default in the web3
    instance.


Properties
----------

The following properties are available on the ``web.shh`` namespace.

.. py:attribute:: Shh.version

    The version of Whisper protocol used by client

    .. code-block:: python

        >>>web3.shh.version
        6.0

.. py:attribute:: Shh.info

    The information and properties currently set for the Whisper protocol

    .. code-block:: python

        >>>web3.shh.info
        {'maxMessageSize': 1024, 'memory': 240, 'messages': 0, 'minPow': 0.2}

Methods
-------

The following methods are available on the ``web3.shh`` namespace.


.. py:method:: Shh.post(self, message)

    * Delegates to ``shh_post`` RPC method

    * ``message`` cannot be ``None`` and should contain a ``payload``

    * Returns ``True`` if the message was succesfully sent, otherwise ``False``

    .. code-block:: python

        >>>web3.shh.post({'payload': web3.toHex(text="test_payload"), 'pubKey': recipient_public, 'topic': '0x12340000', 'powTarget': 2.5, 'powTime': 2})
        True

.. py:method:: Shh.newMessageFilter(self, criteria, poll_interval=None)

    * Delegates to ``shh_newMessageFilter`` RPC method

    * If a ``poll_interval`` is specified, the client will asynchronously poll for new messages

    * Returns ``ShhFilter`` which you can either ``watch(callback)`` or request ``get_new_entries()``

    .. code-block:: python

        >>>web3.shh.newMessageFilter({'topic': '0x12340000', 'privateKeyID': recipient_private})
        ShhFilter({'filter_id': 'b37c3106cfb683e8f01b5019342399e0d1d74e9160f69b27625faba7a6738554'})

.. py:method:: Shh.deleteMessageFilter(self, filter_id)

    * Delegates to ``shh_deleteMessageFilter`` RPC Method

    * Returns ``True`` if the filter was sucesfully uninstalled, otherwise ``False``

    .. code-block:: python

        >>>web3.shh.deleteMessageFilter('b37c3106cfb683e8f01b5019342399e0d1d74e9160f69b27625faba7a6738554')
        True

.. py:method:: Shh.getMessages(self, filter_id)

    * Delegates to ``shh_getMessages`` RPC Method

    * Returns all new messages since the last invocation

    .. code-block:: python

        >>>web3.shh.getMessages('b37c3106cfb683e8f01b5019342399e0d1d74e9160f69b27625faba7a6738554')
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

---------------
Asymmetric Keys
---------------

.. py:method:: Shh.newKeyPair(self)

    * Delegates to ``shh_newKeyPair`` RPC method. Generates a new cryptographic identity for the client, and injects it into the known identities for message decryption

    * Returns the new key pair's identity

    .. code-block:: python

        >>>web3.shh.newKeyPair()
        '86e658cbc6da63120b79b5eec0c67d5dcfb6865a8f983eff08932477282b77bb'

.. py:method:: Shh.addPrivateKey(self, key)

    * Delegates to ``shh_addPrivateKey`` RPC method

    * Returns ``True`` if the key pair was added, otherwise ``False``

    .. code-block:: python

        >>>web3.shh.addPrivateKey('0x7b8190d96cd061a102e551ee36d08d4f3ca1f56fb0008ef5d70c56271d8c46d0')
        True

.. py:method:: Shh.deleteKeyPair(self, id)

    * Delegates to ``shh_deleteKeyPair`` RPC method

    * Returns ``True`` if the key pair was deleted, otherwise ``False``

    .. code-block:: python

        >>>web3.shh.deleteKeyPair('86e658cbc6da63120b79b5eec0c67d5dcfb6865a8f983eff08932477282b77bb')
        True

.. py:method:: Shh.hasKeyPair(self, id)

    * Delegates to ``shh_hasKeyPair`` RPC method

    * Returns ``True`` if the key pair exists, otherwise ``False``

    .. code-block:: python

        >>>web3.shh.hasKeyPair('86e658cbc6da63120b79b5eec0c67d5dcfb6865a8f983eff08932477282b77bb')
        False

.. py:method:: Shh.getPublicKey(self, id)

    * Delegates to ``shh_getPublicKey`` RPC method

    * Returns the public key associated with the key pair

    .. code-block:: python

        >>>web3.shh.getPublicKey('86e658cbc6da63120b79b5eec0c67d5dcfb6865a8f983eff08932477282b77bb')
        '0x041b0777ceb8cf8748fe0bba5e55039d650a03eb0239a909f9ee345bbbad249f2aa236a4b8f41f51bd0a97d87c08e69e67c51f154d634ba51a224195212fc31e4e'

.. py:method:: Shh.getPrivateKey(self, id)

    * Delegates to ``shh_getPrivateKey`` RPC method

    * Returns the private key associated with the key pair

    .. code-block:: python

        >>>web3.shh.getPrivateKey('86e658cbc6da63120b79b5eec0c67d5dcfb6865a8f983eff08932477282b77bb')
        '0x7b8190d96cd061a102e551ee36d08d4f3ca1f56fb0008ef5d70c56271d8c46d0'

---------------
Symmetric Keys
---------------

.. py:method:: Shh.newSymKey(self)

    * Delegates to ``shh_newSymKey`` RPC method. Generates a random symmetric key and stores it under id, which is then returned. Will be used in the future for session key exchange

    * Returns the new key pair's identity

    .. code-block:: python

        >>>web3.shh.newSymKey()
        '6c388d63003deb378700c9dad87f67df0247e660647d6ba1d04321bbc2f6ce0c'

.. py:method:: Shh.addSymKey(self, key)

    * Delegates to ``shh_addSymKey`` RPC method

    * Returns ``True`` if the key was added, otherwise ``False``

    .. code-block:: python

        >>>web3.shh.addSymKey('0x58f6556e56a0d41b464a083161377c8a9c2e95156921f954f99ef97d41cebaa2')
        True

.. py:method:: Shh.generateSymKeyFromPassword(self)

    * Delegates to ``shh_generateSymKeyFromPassword`` RPC method

    * Returns the new key pair's identity

    .. code-block:: python

        >>>web3.shh.generateSymKeyFromPassword('shh secret pwd')
        '6c388d63003deb378700c9dad87f67df0247e660647d6ba1d04321bbc2f6ce0c'

.. py:method:: Shh.deleteSymKey(self, id)

    * Delegates to ``shh_deleteSymKey`` RPC method

    * Returns ``True`` if the key pair was deleted, otherwise ``False``

    .. code-block:: python

        >>>web3.shh.deleteSymKey('6c388d63003deb378700c9dad87f67df0247e660647d6ba1d04321bbc2f6ce0c')
        True

.. py:method:: Shh.hasSymKey(self, id)

    * Delegates to ``shh_hasSymKey`` RPC method

    * Returns ``True`` if the key exists, otherwise ``False``

    .. code-block:: python

        >>>web3.shh.hasSymKey('6c388d63003deb378700c9dad87f67df0247e660647d6ba1d04321bbc2f6ce0c')
        False

.. py:method:: Shh.getSymKey(self, id)

    * Delegates to ``shh_getSymKey`` RPC method

    * Returns the public key associated with the key pair

    .. code-block:: python

        >>>web3.shh.getSymKey('6c388d63003deb378700c9dad87f67df0247e660647d6ba1d04321bbc2f6ce0c')
        '0x58f6556e56a0d41b464a083161377c8a9c2e95156921f954f99ef97d41cebaa2'
