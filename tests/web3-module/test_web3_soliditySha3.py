import pytest


@pytest.mark.parametrize(
    'types,values,expected',
    (
        (
            ['bool'],
            [True],
            "0x5fe7f977e71dba2ea1a68e21057beebb9be2ac30c6410aa38d4f3fbe41dcffd2"
         ),
        (
            ['uint8', 'uint8', 'uint8'],
            [97, 98, 99],
            "0x4e03657aea45a94fc7d47ba826c8d667c0d1e6e33a64a036ec44f58fa12d6c45"
        ),
        (
            ['uint248'],
            [30],
            "0x30f95d210785601eb33ae4d53d405b26f920e765dff87cca8e9a4aec99f82671"
        ),
        (
            ['bool', 'uint16'],
            [True, 299],
            "0xed18599ccd80ee9fae9a28b0e34a5573c3233d7468f808fd659bc171cf0b43bd"
         ),
        (
            ['int256'],
            [-10],
            "0xd6fb717f7e270a360f5093ce6a7a3752183e89c9a9afe5c0cb54b458a304d3d5"
         ),
        (
            ['int256'],
            [10],
            "0xc65a7bb8d6351c1cf70c95a316cc6a92839c986682d98bc35f958f4883f9d2a8"
         ),
        (
            ['int8', 'uint8'],
            [-10, 18],
            "0x5c6ab1e634c08d9c0f4df4d789e8727943ef010dd7ca8e3c89de197a26d148be"
        ),
        (
            ['address'],
            ["0x49eddd3769c0712032808d86597b84ac5c2f5614"],
            "0x2ff37b5607484cd4eecf6d13292e22bd6e5401eaffcc07e279583bc742c68882"
        ),
        (
            ['bytes2'],
            [b'T\x02'],
            "0x4ed9171bda52fca71ab28e7f452bd6eacc3e5a568a47e0fa53b503159a9b8910"
        ),
        (
            ['bytes2'],
            ['0x5402'],
            "0x4ed9171bda52fca71ab28e7f452bd6eacc3e5a568a47e0fa53b503159a9b8910"
        ),
        (
            ['bytes3'],
            ['0x5402'],
            "0x4ed9171bda52fca71ab28e7f452bd6eacc3e5a568a47e0fa53b503159a9b8910"
        ),
        (
            ['bytes'],
            [b'checklongbytestringagainstsoliditysha3hashfunction'],
            "0xd78a84d65721b67e4011b10c99dafdedcdcd7cb30153064f773e210b4762e22f"
        ),
        (
            ['string'],
            ['testing a string!'],
            "0xe8c275c0b4070a5ec6cfcb83f0ba394b30ddd283de785d43f2eabfb04bd96747"
        ),
        (
            ['string', 'bool', 'uint16', 'bytes2', 'address'],
            [
                'testing a string!',
                False,
                299,
                b'T\x02',
                "0x49eddd3769c0712032808d86597b84ac5c2f5614",
            ],
            "0x8cc6eabb25b842715e8ca39e2524ed946759aa37bfb7d4b81829cf5a7e266103",
        ),

    ),
)
def test_soliditySha3(web3, types, values, expected):
    actual = web3.soliditySha3(types, values)
    assert actual == expected
