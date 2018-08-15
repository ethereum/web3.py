Package Manager API
===================

.. py:module:: web3.pm
.. py:class:: PM

The ``web3.pm`` object exposes methods to interact with Packages as defined by `ERC 1123 <https://github.com/ethereum/EIPs/issues/1123>`_.


Installation
------------

.. warning:: The PM module is still under development, and not all use-cases are currently supported, so it is not included by default in the web3 instance.

You must install the eth-pm module separately, until it is stable. Install with:

.. code-block:: python

  pip install --upgrade ethpm

Attaching
---------

To use ``web3.pm``, attach it to your ``web3`` instance.

.. code-block:: python

   from web3.pm import PM
   PM.attach(web3, 'pm')


Methods
-------

The following methods are available on the ``web3.pm`` namespace.

.. py:method:: PM.get_package_from_manifest(self, manifest)
    
    * :manifest: must be a dict representing a valid manifest
    * Returns a ``Package`` instance representing the Manifest

.. py:method:: PM.get_package_from_uri(self, uri)

    * :uri: must be a valid content-addressed URI, as defined in the `Py-EthPM Documentation <https://py-ethpm.readthedocs.io/en/latest/uri_backends.html>`_.
    * Returns a ``Package`` isntance representing the Manifest stored at the URI.
