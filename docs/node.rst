Your Ethereum Node
===================

.. _why_need_connection:

Why do I need to connect to a node?
-----------------------------------

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
----------------------------------

Due to the nature of Ethereum, this is largely a question of personal preference, but
it has significant ramifications on security and usability. Further, node software is
evolving quickly, so please do your own research about the current options.

One of the key decisions is whether to use a local node or a hosted
node. A quick summary is at :ref:`local_vs_hosted`.

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

You can find a list of node software at `ethereum.org
<https://ethereum.org/en/developers/docs/nodes-and-clients/>`__.

Some people decide that the time it takes to sync a local node from scratch is too
high, especially if they are just exploring Ethereum for the first time. One way to
work around this issue is to use a hosted node.

Hosted node options can also be found at
`ethereum.org <https://ethereum.org/en/developers/docs/nodes-and-clients/nodes-as-a-service/>`__.
You can connect to a hosted node as if it were a local node,
with a few caveats. It cannot (and *should not*) host private keys for
you, meaning that some common methods like :meth:`w3.eth.send_transaction()
<web3.eth.Eth.send_transaction>` are not directly available. To send transactions
to a hosted node, read about :ref:`eth-account`.

Once you decide what node option you want, you need to choose which network to connect to.
Typically, you are choosing between the main network and one of the available test networks.
See :ref:`choosing_network`

Can I use MetaMask as a node?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MetaMask is not a node. It is an interface for interacting with a node.
Roughly, it's what you get if you turn Web3.py into a browser extension.

By default, MetaMask connects to an Infura node.
You can also set up MetaMask to use a node that you run locally.

If you are trying to use accounts that were already created in MetaMask, see
:ref:`use_metamask_accounts`

.. _choosing_network:

Which network should I connect to?
----------------------------------

Once you have answered :ref:`choosing_node` you have to pick which network
to connect to. This is easy for some scenarios: if you have ether and you want
to spend it, or you want to interact with any production smart contracts,
then you connect to the main Ethereum network.

If you want to test these things without using real ether, though, then you
need to connect to a test network. There are several test networks to
choose from; view the list on
`ethereum.org <https://ethereum.org/en/developers/docs/networks/#ethereum-testnets>`__.

Each network has its own version of Ether. Main network ether must
be purchased, naturally, but test network ether is usually available for free.
See :ref:`faucets`

Once you have decided which network to connect to, and set up your node for that network,
you need to decide how to connect to it. There are a handful of options in most nodes.
See :ref:`choosing_provider`.
