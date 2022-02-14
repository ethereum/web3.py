version: 2.1

# heavily inspired by https://raw.githubusercontent.com/pinax/pinax-wiki/6bd2a99ab6f702e300d708532a6d1d9aa638b9f8/.circleci/config.yml

common: &common
  working_directory: ~/repo
  steps:
    - checkout
    - restore_cache:
        keys:
          - cache-{{ .Environment.CIRCLE_JOB }}-{{ checksum "setup.py" }}-{{ checksum "tox.ini" }}
    - run:
        name: checkout ethpm-spec submodule
        command: git submodule update --init --recursive
    - run:
        name: install dependencies
        command: pip install --user tox
    - run:
        name: run tox
        command: ~/.local/bin/tox -r
    - save_cache:
        paths:
          - .tox
          - ~/.cache/pip
          - ~/.local
          - ./eggs
          - ~/.ethash
          - ~/.py-geth
        key: cache-{{ .Environment.CIRCLE_JOB }}-{{ checksum "setup.py" }}-{{ checksum "tox.ini" }}

docs_steps: &docs_steps
  working_directory: ~/repo
  steps:
    - checkout
    - restore_cache:
        keys:
          - cache-docs-{{ .Environment.CIRCLE_JOB }}-{{ checksum "setup.py" }}-{{ checksum "tox.ini" }}
    - run:
        name: checkout ethpm-spec submodule
        command: git submodule update --init --recursive
    - run:
        name: install dependencies
        command: pip install --user tox
    - run:
        name: install web3
        command: pip install -U web3
    - run:
        name: run tox
        command: ~/.local/bin/tox -r
    - save_cache:
        paths:
          - .tox
          - ~/.cache/pip
          - ~/.local
          - ./eggs
          - ~/.ethash
          - ~/.py-geth
        key: cache-docs-{{ .Environment.CIRCLE_JOB }}-{{ checksum "setup.py" }}-{{ checksum "tox.ini" }}

geth_steps: &geth_steps
  working_directory: ~/repo
  steps:
    - checkout
    - restore_cache:
        keys:
          - cache-{{ .Environment.CIRCLE_JOB }}-{{ checksum "setup.py" }}-{{ checksum "tox.ini" }}
    - run:
        name: install dependencies
        command: pip install --user tox
    - run:
        name: build geth if missing
        command: |
          mkdir -p $HOME/.ethash
          pip install --user py-geth>=3.6.0
          export GOROOT=/usr/local/go
          echo $GETH_VERSION
          export GETH_BINARY="$HOME/.py-geth/geth-$GETH_VERSION/bin/geth"
          if [ ! -e "$GETH_BINARY" ]; then
            curl -O https://storage.googleapis.com/golang/go1.14.2.linux-amd64.tar.gz
            tar xvf go1.14.2.linux-amd64.tar.gz
            sudo chown -R root:root ./go
            sudo mv go /usr/local
            sudo ln -s /usr/local/go/bin/go /usr/local/bin/go
            sudo apt-get update;
            sudo apt-get install -y build-essential;
            python -m geth.install $GETH_VERSION;
          fi
          sudo ln -s /home/circleci/.py-geth/geth-$GETH_VERSION/bin/geth /usr/local/bin/geth
          geth version
          geth makedag 0 $HOME/.ethash
    - run:
        name: run tox
        command: ~/.local/bin/tox -r
    - save_cache:
        paths:
          - .tox
          - ~/.cache/pip
          - ~/.local
          - ./eggs
          - ~/.ethash
          - ~/.py-geth
        key: cache-{{ .Environment.CIRCLE_JOB }}-{{ checksum "setup.py" }}-{{ checksum "tox.ini" }}

geth_custom_steps: &geth_custom_steps
  working_directory: ~/repo
  steps:
    - checkout
    - restore_cache:
        keys:
          - cache-{{ .Environment.CIRCLE_JOB }}-{{ checksum "setup.py" }}-{{ checksum "tox.ini" }}
    - run:
        name: install dependencies
        command: pip install --user tox
    - run:
        name: use a pre-built geth binary
        command: |
          mkdir -p $HOME/.ethash
          export GOROOT=/usr/local/go
          echo $GETH_VERSION
          export GETH_BINARY="./custom_geth"
          echo 'export GETH_BINARY="./custom_geth"' >> $BASH_ENV
          curl -O https://storage.googleapis.com/golang/go1.14.2.linux-amd64.tar.gz
          tar xvf go1.14.2.linux-amd64.tar.gz
          sudo chown -R root:root ./go
          sudo mv go /usr/local
          sudo ln -s /usr/local/go/bin/go /usr/local/bin/go
          sudo apt-get update;
          sudo apt-get install -y build-essential;
          ./custom_geth version
          ./custom_geth makedag 0 $HOME/.ethash
    - run:
        name: run tox
        command: ~/.local/bin/tox -r
    - save_cache:
        paths:
          - .tox
          - ~/.cache/pip
          - ~/.local
          - ./eggs
          - ~/.ethash
        key: cache-{{ .Environment.CIRCLE_JOB }}-{{ checksum "setup.py" }}-{{ checksum "tox.ini" }}

ethpm_steps: &ethpm_steps
  working_directory: ~/repo
  steps:
    - checkout
    - restore_cache:
        keys:
          - ethpm-cache-{{ .Environment.CIRCLE_JOB }}-{{ checksum "setup.py" }}-{{ checksum "tox.ini" }}
    - run:
        name: install ipfs
        command:
          wget https://dist.ipfs.io/go-ipfs/v0.7.0/go-ipfs_v0.7.0_linux-amd64.tar.gz &&
          tar xvfz go-ipfs_v0.7.0_linux-amd64.tar.gz &&
          sudo cp go-ipfs/ipfs /usr/local/bin &&
          ipfs init
    - run:
        name: start ipfs node in background
        command: ipfs daemon
        background: true
    - run:
        name: checkout ethpm-spec submodule
        command: git submodule update --init --recursive
    - run:
        name: install dependencies
        command: pip install --user tox
    - run:
        name: run tox
        command: ~/.local/bin/tox -r
    - save_cache:
        paths:
          - .tox
          - ~/.cache/pip
          - ~/.local
        key: ethpm-cache-{{ .Environment.CIRCLE_JOB }}-{{ checksum "setup.py" }}-{{ checksum "tox.ini" }}

orbs:
  win: circleci/windows@2.2.0

windows_steps: &windows_steps
  executor:
    name: win/default
    shell: bash.exe
  working_directory: C:\Users\circleci\project\web3py
  steps:
    - checkout
    - restore_cache:
        keys:
          - windows-cache-{{ .Environment.CIRCLE_JOB }}-{{ checksum "setup.py" }}-{{ checksum "tox.ini" }}
    - run:
        name: checkout ethpm-spec submodule
        command: git submodule update --init --recursive
    - run:
        name: install dependencies
        command: pip install --user tox
    - run:
        name: run tox
        command: 'C:/Users/circleci/AppData/Roaming/Python/Python37/Scripts/tox.exe -r'
    - save_cache:
        paths:
          - .tox
        key: windows-cache-{{ .Environment.CIRCLE_JOB }}-{{ checksum "setup.py" }}-{{ checksum "tox.ini" }}


jobs:
  #
  # Python 3.6
  #
  lint:
    <<: *common
    docker:
      - image: circleci/python:3.9
    environment:
      TOXENV: lint

  docs:
    <<: *docs_steps
    docker:
      - image: circleci/python:3.9
    environment:
      TOXENV: docs


  #
  # Python 3.7
  #
  py37-core:
    <<: *common
    docker:
      - image: circleci/python:3.7
    environment:
      TOXENV: py37-core

  py37-ens:
    <<: *common
    docker:
      - image: circleci/python:3.7
    environment:
      TOXENV: py37-ens

  py37-ethpm:
    <<: *ethpm_steps
    docker:
      - image: circleci/python:3.7
    environment:
      TOXENV: py37-ethpm
      # Please don't use this key for any shenanigans
      WEB3_INFURA_PROJECT_ID: 7707850c2fb7465ebe6f150d67182e22

  py37-integration-goethereum-ipc:
    <<: *geth_steps
    docker:
      - image: circleci/python:3.7
    environment:
      TOXENV: py37-integration-goethereum-ipc
      GETH_VERSION: v1.10.13

  py37-integration-goethereum-http:
    <<: *geth_steps
    docker:
      - image: circleci/python:3.7
    environment:
      TOXENV: py37-integration-goethereum-http
      GETH_VERSION: v1.10.13

  py37-integration-goethereum-ws:
    <<: *geth_steps
    docker:
      - image: circleci/python:3.7
    environment:
      TOXENV: py37-integration-goethereum-ws
      GETH_VERSION: v1.10.13

  py37-integration-ethtester-pyevm:
    <<: *common
    docker:
      - image: circleci/python:3.7
    environment:
      TOXENV: py37-integration-ethtester
      ETHEREUM_TESTER_CHAIN_BACKEND: eth_tester.backends.PyEVMBackend

  py37-wheel-cli:
    <<: *common
    docker:
      - image: circleci/python:3.7
    environment:
      TOXENV: py37-wheel-cli

  py37-wheel-cli-windows:
    <<: *windows_steps
    environment:
      TOXENV: py37-wheel-cli-windows

  #
  # Python 3.8
  #
  py38-core:
    <<: *common
    docker:
      - image: circleci/python:3.8
    environment:
      TOXENV: py38-core

  py38-ens:
    <<: *common
    docker:
      - image: circleci/python:3.8
    environment:
      TOXENV: py38-ens

  py38-ethpm:
    <<: *ethpm_steps
    docker:
      - image: circleci/python:3.8
    environment:
      TOXENV: py38-ethpm
      # Please don't use this key for any shenanigans
      WEB3_INFURA_PROJECT_ID: 7707850c2fb7465ebe6f150d67182e22

  py38-integration-goethereum-ipc:
    <<: *geth_steps
    docker:
      - image: circleci/python:3.8
    environment:
      TOXENV: py38-integration-goethereum-ipc
      GETH_VERSION: v1.10.13

  py38-integration-goethereum-http:
    <<: *geth_steps
    docker:
      - image: circleci/python:3.8
    environment:
      TOXENV: py38-integration-goethereum-http
      GETH_VERSION: v1.10.13

  py38-integration-goethereum-ws:
    <<: *geth_steps
    docker:
      - image: circleci/python:3.8
    environment:
      TOXENV: py38-integration-goethereum-ws
      GETH_VERSION: v1.10.13

  py38-integration-ethtester-pyevm:
    <<: *common
    docker:
      - image: circleci/python:3.8
    environment:
      TOXENV: py38-integration-ethtester
      ETHEREUM_TESTER_CHAIN_BACKEND: eth_tester.backends.PyEVMBackend

  py38-wheel-cli:
    <<: *common
    docker:
      - image: circleci/python:3.8
    environment:
      TOXENV: py38-wheel-cli

  #
  # Python 3.9
  #
  py39-core:
    <<: *common
    docker:
      - image: circleci/python:3.9
    environment:
      TOXENV: py39-core

  py39-ens:
    <<: *common
    docker:
      - image: circleci/python:3.9
    environment:
      TOXENV: py39-ens

  py39-ethpm:
    <<: *ethpm_steps
    docker:
      - image: circleci/python:3.9
    environment:
      TOXENV: py39-ethpm
      # Please don't use this key for any shenanigans
      WEB3_INFURA_PROJECT_ID: 7707850c2fb7465ebe6f150d67182e22

  py39-integration-goethereum-ipc:
    <<: *geth_steps
    docker:
      - image: circleci/python:3.9
    environment:
      TOXENV: py39-integration-goethereum-ipc
      GETH_VERSION: v1.10.13

  py39-integration-goethereum-http:
    <<: *geth_steps
    docker:
      - image: circleci/python:3.9
    environment:
      TOXENV: py39-integration-goethereum-http
      GETH_VERSION: v1.10.13

  py39-integration-goethereum-ws:
    <<: *geth_steps
    docker:
      - image: circleci/python:3.9
    environment:
      TOXENV: py39-integration-goethereum-ws
      GETH_VERSION: v1.10.13

  py39-integration-ethtester-pyevm:
    <<: *common
    docker:
      - image: circleci/python:3.9
    environment:
      TOXENV: py39-integration-ethtester
      ETHEREUM_TESTER_CHAIN_BACKEND: eth_tester.backends.PyEVMBackend

  py39-wheel-cli:
    <<: *common
    docker:
      - image: circleci/python:3.9
        environment:
          TOXENV: py39-wheel-cli

  #
  # Python 3.10
  #
  py310-core:
    <<: *common
    docker:
      - image: circleci/python:3.10
    environment:
      TOXENV: py310-core

  py310-ens:
    <<: *common
    docker:
      - image: circleci/python:3.10
    environment:
      TOXENV: py310-ens

  py310-ethpm:
    <<: *ethpm_steps
    docker:
      - image: circleci/python:3.10
    environment:
      TOXENV: py310-ethpm
      # Please don't use this key for any shenanigans
      WEB3_INFURA_PROJECT_ID: 7707850c2fb7465ebe6f150d67182e22

  py310-integration-goethereum-ipc:
    <<: *geth_steps
    docker:
      - image: circleci/python:3.10
    environment:
      TOXENV: py310-integration-goethereum-ipc
      GETH_VERSION: v1.10.11

  py310-integration-goethereum-http:
    <<: *geth_steps
    docker:
      - image: circleci/python:3.10
    environment:
      TOXENV: py310-integration-goethereum-http
      GETH_VERSION: v1.10.11

  py310-integration-goethereum-ws:
    <<: *geth_steps
    docker:
      - image: circleci/python:3.10
    environment:
      TOXENV: py310-integration-goethereum-ws
      GETH_VERSION: v1.10.11

  py310-integration-ethtester-pyevm:
    <<: *common
    docker:
      - image: circleci/python:3.10
    environment:
      TOXENV: py310-integration-ethtester
      ETHEREUM_TESTER_CHAIN_BACKEND: eth_tester.backends.PyEVMBackend

  py310-wheel-cli:
    <<: *common
    docker:
      - image: circleci/python:3.10
        environment:
          TOXENV: py310-wheel-cli

  benchmark:
    <<: *geth_steps
    docker:
      - image: circleci/python:3.10
    environment:
      TOXENV: benchmark
      GETH_VERSION: v1.10.13

workflows:
  version: 2.1
  test:
    jobs:
      # These are the longest running tests, start them first
      - py37-core
      - py38-core
      - py39-core
      - py310-core
      - lint
      - docs
      - benchmark
      - py37-ens
      - py37-ethpm
      - py37-integration-goethereum-ipc
      - py37-integration-goethereum-http
      - py37-integration-goethereum-ws
      - py37-integration-ethtester-pyevm
      - py37-wheel-cli
      - py37-wheel-cli-windows
      - py38-ens
      - py38-ethpm
      - py38-integration-goethereum-ipc
      - py38-integration-goethereum-http
      - py38-integration-goethereum-ws
      - py38-integration-ethtester-pyevm
      - py38-wheel-cli
      - py39-ens
      - py39-ethpm
      - py39-integration-goethereum-ipc
      - py39-integration-goethereum-http
      - py39-integration-goethereum-ws
      - py39-integration-ethtester-pyevm
      - py39-wheel-cli
      - py310-ens
      - py310-ethpm
      - py310-integration-goethereum-ipc
      - py310-integration-goethereum-http
      - py310-integration-goethereum-ws
      - py310-integration-ethtester-pyevm
      - py310-wheel-cli
