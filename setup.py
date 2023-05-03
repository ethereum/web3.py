#!/usr/bin/env python
from setuptools import (
    find_packages,
    setup,
)

extras_require = {
    "tester": [
        "eth-tester[py-evm]==v0.8.0-b.3",
        "py-geth>=3.11.0",
    ],
    "linter": [
        "black>=22.1.0",
        "flake8==3.8.3",
        "isort>=5.11.0",
        "mypy==0.910",
        "types-setuptools>=57.4.4",
        "types-requests>=2.26.1",
        "types-protobuf==3.19.13",
    ],
    "docs": [
        "sphinx>=5.0.0",
        "sphinx_rtd_theme>=1.0.0",
        "towncrier>=21,<22",
    ],
    "dev": [
        "bumpversion",
        "flaky>=3.7.0",
        "hypothesis>=3.31.2",
        "importlib-metadata<5.0;python_version<'3.8'",
        "pytest>=7.0.0",
        "pytest-asyncio>=0.18.1",
        "pytest-mock>=1.10",
        "pytest-watch>=4.2",
        "pytest-xdist>=1.29",
        "setuptools>=38.6.0",
        "tox>=3.18.0",
        "tqdm>4.32",
        "twine>=1.13",
        "pluggy==0.13.1",
        "when-changed>=0.3.0",
        "build>=0.9.0",
    ],
    "ipfs": [
        "ipfshttpclient==0.8.0a2",
    ],
}

extras_require["dev"] = (
    extras_require["tester"]
    + extras_require["linter"]
    + extras_require["docs"]
    + extras_require["ipfs"]
    + extras_require["dev"]
)

with open("./README.md") as readme:
    long_description = readme.read()

setup(
    name="web3",
    # *IMPORTANT*: Don't manually change the version here. Use the 'bumpversion' utility.
    version="6.3.0",
    description="""web3.py""",
    long_description_content_type="text/markdown",
    long_description=long_description,
    author="Piper Merriam",
    author_email="pipermerriam@gmail.com",
    url="https://github.com/ethereum/web3.py",
    include_package_data=True,
    install_requires=[
        "aiohttp>=3.7.4.post0",
        "eth-abi>=4.0.0",
        "eth-account>=0.8.0",
        "eth-hash[pycryptodome]>=0.5.1",
        "eth-typing>=3.0.0",
        "eth-utils>=2.1.0",
        "hexbytes>=0.1.0",
        "jsonschema>=4.0.0",
        "lru-dict>=1.1.6",
        "protobuf>=4.21.6",
        "pywin32>=223;platform_system=='Windows'",
        "requests>=2.16.0",
        # remove typing_extensions after python_requires>=3.8, see web3._utils.compat
        "typing-extensions>=3.7.4.1,<5;python_version<'3.8'",
        "websockets>=10.0.0",
    ],
    python_requires=">=3.7.2",
    extras_require=extras_require,
    py_modules=["web3", "ens", "ethpm"],
    entry_points={"pytest11": ["pytest_ethereum = web3.tools.pytest_ethereum.plugins"]},
    license="MIT",
    zip_safe=False,
    keywords="ethereum",
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={"web3": ["py.typed"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
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
