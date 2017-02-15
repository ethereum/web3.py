# -*- coding: utf-8 -*-
import pytest

from eth_utils import (
    force_bytes,
    force_text,
)


@pytest.fixture()
def math_contract(web3, MathContract):
    deploy_txn = MathContract.deploy()
    deploy_receipt = web3.eth.getTransactionReceipt(deploy_txn)
    assert deploy_receipt is not None
    _math_contract = MathContract(address=deploy_receipt['contractAddress'])
    return _math_contract


@pytest.fixture()
def string_contract(web3, StringContract):
    deploy_txn = StringContract.deploy(args=["Caqalai"])
    deploy_receipt = web3.eth.getTransactionReceipt(deploy_txn)
    assert deploy_receipt is not None
    _string_contract = StringContract(address=deploy_receipt['contractAddress'])
    return _string_contract


@pytest.fixture()
def address_contract(web3, WithConstructorAddressArgumentsContract):
    deploy_txn = WithConstructorAddressArgumentsContract.deploy(args=[
        "0xd3cda913deb6f67967b99d67acdfa1712c293601",
    ])
    deploy_receipt = web3.eth.getTransactionReceipt(deploy_txn)
    assert deploy_receipt is not None
    _address_contract = WithConstructorAddressArgumentsContract(address=deploy_receipt['contractAddress'])
    return _address_contract


def test_call_with_no_arguments(math_contract):
    result = math_contract.call().return13()
    assert result == 13


def test_call_with_one_argument(math_contract):
    result = math_contract.call().multiply7(3)
    assert result == 21


@pytest.mark.parametrize(
    'call_args,call_kwargs',
    (
        ((9, 7), {}),
        ((9,), {'b': 7}),
        (tuple(), {'a': 9, 'b': 7}),
    ),
)
def test_call_with_multiple_arguments(math_contract, call_args, call_kwargs):
    result = math_contract.call().add(*call_args, **call_kwargs)
    assert result == 16


def test_call_get_string_value(string_contract):
    result = string_contract.call().getValue()
    # eth_abi.decode_api() does not assume implicit utf-8
    # encoding of string return values. Thus, we need to decode
    # ourselves for fair comparison.
    assert result == "Caqalai"


def test_call_read_string_variable(string_contract):
    result = string_contract.call().constValue()
    assert force_text(result) == force_text("\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff")


def test_call_read_address_variable(address_contract):
    result = address_contract.call().testAddr()
    assert result == "0xd3cda913deb6f67967b99d67acdfa1712c293601"
