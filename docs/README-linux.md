# Web3.py on Linux

## Developer Setup

1. Install all of the package dependencies

```sh
sudo apt-get install libssl-dev libffi-dev autoconf automake libtool
# ^ This is for Debian-like systems. TODO: Add more platforms

sudo pacman -Sy libsecp256k1
# ^ This is for ArchLinux system

sudo dnf install openssl-devel libffi-devel autoconf automake libtool
# ^ This is for Fedora.
```

2. Install `leveldb` (TODO)


## Examples for specific operating systems

### Ubuntu 16.04

```sh
#!/bin/bash

sudo apt-get update
sudo apt-get -y upgrade

sudo apt-get -y install build-essential
#RESOLVES ERROR:  unable to execute 'x86_64-linux-gnu-gcc': No such file or directory error: command 'x86_64-linux-gnu-gcc' failed with exit status 1

sudo apt-get -y install python3-dev
#RESOLVES ERROR:  cytoolz/dicttoolz.c:17:20: fatal error: Python.h: No such file or directory compilation terminated. error: command 'x86_64-linux-gnu-gcc' failed with exit status 1

sudo apt-get -y install python3-venv
#RESOLVES ERROR: The virtual environment was not created successfully because ensurepip is not available.  On Debian/Ubuntu systems, you need to install the python3-venv package using the following command.

cd ~
git clone https://github.com/ethereum/web3.py.git
cd web3.py
python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install -e .[dev]

```

