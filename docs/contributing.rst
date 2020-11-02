.. _contributing:

Contributing
------------

Thank you for your interest in contributing! We welcome all contributions
no matter their size. Please read along to learn how to get started. If you
get stuck, feel free to reach for help in our
`Gitter channel <https://gitter.im/ethereum/web3.py>`_.

Setting the stage
~~~~~~~~~~~~~~~~~

First, you need to clone the repository. Web3.py depends on submodules, so you
need to clone the repo with the ``--recursive`` flag. Example:

.. code:: sh

    $ git clone --recursive https://github.com/ethereum/web3.py.git
    $ cd web3.py


Install all development dependencies:

.. code:: sh

    $ pip install -e .[dev]


Using Docker
~~~~~~~~~~~~

Developing within Docker is not required, but if you prefer that workflow, use
the *sandbox* container provided in the **docker-compose.yml** file.

To start up the test environment, run:

.. code:: sh

    $ docker-compose up -d


This will build a Docker container set up with an environment to run the
Python test code.

.. note::

    This container does not have `go-ethereum` installed, so you cannot run
    the go-ethereum test suite.

To run the Python tests from your local machine:

.. code:: sh

    $ docker-compose exec sandbox bash -c 'pytest -n 4 -f -k "not goethereum"'


You can run arbitrary commands inside the Docker container by using the
`bash -c` prefix.

.. code:: sh

    $ docker-compose exec sandbox bash -c ''


Or, if you would like to open a session to the container, run:

.. code:: sh

    $ docker-compose exec sandbox bash


Running the tests
~~~~~~~~~~~~~~~~~

A great way to explore the code base is to run the tests.

You can run all tests with:

.. code:: sh

    $ pytest


However, running the entire test suite takes a very long time and is generally impractical.
Typically, you'll just want to run a subset instead, like:

.. code:: sh

    $ pytest tests/core/eth-module/test_accounts.py


You can use ``tox`` to run all the tests for a given version of Python:

.. code:: sh

   $ tox -e py37-core


Linting is also performed by the CI. You can save yourself some time by checking for
linting errors locally:

.. code:: sh

   $ make lint


It is important to understand that each pull request must pass the full test
suite as part of the CI check. This test suite will run in the CI anytime a
pull request is opened or updated.

Code Style
~~~~~~~~~~

We value code consistency. To ensure your contribution conforms to the style
being used in this project, we encourage you to read our `style guide`_.


Type Hints
~~~~~~~~~~

This code base makes use of `type hints`_. Type hints make it easy to prevent
certain types of bugs, enable richer tooling, and enhance the documentation,
making the code easier to follow.

All new code is required to include type hints, with the exception of tests.

All parameters, as well as the return type of defs, are expected to be typed,
with the exception of ``self`` and ``cls`` as seen in the following example.

.. code:: python

    def __init__(self, wrapped_db: DatabaseAPI) -> None:
        self.wrapped_db = wrapped_db
        self.reset()


Documentation
~~~~~~~~~~~~~

Good documentation will lead to quicker adoption and happier users. Please
check out our guide on `how to create documentation`_ for the Python Ethereum
ecosystem.


Pull Requests
~~~~~~~~~~~~~

It's a good idea to make pull requests early on. A pull request represents the
start of a discussion, and doesn't necessarily need to be the final, finished
submission.

See GitHub's documentation for `working on pull requests`_.

Once you've made a pull request take a look at the Circle CI build status in
the GitHub interface and make sure all tests are passing. In general, pull
requests that do not pass the CI build yet won't get reviewed unless explicitly
requested.

If the pull request introduces changes that should be reflected in the release
notes, please add a `newsfragment` file as explained
`here <https://github.com/ethereum/web3.py/blob/master/newsfragments/README.md>`_

If possible, the change to the release notes file should be included in the
commit that introduces the feature or bugfix.


Releasing
~~~~~~~~~

Final test before each release
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before releasing a new version, build and test the package that will be released.
There's a script to build and install the wheel locally, then generate a temporary
virtualenv for smoke testing:

.. code:: sh

    $ git checkout master && git pull

    $ make package

    # in another shell, navigate to the virtualenv mentioned in output of ^

    # load the virtualenv with the packaged web3.py release
    $ source package-smoke-test/bin/activate

    # smoke test the release
    $ pip install ipython
    $ ipython
    >>> from web3.auto import w3
    >>> w3.isConnected()
    >>> ...


Verify the latest documentation 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To preview the documentation that will get published:

.. code:: sh

    $ make docs


Preview the release notes
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: sh

   $ towncrier --draft


Compile the release notes
^^^^^^^^^^^^^^^^^^^^^^^^^

After confirming that the release package looks okay, compile the release notes:

.. code:: sh

    $ make notes bump=$$VERSION_PART_TO_BUMP$$


You may need to fix up any broken release note fragments before committing. Keep
running ``make build-docs`` until it passes, then commit and carry on.


Push the release to GitHub & PyPI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After committing the compiled release notes and pushing them to the master
branch, release a new version:

.. code:: sh

    $ make release bump=$$VERSION_PART_TO_BUMP$$


Which version part to bump
^^^^^^^^^^^^^^^^^^^^^^^^^^

The version format for this repo is ``{major}.{minor}.{patch}`` for
stable, and ``{major}.{minor}.{patch}-{stage}.{devnum}`` for unstable
(``stage`` can be alpha or beta).

During a release, specify which part to bump, like
``make release bump=minor`` or ``make release bump=devnum``.

If you are in an alpha version, ``make release bump=stage`` will bump to beta.
If you are in a beta version, ``make release bump=stage`` will bump to a stable
version.

To issue an unstable version when the current version is stable, specify the new
version explicitly, like ``make release bump="--new-version 4.0.0-alpha.1 devnum"``.


Generating new fixtures
~~~~~~~~~~~~~~~~~~~~~~~

Our integration tests make use of Geth and Parity/OpenEthereum private networks.
When new versions of the client software are introduced, new fixtures should be
generated.

.. note::

    A "fixture" is a pre-synced network. It's the result of configuring and running
    a client, deploying the test contracts, and saving the resulting state for
    testing Web3.py functionality against.


Geth fixtures
^^^^^^^^^^^^^

1. Install the desired Geth version on your machine locally. The Geth team only
   explicitly supports the current version of their client at any given point,
   so older versions are best installed via `py-geth`_. Note that ``py-geth``
   will need updating to support each new version as well.

2. Specify the Geth binary and run the fixture creation script:

   .. code:: sh

       $ GETH_BINARY=/path/to/py-geth/bin python /tests/integration/generate_fixtures/go_ethereum.py /tests/integration/geth-X.Y.Z-fixture

3. The output of this script is your fixture, a zip file. Store the fixture in the
   ``/tests/integration/`` directory and update the ``/tests/integration/go_ethereum/conftest.py``
   file to point to the new fixture.

4. Run the tests. To ensure that the tests run with the correct Geth version,
   you may again include the ``GETH_BINARY`` environment variable.


Parity/OpenEthereum fixtures
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. The most reliable way to get a specific Parity/OE binary is to download
   the source code via `GitHub releases`_.

2. `Build the binary`_ from source. (This is will take a few minutes.)

3. Specify the path to this binary in the ``get_parity_binary`` function
   of the ``/tests/integration/generate_fixtures/parity.py`` file.

4. Run the fixture generation script:

.. code:: sh

    $ python /tests/integration/generate_fixtures/parity.py /tests/integration/parity-X.Y.Z-fixture
 
5. The output of this script is your fixture, a zip file. Store the fixture in the
   ``/tests/integration/`` directory and update the ``/tests/integration/parity/conftest.py``
   file to point the new fixture.

6. By this point, you may have noticed that Parity fixture generation relies
   on a Geth network to sync from. In the output of the generation script are
   the hashes of the various contracts that it mined. Update the corresponding
   values in the ``/parity/conftest.py`` file with those hashes.

7. Run the tests.


.. _style guide: https://github.com/pipermerriam/ethereum-dev-tactical-manual/blob/master/style-guide.md
.. _type hints: https://www.python.org/dev/peps/pep-0484/
.. _how to create documentation: https://github.com/ethereum/snake-charmers-tactical-manual/blob/master/documentation.md
.. _working on pull requests: https://help.github.com/articles/about-pull-requests/
.. _py-geth: https://github.com/ethereum/py-geth
.. _Github releases: https://github.com/openethereum/openethereum/releases
.. _Build the binary: https://github.com/openethereum/openethereum/#3-building-
