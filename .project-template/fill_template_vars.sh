#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail

PROJECT_ROOT=$(dirname $(dirname $(python -c 'import os, sys; sys.stdout.write(os.path.realpath(sys.argv[1]))' "$0")))

echo "What is your python module name?"
read MODULE_NAME

echo "What is your pypi package name? (default: $MODULE_NAME)"
read PYPI_INPUT
PYPI_NAME=${PYPI_INPUT:-$MODULE_NAME}

echo "What is your github project name? (default: $PYPI_NAME)"
read REPO_INPUT
REPO_NAME=${REPO_INPUT:-$PYPI_NAME}

echo "What is your readthedocs.org project name? (default: $PYPI_NAME)"
read RTD_INPUT
RTD_NAME=${RTD_INPUT:-$PYPI_NAME}

echo "What is your project name (ex: at the top of the README)? (default: $REPO_NAME)"
read PROJECT_INPUT
PROJECT_NAME=${PROJECT_INPUT:-$REPO_NAME}

echo "What is a one-liner describing the project?"
read SHORT_DESCRIPTION

_replace() {
  local find_cmd=(find "$PROJECT_ROOT" ! -perm -u=x ! -path '*/.git/*' -type f)

  if [[ $(uname) == Darwin ]]; then
    "${find_cmd[@]}" -exec sed -i '' "$1" {} +
  else
    "${find_cmd[@]}" -exec sed -i "$1" {} +
  fi
}
_replace "s/<MODULE_NAME>/$MODULE_NAME/g"
_replace "s/<PYPI_NAME>/$PYPI_NAME/g"
_replace "s/<REPO_NAME>/$REPO_NAME/g"
_replace "s/<RTD_NAME>/$RTD_NAME/g"
_replace "s/<PROJECT_NAME>/$PROJECT_NAME/g"
_replace "s/<SHORT_DESCRIPTION>/$SHORT_DESCRIPTION/g"

mkdir -p "$PROJECT_ROOT/$MODULE_NAME"
touch "$PROJECT_ROOT/$MODULE_NAME/__init__.py"
