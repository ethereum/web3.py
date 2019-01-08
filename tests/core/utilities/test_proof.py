import pytest

import rlp

from eth_utils import (
    keccak,
)
from hexbytes import (
    HexBytes,
)
from web3._utils.encoding import (
    pad_bytes,
)
from web3._utils.proof import (
    _verify,
    verify_eth_getProof,
)
from web3.datastructures import (
    AttributeDict,
)

# accountProof
acp = [HexBytes('0xf90211a03841a7ddd65c70c94b8efa79190d00f0ab134b26f18dcad508f60a7e74559d0ba0464'
                'b07429a05039e22931492d6c6251a860c018ea390045d596b1ac11b5c7aa7a011f4b89823a03c9c'
                '4b5a8ab079ee1bc0e2a83a508bb7a5dc7d7fb4f2e95d3186a0b5f7c51c3b2d51d97f171d2b38a4d'
                'f1a7c0acc5eb0de46beeff4d07f5ed20e19a0b591a2ce02367eda31cf2d16eca7c27fd44dbf0864'
                'b64ea8259ad36696eb2a04a02b646a7552b8392ae94263757f699a27d6e9176b4c06b9fc0a722f8'
                '93b964795a02df05d68bceb88eebf68aafde61d10ab942097afc1c58b8435ffd3895358a742a0c2'
                'f16143c4d1db03276c433696dddb3e9f3b113bcd854b127962262e98f43147a0828820316cc02bf'
                'efd899aba41340659fd06df1e0a0796287ec2a4110239f6d2a050496598670b04df7bbff3718887'
                'fa36437d6d8c7afb4eff86f76c5c7097dcc4a0c14e9060c6b3784e35b9e6ae2ad2984142a75910c'
                'cc89eb89dc1e2f44b6c58c2a009804db571d0ce07913e1cbacc4f1dc4fb8265c936f5c612e3a47e'
                '91c64d8e9fa063d96f38b3cb51b1665c6641e25ffe24803f2941e5df79942f6a53b7169647e4a08'
                '99f71abb18c6c956118bf567fac629b75f7e9526873e429d3d8abb6dbb58021a00fd71723529874'
                '2623c0b3cafb3e4bd86c0b5ab1f71097b4dd19f3d6925d758da0096437146c16097f2ccc1d3e910'
                'd65a4132803baee2249e72c8bf0bcaaeb37e580'),
       HexBytes('0xf90151a097b17a89fd2c03ee98cb6459c08f51b269da5cee46650e84470f62bf83b43efe80a03'
                'b269d284a4c3cf8f8deacafb637c6d77f607eec8d75e8548d778e629612310480a01403217a7f14'
                '16830c870087c524dabade3985271f6f369a12b010883c71927aa0f592ac54c879817389663be67'
                '7166f5022943e2fe1b52617a1d15c2f353f27dda0ac8d015a9e668f5877fcc391fae33981c00577'
                '096f0455b42df4f8e8089ece24a003ba34a13e2f2fb4bf7096540b42d4955c5269875b9cf0f7b87'
                '632585d44c9a580a0b179e3230b07db294473ae57f0170262798f8c551c755b5665ace1215cee10'
                'ca80a0552d24252639a6ae775aa1df700ffb92c2411daea7286f158d44081c8172d072a0772a87d'
                '08cf38c4c68bfde770968571abd16fd3835cb902486bd2e515d53c12d80a0413774f3d900d2d2be'
                '7a3ad999ffa859a471dc03a74fb9a6d8275455f5496a548080'),
       HexBytes('0xf869a020d13b52a61d3c1325ce3626a51418adebd6323d4840f1bdd93906359d11c933b846f84'
                '40180a01ab7c0b0a2a4bbb5a1495da8c142150891fc64e0c321e1feb70bd5f881951f7ea0551332'
                'd96d085185ab4019ad8bcf89c45321e136c261eb6271e574a2edf1461f')
       ]

# storage proofs
stp0 = [HexBytes('0xf9019180a01ace80e7bed79fbadbe390876bd1a7d9770edf9462049ef8f4b555d05715d53ea0'
                 '49347a3c2eac6525a3fd7e3454dab19d73b4adeb9aa27d29493b9843f3f88814a085079b4abcd0'
                 '7fd4a5d6c52d35f4c4574aecc85830e90c478ca8c18fcbe590de80a02e3f8ad7ea29e784007f51'
                 '852b9c3e470aef06b11bac32586a8b691134e4c27da064d2157a14bc31f195f73296ea4dcdbe76'
                 '98edbf3ca81c44bf7730179d98d94ca09e7dc2597c9b7f72ddf84d7eebb0fe2a2fa2ab54fe668c'
                 'd14fee44d9b40b1a53a0aa5d4acc7ac636d16bc9655556770bc325e1901fb62dc53770ef911000'
                 '9e080380a0d5fde962bd2fb5326ddc7a9ca7fe0ee47c5bb3227f838b6d73d3299c22457596a086'
                 '91410eff46b88f929ef649ea25025f62a5362ca8dc8876e5e1f4fc8e79256d80a0673e88d3a8a4'
                 '616f676793096b5ae87cff931bd20fb8dd466f97809a1126aad8a08b774a45c2273553e2daf4bb'
                 'c3a8d44fb542ea29b6f125098f79a4d211b3309ca02fed3139c1791269acb9365eddece93e7439'
                 '00eba6b42a6a8614747752ba268f80'),
        HexBytes('0xf891808080a0c7d094301e0c54da37b696d85f72de5520b224ab2cf4f045d8db1a3374caf048'
                 '8080a0fc5581783bfe27fab9423602e1914d719fd71433e9d7dd63c95fe7e58d10c9c38080a0c6'
                 '4f346fc7a21f6679cba8abdf37ca2de8c4fcd8f8bcaedb261b5f77627c93908080808080a0ddef'
                 '2936a67a3ac7d3d4ff15a935a45f2cc4976c8f0310aed85daf763780e2b480'),
        HexBytes('0xf843a0200decd9548b62a8d60345a988386fc84ba6bc95484008f6362f93160ef3e563a1a048'
                 '656c6c6f00000000000000000000000000000000000000000000000000000a')
        ]
stp1 = [HexBytes('0xf9019180a01ace80e7bed79fbadbe390876bd1a7d9770edf9462049ef8f4b555d05715d53ea0'
                 '49347a3c2eac6525a3fd7e3454dab19d73b4adeb9aa27d29493b9843f3f88814a085079b4abcd0'
                 '7fd4a5d6c52d35f4c4574aecc85830e90c478ca8c18fcbe590de80a02e3f8ad7ea29e784007f51'
                 '852b9c3e470aef06b11bac32586a8b691134e4c27da064d2157a14bc31f195f73296ea4dcdbe76'
                 '98edbf3ca81c44bf7730179d98d94ca09e7dc2597c9b7f72ddf84d7eebb0fe2a2fa2ab54fe668c'
                 'd14fee44d9b40b1a53a0aa5d4acc7ac636d16bc9655556770bc325e1901fb62dc53770ef911000'
                 '9e080380a0d5fde962bd2fb5326ddc7a9ca7fe0ee47c5bb3227f838b6d73d3299c22457596a086'
                 '91410eff46b88f929ef649ea25025f62a5362ca8dc8876e5e1f4fc8e79256d80a0673e88d3a8a4'
                 '616f676793096b5ae87cff931bd20fb8dd466f97809a1126aad8a08b774a45c2273553e2daf4bb'
                 'c3a8d44fb542ea29b6f125098f79a4d211b3309ca02fed3139c1791269acb9365eddece93e7439'
                 '00eba6b42a6a8614747752ba268f80'),
        HexBytes('0xf891808080a0885a73846da76a8f45e9037c2991c35028757eca0519d54778424206b5f7987b'
                 '80808080808080a0de76bd384f281e5b6fcea2b7d7c3837215a6216ced58afa4d7f4aa9fc5491f'
                 '518080a0192bba39de6e8182bcccc719799227a83138b6b8b4d01d172f910ffe1eb19a1ba09815'
                 '6bc7db72a566ec89f6b04591ecc82044c946bff6afc20e1bb078bebab80980'),
        HexBytes('0xe5a020125a9d0424db41c2ea393b877b2c0e53b0a684e16920b6767c46e570a3827483828235')
        ]
stp2 = [HexBytes('0xf9019180a01ace80e7bed79fbadbe390876bd1a7d9770edf9462049ef8f4b555d05715d53ea0'
                 '49347a3c2eac6525a3fd7e3454dab19d73b4adeb9aa27d29493b9843f3f88814a085079b4abcd0'
                 '7fd4a5d6c52d35f4c4574aecc85830e90c478ca8c18fcbe590de80a02e3f8ad7ea29e784007f51'
                 '852b9c3e470aef06b11bac32586a8b691134e4c27da064d2157a14bc31f195f73296ea4dcdbe76'
                 '98edbf3ca81c44bf7730179d98d94ca09e7dc2597c9b7f72ddf84d7eebb0fe2a2fa2ab54fe668c'
                 'd14fee44d9b40b1a53a0aa5d4acc7ac636d16bc9655556770bc325e1901fb62dc53770ef911000'
                 '9e080380a0d5fde962bd2fb5326ddc7a9ca7fe0ee47c5bb3227f838b6d73d3299c22457596a086'
                 '91410eff46b88f929ef649ea25025f62a5362ca8dc8876e5e1f4fc8e79256d80a0673e88d3a8a4'
                 '616f676793096b5ae87cff931bd20fb8dd466f97809a1126aad8a08b774a45c2273553e2daf4bb'
                 'c3a8d44fb542ea29b6f125098f79a4d211b3309ca02fed3139c1791269acb9365eddece93e7439'
                 '00eba6b42a6a8614747752ba268f80'),
        HexBytes('0xf8518080a0baeb1e575b459867de7e0cbf05e1e2ef2fea87a769ad3a6a049ba159f46e82a680'
                 '808080a090a2f86d45ebaf52b4ef4315a87b324efa2fe5191b1989d1439f8f74e0e4dddc808080'
                 '808080808080'),
        HexBytes('0xe4820007a0ac06a063e33642c91fa02a8025ac4237059b0b8d9ca52acfca875032c26137b8'),
        HexBytes('0xf851808080a064b6798635ebef2d301b5038f70c56e3340c346bef5c26088d13e2bf32b1e261'
                 '8080808080808080a0f2fe653379ccbf6d015cc9eb321e56e0a9583a3d943767835e157bc60124'
                 'e8a380808080'),
        HexBytes('0xe09e39ae181c101dc0b4e1811f1f29cc26ce82644bc675302d238468ba2090ba01')
        ]
stp3 = [HexBytes('0xf9019180a01ace80e7bed79fbadbe390876bd1a7d9770edf9462049ef8f4b555d05715d53ea0'
                 '49347a3c2eac6525a3fd7e3454dab19d73b4adeb9aa27d29493b9843f3f88814a085079b4abcd0'
                 '7fd4a5d6c52d35f4c4574aecc85830e90c478ca8c18fcbe590de80a02e3f8ad7ea29e784007f51'
                 '852b9c3e470aef06b11bac32586a8b691134e4c27da064d2157a14bc31f195f73296ea4dcdbe76'
                 '98edbf3ca81c44bf7730179d98d94ca09e7dc2597c9b7f72ddf84d7eebb0fe2a2fa2ab54fe668c'
                 'd14fee44d9b40b1a53a0aa5d4acc7ac636d16bc9655556770bc325e1901fb62dc53770ef911000'
                 '9e080380a0d5fde962bd2fb5326ddc7a9ca7fe0ee47c5bb3227f838b6d73d3299c22457596a086'
                 '91410eff46b88f929ef649ea25025f62a5362ca8dc8876e5e1f4fc8e79256d80a0673e88d3a8a4'
                 '616f676793096b5ae87cff931bd20fb8dd466f97809a1126aad8a08b774a45c2273553e2daf4bb'
                 'c3a8d44fb542ea29b6f125098f79a4d211b3309ca02fed3139c1791269acb9365eddece93e7439'
                 '00eba6b42a6a8614747752ba268f80'),
        HexBytes('0xe2a0371fb72cbe0369f5d3a24dca1acb23139df79992d093906bc85d6424757cc51a01')
        ]
stp4 = [HexBytes('0xf9019180a01ace80e7bed79fbadbe390876bd1a7d9770edf9462049ef8f4b555d05715d53ea0'
                 '49347a3c2eac6525a3fd7e3454dab19d73b4adeb9aa27d29493b9843f3f88814a085079b4abcd0'
                 '7fd4a5d6c52d35f4c4574aecc85830e90c478ca8c18fcbe590de80a02e3f8ad7ea29e784007f51'
                 '852b9c3e470aef06b11bac32586a8b691134e4c27da064d2157a14bc31f195f73296ea4dcdbe76'
                 '98edbf3ca81c44bf7730179d98d94ca09e7dc2597c9b7f72ddf84d7eebb0fe2a2fa2ab54fe668c'
                 'd14fee44d9b40b1a53a0aa5d4acc7ac636d16bc9655556770bc325e1901fb62dc53770ef911000'
                 '9e080380a0d5fde962bd2fb5326ddc7a9ca7fe0ee47c5bb3227f838b6d73d3299c22457596a086'
                 '91410eff46b88f929ef649ea25025f62a5362ca8dc8876e5e1f4fc8e79256d80a0673e88d3a8a4'
                 '616f676793096b5ae87cff931bd20fb8dd466f97809a1126aad8a08b774a45c2273553e2daf4bb'
                 'c3a8d44fb542ea29b6f125098f79a4d211b3309ca02fed3139c1791269acb9365eddece93e7439'
                 '00eba6b42a6a8614747752ba268f80'),
        HexBytes('0xf891808080a0c7d094301e0c54da37b696d85f72de5520b224ab2cf4f045d8db1a3374caf048'
                 '8080a0fc5581783bfe27fab9423602e1914d719fd71433e9d7dd63c95fe7e58d10c9c38080a0c6'
                 '4f346fc7a21f6679cba8abdf37ca2de8c4fcd8f8bcaedb261b5f77627c93908080808080a0ddef'
                 '2936a67a3ac7d3d4ff15a935a45f2cc4976c8f0310aed85daf763780e2b480'),
        HexBytes('0xe2a0206753f8e5aa3ce421cb983577928a244ee9afbabf862d69d702cd067379f67701')
        ]
stp5 = [HexBytes('0xf9019180a01ace80e7bed79fbadbe390876bd1a7d9770edf9462049ef8f4b555d05715d53ea0'
                 '49347a3c2eac6525a3fd7e3454dab19d73b4adeb9aa27d29493b9843f3f88814a085079b4abcd0'
                 '7fd4a5d6c52d35f4c4574aecc85830e90c478ca8c18fcbe590de80a02e3f8ad7ea29e784007f51'
                 '852b9c3e470aef06b11bac32586a8b691134e4c27da064d2157a14bc31f195f73296ea4dcdbe76'
                 '98edbf3ca81c44bf7730179d98d94ca09e7dc2597c9b7f72ddf84d7eebb0fe2a2fa2ab54fe668c'
                 'd14fee44d9b40b1a53a0aa5d4acc7ac636d16bc9655556770bc325e1901fb62dc53770ef911000'
                 '9e080380a0d5fde962bd2fb5326ddc7a9ca7fe0ee47c5bb3227f838b6d73d3299c22457596a086'
                 '91410eff46b88f929ef649ea25025f62a5362ca8dc8876e5e1f4fc8e79256d80a0673e88d3a8a4'
                 '616f676793096b5ae87cff931bd20fb8dd466f97809a1126aad8a08b774a45c2273553e2daf4bb'
                 'c3a8d44fb542ea29b6f125098f79a4d211b3309ca02fed3139c1791269acb9365eddece93e7439'
                 '00eba6b42a6a8614747752ba268f80'),
        HexBytes('0xf8518080a0baeb1e575b459867de7e0cbf05e1e2ef2fea87a769ad3a6a049ba159f46e82a680'
                 '808080a090a2f86d45ebaf52b4ef4315a87b324efa2fe5191b1989d1439f8f74e0e4dddc808080'
                 '808080808080'),
        HexBytes('0xe21aa0990554b85cd95fbd5dde99b7bf703f21a97abc58b7e58121f07762e2b288b941'),
        HexBytes('0xf851808080808080a083c5cdd22efbc05cf2c190b62a0628e38235ad2c4a1419f1a2b402bdb7'
                 'bc3c80a0b050e06ae61184eef34d977ded60b6dd28a5515f0c26b77f044816d28733c351808080'
                 '808080808080'),
        HexBytes('0xe19f20ac017d29f2ac78f8a7446b686fe1829697db9d432a229163a5cdf9a716ce01')
        ]

# This example proof contains storage proofs for different contract state
# variables. All types of patricia tree nodes (branch, even/odd leaf, even/odd
# extension) are present in the proof.
exp = AttributeDict({'address': '0x4CB06C43fcdABeA22541fcF1F856A6a296448B6c',
                     'accountProof': acp,
                     'balance': 0,
                     'codeHash': HexBytes('0x551332d96d085185ab4019ad8bcf89c45321e136c261eb6271e5'
                                          '74a2edf1461f'),
                     'nonce': 1,
                     'storageHash': HexBytes('0x1ab7c0b0a2a4bbb5a1495da8c142150891fc64e0c321e1feb'
                                             '70bd5f881951f7e'),
                     'storageProof': [AttributeDict({'key': HexBytes('0x00'),
                                                     'value': HexBytes('0x48656c6c6f0000000000000'
                                                                       '0000000000000000000000000'
                                                                       '000000000000000a'),
                                                     'proof': stp0
                                                     }),
                                      AttributeDict({'key': HexBytes('0xa78e01754db126511c9323f92'
                                                                     'a2864f37d45132dcd962cb6a3ca'
                                                                     '3e544dbf49b5'),
                                                     'value': HexBytes('0x8235'),
                                                     'proof': stp1
                                                     }),
                                      AttributeDict({'key': HexBytes('0x4a5bded210bb862fae2c0d18b'
                                                                     '9d29bf7f88b08a75dd1594b1369'
                                                                     'abc7881e3fe1'),
                                                     'value': HexBytes('0x01'),
                                                     'proof': stp2
                                                     }),
                                      AttributeDict({'key': HexBytes('0xad2d52b8047a96778c45f477d'
                                                                     'abddaae71b5ff6b355ac44a03c9'
                                                                     '522a54a18a26'),
                                                     'value': HexBytes('0x01'),
                                                     'proof': stp3
                                                     }),
                                      AttributeDict({'key': HexBytes('0x7352bc45c8aa6995480780fe15'
                                                                     'a07c4daa795263b5e7a9d04d9ed9'
                                                                     '79c93ca85e'),
                                                     'value': HexBytes('0x01'),
                                                     'proof': stp4
                                                     }),
                                      AttributeDict({'key': HexBytes('0x82fb8bdd0a53542a1f59046c16'
                                                                     'f7a1350c43d22db36425bb53f551'
                                                                     'e7c6a09181'),
                                                     'value': HexBytes('0x01'),
                                                     'proof': stp5
                                                     })
                                      ]
                     })


def test_verify_eth_getProof():
    block_stateRoot = "0xe8cbf0ef6814a55f071be90cdc0b699a3795208a0792ca18bc2a3b7947a594b7"
    stateRoot = bytes.fromhex(block_stateRoot[2:])
    assert verify_eth_getProof(exp, stateRoot)


@pytest.mark.parametrize(
    "key,proof,value",
    [
        (exp.storageProof[0].key, stp0, exp.storageProof[0].value),
        (exp.storageProof[1].key, stp1, exp.storageProof[1].value),
        (exp.storageProof[2].key, stp2, exp.storageProof[2].value),
        (exp.storageProof[3].key, stp3, exp.storageProof[3].value),
        (exp.storageProof[4].key, stp4, exp.storageProof[4].value),
        (exp.storageProof[5].key, stp5, exp.storageProof[5].value),
    ]
)
def test_verify(key, proof, value):
    trie_key = keccak(pad_bytes(b'\x00', 32, key)).hex()
    root = exp.storageHash
    expected_value = rlp.encode(value)
    assert _verify(root, trie_key, proof, 0, 0, expected_value)
