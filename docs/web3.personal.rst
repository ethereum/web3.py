Personal API
============

.. py:module:: web3.personal

.. py:class:: Personal

The ``web3.personal`` object exposes methods to interact with the RPC APIs
under the ``personal_`` namespace.


Properties
----------

The following properties are available on the ``web3.personal`` namespace.

.. py:attribute:: listAccounts

    * Delegates to ``personal_listAccounts`` RPC Method

    Returns the list of known accounts.

    .. code-block:: python

        >>> web3.personal.listAccounts
        ['0xd3cda913deb6f67967b99d67acdfa1712c293601']


Methods
-------

The following methods are available on the ``web3.personal`` namespace.

.. py:method:: importRawKey(self, private_key, passphrase)

    * Delegates to ``personal_importRawKey`` RPC Method

    Adds the given ``private_key`` to the node's keychain, encrypted with the
    given ``passphrase``.  Returns the address of the imported account.

    .. code-block:: python

        >>> web3.personal.importRawKey(some_private_key, 'the-passphrase')
        ['0xd3cda913deb6f67967b99d67acdfa1712c293601']


.. py:method:: newAccount(self, password=None)

    * Delegates to ``personal_newAccount`` RPC Method

    Generates a new account in the node's keychain encrypted with the
    given ``passphrase``.  Returns the address of the created account.

    .. code-block:: python

        >>> web3.personal.newAccount('the-passphrase')
        ['0xd3cda913deb6f67967b99d67acdfa1712c293601']


.. py:method:: signAndSendTransaction(self, tx, passphrase)

    * Delegates to ``personal_signAndSendTransaction`` RPC Method

    Signs and sends the given ``transaction`` without requiring the ``from``
    account to be unlocked.  ``passphrase`` must be the passphrase for the
    ``from`` account for the provided ``transaction``.

    Behaves in the same manner as
    :py:method::`web3.eth.Eth.sendTransaction(transaction)`.

    .. code-block:: python

        >>> web3.personal.signAndSendTransaction({'to': '0xd3cda913deb6f67967b99d67acdfa1712c293601', 'from': web3.eth.coinbase, 'value': 12345}, 'the-passphrase')
        '0xe670ec64341771606e55d6b4ca35a1a6b75ee3d5145a99d05921026d1527331'


.. py:method:: lockAccount(self, account)

    * Delegates to ``personal_lockAccount`` RPC Method

    Locks the given ``account``.

    .. code-block:: python

        >>> web3.personal.lockAccount('0xd3cda913deb6f67967b99d67acdfa1712c293601')


.. py:method:: unlockAccount(self, account, passphrase, duration=None)

    * Delegates to ``personal_unlockAccount`` RPC Method

    Unlocks the given ``account`` for ``duration`` seconds.  If ``duration`` is
    ``None`` then the account will remain unlocked indefinitely.  Returns
    boolean as to whether the account was successfully unlocked.

    .. code-block:: python

        >>> web3.personal.unlockAccount('0xd3cda913deb6f67967b99d67acdfa1712c293601', 'wrong-passphrase')
        False
        >>> web3.personal.unlockAccount('0xd3cda913deb6f67967b99d67acdfa1712c293601', 'the-passphrase')
        True
