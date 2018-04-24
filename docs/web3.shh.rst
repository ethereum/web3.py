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

    Returns the Whisper version this node offers.

    .. code-block:: python

        >>>web3.shh.version
        6.0

.. py:attribute:: Shh.info

    Returns the Whisper statistics for diagnostics.

    .. code-block:: python

        >>>web3.shh.info
        {'maxMessageSize': 1024, 'memory': 240, 'messages': 0, 'minPow': 0.2}

Methods
-------

The following methods are available on the ``web3.shh`` namespace.


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

        >>>web3.shh.post({'payload': web3.toHex(text="test_payload"), 'pubKey': recipient_public, 'topic': '0x12340000', 'powTarget': 2.5, 'powTime': 2})
        True

.. py:method:: Shh.newMessageFilter(self, criteria, poll_interval=None)

    * Create a new filter within the node. This filter can be used to poll for new messages that match the set of criteria. 

    * If a ``poll_interval`` is specified, the client will asynchronously poll for new messages.

    * Parameters:
        * ``symKeyID``: When using symmetric key encryption, holds the symmetric key ID.
        * ``privateKeyID``: When using asymmetric key encryption, holds the private key ID.
        * ``sig``: Public key of the signature.
        * ``minPoW``: Minimal PoW requirement for incoming messages.
        * ``topics``: Array of possible topics (or partial topics).
        * ``allowP2P``: Indicates if this filter allows processing of direct peer-to-peer messages.

    * Returns ``ShhFilter`` which you can either ``watch(callback)`` or request ``get_new_entries()``

    .. code-block:: python

        >>>web3.shh.newMessageFilter({'topic': '0x12340000', 'privateKeyID': recipient_private})
        ShhFilter({'filter_id': 'b37c3106cfb683e8f01b5019342399e0d1d74e9160f69b27625faba7a6738554'})

.. py:method:: Shh.deleteMessageFilter(self, filter_id)

    * Deletes a message filter in the node.

    * Returns ``True`` if the filter was sucesfully uninstalled, otherwise ``False``

    .. code-block:: python

        >>>web3.shh.deleteMessageFilter('b37c3106cfb683e8f01b5019342399e0d1d74e9160f69b27625faba7a6738554')
        True

.. py:method:: Shh.getMessages(self, filter_id)

    * Retrieve messages that match the filter criteria and are received between the last time this function was called and now.

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

.. py:method:: Shh.setMaxMessageSize(self, size)

    * Sets the maximal message size allowed by this node. Incoming and outgoing messages with a larger size will be rejected. Whisper message size can never exceed the limit imposed by the underlying P2P protocol (10 Mb).

    * Returns ``True`` if the filter was sucesfully uninstalled, otherwise ``False``

    .. code-block:: python

        >>>web3.shh.setMaxMessageSize(1024)
        True

.. py:method:: Shh.setMinPoW(self, min_pow)

    * Sets the minimal PoW required by this node.

    * Returns ``True`` if the filter was sucesfully uninstalled, otherwise ``False``

    .. code-block:: python

        >>>web3.shh.setMinPoW(0.4)
        True

.. py:method:: Shh.markTrustedPeer(self, enode)

    * Marks specific peer trusted, which will allow it to send historic (expired) messages.

    * Returns ``True`` if the filter was sucesfully uninstalled, otherwise ``False``

    .. code-block:: python

        >>>web3.shh.markTrustedPeer('enode://d25474361659861e9e651bc728a17e807a3359ca0d344afd544ed0f11a31faecaf4d74b55db53c6670fd624f08d5c79adfc8da5dd4a11b9213db49a3b750845e@52.178.209.125:30379')
        True

---------------
Asymmetric Keys
---------------

.. py:method:: Shh.newKeyPair(self)

    * Generates a new cryptographic identity for the client, and injects it into the known identities for message decryption

    * Returns the new key pair's identity

    .. code-block:: python

        >>>web3.shh.newKeyPair()
        '86e658cbc6da63120b79b5eec0c67d5dcfb6865a8f983eff08932477282b77bb'

.. py:method:: Shh.addPrivateKey(self, key)

    * Stores a key pair derived from a private key, and returns its ID.

    * Returns the added key pair's ID

    .. code-block:: python

        >>>web3.shh.addPrivateKey('0x7b8190d96cd061a102e551ee36d08d4f3ca1f56fb0008ef5d70c56271d8c46d0')
        '86e658cbc6da63120b79b5eec0c67d5dcfb6865a8f983eff08932477282b77bb'

.. py:method:: Shh.deleteKeyPair(self, id)

    * Deletes the specifies key if it exists.

    * Returns ``True`` if the key pair was deleted, otherwise ``False``

    .. code-block:: python

        >>>web3.shh.deleteKeyPair('86e658cbc6da63120b79b5eec0c67d5dcfb6865a8f983eff08932477282b77bb')
        True

.. py:method:: Shh.hasKeyPair(self, id)

    * Checks if the whisper node has a private key of a key pair matching the given ID.

    * Returns ``True`` if the key pair exists, otherwise ``False``

    .. code-block:: python

        >>>web3.shh.hasKeyPair('86e658cbc6da63120b79b5eec0c67d5dcfb6865a8f983eff08932477282b77bb')
        False

.. py:method:: Shh.getPublicKey(self, id)

    * Returns the public key associated with the key pair.

    .. code-block:: python

        >>>web3.shh.getPublicKey('86e658cbc6da63120b79b5eec0c67d5dcfb6865a8f983eff08932477282b77bb')
        '0x041b0777ceb8cf8748fe0bba5e55039d650a03eb0239a909f9ee345bbbad249f2aa236a4b8f41f51bd0a97d87c08e69e67c51f154d634ba51a224195212fc31e4e'

.. py:method:: Shh.getPrivateKey(self, id)

    * Returns the private key associated with the key pair.

    .. code-block:: python

        >>>web3.shh.getPrivateKey('86e658cbc6da63120b79b5eec0c67d5dcfb6865a8f983eff08932477282b77bb')
        '0x7b8190d96cd061a102e551ee36d08d4f3ca1f56fb0008ef5d70c56271d8c46d0'

---------------
Symmetric Keys
---------------

.. py:method:: Shh.newSymKey(self)

    * Generates a random symmetric key and stores it under id, which is then returned. Will be used in the future for session key exchange

    * Returns the new key pair's identity

    .. code-block:: python

        >>>web3.shh.newSymKey()
        '6c388d63003deb378700c9dad87f67df0247e660647d6ba1d04321bbc2f6ce0c'

.. py:method:: Shh.addSymKey(self, key)

    * Stores the key, and returns its ID.

    * Returns the new key pair's identity

    .. code-block:: python

        >>>web3.shh.addSymKey('0x58f6556e56a0d41b464a083161377c8a9c2e95156921f954f99ef97d41cebaa2')
        '6c388d63003deb378700c9dad87f67df0247e660647d6ba1d04321bbc2f6ce0c'

.. py:method:: Shh.generateSymKeyFromPassword(self)

    * Generates the key from password, stores it, and returns its ID.

    * Returns the new key pair's identity

    .. code-block:: python

        >>>web3.shh.generateSymKeyFromPassword('shh secret pwd')
        '6c388d63003deb378700c9dad87f67df0247e660647d6ba1d04321bbc2f6ce0c'

.. py:method:: Shh.hasSymKey(self, id)

    * Checks if there is a symmetric key stored with the given ID.

    * Returns ``True`` if the key exists, otherwise ``False``

    .. code-block:: python

        >>>web3.shh.hasSymKey('6c388d63003deb378700c9dad87f67df0247e660647d6ba1d04321bbc2f6ce0c')
        False

.. py:method:: Shh.getSymKey(self, id)

    * Returns the symmetric key associated with the given ID.

    * Returns the public key associated with the key pair

    .. code-block:: python

        >>>web3.shh.getSymKey('6c388d63003deb378700c9dad87f67df0247e660647d6ba1d04321bbc2f6ce0c')
        '0x58f6556e56a0d41b464a083161377c8a9c2e95156921f954f99ef97d41cebaa2'

.. py:method:: Shh.deleteSymKey(self, id)

    * Deletes the symmetric key associated with the given ID.

    * Returns ``True`` if the key pair was deleted, otherwise ``False``

    .. code-block:: python

        >>>web3.shh.deleteSymKey('6c388d63003deb378700c9dad87f67df0247e660647d6ba1d04321bbc2f6ce0c')
        True
