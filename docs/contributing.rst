Contributing
------------

Thank you for your interest in contributing! We welcome all contributions no matter
their size. Please read along to learn how to get started. If you get stuck, feel free
to ask for help in `Ethereum Python Discord server <https://discord.gg/GHryRvPB84>`_.

Setting the stage
~~~~~~~~~~~~~~~~~

To get started, fork the repository to your own github account, then clone it to your
development machine:

.. code:: sh
    git clone git@github.com:your-github-username/<REPO_NAME>.git

Next, install the development dependencies. We recommend using a virtual environment,
such as `virtualenv <https://virtualenv.pypa.io/en/stable/>`_.

.. code:: sh
    cd <REPO_NAME>
    virtualenv -p python venv
    . venv/bin/activate
    python -m pip install -e ".[dev]"
    pre-commit install

Running the tests
~~~~~~~~~~~~~~~~~

A great way to explore the code base is to run the tests.

We can run all tests with:

.. code:: sh
    pytest tests

Code Style
~~~~~~~~~~

We use `pre-commit <https://pre-commit.com/>`_ to enforce a consistent code style across
the library. This tool runs automatically with every commit, but you can also run it
manually with:

.. code:: sh
    make lint

If you need to make a commit that skips the ``pre-commit`` checks, you can do so with
``git commit --no-verify``.

This library uses type hints, which are enforced by the ``mypy`` tool (part of the
``pre-commit`` checks). All new code is required to land with type hints, with the
exception of code within the ``tests`` directory.

Documentation
~~~~~~~~~~~~~

Good documentation will lead to quicker adoption and happier users. Please check out our
guide on
`how to create documentation for the Python Ethereum ecosystem <https://github.com/ethereum/snake-charmers-tactical-manual/blob/main/documentation.md>`_.

Pull Requests
~~~~~~~~~~~~~

It's a good idea to make pull requests early on. A pull request represents the start of
a discussion, and doesn't necessarily need to be the final, finished submission.

GitHub's documentation for working on pull requests is
`available here <https://docs.github.com/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests>`_.

Once you've made a pull request, take a look at the Circle CI build status in the
GitHub interface and make sure all tests are passing. In general pull requests that
do not pass the CI build yet won't get reviewed unless explicitly requested.

If the pull request introduces changes that should be reflected in the release notes,
please add a `newsfragment` file as explained
`here <https://github.com/ethereum/<REPO_NAME>/blob/main/newsfragments/README.md>`_.

If possible, the change to the release notes file should be included in the commit that
introduces the feature or bugfix.

Releasing
~~~~~~~~~

Releases are typically done from the ``main`` branch, except when releasing a beta (in
which case the beta is released from ``main``, and the previous stable branch is
released from said branch).

Final test before each release
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before releasing a new version, build and test the package that will be released:

.. code:: sh
    git checkout main && git pull
    make package-test

This will build the package and install it in a temporary virtual environment. Follow
the instructions to activate the venv and test whatever you think is important.

You can also preview the release notes:

.. code:: sh
    towncrier --draft

Build the release notes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before bumping the version number, build the release notes. You must include the part of
the version to bump (see below), which changes how the version number will show in the
release notes.

.. code:: sh
    make notes bump=$$VERSION_PART_TO_BUMP$$

If there are any errors, be sure to re-run make notes until it works.

Push the release to github & pypi
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After confirming that the release package looks okay, release a new version:

.. code:: sh
    make release bump=$$VERSION_PART_TO_BUMP$$

This command will:

- Bump the version number as specified in ``.pyproject.toml`` and ``setup.py``.
- Create a git commit and tag for the new version.
- Build the package.
- Push the commit and tag to github.
- Push the new package files to pypi.

Which version part to bump
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``$$VERSION_PART_TO_BUMP$$`` must be one of: ``major``, ``minor``, ``patch``, ``stage``,
or ``devnum``.

The version format for this repo is ``{major}.{minor}.{patch}`` for stable, and
``{major}.{minor}.{patch}-{stage}.{devnum}`` for unstable (``stage`` can be alpha or
beta).

If you are in a beta version, ``make release bump=stage`` will switch to a stable.

To issue an unstable version when the current version is stable, specify the new version
explicitly, like ``make release bump="--new-version 4.0.0-alpha.1"``

You can see what the result of bumping any particular version part would be with
``bump-my-version show-bump``
