#!/bin/bash

set -o errexit
set -o nounset
set -o pipefail

# List of all non-executable files
TEMPLATE_FILES=$(find . ! -perm -u=x -type f | grep -v "\.git")

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

sed -i "s/<MODULE_NAME>/$MODULE_NAME/g" $TEMPLATE_FILES
sed -i "s/<PYPI_NAME>/$PYPI_NAME/g" $TEMPLATE_FILES
sed -i "s/<REPO_NAME>/$REPO_NAME/g" $TEMPLATE_FILES
sed -i "s/<RTD_NAME>/$RTD_NAME/g" $TEMPLATE_FILES
sed -i "s/<PROJECT_NAME>/$PROJECT_NAME/g" $TEMPLATE_FILES
sed -i "s/<SHORT_DESCRIPTION>/$SHORT_DESCRIPTION/g" $TEMPLATE_FILES
