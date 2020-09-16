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

> If you are on `>=OSX 10.15 Catalina` you may encounter the following error with the default `ZSH` shell. This can be fixed by wrapping the `[dev]` part in quotes.
```sh
pip install -e .[dev]
zsh: no matches found: .[dev]
```

Run install commands as follows:
```sh
pip install -e .'[dev]'
```
