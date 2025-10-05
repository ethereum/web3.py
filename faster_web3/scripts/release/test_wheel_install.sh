#!/bin/bash

set -e
rm -rf build dist
python -m build
cd $(mktemp -d)
python -m venv venv-test
source venv-test/bin/activate
pip install --upgrade "$(ls ~/repo/dist/web3-*-py3-none-any.whl)"
python -c "import web3"
