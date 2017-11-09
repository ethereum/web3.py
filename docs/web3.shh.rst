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
        2

Methods
-------

The following methods are available on the ``web3.shh`` namespace.


.. py:method:: Shh.post(self, params)

    * Delegates to ``shh_post`` RPC method

    * ``params`` cannot be ``None`` and should contain ``topics`` and ``payload``
 
    * Returns ``True`` if the message was succesfully sent,otherwise ``False``

    .. code-block:: python
    
        >>>web3.shh.post({"topics":[web3.toHex(text="test_topic")],"payload":web3.toHex(text="test_payload")})
        True

.. py:method:: Shh.newIdentity(self)

    * Delegates to ``shh_newIdentity`` RPC method

    * Returns ``address`` of newly created identity.

    .. code-block:: python
   
        >>>web3.shh.newIdentity()
        u'0x045ed8042f436e1b546afd16e1f803888b896962484c0154fcc7c5fc43e276972af85f29a995a3beb232a4e9a0648858c0c8c0639d709f5d3230807d084b2d5030'        

.. py:method:: Shh.hasIdentity(self, identity)

    * Delegates to ``shh_hasIdentity`` RPC method
 
    * Returns ``True`` if the client holds the private key for the given identity,otherwise ``False``

    .. code-block:: python
    
        >>>web3.shh.hasIdentity(u'0x045ed8042f436e1b546afd16e1f803888b896962484c0154fcc7c5fc43e276972af85f29a995a3beb232a4e9a0648858c0c8c0639d709f5d3230807d084b2d5030')
        True

.. py:method:: Shh.newGroup(self)

    * Delegates to ``shh_newGroup`` RPC method

    * Returns ``address`` of newly created group.

    .. note:: This method is not implemented yet in ``Geth``. `Open Issue <https://github.com/ethereum/go-ethereum/issues/310>`_

.. py:method:: Shh.addToGroup(self, identity)

    * Delegates to ``shh_addToGroup`` RPC Method

    * Returns ``True`` if the identity was succesfully added to the group,otherwise ``False``

    .. note:: This method is not implemented yet in ``Geth``. `Open Issue <https://github.com/ethereum/go-ethereum/issues/310>`_

.. py:method:: Shh.filter(self, filter_params)

    * Delegates to ``shh_newFilter`` RPC Method

    * ``filter_params`` should contain the ``topics`` to subscribe

    * Returns an instance of ``ShhFilter`` on succesful creation of filter,otherwise raises ``ValueError`` exception

    .. code-block:: python

        >>>shh_filter = shh.filter({"topics":[web.toHex(text="topic_to_subscribe")]})
        >>>shh_filter.filter_id
        u'0x0'

.. py:method:: Shh.uninstallFilter(self, filter_id)

    * Delegates to ``shh_uninstallFilter`` RPC Method

    * Returns ``True`` if the filter was sucesfully uninstalled ,otherwise ``False``

    .. code-block:: python

        >>>web3.shh.uninstallFilter("0x2")
        True

.. py:method:: Shh.getFilterChanges(self, filter_id)

    * Delegates to ``shh_getFilterChanges`` RPC Method

    * Returns list of messages recieved since last poll
    
    .. code-block:: python
       
        >>>web3.shh.getFilterChanges(self,"0x2")
        [{u'from': u'0x0', u'to': u'0x0', u'ttl': 50, u'hash': u'0xf84900b57d856a6ab1b41afc9784c31be48e841b9bcfc6accac14d05d7189f2f', u'payload': u'0x746573696e67', u'sent': 1476625149}]

.. py:method:: Shh.getMessages(self, filter_id)

    * Delegates to ``shh_getMessages`` RPC Method

    * Returns a list of all messages

    .. code-block:: python
     
        >>>web3.shh.getMessages("0x2")
        [{u'from': u'0x0', u'to': u'0x0', u'ttl': 50, u'hash': u'0x808d74d003d1dcbed546cca29d7a4e839794c226296b613b0fa7a8c670f84146', u'payload': u'0x746573696e67617364', u'sent': 1476625342}, {u'from': u'0x0', u'to': u'0x0', u'ttl': 50, u'hash': u'0x62a2eb9a19968d59d8a85e6dc8d73deb9b4cd40c83d95b796262d6affe6397c6', u'payload': u'0x746573696e67617364617364', u'sent': 1476625369}]
