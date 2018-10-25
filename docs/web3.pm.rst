Package Manager API
===================

.. py:module:: web3.pm
.. py:class:: PM

The ``web3.pm`` object exposes methods to interact with Packages as defined by `ERC 1123 <https://github.com/ethereum/EIPs/issues/1123>`_.


Installation
------------

.. warning:: The PM module is still under development, and not all use-cases are currently supported, so it is not included by default in the web3 instance.

Attaching
---------

To use ``web3.pm``, attach it to your ``web3`` instance.

.. code-block:: python

   from web3.pm import PM
   PM.attach(web3, 'pm')


Methods
-------

The following methods are available on the ``web3.pm`` namespace.

.. autoclass:: web3.pm.PM
   :members:

.. note:: The ``web3.pm.Registry`` class is not designed to be interacted with directly, rather via the ``web3.pm.PM`` api.

.. autoclass:: web3.pm.Registry
   :members:
