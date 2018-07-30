#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (
    find_packages,
    setup,
)


setup(
    name='web3',
    # *IMPORTANT*: Don't manually change the version here. Use the 'bumpversion' utility.
    version='4.5.0',
    description="""Web3.py""",
    long_description_markdown_filename='README.md',
    author='Piper Merriam',
    author_email='pipermerriam@gmail.com',
    url='https://github.com/ethereum/web3.py',
    include_package_data=True,
    install_requires=[
        "toolz>=0.9.0,<1.0.0;implementation_name=='pypy'",
        "cytoolz>=0.9.0,<1.0.0;implementation_name=='cpython'",
        "eth-abi>=1.1.1,<2",
        "eth-account>=0.2.1,<0.4.0",
        "eth-utils>=1.0.1,<2.0.0",
        "hexbytes>=0.1.0,<1.0.0",
        "lru-dict>=1.1.6,<2.0.0",
        "eth-hash[pycryptodome]",
        "requests>=2.16.0,<3.0.0",
        "websockets>=5.0.1,<6.0.0",
        "pypiwin32>=223;platform_system=='Windows'",
    ],
    setup_requires=['setuptools-markdown'],
    python_requires='>=3.5, <4',
    extras_require={
        'tester': [
            "eth-tester[py-evm]==0.1.0-beta.29",
            "py-geth>=2.0.1,<3.0.0",
        ],
        'testrpc': ["eth-testrpc>=1.3.3,<2.0.0"],
        'linter': [
            "flake8==3.4.1",
            "isort>=4.2.15,<5",
        ],
    },
    py_modules=['web3', 'ens'],
    license="MIT",
    zip_safe=False,
    keywords='ethereum',
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
