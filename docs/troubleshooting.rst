Troubleshooting
=============================

.. _setup-environment:

Set up a clean environment
------------------------------------------------

Many things can cause a broken environment. You might be on an unsupported version of Python.
Another package might be installed that has a name or version conflict.
Often, the best way to guarantee a correct environment is with ``virtualenv``, like:

.. code-block:: shell

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

.. _use-metamask-accounts:

How do I use my Metamask accounts from Web3.py?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This requires exporting your private key from metamask, and using
the local private key tools in web3 to sign and send transactions.

See `how to export your private key
<https://ethereum.stackexchange.com/questions/33053/what-is-a-private-key-in-an-ethereum-wallet-like-metamask-and-how-do-i-find-it>`_
and :ref:`eth-account`.
