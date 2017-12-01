#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (
    setup,
    find_packages,
)


setup(
    name='web3',
    # *IMPORTANT*: Don't manually change the version here. Use the 'bumpversion' utility.
    version='3.16.4',
    description="""Web3.py""",
    long_description_markdown_filename='README.md',
    author='Piper Merriam',
    author_email='pipermerriam@gmail.com',
    url='https://github.com/ethereum/web3.py',
    include_package_data=True,
    install_requires=[
        "cytoolz>=0.8.2",
        "eth-abi>=0.5.0",
        "eth-keyfile>=0.4.0",
        "eth-keys>=0.1.0-beta.3",
        "eth-utils>=0.7.1",
        "pylru>=1.0.9",
        "pysha3>=0.3",
        "requests>=2.12.4",
        "rlp>=0.4.7",
        "toolz>=0.8.2",
        "eth-tester~=0.1.0b2",
    ],
    setup_requires=['setuptools-markdown'],
    extras_require={
        'tester': ["eth-testrpc>=1.2.0"],
        'gevent': [
            "gevent>=1.1.1,<1.2.0",
            "geventhttpclient>=1.3.1",
        ],
        'platform_system=="Windows"': [
            'pypiwin32',
        ],
    },
    py_modules=['web3'],
    license="MIT",
    zip_safe=False,
    keywords='ethereum',
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
