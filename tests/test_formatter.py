# -*- coding: utf-8 -*-
import pytest
import web3.web3.formatter as formatter


@pytest.mark.parametrize(
    "value,expected",
    [
    ('XE7338O073KYGTWWZN0F2WZ0R8PX5ZPPZS', '0x00c5496aee77c1ba1f0854206a26dda82a81d6d8'),
    ('0x00c5496aee77c1ba1f0854206a26dda82a81d6d8', '0x00c5496aee77c1ba1f0854206a26dda82a81d6d8'),
    ('00c5496aee77c1ba1f0854206a26dda82a81d6d8', '0x00c5496aee77c1ba1f0854206a26dda82a81d6d8'),
    ('0x11f4d0a3c12e86b4b5f39b213f7e19d048276dae', '0x11f4d0a3c12e86b4b5f39b213f7e19d048276dae')
    ]
)
def test_inputAddressFormatter(value, expected):
    assert formatter.inputAddressFormatter(value) == expected

@pytest.mark.parametrize(
    "value",
    [
    ('0x0c5496aee77c1ba1f0854206a26dda82a81d6d8'),
    ('0x0c5496aee77c1ba1f0854206a26dda82a81d6d8'),
    ('00c5496aee77c1ba1f0854206a26dda82a81d6d'),
    ('XE7338O073KYGTWWZN0F2WZ0R8PX5ZPPZE'),
    ('0x'),
    ]
)
def test_inputAddressFormatter2(value):
    with pytest.raises(Exception):
        formatter.inputAddressFormatter(value)

@pytest.mark.parametrize(
    "value,expected",
    [
    ('latest', 'latest'),
    ('pending', 'pending'),
    ('earliest', 'earliest'),
    (1, '0x1')
    ('0x1', '0x1')
    ]
)
def test_inputDefaultBlockNumberFormatter(value, expected):
    assert formatter.inputDefaultBlockNumberFormatter(value) == expected


@pytest.mark.parametrize(
    "value,expected",
    [
    ({
        "from": '0x00000',
        "to": '0x00000',
        "payload": '0x7b2274657374223a2274657374227d',
        "ttl": 200,
        "priority": 1000,
        "topics": ['hello','mytopics']
    },
    {
        "from": '0x00000',
        "to": '0x00000',
        "payload": '0x7b2274657374223a2274657374227d',
        "ttl": '0xc8',
        "priority": '0x3e8',
        "topics": ['0x68656c6c6f','0x6d79746f70696373'],
        "workToProve": '0x0'
    })
    ]
)
def test_inputPostFormatter(value, expected):
    assert formatter.inputPostFormatter(value) == expected


@pytest.mark.parametrize(
    "value,expected",
    [({
            "data": '0x34234bf23bf4234',
            "value": 100,
            "from": '0x00c5496aee77c1ba1f0854206a26dda82a81d6d8',
            "to": '0x00c5496aee77c1ba1f0854206a26dda82a81d6d8',
            "nonce": 1000,
            "gas": 1000,
            "gasPrice": 1000
        },
        {
            "data": '0x34234bf23bf4234',
            "value": '0x64',
            "from": '0x00c5496aee77c1ba1f0854206a26dda82a81d6d8',
            "to": '0x00c5496aee77c1ba1f0854206a26dda82a81d6d8',
            "nonce": '0x3e8',
            "gas": '0x3e8',
            "gasPrice": '0x3e8'
        }
    ),({
            "data": '0x34234bf23bf4234',
            "value": 100,
            "from": '00c5496aee77c1ba1f0854206a26dda82a81d6d8',
            "to": '00c5496aee77c1ba1f0854206a26dda82a81d6d8',
        },
        {
            "data": '0x34234bf23bf4234',
            "value": '0x64',
            "from": '0x00c5496aee77c1ba1f0854206a26dda82a81d6d8',
            "to": '0x00c5496aee77c1ba1f0854206a26dda82a81d6d8',
        }
    ),({
            "data": '0x34234bf23bf4234',
            "value": 100,
            "from": '00c5496aee77c1ba1f0854206a26dda82a81d6d8',
            "to": '00c5496aee77c1ba1f0854206a26dda82a81d6d8',
            "gas": '1000',
            "gasPrice": 1000
        },
        {
            "data": '0x34234bf23bf4234',
            "value": '0x64',
            "from": '0x00c5496aee77c1ba1f0854206a26dda82a81d6d8',
            "to": '0x00c5496aee77c1ba1f0854206a26dda82a81d6d8',
            "gas": '0x3e8',
            "gasPrice": '0x3e8'
        },
    ), ({
            "data": '0x34234bf23bf4234',
            "value": 100,
            "from": 'XE7338O073KYGTWWZN0F2WZ0R8PX5ZPPZS',
            "to": 'XE7338O073KYGTWWZN0F2WZ0R8PX5ZPPZS',
            "gas": '1000',
            "gasPrice": 1000
        },
        {
            "data": '0x34234bf23bf4234',
            "value": '0x64',
            "from": '0x00c5496aee77c1ba1f0854206a26dda82a81d6d8',
            "to": '0x00c5496aee77c1ba1f0854206a26dda82a81d6d8',
            "gas": '0x3e8',
            "gasPrice": '0x3e8'
        },
    ), ({
            "data": '0x34234bf23bf4234',
            "value": 100,
            "from": 'XE7338O073KYGTWWZN0F2WZ0R8PX5ZPPZS',
            "gas": '1000',
            "gasPrice": 1000
        },
        {
            "data": '0x34234bf23bf4234',
            "value": '0x64',
            "from": '0x00c5496aee77c1ba1f0854206a26dda82a81d6d8',
            "gas": '0x3e8',
            "gasPrice": '0x3e8'
        }
    )]
)
def test_inputTransactionFormatter(value, expected):
    assert formatter.inputTransactionFormatter(value) == expected


@pytest.mark.parametrize(
    "value,expected",
    [
        ({
                "hash": '0xd6960376d6c6dea93647383ffb245cfced97ccc5c7525397a543a72fdaea5265',
                "parentHash": '0x83ffb245cfced97ccc5c75253d6960376d6c6dea93647397a543a72fdaea5265',
                "miner": '0xdcc6960376d6c6dea93647383ffb245cfced97cf',
                "stateRoot": '0x54dda68af07643f68739a6e9612ad157a26ae7e2ce81f77842bb5835fbcde583',
                "sha3Uncles": '0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347',
                "bloom": '0xd6960376d6c6dea93647383ffb245cfced97ccc5c7525397a543a72fdaea5265',
                "difficulty": '0x3e8',
                "totalDifficulty": '0x3e8',
                "number": '0x3e8',
                "gasLimit": '0x3e8',
                "gasUsed": '0x3e8',
                "timestamp": '0x3e8',
                "extraData": '0xd6960376d6c6dea93647383ffb245cfced97ccc5c7525397a543a72fdaea5265',
                "nonce": '0xd6960376d6c6dea93647383ffb245cfced97ccc5c7525397a543a72fdaea5265',
                "size": '0x3e8'
            }, {
                "hash": '0xd6960376d6c6dea93647383ffb245cfced97ccc5c7525397a543a72fdaea5265',
                "parentHash": '0x83ffb245cfced97ccc5c75253d6960376d6c6dea93647397a543a72fdaea5265',
                "miner": '0xdcc6960376d6c6dea93647383ffb245cfced97cf',
                "stateRoot": '0x54dda68af07643f68739a6e9612ad157a26ae7e2ce81f77842bb5835fbcde583',
                "sha3Uncles": '0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347',
                "bloom": '0xd6960376d6c6dea93647383ffb245cfced97ccc5c7525397a543a72fdaea5265',
                "difficulty": 1000,
                "totalDifficulty": 1000,
                "number": 1000,
                "gasLimit": 1000,
                "gasUsed": 1000,
                "timestamp": 1000,
                "extraData": '0xd6960376d6c6dea93647383ffb245cfced97ccc5c7525397a543a72fdaea5265',
                "nonce": '0xd6960376d6c6dea93647383ffb245cfced97ccc5c7525397a543a72fdaea5265',
                "size": 1000
        }),


        ({
                "hash": None,
                "parentHash": '0x83ffb245cfced97ccc5c75253d6960376d6c6dea93647397a543a72fdaea5265',
                "miner": None,
                "stateRoot": '0x54dda68af07643f68739a6e9612ad157a26ae7e2ce81f77842bb5835fbcde583',
                "sha3Uncles": '0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347',
                "bloom": '0xd6960376d6c6dea93647383ffb245cfced97ccc5c7525397a543a72fdaea5265',
                "difficulty": '0x3e8',
                "totalDifficulty": '0x3e8',
                "number": None,
                "gasLimit": '0x3e8',
                "gasUsed": '0x3e8',
                "timestamp": '0x3e8',
                "extraData": '0xd6960376d6c6dea93647383ffb245cfced97ccc5c7525397a543a72fdaea5265',
                "nonce": None,
                "size": '0x3e8'
            }, {
                "hash": None,
                "parentHash": '0x83ffb245cfced97ccc5c75253d6960376d6c6dea93647397a543a72fdaea5265',
                "miner": None,
                "stateRoot": '0x54dda68af07643f68739a6e9612ad157a26ae7e2ce81f77842bb5835fbcde583',
                "sha3Uncles": '0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347',
                "bloom": '0xd6960376d6c6dea93647383ffb245cfced97ccc5c7525397a543a72fdaea5265',
                "difficulty": 1000,
                "totalDifficulty": 1000,
                "number": None,
                "gasLimit": 1000,
                "gasUsed": 1000,
                "timestamp": 1000,
                "extraData": '0xd6960376d6c6dea93647383ffb245cfced97ccc5c7525397a543a72fdaea5265',
                "nonce": None,
                "size": 1000
        })
    ]
)
def test_outputBlockFormatter(value, expected):
    assert formatter.outputBlockFormatter(value) == expected


@pytest.mark.parametrize(
    "value,expected",
    [

        ({
                "transactionIndex": '0x3e8',
                "logIndex": '0x3e8',
                "blockNumber": '0x3e8',
                "transactionHash": '0xd6960376d6c6dea93647383ffb245cfced97ccc5c7525397a543a72fdaea5265',
                "blockHash": '0xd6960376d6c6dea93647383ffb245cfced97ccc5c7525397a543a72fdaea5265',
                "data": '0x7b2274657374223a2274657374227',
                "topics": ['0x68656c6c6f','0x6d79746f70696373']                
            }, {
                "transactionIndex": 1000,
                "logIndex": 1000,
                "blockNumber": 1000,
                "transactionHash": '0xd6960376d6c6dea93647383ffb245cfced97ccc5c7525397a543a72fdaea5265',
                "blockHash": '0xd6960376d6c6dea93647383ffb245cfced97ccc5c7525397a543a72fdaea5265',
                "data": '0x7b2274657374223a2274657374227',
                "topics": ['0x68656c6c6f','0x6d79746f70696373']
        }),



        ({
                "transactionIndex": None,
                "logIndex": None,
                "blockNumber": None,
                "transactionHash": None,
                "blockHash": None,
                "data": '0x7b2274657374223a2274657374227',
                "topics": ['0x68656c6c6f','0x6d79746f70696373']                
            }, {
                "transactionIndex": None,
                "logIndex": None,
                "blockNumber": None,
                "transactionHash": None,
                "blockHash": None,
                "data": '0x7b2274657374223a2274657374227',
                "topics": ['0x68656c6c6f','0x6d79746f70696373']
        })


    ]
)
def test_outputLogFormatter(value, expected):
    assert formatter.outputLogFormatter(value) == expected


@pytest.mark.parametrize(
    "value,expected",
    [
        ({
                "expiry": '0x3e8',
                "sent": '0x3e8',
                "ttl": '0x3e8',
                "workProved": '0x3e8',
                "payload": '0x7b2274657374223a2274657374227d',
                "topics": ['0x68656c6c6f','0x6d79746f70696373']                
            }, {
                "expiry": 1000,
                "sent": 1000,
                "ttl": 1000,
                "workProved": 1000,
                "payload": '0x7b2274657374223a2274657374227d',
                "topics": ['hello','mytopics']
        })
    ]
)
def test_outputPostFormatter(value, expected):
    assert formatter.outputPostFormatter(value) == expected


@pytest.mark.parametrize(
    "value,expected",
    [
        ({
                "input": '0x3454645634534',
                "from": '0x00000',
                "to": '0x00000',
                "value": '0x3e8',
                "gas": '0x3e8',
                "gasPrice": '0x3e8',
                "nonce": '0xb',
                "transactionIndex": '0x1',
                "blockNumber": '0x3e8',
                "blockHash": '0xc9b9cdc2092a9d6589d96662b1fd6949611163fb3910cf8a173cd060f17702f9'
            }, {
                "input": '0x3454645634534',
                "from": '0x00000',
                "to": '0x00000',
                "value": 1000,
                "gas": 1000,
                "gasPrice": 1000,
                "nonce": 11,
                "blockNumber": 1000,
                "blockHash": '0xc9b9cdc2092a9d6589d96662b1fd6949611163fb3910cf8a173cd060f17702f9',
                "transactionIndex": 1
        })
    ]
)
def test_outputTransactionFormatter(value, expected):
    assert formatter.outputTransactionFormatter(value) == expected
