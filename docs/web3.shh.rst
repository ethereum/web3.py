SHH API
=======

.. py:module:: web3.shh
.. py:class:: Shh

The ``web3.shh`` object exposes methods to interact with the RPC APIs under the
``shh_`` namespace.

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
    
        >>>web3.shh.post({"topics":[web3.fromAscii("test_topic")],"payload":web3.fromAscii("test_payload")})
        True

.. py:method:: Shh.newIdentity(self)

    * Delegates to ``shh_newIdentity`` RPC method

    * Returns ``address`` of newly created identity.

    .. code-block:: python
   
        >>>web3.shh.newIdentity()
        "0xc931d93e97ab07fe42d923478ba2465f283f440fd6cabea4dd7a2c807108f651b7135d1d6ca9007d5b68aa497e4619ac10aa3b27726e1863c1fd9b570d99bbaf"

.. py:method:: Shh.hasIdentity(self, identity)

    * Delegates to ``shh_hasIdentity`` RPC method
 
    * Returns ``True`` if the client holds the private key for the given identity,otherwise ``False``

    .. code-block:: python
    
        >>>web3.shh.hasIdentity("0xc931d93e97ab07fe42d923478ba2465f283f440fd6cabea4dd7a2c807108f651b7135d1d6ca9007d5b68aa497e4619ac10aa3b27726e1863c1fd9b570d99bbaf")
        True

.. py:method:: Shh.newGroup(self)

    * Delegates to ``shh_newGroup`` RPC method

    * Returns ``address`` of newly created group.

    .. code-block:: python

        >>>web3.shh.newGroup()
        "0xc65f283f440fd6cabea4dd7a2c807108f651b7135d1d6ca90931d93e97ab07fe42d923478ba2407d5b68aa497e4619ac10aa3b27726e1863c1fd9b570d99bbaf"

.. py:method:: Shh.addToGroup(self, identity)

    * Delegates to ``shh_addToGroup`` RPC Method

    * Return ``True`` if the identity was succesfully added to the group,otherwise ``False``

    .. code-block:: python
   
        >>>web3.shh.addToGroup("0xc65f283f440fd6cabea4dd7a2c807108f651b7135d1d6ca90931d93e97ab07fe42d923478ba2407d5b68aa497e4619ac10aa3b27726e1863c1fd9b570d99bbaf")
        True

.. py:method:: Shh.filter(self, filter_params)

    * Delegates to ``shh_newFilter`` RPC Method

    * ``filter_params`` should contain the ``topics`` to subscribe

    * Returns an instance of ``ShhFilter`` on succesful creation of filter,otherwise raises ``ValueError`` exception

    .. code-block:: python

        >>>shh.filter({"topics":[web.fromAscii("topic_to_subscribe")]})


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
        

.. py:method:: Shh.getMessages(self, filter_id)

    * Delegates to ``shh_getMessages`` RPC Method

    * Returns a list of all messages

    .. code-block:: python
     
        >>>web3.shh.getMessages("0x2")
