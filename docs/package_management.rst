.. _package_management:

Package Management
==================

.. py:module:: web3.pm

Web3.py provides a number of features for installing and using resources in
EthPM packages.  These features enable a user to perform any task or realize
any use-case detailed in the `EthPM specification
<http://ethpm.github.io/ethpm-spec/index.html>`_.  Below, we'll go over a
number of examples of how to use this functionality in web3.py.

.. _pm_download_a_package:

Downloading a Package
---------------------

To use a package with web3.py, its manifest file must be downloaded or read
from the local filesystem.  In the code snippet below, a number of different
approaches are used to get a package object for a ``greeter`` package:

.. code-block:: python

    >>> from web3 import Web3, HTTPProvider
    >>> w3 = Web3(HTTPProvider('https://ropsten.infura.io/<token>'))

    >>> # Get a package from a registry URI
    >>> greeter_pkg = w3.pm.get_package_from_uri('ens://packages.ethereum.eth/greeter')

    >>> # Get a package from a content-addressed URI
    >>> greeter_pkg = w3.pm.get_package_from_uri('ipfs://QmdFzNU6SHyvfMZWSGzo6V17ftFgfL47EC88u6UiR2ofnA')

    >>> # Get a package from a file system path
    >>> greeter_pkg = w3.pm.get_package_from_path('greeter/1.0.0.json')

With this :py:class:`~ethpm.package.Package` object ``greeter_pkg``, we can
access any of the resources provided by the ``greeter`` package.

Interacting with a Deployed Contract
------------------------------------

A package can contain an address for an instance of a deployed contract.  For
example, the ``greeter`` package, which was mentioned in the
:ref:`pm_download_a_package` section, contains an address for a deployed
instance of its ``Greeter`` contract on Ropsten.  Here's how we can get a
:py:class:`~web3.contract.Contract` object for this deployed instance:

.. code-block:: python

    >>> greeter_pkg = w3.pm.get_package_from_uri('ipfs://QmdFzNU6SHyvfMZWSGzo6V17ftFgfL47EC88u6UiR2ofnA')

    >>> # Get a deployment by name
    >>> greeter = greeter_pkg.get_deployment('Greeter')
