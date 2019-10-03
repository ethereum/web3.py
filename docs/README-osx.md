# Web3.py on OSX

## Developer Setup

1. Install XCode command line tools

```sh
xcode-select --install
```

2. Install all of the package dependencies

```sh
brew install openssl libffi autoconf automake libtool
```

3. Install `leveldb`

```sh
brew install leveldb
```

4. When you are on `>=OSX 10.15 Catalina` and you encounter error with default `ZSH` shell:
```sh
pip install -e .[dev]
zsh: no matches found: .[dev]
```

Run install commands as follows:
```sh
pip install -e .'[dev]'
```
