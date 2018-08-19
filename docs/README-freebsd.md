# Web3.py on FreeBSD (11.2)

## Developer Setup

### Prerequisites

#### As superuser
```
pkg install python3 py36-virtualenv leveldb libxml2 libxslt pkgconf secp256k1 wget git hs-pandoc
wget https://raw.githubusercontent.com/bitcoin/bitcoin/master/src/secp256k1/include/secp256k1_recovery.h -O /usr/local/include/secp256k1_recovery.h
echo '#include "/usr/include/stdlib.h"' > /usr/include/alloca.h
```

#### As user
```
mkdir -p /tmp/venv_python
virtualenv-3.6 /tmp/venv_python/python3
source /tmp/venv_python/python3/bin/activate.csh

pip install eth-account ptyprocess

cd /tmp
git clone https://github.com/ethereum/web3.py.git
cd web3.py
pip install -e .\[tester\] -r requirements-dev.txt --global-option=build_ext --global-option='-I/usr/local/include'
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
sudo cp go-ethereum/build/bin/geth /usr/local/bin/
```

##### cargo (https://github.com/paukstis/freebsd_parity/blob/v1.6/README.md)
```
BROKEN (build crashes in FreeBSD 11.2)
```

```
py.test tests/core
py.test tests/ens
py.test tests/integration
```
