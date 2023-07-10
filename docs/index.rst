.. meta::
   :description: Python Web3 SDK for Ethereum and EVM blockchains

.. important::

    For **ENS (Ethereum Name Service)** users, web3.py ``v6.1.0`` introduced ENS name
    normalization standard
    `ENSIP-15 <https://docs.ens.domains/ens-improvement-proposals/ensip-15-normalization-standard>`_
    by default. This update to ENS name validation and normalization won't affect ~99%
    of names but may prevent invalid names from being created and from interacting with
    the ENS contracts via web3.py. We feel strongly that this change, though breaking,
    is in the best interest of our users as it ensures compatibility with the latest ENS
    standards.

gm
==

**web3.py** is a Python library for interacting with Ethereum.

It's commonly found in `decentralized apps (dapps)`_ to help with
sending transactions, interacting with smart contracts, reading
block data, and a variety of other use cases.

The original API was derived from the `Web3.js`_ Javascript API,
but has since evolved toward the needs and creature comforts of
Python developers.


Getting Started
---------------

.. NOTE::
   👋 Brand new to Ethereum?

   0. Don't travel alone! Join the Ethereum Python Community `Discord`_.
   1. Read this `blog post series`_ for a gentle introduction to Ethereum blockchain concepts.
   2. The :ref:`Overview` page will give you a quick idea of what else web3.py can do.
   3. Try building a little something!

- Ready to code? → :ref:`quickstart`
- Interested in a quick tour? → :ref:`overview`
- Need help debugging? → `StackExchange`_
- Found a bug? → :ref:`Contribute <contributing>`
- Want to chat? → `Discord`_
- Read the source? → `Github`_

.. include:: toc.rst


.. _decentralized apps (dapps): https://ethereum.org/dapps/
.. _Web3.js: https://web3js.readthedocs.io/
.. _blog post series: https://snakecharmers.ethereum.org/a-developers-guide-to-ethereum-pt-1
.. _StackExchange: https://ethereum.stackexchange.com/questions/tagged/web3.py
.. _Discord: https://discord.gg/GHryRvPB84
.. _Github: https://github.com/ethereum/web3.py
