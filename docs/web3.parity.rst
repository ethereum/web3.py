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
