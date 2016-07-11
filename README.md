# Web3.py

[![Join the chat at https://gitter.im/pipermerriam/web3.py](https://badges.gitter.im/pipermerriam/web3.py.svg)](https://gitter.im/pipermerriam/web3.py?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

[![Build Status](https://travis-ci.org/pipermerriam/web3.py.png)](https://travis-ci.org/pipermerriam/web3.py)
[![Documentation Status](https://readthedocs.org/projects/web3.py/badge/?version=latest)](https://readthedocs.org/projects/web3.py/?badge=latest)
[![PyPi version](https://pypip.in/v/web3.py/badge.png)](https://pypi.python.org/pypi/web3.py)
[![PyPi downloads](https://pypip.in/d/web3.py/badge.png)](https://pypi.python.org/pypi/web3.py)
   

A python implementation of [web3.js](https://github.com/ethereum/web3.js)

## Goals

* Python 2.7, 3.4, 3.5 support
* Provide a feature-for-feature python implementation of Web3.js


## Installation

```sh
pip install web3
```


## API

This documentation is not yet complete, although the API should offer most functionality described in the [Javascript API documentation](https://github.com/ethereum/wiki/wiki/JavaScript-API), except for contract events and filters.


### Initialisation

Initialising the Ethereum node
```sh
# IPC
geth --unlock 0 console

# RPC, if required, with --rpcaddr "localhost" --rpcport <port>
geth --rpc --unlock 0 console
```

Connecting to the Ethereum node

```python
from web3 import Web3, RPCProvider, IPCProvider

# Initialising a Web3 instance with an RPCProvider:
web3rpc = Web3(RPCProvider(host="127.0.0.1", port="8545"))

# Initialising a Web3 instance with an IPCProvider:
web3ipc = Web3(IPCProvider(ipcpath=None, testnet=False))
# Both arguments can be omitted, the ipcpath should be found automatically
```


### Testing

For testing you can use the `TestRPCProvider`.  This depends on
`eth-testrpc>=0.2.0` which must be installed independently (It is not included
as a hard dependency for this package.)


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
web3.config.defaultAccount = <your (unlocked) account>
web3.config.defaultBlock = "latest"
# Can also be an integer or one of "latest", "pending", "earliest"
```

### Interacting with contracts
```python
abi = "<abi string>"
contractFactory = web3.eth.contract(abi)
contract = contractFactory.at("0xaddress")
# The abi methods should now be available on the contract instance
```

### Timeouts, blocking and nonblocking requests
All function and property requests block by default until the result is available. It is possible to provide an additional keyword argument 'timeout'.
```python
# Blocks indefinitely
>>> web3.eth.getBalance("0xaddress", timeout=None)
23423234

# Blocks until the response is available until the timeout is reached
# returning the response or raising a ValueError with the request id
>>> web3.eth.getBalance("0xaddress", timeout=3) # in seconds
23423234

# Does not block, returns the unique request id immediately
id = web3.eth.getBalance("0xaddress", timeout=0)

# This id can be used to poll the Web3 instance later:
web3.receive(id, timeout=0, keep=False)

# By default, the timeout is 0 and the receive function does not block, returning None if
# the response wasn't available. Otherwise, the timeout argument has the same behaviour
# as a normal call described above.
# Receive will discard the response after the call unless keep is true.
```

### `web3`

#### web3.db.*
Available as described in the [Javascript API documentation](https://github.com/ethereum/wiki/wiki/JavaScript-API).

#### web3.eth.*,
Available as described in the [Javascript API documentation](https://github.com/ethereum/wiki/wiki/JavaScript-API).

#### web3.net.*
Available as described in the [Javascript API documentation](https://github.com/ethereum/wiki/wiki/JavaScript-API).

#### web3.personal.*

Available as described in the [Javascript API documentation](https://github.com/ethereum/wiki/wiki/JavaScript-API).

#### web3.ssh.*

Available as described in the [Javascript API documentation](https://github.com/ethereum/wiki/wiki/JavaScript-API).

##### `web3.sha3`

```python
>>> web3.sha3(b'some text')
'46ba1b442d3606a3437800ee7ae5a0249756405e676739b46aa8f6e85b13fe2b'
>>> web3.sha3('0x80', encoding='hex')
'56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421'
```


#### `web3.eth`

##### `web3.eth.iban`

```python
>>> web3.eth.iban("XE81ETHXREGGAVOFYORK")
<web3.eth.iban.Iban at 0x107301dd8>
```


###### `web3.eth.iban.fromAddress`

```python
>>> web3.eth.iban.fromAddress('0x00c5496aee77c1ba1f0854206a26dda82a81d6d8').toString()
'XE7338O073KYGTWWZN0F2WZ0R8PX5ZPPZS'
```


###### `web3.eth.iban.fromBban`

```python
>>> web3.eth.iban.fromBban('ETHXREGGAVOFYORK').toString()
'XE81ETHXREGGAVOFYORK'
```


###### `web3.eth.iban.createIndirect`

```python
>>> web3.eth.iban.createIndirect({
...   'institution': "XREG",
...   'identifier': "GAVOFYORK"
... }).toString()
'XE81ETHXREGGAVOFYORK'
```


###### `web3.eth.iban.isValid`

```python
>>> web3.eth.iban.isValid("XE81ETHXREGGAVOFYORK")
True

>>> web3.eth.iban.isValid("XE82ETHXREGGAVOFYORK")
False  # false, cause checksum is incorrect

web3.eth.iban("XE81ETHXREGGAVOFYORK").isValid()
True
```


###### `web3.eth.iban.isDirect`

```python
>>> web3.eth.iban("XE81ETHXREGGAVOFYORK").isDirect()
False
```


###### `web3.eth.iban.isIndirect`

```python
>>> web3.eth.iban("XE81ETHXREGGAVOFYORK").isIndirect()
True
```


###### `web3.eth.iban.checksum`

```python
>>> web3.eth.iban("XE81ETHXREGGAVOFYORK").checksum()
'81'
```


###### `web3.eth.iban.institution`

```python
>>> web3.eth.iban("XE81ETHXREGGAVOFYORK").institution()
'XREG'
```


###### `web3.eth.iban.client`

```python
>>> web3.eth.iban("XE81ETHXREGGAVOFYORK").client()
'GAVOFYORK'
```


###### `web3.eth.iban.address`

```python
>>> web3.eth.iban('XE7338O073KYGTWWZN0F2WZ0R8PX5ZPPZS').address()
'00c5496aee77c1ba1f0854206a26dda82a81d6d8'
```


###### `web3.eth.iban.toString`

```python
>>> web3.eth.iban('XE7338O073KYGTWWZN0F2WZ0R8PX5ZPPZS').toString()
'XE7338O073KYGTWWZN0F2WZ0R8PX5ZPPZS'
```
