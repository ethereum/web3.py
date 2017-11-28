Ethereum Name Service
================================

The Ethereum Name Service is analogous to the Domain Name Service. It
enables users and developers to use human-friendly names in place of error-prone
hexadecimal addresses, content hashes, and more.

The :mod:`ens` module is included with web3.py. It provides an interface to look up
an address from a name, set up your own address, and more.

Setup
-----

Create an :class:`~ens.main.ENS` object (named ``ns`` below) in one of three ways:

1. Automatic detection
2. Specify an instance or list of :ref:`providers`
3. From an existing :class:`web3.Web3` object

::

    # automatic detection
    from ens.auto import ns


    # or, with a provider
    from web3 import IPCProvider
    from ens import ENS

    provider = IPCProvider(...)
    ns = ENS(provider)


    # or, with a w3 instance
    from ens import ENS

    w3 = Web3(...)
    ns = ENS.fromWeb3(w3)


Usage
-----

Name info
~~~~~~~~~

.. _ens_get_address:

Look up the address for an ENS name
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    from ens.auto import ns


    # look up the hex representation of the address for a name

    eth_address = ns.address('jasoncarver.eth')

    assert eth_address == '0x5B2063246F2191f18F2675ceDB8b28102e957458'


    # ens.py will assume you want a .eth name if you don't specify a full name

    assert ns.address('jasoncarver') == eth_address


Get name from address
^^^^^^^^^^^^^^^^^^^^^

::

    domain = ns.name('0x5B2063246F2191f18F2675ceDB8b28102e957458')


    # name() also accepts the bytes version of the address

    assert ns.name(b'[ c$o!\x91\xf1\x8f&u\xce\xdb\x8b(\x10.\x95tX') == domain


    # confirm that the name resolves back to the address that you looked up:

    assert ns.address(domain) == '0x5B2063246F2191f18F2675ceDB8b28102e957458'

Get owner of name
^^^^^^^^^^^^^^^^^

::

    eth_address = ns.owner('exchange.eth')

Set up your name
~~~~~~~~~~~~~~~~

Point your name to your address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Do you want to set up your name so that :meth:`~ens.main.ENS.address` will show the
address it points to?

::

    ns.setup_address('jasoncarver.eth', '0x5B2063246F2191f18F2675ceDB8b28102e957458')

You must already be the owner of the domain (or its parent).

In the common case where you want to point the name to the owning
address, you can skip the address

::

    ns.setup_address('jasoncarver.eth')

You can claim arbitrarily deep subdomains. *Gas costs scale up with the
number of subdomains!*

::

    ns.setup_address('supreme.executive.power.derives.from.a.mandate.from.the.masses.jasoncarver.eth')

Wait for the transaction to be mined, then:

::

    assert ns.address('supreme.executive.power.derives.from.a.mandate.from.the.masses.jasoncarver.eth') == \
        '0x5B2063246F2191f18F2675ceDB8b28102e957458'

Allow people to find your name using your address
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Do you want to set up your address so that :meth:`~ens.main.ENS.name` will show the
name that points to it?

This is like Caller ID. It enables you and others to take an account and
determine what name points to it. Sometimes this is referred to as
"reverse" resolution.

::

    ns.setup_name('jasoncarver.eth', '0x5B2063246F2191f18F2675ceDB8b28102e957458')

.. note:: Do not rely on reverse resolution for security.

  Anyone can claim any "caller ID". Only forward resolution implies that
  the owner of the name gave their stamp of approval.

If you don't supply the address, :meth:`~ens.main.ENS.setup_name` will assume you want the
address returned by :meth:`~ens.main.ENS.address`.

::

    ns.setup_name('jasoncarver.eth')

If the name doesn't already point to an address, :meth:`~ens.main.ENS.setup_name` will
call :meth:`~ens.main.ENS.setup_address` for you.

Wait for the transaction to be mined, then:

::

    assert ns.name('0x5B2063246F2191f18F2675ceDB8b28102e957458') == 'jasoncarver.eth'
