#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (
    setup,
    find_packages,
)

extras_require = {
    "test": [
        "pytest>=7.0.0",
        "pytest-xdist>=2.4.0",
    ],
    "lint": [
        "flake8==6.0.0",  # flake8 claims semver but adds new warnings at minor releases, leave it pinned.
        "flake8-bugbear==23.3.23",  # flake8-bugbear does not follow semver, leave it pinned.
        "isort>=5.10.1",
        "mypy==0.971",  # mypy does not follow semver, leave it pinned.
        "pydocstyle>=6.0.0",
        "black>=23",
    ],
    "doc": [
        "sphinx>=5.0.0",
        "sphinx_rtd_theme>=1.0.0",
        "towncrier>=21,<22",
    ],
    "dev": [
        "bumpversion>=0.5.3",
        "pytest-watch>=4.1.0",
        "tox>=4.0.0",
        "build>=0.9.0",
        "wheel",
        "twine",
        "ipython",
    ],
}

extras_require["dev"] = (
    extras_require["dev"]
    + extras_require["test"]
    + extras_require["lint"]
    + extras_require["doc"]
)


with open("./README.md") as readme:
    long_description = readme.read()


setup(
    name="<PYPI_NAME>",
    # *IMPORTANT*: Don't manually change the version here. Use `make bump`, as described in readme
    version="0.1.0-alpha.0",
    description="""<PYPI_NAME>: <SHORT_DESCRIPTION>""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="The Ethereum Foundation",
    author_email="snakecharmers@ethereum.org",
    url="https://github.com/ethereum/<REPO_NAME>",
    include_package_data=True,
    install_requires=[
        "eth-utils>=2",
    ],
    python_requires=">=3.7, <4",
    extras_require=extras_require,
    py_modules=["<MODULE_NAME>"],
    license="MIT",
    zip_safe=False,
    keywords="ethereum",
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={"<MODULE_NAME>": ["py.typed"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
