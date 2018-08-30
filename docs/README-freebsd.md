# Web3.py on FreeBSD (11.2)

## Developer Setup

### Prerequisites

Make sure you've UTF-8 defined for charset and lang in your [~/.login_conf](https://www.freebsd.org/doc/en_US.ISO8859-1/books/handbook/using-localization.html),
otherwise almost every module will fail to install. Python 3 is very sensitive to that.

```
sudo pkg install python3 py36-virtualenv leveldb libxml2 libxslt pkgconf secp256k1 wget git
sudo wget https://raw.githubusercontent.com/bitcoin/bitcoin/master/src/secp256k1/include/secp256k1_recovery.h -O /usr/local/include/secp256k1_recovery.h
echo '#include "/usr/include/stdlib.h"' | sudo tee -a /usr/include/alloca.h > /dev/null
mkdir -p /tmp/venv_python
virtualenv-3.6 /tmp/venv_python/python3
source /tmp/venv_python/python3/bin/activate.csh

# these two modules fail to install natively
pip install ptyprocess eth-account

cd /tmp
git clone https://github.com/ethereum/web3.py.git
cd web3.py
pip install -e .\[dev\] --global-option=build_ext --global-option='-I/usr/local/include'
```

## Test

#### Prerequisites for integration tests:

##### geth (https://github.com/ethereum/go-ethereum/wiki/Installation-Instructions-for-FreeBSD)
```
pkg install go
cd /tmp
git clone https://github.com/ethereum/go-ethereum
cd go-ethereum
make geth
cp build/bin/geth /usr/local/bin/
```

##### parity (https://github.com/paukstis/freebsd_parity/blob/v1.6/README.md)
```
BROKEN (build crashes on FreeBSD 11.2)
```

```
py.test tests/core
py.test tests/ens
py.test tests/integration
```
