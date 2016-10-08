Managers
========

.. py:module:: web3.providers.manager
.. py:currentmodule:: web3.providers.manager


Managers control the flow of RPC requests that get passed to and from whatever
provider is in use.


RequestManager
--------------

.. py:class:: RequestManager(provider)

    This is the default manager that web3 will use.



Delegated Signing Manager
-------------------------


.. py:class:: DelegatedSigningManager(wrapped_manager, signing_manager)

    This manager incercepts any attempt to send a transaction and instead
    routes it through the ``eth_sendRawTransaction`` method, using the
    ``signing_manager`` to sign the transactions, and the ``wrapped_manager``
    for the actual sending of the transaction.

    Any calls to the following RPC methods will incercepted:

    * ``eth_sendTransaction``
    * ``personal_sendTransaction``
    * ``personal_signAndSendTransaction``

    The ``signing_manager`` is only used for the signing of transactions via
    the ``eth_sign`` RPC method.  Any account which you wish to send from needs
    to be unlocked on whatever node this manager is connected to.

    The ``wrapped_manager`` is used for all other RPC methods.

    This manager is useful for using a public Ethreum node such as Infura for
    your RPC interactions while keeping your private keys held on a local node
    that does not need to be connected or synced with the network.


Private Key Signing Manager
---------------------------

.. py:class:: PrivateKeySigningManager(wrapped_manager, keys={})

    This manager is similar to the ``DelegatedSigningManager`` except that
    rather than delegating to a node to do the signing, it holds the private
    keys and does the signing itself.

    The optional ``keys`` constructor should be a mapping between ethereum
    address and private key encoded as bytes.

.. py:method:: PrivateKeySigningManager.register_private_key(key)

    This method registers a private key with the manager which will allow
    sending from the derived address.
