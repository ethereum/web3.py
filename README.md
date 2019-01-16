# Web3.py

[![Join the chat at https://gitter.im/ethereum/web3.py](https://badges.gitter.im/ethereum/web3.py.svg)](https://gitter.im/ethereum/web3.py?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

[![Build Status](https://circleci.com/gh/ethereum/web3.py.svg?style=shield)](https://circleci.com/gh/ethereum/web3.py)


A Python implementation of [web3.js](https://github.com/ethereum/web3.js)

* Python 3.6+ support

Read more in the [documentation on ReadTheDocs](http://web3py.readthedocs.io/). [View the change log on Github](docs/releases.rst).

## Developer Setup

```sh
git clone git@github.com:ethereum/web3.py.git
cd web3.py
```

Please see OS-specific instructions for:

- [Linux](docs/README-linux.md#Developer-Setup)
- [Mac](docs/README-osx.md#Developer-Setup)
- [Windows](docs/README-windows.md#Developer-Setup)
- [FreeBSD](docs/README-freebsd.md#Developer-Setup)

Then run these install commands:

```sh
virtualenv venv
. venv/bin/activate
pip install -e .[dev]
```

For different environments, you can set up multiple `virtualenv`. For example, if you want to create a `venvdocs`, then you do the following:

```sh
virtualenv venvdocs
. venvdocs/bin/activate
pip install -e .[docs]
pip install -e .
```

## Using Docker

If you would like to develop and test inside a Docker environment, use the *sandbox* container provided in the **docker-compose.yml** file.

To start up the test environment, run:

```
docker-compose up -d
```

This will build a Docker container set up with an environment to run the Python test code.  

**Note: This container does not have `go-ethereum` installed, so you cannot run the go-ethereum test suite.**

To run the Python tests from your local machine:

```
docker-compose exec sandbox bash -c 'pytest -n 4 -f -k "not goethereum"'
```

You can run arbitrary commands inside the Docker container by using the `bash -c` prefix.

```
docker-compose exec sandbox bash -c ''
```

Or, if you would like to just open a session to the container, run:

```
docker-compose exec sandbox bash
```

### Testing Setup

During development, you might like to have tests run on every file save.

Show flake8 errors on file change:

```sh
# Test flake8
when-changed -v -s -r -1 web3/ tests/ ens/ -c "clear; flake8 web3 tests ens && echo 'flake8 success' || echo 'error'"
```

You can use `pytest-watch`, running one for every Python environment:

```sh
pip install pytest-watch

cd venv
ptw --onfail "notify-send -t 5000 'Test failure ⚠⚠⚠⚠⚠' 'python 3 test on web3.py failed'" ../tests ../web3
```

Or, you can run multi-process tests in one command, but without color:

```sh
# in the project root:
pytest --numprocesses=4 --looponfail --maxfail=1
# the same thing, succinctly:
pytest -n 4 -f --maxfail=1
```

#### How to Execute the Tests?

1. [Setup your development environment](https://github.com/ethereum/web3.py/#developer-setup).

2. Execute `tox` for the tests

There are multiple [components](https://github.com/ethereum/web3.py/blob/master/.travis.yml#L53) of the tests. You can run test to against specific component. For example:

```sh
# Run Tests for the Core component (for Python 3.5):
tox -e py35-core

# Run Tests for the Core component (for Python 3.6):
tox -e py36-core
```

If for some reason it is not working, add `--recreate` params.

`tox` is good for testing against the full set of build targets. But if you want to run the tests individually, `py.test` is better for development workflow. For example, to run only the tests in one file:

```sh
py.test tests/core/gas-strategies/test_time_based_gas_price_strategy.py
```

### Release setup

For Debian-like systems:
```
apt install pandoc
```

To release a new version:

```sh
make release bump=$$VERSION_PART_TO_BUMP$$
```

#### How to bumpversion

The version format for this repo is `{major}.{minor}.{patch}` for stable, and
`{major}.{minor}.{patch}-{stage}.{devnum}` for unstable (`stage` can be alpha or beta).

To issue the next version in line, specify which part to bump,
like `make release bump=minor` or `make release bump=devnum`.

If you are in a beta version, `make release bump=stage` will switch to a stable.

To issue an unstable version when the current version is stable, specify the
new version explicitly, like `make release bump="--new-version 4.0.0-alpha.1 devnum"`
