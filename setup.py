#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (
    setup,
    find_packages,
)


setup(
    name='web3',
    # *IMPORTANT*: Don't manually change the version here. Use the 'bumpversion' utility.
    version='4.0.0-beta.9',
    description="""Web3.py""",
    long_description_markdown_filename='README.md',
    author='Piper Merriam',
    author_email='pipermerriam@gmail.com',
    url='https://github.com/ethereum/web3.py',
    include_package_data=True,
    install_requires=[
        "cytoolz>=0.9.0,<1.0.0",
        "eth-abi>=1.0.0-beta.0,<2",
        "eth-account>=0.1.0a2,<1.0.0",
        "eth-utils>=1.0.0b1,<2.0.0",
        "hexbytes>=0.1.0b0,<1.0.0",
        "lru-dict>=1.1.6,<2.0.0",
        "pysha3>=1.0.0,<2.0.0",
        "requests>=2.16.0,<3.0.0",
    ],
    setup_requires=['setuptools-markdown'],
    extras_require={
        'tester': [
            "eth-tester[py-evm]==0.1.0b16",
        ],
        'testrpc': ["eth-testrpc>=1.3.3,<2.0.0"],
        'linter': [
            "flake8==3.4.1",
            "isort>=4.2.15,<5",
        ],
        'platform_system=="Windows"': [
            'pypiwin32'  # TODO: specify a version number, move under install_requires
        ],
    },
    py_modules=['web3', 'ens'],
    license="MIT",
    zip_safe=False,
    keywords='ethereum',
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
