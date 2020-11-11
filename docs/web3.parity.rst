Parity API
==========

.. py:module:: web3.parity

The ``web3.parity`` object exposes modules that enable you to interact with the JSON-RPC endpoints supported by `Parity <https://wiki.parity.io/JSONRPC>`_ that are not defined in the standard set of Ethereum JSONRPC endpoints according to `EIP 1474 <https://github.com/ethereum/EIPs/pull/1474>`_.

.. py:module:: web3.parity.personal

ParityPersonal
--------------

The following methods are available on the ``web3.parity.personal`` namespace.

.. py:method:: list_accounts()

    * Delegates to ``personal_listAccounts`` RPC Method

    Returns the list of known accounts.

    .. code-block:: python

        >>> web3.parity.personal.list_accounts()
        ['0xd3CdA913deB6f67967B99D67aCDFa1712C293601']

.. py:method:: listAccounts

    .. warning:: Deprecated: This method is deprecated in favor of
      :meth:`~web3.parity.personal.list_accounts()`

.. py:method:: import_raw_key(self, private_key, passphrase)

    * Delegates to ``personal_importRawKey`` RPC Method

    Adds the given ``private_key`` to the node's keychain, encrypted with the
    given ``passphrase``.  Returns the address of the imported account.

    .. code-block:: python

        >>> web3.parity.personal.import_raw_key(some_private_key, 'the-passphrase')
        '0xd3CdA913deB6f67967B99D67aCDFa1712C293601'

.. py:method:: importRawKey(self, private_key, passphrase)

    .. warning:: Deprecated: This method is deprecated in favor of
      :meth:`~web3.parity.personal.import_raw_key()`

.. py:method:: new_account(self, password)

    * Delegates to ``personal_newAccount`` RPC Method

    Generates a new account in the node's keychain encrypted with the
    given ``passphrase``.  Returns the address of the created account.

    .. code-block:: python

        >>> web3.parity.personal.new_account('the-passphrase')
        '0xd3CdA913deB6f67967B99D67aCDFa1712C293601'

.. py:method:: newAccount(self, password)

    .. warning:: Deprecated: This method is deprecated in favor of
      :meth:`~web3.parity.personal.new_account()`

.. py:method:: unlock_account(self, account, passphrase, duration=None)

    * Delegates to ``personal_unlockAccount`` RPC Method

    Unlocks the given ``account`` for ``duration`` seconds.  If ``duration`` is
    ``None`` then the account will remain unlocked indefinitely.  Returns
    boolean as to whether the account was successfully unlocked.

    .. code-block:: python

        # Invalid call to personal_unlockAccount on Parity currently returns True, due to Parity bug
        >>> web3.parity.personal.unlock_account('0xd3CdA913deB6f67967B99D67aCDFa1712C293601', 'wrong-passphrase')
        True
        >>> web3.parity.personal.unlock_account('0xd3CdA913deB6f67967B99D67aCDFa1712C293601', 'the-passphrase')
        True

.. py:method:: unlockAccount(self, account, passphrase, duration=None)

    .. warning:: Deprecated: This method is deprecated in favor of
      :meth:`~web3.parity.personal.unlock_account()`

.. py:method:: send_transaction(self, transaction, passphrase)

    * Delegates to ``personal_sendTransaction`` RPC Method

    Sends the transaction.

.. py:method:: sendTransaction(self, account, passphrase, duration=None)

    .. warning:: Deprecated: This method is deprecated in favor of
      :meth:`~web3.parity.personal.send_transaction()`

.. py:method:: sign_typed_data(self, jsonMessage, account, passphrase)

    * Delegates to ``personal_signTypedData`` RPC Method

    Please note that the ``jsonMessage`` argument is the loaded JSON Object
    and **NOT** the JSON String itself.

    Signs the ``Structured Data`` (or ``Typed Data``) with the passphrase of the given ``account``

.. py:method:: signTypedData(self, jsonMessage, account, passphrase)

    .. warning:: Deprecated: This method is deprecated in favor of
      :meth:`~web3.parity.personal.sign_typed_data()`
