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
