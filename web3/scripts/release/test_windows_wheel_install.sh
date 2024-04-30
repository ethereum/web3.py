#!/bin/bash

bash.exe -c "set -e"
bash.exe -c "rm -rf build dist"
python -m build
bash.exe -c "export temp_dir=$(mktemp -d)"
cd $temp_dir
python -m venv venv-test
bash.exe -c "source venv-test/Scripts/activate"
bash.exe -c 'pip install --upgrade "$(ls /c/Users/circleci/project/web3py/dist/web3-*-py3-none-any.whl)" --progress-bar off'
python -c "from web3 import Web3"
