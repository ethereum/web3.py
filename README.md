# Web3.py

[![Join the chat at https://gitter.im/ethereum/web3.py](https://badges.gitter.im/ethereum/web3.py.svg)](https://gitter.im/ethereum/web3.py?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

[![Build Status](https://travis-ci.org/ethereum/web3.py.png)](https://travis-ci.org/ethereum/web3.py)
   

A Python implementation of [web3.js](https://github.com/ethereum/web3.js)

* Python 3.5+ support

Read more in the [documentation on ReadTheDocs](http://web3py.readthedocs.io/). [View the change log on Github](docs/releases.rst).

## Quickstart

```python
import json
import web3

from web3 import Web3, HTTPProvider, TestRPCProvider
from solc import compile_source
from web3.contract import ConciseContract

# Solidity source code
contract_source_code = '''
pragma solidity ^0.4.0;

contract Greeter {
    string public greeting;

    function Greeter() {
        greeting = 'Hello';
    }

    function setGreeting(string _greeting) public {
        greeting = _greeting;
    }

    function greet() constant returns (string) {
        return greeting;
    }
}
'''

compiled_sol = compile_source(contract_source_code) # Compiled source code
contract_interface = compiled_sol['<stdin>:Greeter']

# web3.py instance
w3 = Web3(TestRPCProvider())

# Instantiate and deploy contract
contract = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bin'])

# Get transaction hash from deployed contract
tx_hash = contract.deploy(transaction={'from': w3.eth.accounts[0], 'gas': 410000})

# Get tx receipt to get contract address
tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
contract_address = tx_receipt['contractAddress']

# Contract instance in concise mode
contract_instance = w3.eth.contract(contract_interface['abi'], contract_address, ContractFactoryClass=ConciseContract)

# Getters + Setters for web3.eth.contract object
print('Contract value: {}'.format(contract_instance.greet()))
contract_instance.setGreeting('Nihao', transact={'from': w3.eth.accounts[0]})
print('Setting value to: Nihao')
print('Contract value: {}'.format(contract_instance.greet()))
```

## Developer setup

If you would like to hack on web3.py, set up your dev environment with:

```sh
sudo apt-get install libssl-dev libffi-dev autoconf automake libtool
# ^ This is for Debian-like systems. TODO: Add more platforms

sudo pacman -Sy libsecp256k1
# ^ This is for ArchLinux system

git clone git@github.com:ethereum/web3.py.git
cd web3.py
virtualenv venv
. venv/bin/activate
pip install -r requirements-dev.txt
pip install -e .
```

For different environments, you can set up multiple virtualenvs, like:

**Python 3**

```sh
virtualenv -p python3 venvpy3
. venvpy3/bin/activate
pip install -r requirements-dev.txt
pip install -e .[tester]
```

**Docs**

```sh
virtualenv venvdocs
. venvdocs/bin/activate
pip install -r requirements-docs.txt
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

You can use pytest-watch, running one for every Python environment:

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
