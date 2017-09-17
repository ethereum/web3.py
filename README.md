# Web3.py

[![Join the chat at https://gitter.im/pipermerriam/web3.py](https://badges.gitter.im/pipermerriam/web3.py.svg)](https://gitter.im/pipermerriam/web3.py?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

[![Build Status](https://travis-ci.org/pipermerriam/web3.py.png)](https://travis-ci.org/pipermerriam/web3.py)
   

A Python implementation of [web3.js](https://github.com/ethereum/web3.js)

* Python 2.7, 3.4, 3.5 support

Read more in the [documentation on ReadTheDocs](http://web3py.readthedocs.io/). [View the change log on Github](docs/releases.rst).

## Developer setup

If you would like to hack on web3.py, set up your dev environment with:

```sh
sudo apt-get install libssl-dev
# ^ This is for Debian-like systems. TODO: Add more platforms

git clone git@github.com:pipermerriam/web3.py.git
cd web3.py
virtualenv venv
. venv/bin/activate
pip install -r requirements-dev.txt
pip install -e .
```

For different environments, you can set up multiple virtualenvs, like:

**Python 2**

```sh
virtualenv -p python2 venvpy2
. venvpy2/bin/activate
pip install -r requirements-dev.txt
pip install -e .
```

**Docs**

```sh
virtualenv venvdocs
. venvdocs/bin/activate
pip install -r requirements-dev.txt
pip install -e .
```

### Testing Setup

During development, you might like to have tests run on every file save.

Show flake8 errors on file change:

```sh
# Test flake8
when-changed -r web3/ tests/ -c "clear; git diff HEAD^ | flake8 --diff"
```

You can use pytest-watch, running one for every python environment:

```sh
pip install pytest-watch

cd venv
ptw --onfail "notify-send -t 5000 'Test failure ⚠⚠⚠⚠⚠' 'python 3 test on web3.py failed'" ../tests ../web3

#in a new console
cd venvpy2
ptw --onfail "notify-send -t 5000 'Test failure ⚠⚠⚠⚠⚠' 'python 2 test on web3.py failed'" ../tests ../web3
```

Or, you can run multi-process tests in one command, but without color:

```sh
# in the project root:
py.test --numprocesses=4 --looponfail --maxfail=1
# the same thing, succinctly:
pytest -n 4 -f --maxfail=1
```

### Release setup

For Debian-like systems:
```
apt install pandoc
```

*TODO* other release instructions
