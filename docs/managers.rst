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

.. warning:: The ``DelegatedSigningManager`` has been deprecated and will be removed in subsequent releases.

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


.. code-block:: python

    # setup RPC provider connected to infura.
    >>> web3 = Web3(Web3.RPCProvider(host='mainnet.infura.io', path='your-infura-access-key'))
    # create second manager connected to local node (which must be unlocked)
    >>> signature_manager = web3.RequestManager(IPCProvider())
    # Setup the signing manager.
    >>> delegated_manager = Web3.DelegatedSigningManager(web3._requestManager, signature_manager)
    >>> web3.setManager(delegated_manager)
    >>> web3.eth.sendTransaction({
    ...     'from': '0x...'
    ...     ...
    ... }) 
    
In this example the transaction will be signed using the locally unlocked IPC
node and then the public Infura RPC node is used relay the pre-signed
transaction to the network using the ``eth_sendRawTransaction`` method.


Private Key Signing Manager
---------------------------

.. warning:: The ``PrivateKeySigningManager`` has been deprecated and will be removed in subsequent releases.

.. py:class:: PrivateKeySigningManager(wrapped_manager, keys={})

    This manager is similar to the ``DelegatedSigningManager`` except that
    rather than delegating to a node to do the signing, it holds the private
    keys and does the signing itself.

    The optional ``keys`` constructor should be a mapping between ethereum
    address and private key encoded as bytes.

.. py:method:: PrivateKeySigningManager.register_private_key(key)

    This method registers a private key with the manager which will allow
    sending from the derived address.


.. code-block:: python

    >>> web3 = Web3(Web3.RPCProvider(host='mainnet.infura.io', path='your-infura-access-key'))
    >>> pk_manager = Web3.PrivateKeySigningManager(web3._requestManager)
    >>> pk_manager.register_private_key(b'the-private-key-as-bytes')
    >>> web3.setManager(pk_manager)
    >>> web3.eth.sendTransaction({
    ...     'from': '0x...'  # the public address for the registered private key.
    ...     ...
    ... }) 

In this example, the transaction will be signed using the private key it was
given, after which it will be sent using the ``eth_sendRawTransaction`` through
the connected Infura RPC node.
