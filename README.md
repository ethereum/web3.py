# Web3.py

[![Join the chat at https://gitter.im/pipermerriam/web3.py](https://badges.gitter.im/pipermerriam/web3.py.svg)](https://gitter.im/pipermerriam/web3.py?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

[![Build Status](https://travis-ci.org/pipermerriam/web3.py.png)](https://travis-ci.org/pipermerriam/web3.py)

[Documentation on ReadTheDocs](http://web3py.readthedocs.io/)
   

A python implementation of [web3.js](https://github.com/ethereum/web3.js)

* Python 2.7, 3.4, 3.5 support


## Installation

```sh
pip install web3
```


### Testing

For testing you can use the `TestRPCProvider`.  This depends on
`eth-testrpc>=0.9.0` which must be eithe installed independently or with the
following installation command.

```sh
pip install web3[Tester]
```

Then in your code:


```python
from web3 import Web3, TestRPCProvider

# Initialising a Web3 instance with an RPCProvider:
web3rpc = Web3(TestRPCProvider())

# or specifying host and port.
web3rpc = Web3(TestRPCProvider(host="127.0.0.1", port="8545"))
```

The `TestRPCProvider` uses an EVM backed by the `ethereum.tester` module from
the `pyethereum` package.  This can be quite useful for testing your code which
uses `web3.py`.


### Setting defaults
```python
web3.eth.defaultAccount = <your (unlocked) account>
web3.eth.defaultBlock = "latest"
# Can also be an integer or one of "latest", "pending", "earliest"
```

### Interacting with contracts


```python
>>> abi = json.joads("<abi-json-string>")
>>> ContractFactory = web3.eth.contract(abi, code="0x...")
>>> ContractFactory.deploy()
... '0x461e829a731d96539ec1f147232f1d52b475225ed343e5853ff6bf3b237c6e79'
>>> contract = web3.eth.contract(abi, address="0x...")
>>> contract.transact().someMethod()
... '0xfbb0f76aa6a6bb8d178bc2b54de8fc7ca778d704af47d135c188ca7b5d25f2e4'
>>> contract.call().return13()
... 13
>>> contract.estimateGas().someMethod()
... 23212
```

You can listen for events using the `on` and `pastEvents` functions on a
contract.

```python
def transfer_callback(log_entry):
    ...  # do something with the log.

# create a filter and register a callback.
filter = MyContract.on("Transfer", {})
filter.watch(transfer_callback)

filter.stop_watching()
```


> The underlying asynchronous operations are managed by `gevent`.


### Timeouts, blocking and nonblocking requests

Web3.py does not currently support asynchronous calling patterns.
