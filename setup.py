#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import (
    setup,
    find_packages,
)


DIR = os.path.dirname(os.path.abspath(__file__))


readme = open(os.path.join(DIR, 'README.md')).read()


setup(
    name='web3',
    version='3.4.2',
    description="""Web3.py""",
    long_description=readme,
    author='Piper Merriam',
    author_email='pipermerriam@gmail.com',
    url='https://github.com/pipermerriam/web3.py',
    include_package_data=True,
    install_requires=[
        "pysha3>=0.3",
        "rlp>=0.4.6,<0.4.7",
        "gevent>=1.1.1,<1.2.0",
        "geventhttpclient>=1.3.1",
        "ethereum-abi-utils>=0.2.1",
        "pysha3>=0.3",
        "pylru>=1.0.9",
    ],
    extras_require={
        'Tester': ["eth-testrpc>=0.9.0"],
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
