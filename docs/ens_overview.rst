.. _ens_overview:

Ethereum Name Service (ENS)
===========================

The Ethereum Name Service (ENS) is analogous to the Domain Name Service. It
enables users and developers to use human-friendly names in place of error-prone
hexadecimal addresses, content hashes, and more.

The :mod:`ens` module is included with Web3.py. It provides an interface to look up
domains and addresses, add resolver records, or get and set metadata.

Setup
-----

Create an :class:`~ens.ENS` object (named ``ns`` below) in one of three ways:

1. Automatic detection
2. Specify an instance or list of :ref:`providers`
3. From an existing :class:`web3.Web3` object

.. code-block:: python

    # automatic detection
    from ens.auto import ns

    # or, with a provider
    from web3 import IPCProvider
    from ens import ENS

    provider = IPCProvider(...)
    ns = ENS(provider)

    # or, with a w3 instance
    # Note: This inherits the w3 middlewares from the w3 instance and adds a stalecheck middleware to the middleware onion
    from ens import ENS
    w3 = Web3(...)
    ns = ENS.fromWeb3(w3)


Asynchronous support is available via the ``AsyncENS`` module:

.. code-block:: python

    from ens import AsyncENS

    ns = AsyncENS(provider)


Note that an ``ens`` module instance is also avaliable on the ``w3`` instance.
The first time it's used, Web3.py will create the  ``ens`` instance using
``ENS.fromWeb3(w3)`` or ``AsyncENS.fromWeb3(w3)`` as appropriate.

.. code-block:: python

    # instantiate w3 instance
    from web3 import Web3, IPCProvider
    w3 = Web3(IPCProvider(...))

    # use the module
    w3.ens.address('ethereum.eth')


Usage
-----

Name Info
~~~~~~~~~

.. _ens_get_address:

Get the Address for an ENS Name
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from ens.auto import ns
    eth_address = ns.address('jasoncarver.eth')
    assert eth_address == '0x5B2063246F2191f18F2675ceDB8b28102e957458'

The ``ENS`` module has no opinion as to which TLD you can use,
but will not infer a TLD if it is not provided with the name.

Get the ENS Name for an Address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    domain = ns.name('0x5B2063246F2191f18F2675ceDB8b28102e957458')

    # name() also accepts the bytes version of the address
    assert ns.name(b'[ c$o!\x91\xf1\x8f&u\xce\xdb\x8b(\x10.\x95tX') == domain

    # confirm that the name resolves back to the address that you looked up:
    assert ns.address(domain) == '0x5B2063246F2191f18F2675ceDB8b28102e957458'

.. note:: For accuracy, and as a recommendation from the ENS documentation on
    `reverse resolution <https://docs.ens.domains/dapp-developer-guide/resolving-names#reverse-resolution>`_,
    the ``ENS`` module now verifies that the forward resolution matches the address with every call to get the
    ``name()`` for an address. This is the only sure way to know whether the reverse resolution is correct. Anyone can
    claim any name, only forward resolution implies that the owner of the name gave their stamp of approval.

Get the Owner of a Name
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    eth_address = ns.owner('exchange.eth')

....

Set Up Your Name and Address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Link a Name to an Address
^^^^^^^^^^^^^^^^^^^^^^^^^

You can set up your name so that :meth:`~ens.ENS.address` will show the address it points to. In order to do so,
you must already be the owner of the domain (or its parent).

.. code-block:: python

    ns.setup_address('jasoncarver.eth', '0x5B2063246F2191f18F2675ceDB8b28102e957458')

In the common case where you want to point the name to the owning address, you can skip the address.

.. code-block:: python

    ns.setup_address('jasoncarver.eth')

You can claim arbitrarily deep subdomains.

.. code-block:: python

    ns.setup_address('supreme.executive.power.derives.from.a.mandate.from.the.masses.jasoncarver.eth')

    # wait for the transaction to be mined, then:
    assert (
        ns.address('supreme.executive.power.derives.from.a.mandate.from.the.masses.jasoncarver.eth')
        == '0x5B2063246F2191f18F2675ceDB8b28102e957458'
    )

.. warning:: Gas costs scale up with the number of subdomains!

Link an Address to a Name
^^^^^^^^^^^^^^^^^^^^^^^^^

You can set up your address so that :meth:`~ens.ENS.name` will show the name that points to it.

This is like Caller ID. It enables you and others to take an account and determine what name points to it. Sometimes
this is referred to as "reverse" resolution. The ENS Reverse Resolver is used for this functionality.

.. code-block:: python

    ns.setup_name('jasoncarver.eth', '0x5B2063246F2191f18F2675ceDB8b28102e957458')

If you don't supply the address, :meth:`~ens.ENS.setup_name` will assume you want the
address returned by :meth:`~ens.ENS.address`.

.. code-block:: python

    ns.setup_name('jasoncarver.eth')

If the name doesn't already point to an address, :meth:`~ens.ENS.setup_name` will
call :meth:`~ens.ENS.setup_address` for you.

Wait for the transaction to be mined, then:

.. code-block:: python

    assert ns.name('0x5B2063246F2191f18F2675ceDB8b28102e957458') == 'jasoncarver.eth'

....

Text Records
~~~~~~~~~~~~

Set Text Metadata for an ENS Record
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

As the owner of an ENS record, you can add text metadata.
A list of supported fields can be found in the
`ENS documentation <https://docs.ens.domains/contract-api-reference/publicresolver#get-text-data>`_.
You'll need to setup the address first, and then the text can be set:

.. code-block:: python

    ns.setup_address('jasoncarver.eth', '0x5B2063246F2191f18F2675ceDB8b28102e957458')
    ns.set_text('jasoncarver.eth', 'url', 'https://example.com')

A transaction dictionary can be passed as the last argument if desired:

.. code-block:: python

    transaction_dict = {'from': '0x123...'}
    ns.set_text('jasoncarver.eth', 'url', 'https://example.com', transaction_dict)

If the transaction dictionary is not passed, sensible defaults will be used, and if
a transaction dictionary is passed but does not have a ``from`` value,
the default will be the ``owner``.

Read Text Metadata for an ENS Record
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Anyone can read the data from an ENS Record:

.. code-block:: python

    url = ns.get_text('jasoncarver.eth', 'url')
    assert url == 'https://example.com'

....

Working With Resolvers
~~~~~~~~~~~~~~~~~~~~~~

Get the Resolver for an ENS Record
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can get the resolver for an ENS name via the :meth:`~ens.ENS.resolver` method.

.. code-block:: python

    >>> resolver = ns.resolver('jasoncarver.eth')
    >>> resolver.address
    '0x5FfC014343cd971B7eb70732021E26C35B744cc4'

....

Wildcard Resolution Support
---------------------------

The ``ENS`` module supports Wildcard Resolution for resolvers that implement the ``ExtendedResolver`` interface
as described in `ENSIP-10 <https://docs.ens.domains/ens-improvement-proposals/ensip-10-wildcard-resolution>`_.
Resolvers that implement the extended resolver interface should return ``True`` when calling the
``supportsInterface()`` function with the extended resolver interface id ``"0x9061b923"`` and should resolve subdomains
to a unique address.
