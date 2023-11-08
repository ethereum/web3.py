.PHONY: clean-pyc clean-build docs

help:
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "testall - run tests on every Python version with tox"
	@echo "release - package and upload a release"
	@echo "dist - package"

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

lint:
	tox -e lint

lint-roll:
	isort web3 ens tests
	black web3 ens tests setup.py
	$(MAKE) lint

test:
	pytest tests

test-all:
	tox

benchmark:
	tox -e benchmark

build-docs:
	sphinx-apidoc -o docs/ . setup.py "*conftest*" "tests" "ethpm" "web3/tools/*"
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(MAKE) -C docs doctest

docs: build-docs validate-docs
	open docs/_build/html/index.html

validate-docs: build-docs
	python newsfragments/validate_files.py
	towncrier build --draft

linux-docs: build-docs
	readlink -f docs/_build/html/index.html

notes:
	# Let UPCOMING_VERSION be the version that is used for the current bump
	$(eval UPCOMING_VERSION=$(shell bumpversion $(bump) --dry-run --list | grep new_version= | sed 's/new_version=//g'))
	# Now generate the release notes to have them included in the release commit
	towncrier build --yes --version $(UPCOMING_VERSION)
	# Before we bump the version, make sure that the towncrier-generated docs will build
	make build-docs
	git commit -m "Compile release notes for v$(UPCOMING_VERSION)"

release: clean
	# require that upstream is configured for ethereum/web3.py
	git remote -v | grep "upstream\tgit@github.com:ethereum/web3.py.git (push)\|upstream\thttps://github.com/ethereum/web3.py (push)"
	./newsfragments/validate_files.py is-empty
	# verify that docs build correctly
	make build-docs
	CURRENT_SIGN_SETTING=$(git config commit.gpgSign)
	git config commit.gpgSign true
	bumpversion $(bump)
	git push upstream && git push upstream --tags
	python -m build
	twine upload dist/*
	git config commit.gpgSign "$(CURRENT_SIGN_SETTING)"

dist: clean
	python -m build
	ls -l dist

package: clean
	python -m build
	python web3/scripts/release/test_package.py
