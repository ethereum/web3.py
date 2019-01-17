Package Manager API
===================


The ``web3.pm`` object exposes methods to interact with Packages as defined by `ERC 1123 <https://github.com/ethereum/EIPs/issues/1123>`_.

To learn more about the EthPM spec, visit the `documentation <http://ethpm.github.io/ethpm-spec/>`__.
To learn more about the Py-EthPM library used in this module, visit the `documentation <https://py-ethpm.readthedocs.io/en/latest/>`__.


.. WARNING::

   The ``web3.pm`` API is still under development and likely to change quickly.

   Now is a great time to get familiar with the API, and test out writing
   code that uses some of the great upcoming features.

   By default, access to this module has been turned off in the stable version of Web3.py:

   .. code-block:: python

      >>> from web3.auto import w3
      >>> w3.pm
      ...
      AttributeError: The Package Management feature is disabled by default ...

   In order to access these features, you can turn it on with...

   .. code-block:: python

      >>> web3.enable_unstable_package_management_api()
      >>> w3.pm
      <web3.pm.PM at 0x....>


Methods
-------
The following methods are available on the ``web3.pm`` namespace.

.. autoclass:: web3.pm.PM
   :members:

.. note:: If you want to implement your own registry and use it with ``web3.pm``, you must create a subclass that inherits from ``ERCRegistry``, implements all the methods defined in ``ERCRegistry``, and manually set it as the ```registry`` attribute on ``web3.pm``.

.. autoclass:: web3.pm.ERCRegistry
   :members: __init__, _release, _get_package_name, _get_all_package_ids, _get_release_id, _get_all_release_ids, _get_release_data, _generate_release_id, _num_package_ids, _num_release_ids

.. autoclass:: web3.pm.VyperReferenceRegistry
   :members: deploy_new_instance, owner, transfer_owner

.. autoclass:: web3.pm.SolidityReferenceRegistry
   :members:

