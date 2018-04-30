Troubleshooting
=============================

.. _setup_environment:

Set up a clean environment
----------------------------------------------

Many things can cause a broken environment. You might be on an unsupported version of Python.
Another package might be installed that has a name or version conflict.
Often, the best way to guarantee a correct environment is with ``virtualenv``, like:

.. code-block:: shell

    # Install pip if it is not available:
    $ which pip || curl https://bootstrap.pypa.io/get-pip.py | python

    # Install virtualenv if it is not available:
    $ which virtualenv || pip install --upgrade virtualenv

    # *If* the above command displays an error, you can try installing as root:
    $ sudo pip install virtualenv

    # Create a virtual environment:
    $ virtualenv -p python3 ~/.venv-py3

    # Activate your new virtual environment:
    $ source ~/.venv-py3/bin/activate

    # With virtualenv active, make sure you have the latest packaging tools
    $ pip install --upgrade pip setuptools

    # Now we can install web3.py...
    $ pip install --upgrade web3

.. NOTE:: Remember that each new terminal session requires you to reactivate your virtualenv, like:
    ``$ source ~/.venv-py3/bin/activate``

.. _use_metamask_accounts:

How do I use my MetaMask accounts from Web3.py?
--------------------------------------------------------
Often you don't need to do this, just make a new account in Web3.py,
and transfer funds from your MetaMask account into it. But if you must...

Export your private key from MetaMask, and use
the local private key tools in Web3.py to sign and send transactions.

See `how to export your private key
<https://ethereum.stackexchange.com/questions/33053/what-is-a-private-key-in-an-ethereum-wallet-like-metamask-and-how-do-i-find-it>`_
and :ref:`eth-account`.

.. _faucets:

How do I get ether for my test network?
--------------------------------------------------------

Test networks usually have something called a "faucet" to
help get test ether to people who want to use it. The faucet
simply sends you test ether when you visit a web page, or ping a chat bot, etc.

Each test network has its own version of test ether, so each one
must maintain its own faucet. If you're not sure which test network
to use, see :ref:`choosing_network`

Faucet mechanisms tend to come and go, so if any information here is
out of date, try the `Ethereum Stackexchange <https://ethereum.stackexchange.com/>`_.
Here are some links to testnet ether instructions (in no particular order):

- `Kovan <https://github.com/kovan-testnet/faucet>`_
- `Rinkeby <https://www.rinkeby.io/#faucet>`_
- `Ropsten <https://www.reddit.com/r/ethdev/comments/72ltwj/the_new_if_you_need_some_ropsten_testnet_ethers/>`_
