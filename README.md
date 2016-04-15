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


# API

## `web3`

## `web3.sha3`

```python
>>> web3.sha3(b'some text')
'46ba1b442d3606a3437800ee7ae5a0249756405e676739b46aa8f6e85b13fe2b'
>>> web3.sha3('0x80', encoding='hex')
'56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421'
```
