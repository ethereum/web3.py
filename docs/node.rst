Your Ethereum Node
===================

.. _why_need_connection:

Why do I need to connect to a node?
--------------------------------------

The Ethereum protocol defines a way for people to interact with
smart contracts and each other over a network.
In order to have up-to-date information about the status of contracts,
balances, and new transactions, the protocol requires a connection
to nodes on the network. These nodes are constantly sharing new data
with each other.

Web3.py is a python library for connecting to these nodes. It does
not run its own node internally.

.. _choosing_node:

How do I choose which node to use?
--------------------------------------

Due to the nature of Ethereum, this is largely a question of personal preference, but
it has significant ramifications on security and usability. Further, node software is
evolving quickly, so please do your own research about the current options.
We won't advocate for any particular node,
but list some popular options and some basic details on each.

One of the primary decisions to make is whether to use a local node or a hosted
node. A quick summary is at :ref:`local-vs-hosted`.

A local node requires less trust than a hosted one.
A malicious hosted node can give you incorrect information, log your
sent transactions with your IP address, or simply go offline. Incorrect information
can cause all kinds of problems, including loss of assets.

On the other hand, with a local node your machine is individually verifying
all the transactions on the network, and providing you with the latest state.
Unfortunately, this means using up a
significant amount of disk space, and sometimes notable
bandwidth and computation.
Additionally, there is a big up-front time cost for downloading the full blockchain history.

If you want to have your
node manage keys for you (a popular option), you must use a local node.
Note that even if you run a node on your own machine, you are still trusting
the node software with any accounts you create on the node.

The most popular self-run node options are:

- `geth (go-ethereum) <https://ethereum.github.io/go-ethereum/>`_
- `parity <https://www.parity.io/>`_

You can find a fuller list of node software at `ethdocs.org
<http://ethdocs.org/en/latest/ethereum-clients/>`_.

Some people decide that the time it takes to sync a local node from scratch is too
high, especially those just experimenting for the first time. One way to
work around this issue is to use a hosted node.

The most popular hosted node option is `Infura <infura.io>`_.
You can connect to it as if it were a local node,
with a few caveats. It cannot (and *should not*) host private keys for
you, meaning that some common methods like :meth:`w3.eth.sendTransaction()
<web3.eth.Eth.sendTransaction>` are not directly available. To send trensactions
to a hosted node, read about :ref:`eth-account`.

Once you decide what node option you want, you need to choose how to connect to it.
Any given node software provides a variety of options. See
:ref:`choosing_provider`.

Can I use MetaMask as a node?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MetaMask is not a node. It is an interface for interacting with a node.
Roughly, it's what you get if you turn Web3.py into a browser extension.

By default, MetaMask connects to an Infura node.
You can also set up MetaMask to use a node that you run locally.

If you are trying to use accounts that were already created in MetaMask, see
:ref:`use-metamask-accounts`
