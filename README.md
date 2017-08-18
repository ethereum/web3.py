# Web3.py

[![Join the chat at https://gitter.im/pipermerriam/web3.py](https://badges.gitter.im/pipermerriam/web3.py.svg)](https://gitter.im/pipermerriam/web3.py?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

[![Build Status](https://travis-ci.org/pipermerriam/web3.py.png)](https://travis-ci.org/pipermerriam/web3.py)
   

A Python implementation of [web3.js](https://github.com/ethereum/web3.js)

* Python 2.7, 3.4, 3.5 support

Read more in the [documentation on ReadTheDocs](http://web3py.readthedocs.io/). [View the change log on Github](https://github.com/pipermerriam/web3.py/blob/master/CHANGELOG).

## Developer setup

If you would like to hack on web3.py, set up your dev environment with:

```
sudo apt-get install libssl-dev
# ^ This is for Debian-like systems. TODO: Add more platforms

git clone git@github.com:pipermerriam/web3.py.git
cd web3.py
virtualenv venv
. venv/bin/activate
pip install -r requirements-dev.txt
pip install -e .
```
