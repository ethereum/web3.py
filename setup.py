#!/usr/bin/env python
from setuptools import (
    find_packages,
    setup,
)

extras_require = {
    "dev": [
        "build>=0.9.0",
        "bumpversion>=0.5.3",
        "flaky>=3.7.0",
        "hypothesis>=3.31.2",
        "ipython",
        "mypy==1.10.0",
        "pre-commit>=3.4.0",
        "pytest-asyncio>=0.21.2,<0.23",
        "pytest-mock>=1.10",
        "setuptools>=38.6.0",
        "tox>=4.0.0",
        "tqdm>4.32",
        "twine>=1.13",
        "wheel",
    ],
    "docs": [
        "sphinx>=6.0.0",
        "sphinx-autobuild>=2021.3.14",
        "sphinx_rtd_theme>=1.0.0",
        "towncrier>=21,<22",
    ],
    "test": [
        # Note: ethereum-maintained libraries in this list should be added to the
        # `install_pre_releases.py` script.
        "eth-tester[py-evm]>=0.11.0b1,<0.13.0b1",
        "py-geth>=5.0.0",
        "pytest-asyncio>=0.18.1,<0.23",
        "pytest-mock>=1.10",
        "pytest-xdist>=2.4.0",
        "pytest>=7.0.0",
    ],
}

extras_require["dev"] = (
    extras_require["dev"] + extras_require["docs"] + extras_require["test"]
)


with open("./README.md") as readme:
    long_description = readme.read()


setup(
    name="web3",
    # *IMPORTANT*: Don't manually change the version here. Use `make bump`, as described in readme
    version="7.1.0",
    description="""web3: A Python library for interacting with Ethereum""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="The Ethereum Foundation",
    author_email="snakecharmers@ethereum.org",
    url="https://github.com/ethereum/web3.py",
    include_package_data=True,
    install_requires=[
        # Note: ethereum-maintained libraries in this list should be added to the
        # `install_pre_releases.py` script.
        "eth-abi>=5.0.1",
        "eth-account>=0.13.1",
        "eth-hash[pycryptodome]>=0.5.1",
        "eth-typing>=5.0.0",
        "eth-utils>=5.0.0",
        "hexbytes>=1.2.0",
        "aiohttp>=3.7.4.post0",
        "pydantic>=2.4.0",
        "pywin32>=223;platform_system=='Windows'",
        "requests>=2.23.0",
        "typing-extensions>=4.0.1",
        "types-requests>=2.0.0",
        "websockets>=10.0.0",
        "pyunormalize>=15.0.0",
    ],
    python_requires=">=3.8, <4",
    extras_require=extras_require,
    py_modules=["web3", "ens"],
    license="MIT",
    zip_safe=False,
    keywords="ethereum",
    packages=find_packages(exclude=["scripts", "scripts.*", "tests", "tests.*"]),
    package_data={"web3": ["py.typed"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
