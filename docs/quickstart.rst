Quickstart
==========

.. contents:: :local:


System Dependencies
-------------------

Populus depends on the following system dependencies.

* `Solidity`_ : For contract compilation
* `Go Ethereum`_: For running test chains and contract deployment.

In addition, populus needs some system dependencies to be able to install the
`PyEthereum`_ library.

Debian, Ubuntu, Mint
~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    sudo apt-get install libssl-dev


Fedora, CentOS, RedHat
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

    sudo yum install openssl-devel


OSX
~~~

.. code-block:: shell

    brew install pkg-config libffi autoconf automake libtool openssl


Installation
------------

Populus can be installed using ``pip`` as follows.

.. code-block:: shell

   $ pip install populus

Installation from source can be done from the root of the project with the
following command.

.. code-block:: shell

   $ python setup.py install


Initializing a new project
--------------------------

Populus can initialize your project using the ``$ populus init`` command.

.. code-block:: shell

    $ populus init
    Created Directory: ./contracts
    Created Example Contract: ./contracts/Greeter.sol
    Created Directory: ./tests
    Created Example Tests: ./tests/test_greeter.py


Your project will now have a ``./contracts`` directory with a single Solidity
source file in it named ``Greeter.sol``, as well as a ``./tests`` directory
with a single test file named ``test_greeter.py``.

Compiling your contracts
------------------------

Before you compile our project, lets take a look at the ``Greeter`` contract
that is generated as part of the project initialization.


.. code-block:: solidity

    contract Greeter {
        string public greeting;

        function Greeter() {
            greeting = "Hello";
        }

        function setGreeting(string _greeting) public {
            greeting = _greeting;
        }

        function greet() constant returns (string) {
            return greeting;
        }
    }

``Greeter`` is simple contract that is initialized with a default greeting of
the string ``'Hello'``.  It exposes the ``greet`` function which returns
whatever string is set as the greeting, as well as a ``setGreeting`` function
which allows the greeting to be changed.

You can now compile the contract using ``$ populus compile``


.. code-block:: shell

    $ populus compile
    ============ Compiling ==============
    > Loading source files from: ./contracts

    > Found 1 contract source files
    - contracts/Greeter.sol

    > Compiled 1 contracts
    - Greeter

    > Wrote compiled assets to: ./build/contracts.json


Testing your contract
---------------------

Now that you have a basic contract you'll want to test that it behaves as
expected.  The project should already have a test module named
``test_greeter.py`` located in the ``./tests`` directory that looks like the
following.

.. code-block:: python

    def test_greeter(chain):
        greeter = chain.get_contract('Greeter')

        greeting = greeter.call().greet()
        assert greeting == 'Hello'

    def test_custom_greeting(chain):
        greeter = chain.get_contract('Greeter')

        set_txn_hash = greeter.transact().setGreeting('Guten Tag')
        chain.wait.for_receipt(set_txn_hash)

        greeting = greeter.call().greet()
        assert greeting == 'Guten Tag'


You should see two tests, one that tests the default greeting, and one that
tests that we can set a custom greeting.


.. _Go Ethereum: https://github.com/ethereum/go-ethereum/
.. _Solidity: https://github.com/ethereum/solidity/
.. _PyEthereum: https://github.com/ethereum/pyethereum/
