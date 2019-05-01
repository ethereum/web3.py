Parity API
==========

.. py:module:: web3.parity

The ``web3.parity`` object exposes modules that enable you to interact with the JSON-RPC endpoints supported by `Parity <https://wiki.parity.io/JSONRPC>`_ that are not defined in the standard set of Ethereum JSONRPC endpoints according to `EIP 1474 <https://github.com/ethereum/EIPs/pull/1474>`_.

ParityPersonal
--------------

The following methods are available on the ``web3.parity.personal`` namespace.

.. py:method:: listAccounts

    * Delegates to ``personal_listAccounts`` RPC Method

    Returns the list of known accounts.

    .. code-block:: python

        >>> web3.parity.personal.listAccounts()
        ['0xd3cda913deb6f67967b99d67acdfa1712c293601']


.. py:method:: importRawKey(self, private_key, passphrase)

    * Delegates to ``personal_importRawKey`` RPC Method

    Adds the given ``private_key`` to the node's keychain, encrypted with the
    given ``passphrase``.  Returns the address of the imported account.

    .. code-block:: python

        >>> web3.parity.personal.importRawKey(some_private_key, 'the-passphrase')
        '0xd3cda913deb6f67967b99d67acdfa1712c293601'


.. py:method:: newAccount(self, password)

    * Delegates to ``personal_newAccount`` RPC Method

    Generates a new account in the node's keychain encrypted with the
    given ``passphrase``.  Returns the address of the created account.

    .. code-block:: python

        >>> web3.parity.personal.newAccount('the-passphrase')
        '0xd3cda913deb6f67967b99d67acdfa1712c293601'


.. py:method:: unlockAccount(self, account, passphrase, duration=None)

    * Delegates to ``personal_unlockAccount`` RPC Method

    Unlocks the given ``account`` for ``duration`` seconds.  If ``duration`` is
    ``None`` then the account will remain unlocked indefinitely.  Returns
    boolean as to whether the account was successfully unlocked.

    .. code-block:: python

        # Invalid call to personal_unlockAccount on Parity currently returns True, due to Parity bug
        >>> web3.parity.personal.unlockAccount('0xd3cda913deb6f67967b99d67acdfa1712c293601', 'wrong-passphrase')
        True
        >>> web3.parity.personal.unlockAccount('0xd3cda913deb6f67967b99d67acdfa1712c293601', 'the-passphrase')
        True


.. py:method:: sendTransaction(self, transaction, passphrase)

    * Delegates to ``personal_sendTransaction`` RPC Method

    Sends the transaction.


.. py:method:: signTypedData(self, jsonMessage, account, passphrase)

    * Delegates to ``personal_signTypedData`` RPC Method

    Please note that the ``jsonMessage`` argument is the loaded JSON Object
    and **NOT** the JSON String itself.

    Signs the ``Structured Data`` (or ``Typed Data``) with the passphrase of the given ``account``


ParityShh
---------

The ``web3.parity.shh`` object exposes methods to interact with the RPC APIs under the `shh_`` namespace.

Full documentation for Parity-supported endpoints can be found `here <https://wiki.parity.io/JSONRPC-shh-module>`_.

.. warning:: The Whisper protocol is in flux, with incompatible versions supported
    by different major clients.


.. py:method:: Shh.info()

    Returns the Whisper statistics for diagnostics.

    .. code-block:: python

        >>> web3.parity.shh.info()
        {'memory': 240, 'messages': 0, 'targetMemory': 102485760}

.. py:method:: Shh.post(self, message)

    * Creates a whisper message and injects it into the network for distribution.

    * Parameters:
        * ``to``: The receiver of the message. Can be omitted for a broadcast message. Use one of the following two fields.
            * ``public``: The public key of the recipient.
            * ``identity``: The identity of the recipient key on your local node.
        * ``from``: Asymmetric identity to sign the message with, or null.
        * ``topics``: Array of topics for the message. Should be non-empty.
        * ``payload``: Payload to be encrypted.
        * ``padding``: Optional padding. Up to 2^24 -1 bytes.
        * ``priority``: How many milliseconds to spend doing POW.
        * ``ttl``: Time-to-live (in seconds) of the message before expiry.

    * Returns ``True`` if the message was succesfully sent, otherwise ``False``

    .. code-block:: python

        >>> web3.parity.shh.post({
   		   	"from":"0x193f71c502feb0c181ed0b97352fdcebcb621c733cd80637b2154a2a2b867a12",
   			"topics":["0x12270000"],
   			"payload":"0xb10e2d527612073b26eecdfd717e6a320cf44b4afac2b0732d9fcbe2b7fa0cf6",
   			"priority":40,
   			"ttl":400
 			})
        True

.. py:method:: Shh.newMessageFilter(self, criteria)

    * Return the filter ID that can be used with ``ShhFilter`` to poll for new messages that match the set of criteria.

    * Parameters:
        * ``decryptWith``: 32 bytes - Identity of key used for description. Null if listening for broadcasts.
        * ``from``: 64 bytes - If present, only accept messages signed by this key.
        * ``topics``: Array of possible topics (or partial topics). Should be non-empty.

    * Returns the newly created filter id.

    .. code-block:: python

        >>>web3.parity.shh.newMessageFilter({'topic': '0x12340000', 'privateKeyID': recipient_private})
		0xea7120c5408c72cfd7e0e1d2ff62df8e208d9a1f85d2ed54a4a3e1ad6daeb6f9

.. py:method:: Shh.deleteMessageFilter(self, filter_id)

    * Deletes a message filter in the node.

    * Returns ``True`` if the filter was sucesfully uninstalled, otherwise ``False``

    .. code-block:: python

        >>>web3.parity.shh.deleteMessageFilter('0xea7120c5408c72cfd7e0e1d2ff62df8e208d9a1f85d2ed54a4a3e1ad6daeb6f9')
        True

.. py:method:: Shh.getMessages(self, filter_id)

    * Retrieve messages that match the filter criteria and are received between the last time this function was called and now.

    * Returns all new messages since the last invocation

    .. code-block:: python

        >>>web3.parity.shh.getMessages('0xea7120c5408c72cfd7e0e1d2ff62df8e208d9a1f85d2ed54a4a3e1ad6daeb6f9')
        [{
            'ttl': 50,
            'timestamp': 1524497850,
            'topics': HexBytes('0x13370000'),
            'payload': HexBytes('0x74657374206d657373616765203a29'),
            'padding': HexBytes('0x50ab643f1b23bc6df1b1532bb6704ad947c2453366754aade3e3597553eeb96119f4f4299834d9989dc4ecc67e6b6470317bb3f7396ace0417fc0d6d2023900d3'),
            'recipient': HexBytes('0x047d36c9e45fa82fcd27d35bc7d2fd41a2e41e512feec9e4b90ee4293ab12dcac'),
        }]

.. py:method:: Shh.subscribe(self, filter_id)

	* Open a subscription to a filter. Subscription calls are only supported on the websocket transport.

    * Returns ``True`` if the filter was sucesfully subscribed to, otherwise ``False``

  	.. code-block:: python

        >>>web3.parity.shh.subscribe('0xea7120c5408c72cfd7e0e1d2ff62df8e208d9a1f85d2ed54a4a3e1ad6daeb6f9')
		True

.. py:method:: Shh.unsubscribe(self, filter_id)

	* Close a subscribed filter.

    * Returns ``True`` if the filter subscription was sucesfully closed, otherwise ``False``

  	.. code-block:: python

        >>>web3.parity.shh.unsubscribe('0xea7120c5408c72cfd7e0e1d2ff62df8e208d9a1f85d2ed54a4a3e1ad6daeb6f9')
		True

---------------
Asymmetric Keys
---------------

.. py:method:: Shh.newKeyPair(self)

    * Generates a new cryptographic identity for the client, and injects it into the known identities for message decryption

    * Returns the new key pair's identity

    .. code-block:: python

        >>>web3.parity.shh.newKeyPair()
        '86e658cbc6da63120b79b5eec0c67d5dcfb6865a8f983eff08932477282b77bb'

.. py:method:: Shh.addPrivateKey(self, key)

    * Stores a key pair derived from a private key, and returns its ID.

    * Returns the added key pair's ID

    .. code-block:: python

        >>>web3.parity.shh.addPrivateKey('0x7b8190d96cd061a102e551ee36d08d4f3ca1f56fb0008ef5d70c56271d8c46d0')
        '86e658cbc6da63120b79b5eec0c67d5dcfb6865a8f983eff08932477282b77bb'

.. py:method:: Shh.getPublicKey(self, id)

    * Returns the public key associated with the key pair.

    .. code-block:: python

        >>>web3.parity.shh.getPublicKey('86e658cbc6da63120b79b5eec0c67d5dcfb6865a8f983eff08932477282b77bb')
        '0x041b0777ceb8cf8748fe0bba5e55039d650a03eb0239a909f9ee345bbbad249f2aa236a4b8f41f51bd0a97d87c08e69e67c51f154d634ba51a224195212fc31e4e'

.. py:method:: Shh.getPrivateKey(self, id)

    * Returns the private key associated with the key pair.

    .. code-block:: python

        >>>web3.parity.shh.getPrivateKey('86e658cbc6da63120b79b5eec0c67d5dcfb6865a8f983eff08932477282b77bb')
        '0x7b8190d96cd061a102e551ee36d08d4f3ca1f56fb0008ef5d70c56271d8c46d0'

---------------
Symmetric Keys
---------------

.. py:method:: Shh.newSymKey(self)

    * Generates a random symmetric key and stores it under id, which is then returned. Will be used in the future for session key exchange

    * Returns the new key pair's identity

    .. code-block:: python

        >>>web3.parity.shh.newSymKey()
        '6c388d63003deb378700c9dad87f67df0247e660647d6ba1d04321bbc2f6ce0c'

.. py:method:: Shh.addSymKey(self, key)

    * Stores the key, and returns its ID.

    * Returns the new key pair's identity

    .. code-block:: python

        >>>web3.parity.shh.addSymKey('0x58f6556e56a0d41b464a083161377c8a9c2e95156921f954f99ef97d41cebaa2')
        '6c388d63003deb378700c9dad87f67df0247e660647d6ba1d04321bbc2f6ce0c'

.. py:method:: Shh.getSymKey(self, id)

    * Returns the symmetric key associated with the given ID.

    * Returns the public key associated with the key pair

    .. code-block:: python

        >>>web3.parity.shh.getSymKey('6c388d63003deb378700c9dad87f67df0247e660647d6ba1d04321bbc2f6ce0c')
        '0x58f6556e56a0d41b464a083161377c8a9c2e95156921f954f99ef97d41cebaa2'

.. py:method:: Shh.deleteKey(self, id)

    * Deletes the symmetric key associated with the given ID.

    * Returns ``True`` if the key pair was deleted, otherwise ``False``

    .. code-block:: python

        >>>web3.parity.shh.deleteKey('6c388d63003deb378700c9dad87f67df0247e660647d6ba1d04321bbc2f6ce0c')
        True
