#!/usr/bin/env python
import sys
from setuptools import (
    find_packages,
    setup,
)
from mypyc.build import mypycify

extras_require = {
    "tester": [
        # Note: ethereum-maintained libraries in this list should be added to the
        # `install_pre_releases.py` script.
        "eth-tester[py-evm]>=0.13.0b1,<0.14.0b1",
        "py-geth>=5.1.0",
    ],
    "dev": [
        "build>=0.9.0",
        "bump_my_version>=0.19.0",
        "ipython",
        "setuptools>=38.6.0",
        "tqdm>4.32",
        "twine>=1.13",
        "wheel",
    ],
    "docs": [
        "sphinx>=6.0.0",
        "sphinx-autobuild>=2021.3.14",
        "sphinx_rtd_theme>=1.0.0",
        "towncrier>=25,<26",
    ],
    "test": [
        "pytest-asyncio>=1.2,<1.3",
        "pytest-mock>=1.10",
        "pytest-xdist>=2.4.0",
        "pytest>=7.0.0",
        "flaky>=3.7.0",
        "hypothesis>=3.31.2",
        "tox>=4.0.0",
        f"mypy=={'1.14.1' if sys.version_info < (3, 9) else '1.18.2'}",
        "pre-commit>=3.4.0",
    ],
}

extras_require["dev"] = (
    extras_require["dev"]
    + extras_require["docs"]
    + extras_require["test"]
    + extras_require["tester"]
)
extras_require["test"] = extras_require["test"] + extras_require["tester"]


with open("./README.md") as readme:
    long_description = readme.read()


ext_modules = mypycify(
    [
        "faster_ens/_normalization.py",
        # "faster_ens/async_ens.py",  figure out `default`
        "faster_ens/auto.py",
        "faster_ens/base_ens.py",
        "faster_ens/constants.py",
        # "faster_ens/ens.py",  figure out `default`
        "faster_ens/utils.py",
        "faster_web3/beacon",
        "faster_web3/_utils/blocks.py",
        "faster_web3/_utils/caching",
        "faster_web3/_utils/datatypes.py",
        "faster_web3/_utils/http.py",
        "faster_web3/_utils/math.py",
        "faster_web3/_utils/type_conversion.py",
        "faster_web3/_utils/utility_methods.py",
        "faster_web3/auto",
        "faster_web3/gas_strategies",
        "faster_web3/tools/benchmark/node.py",
        "faster_web3/tools/benchmark/reporting.py",
        "faster_web3/tools/benchmark/utils.py",
        "faster_web3/utils/caching.py",
        "faster_web3/constants.py",
        "faster_web3/types.py",
        "--pretty",
        "--disable-error-code=return-value",
        "--disable-error-code=arg-type",
        "--disable-error-code=union-attr",
        "--disable-error-code=redundant-cast",
        "--disable-error-code=type-arg",
        "--disable-error-code=type-var",
        "--disable-error-code=call-arg",
        "--disable-error-code=call-overload",
        "--disable-error-code=str-bytes-safe",
        "--disable-error-code=dict-item",
        "--disable-error-code=typeddict-item",
        "--disable-error-code=truthy-function",
        "--disable-error-code=var-annotated",
        "--disable-error-code=assignment",
        "--disable-error-code=index",
        "--disable-error-code=operator",
        "--disable-error-code=override",
        "--disable-error-code=misc",
        "--disable-error-code=unused-ignore",
    ]
)

setup(
    name="faster_web3",
    # *IMPORTANT*: Don't manually change the version here. See Contributing docs for the release process.
    version="7.13.0",
    description="""A faster fork of web3: A Python library for interacting with Ethereum. Implemented in C.""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="The Ethereum Foundation",
    author_email="snakecharmers@ethereum.org",
    url="https://github.com/ethereum/web3.py",
    include_package_data=True,
    install_requires=[
        # Note: ethereum-maintained libraries in this list should be added to the
        # `install_pre_releases.py` script.
        "eth-account>=0.13.6",
        "eth-hash[pycryptodome]>=0.5.1",
        "eth-typing>=5.0.0",
        "faster-eth-abi>=5.0.1",
        "faster-eth-utils>=5.3.8",
        "faster-hexbytes>=1.2.0",
        "aiohttp>=3.7.4.post0",
        "pydantic>=2.4.0",
        "pywin32>=223;platform_system=='Windows'",
        "requests>=2.23.0",
        "typing-extensions>=4.0.1",
        "types-requests>=2.0.0",
        "websockets>=10.0.0,<16.0.0",
        "pyunormalize>=15.0.0",
    ],
    python_requires=">=3.9, <4",
    extras_require=extras_require,
    py_modules=["faster_web3", "faster_ens"],
    license="MIT",
    zip_safe=False,
    keywords="ethereum",
    packages=find_packages(exclude=["scripts", "scripts.*", "tests", "tests.*", "benchmarks", "benchmarks.*"]),
    ext_modules=ext_modules,
    package_data={"faster_web3": ["py.typed"], "faster_ens": ["py.typed"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
)
