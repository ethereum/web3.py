# Strict bytes checking seems to only be supported with solidity versions below `0.5.0`.
# This older emitter contract, compiled with solidity `0.4.21`, can still test against the strict
# bytes check but we can update all other tests using the emitter contract to use the new version
# compiled with `0.8.11`.
# See: https://github.com/ethereum/web3.py/issues/2301

CONTRACT_EMITTER_CODE_OLD = (
    "608060405234801561001057600080fd5b50610aed806100206000396000f300608060405260043"
    "6106100ae5763ffffffff7c01000000000000000000000000000000000000000000000000000000"
    "006000350416630bb563d681146100b357806317c0c1801461010e57806320f0256e14610129578"
    "06390b41d8b14610150578063966b50e0146101715780639c377053146101ff578063aa6fd82214"
    "610223578063acabb9ed14610241578063b2ddc449146102d8578063e17bf9561461030c578063f"
    "82ef69e14610365575b600080fd5b3480156100bf57600080fd5b50604080516020600480358082"
    "0135601f810184900484028501840190955284845261010c9436949293602493928401919081908"
    "401838280828437509497506103999650505050505050565b005b34801561011a57600080fd5b50"
    "61010c60ff60043516610435565b34801561013557600080fd5b5061010c60ff600435166024356"
    "04435606435608435610527565b34801561015c57600080fd5b5061010c60ff6004351660243560"
    "44356105e4565b34801561017d57600080fd5b50604080516020600480358082013583810280860"
    "1850190965280855261010c95369593946024949385019291829185019084908082843750506040"
    "805187358901803560208181028481018201909552818452989b9a9989019892975090820195509"
    "350839250850190849080828437509497506106b49650505050505050565b34801561020b576000"
    "80fd5b5061010c60ff6004351660243560443560643561076d565b34801561022f57600080fd5b5"
    "061010c60ff60043516602435610818565b34801561024d57600080fd5b50604080516020600480"
    "3580820135601f810184900484028501840190955284845261010c9436949293602493928401919"
    "0819084018382808284375050604080516020601f89358b01803591820183900483028401830190"
    "9452808352979a9998810197919650918201945092508291508401838280828437509497506108c"
    "a9650505050505050565b3480156102e457600080fd5b5061010c73ffffffffffffffffffffffff"
    "ffffffffffffffff600435811690602435166109bb565b34801561031857600080fd5b506040805"
    "160206004803580820135601f810184900484028501840190955284845261010c94369492936024"
    "9392840191908190840183828082843750949750610a0d9650505050505050565b3480156103715"
    "7600080fd5b5061010c73ffffffffffffffffffffffffffffffffffffffff600435811690602435"
    "16610a6b565b7fa95e6e2a182411e7a6f9ed114a85c3761d87f9b8f453d842c71235aa64fff99f8"
    "16040518080602001828103825283818151815260200191508051906020019080838360005b8381"
    "10156103f85781810151838201526020016103e0565b50505050905090810190601f16801561042"
    "55780820380516001836020036101000a031916815260200191505b509250505060405180910390"
    "a150565b600181601181111561044357fe5b1415610477576040517f1e86022f78f8d04f8e3dfd1"
    "3a2bdb280403e6632877c0dbee5e4eeb259908a5c90600090a1610524565b600081601181111561"
    "048557fe5b141561049757604051600090a0610524565b604080517f08c379a0000000000000000"
    "00000000000000000000000000000000000000000815260206004820152602660248201527f4469"
    "646e2774206d6174636820616e7920616c6c6f7761626c65206576656e7460448201527f20696e6"
    "4657800000000000000000000000000000000000000000000000000006064820152905190819003"
    "60840190fd5b50565b600585601181111561053557fe5b141561058757604080518581526020810"
    "18590528082018490526060810183905290517ff039d147f23fe975a4254bdf6b1502b8c79132ae"
    "1833986b7ccef2638e73fdf99181900360800190a16105dd565b600b85601181111561059557fe5"
    "b14156104975780827fa30ece802b64cd2b7e57dabf4010aabf5df26d1556977affb07b98a77ad9"
    "55b58686604051808381526020018281526020019250505060405180910390a35b5050505050565"
    "b60038360118111156105f257fe5b141561063857604080518381526020810183905281517fdf0c"
    "b1dea99afceb3ea698d62e705b736f1345a7eee9eb07e63d1f8f556c1bc5929181900390910190a"
    "16106af565b600983601181111561064657fe5b14156106875760408051838152905182917f057b"
    "c32826fbe161da1c110afcdcae7c109a8b69149f727fc37a603c60ef94ca919081900360200190a"
    "26106af565b600883601181111561069557fe5b1415610497576040805183815290518291819003"
    "60200190a15b505050565b8160405180828051906020019060200280838360005b838110156106e"
    "25781810151838201526020016106ca565b5050505090500191505060405180910390207fdbc4c1"
    "d1d2f0d84e58d36ca767ec9ba2ec2f933c055e50e5ccdd57697f7b58b0826040518080602001828"
    "103825283818151815260200191508051906020019060200280838360005b838110156107565781"
    "8101518382015260200161073e565b505050509050019250505060405180910390a25050565b600"
    "484601181111561077b57fe5b14156107c657604080518481526020810184905280820183905290"
    "517f4a25b279c7c585f25eda9788ac9420ebadae78ca6b206a0e6ab488fd81f5506291819003606"
    "00190a1610812565b600a8460118111156107d457fe5b1415610497576040805184815290518291"
    "84917ff16c999b533366ca5138d78e85da51611089cd05749f098d6c225d4cd42ee6ec918190036"
    "0200190a35b50505050565b600282601181111561082657fe5b1415610864576040805182815290"
    "517f56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d491819003602"
    "00190a16108c6565b600782601181111561087257fe5b14156108a85760405181907ff70fe689e2"
    "90d8ce2b2a388ac28db36fbb0e16a6d89c6804c461f65a1b40bb1590600090a26108c6565b60068"
    "260118111156108b657fe5b1415610497576040518190600090a15b5050565b8160405180828051"
    "90602001908083835b602083106108fa5780518252601f1990920191602091820191016108db565"
    "b51815160209384036101000a600019018019909216911617905260408051929094018290038220"
    "81835287518383015287519096507fe77cf33df73da7bc2e253a2dae617e6f15e4e337eaa462a10"
    "8903af4643d1b7595508794929350839283019185019080838360005b8381101561097d57818101"
    "5183820152602001610965565b50505050905090810190601f1680156109aa57808203805160018"
    "36020036101000a031916815260200191505b509250505060405180910390a25050565b60408051"
    "73ffffffffffffffffffffffffffffffffffffffff83811682529151918416917ff922c21568954"
    "8d72c3d2fe4ea8dafb2a30c43312c9b43fe5d10f713181f991c9181900360200190a25050565b7f"
    "532fd6ea96cfb78bb46e09279a26828b8b493de1a2b8b1ee1face527978a15a5816040518080602"
    "00182810382528381815181526020019150805190602001908083836000838110156103f8578181"
    "0151838201526020016103e0565b6040805173ffffffffffffffffffffffffffffffffffffffff8"
    "0851682528316602082015281517f06029e18f16caae06a69281f35b00ed3fcf47950e6c99dafa1"
    "bdd8c4b93479a0929181900390910190a150505600a165627a7a72305820962bb0d0c7c052407e6"
    "ad0911da133e939baa8783fbd0220169b97b54160a89e0029"
)

CONTRACT_EMITTER_RUNTIME_OLD = (
    "6080604052600436106100ae5763ffffffff7c01000000000000000000000000000000000000000"
    "000000000000000006000350416630bb563d681146100b357806317c0c1801461010e57806320f0"
    "256e1461012957806390b41d8b14610150578063966b50e0146101715780639c377053146101ff5"
    "78063aa6fd82214610223578063acabb9ed14610241578063b2ddc449146102d8578063e17bf956"
    "1461030c578063f82ef69e14610365575b600080fd5b3480156100bf57600080fd5b50604080516"
    "0206004803580820135601f810184900484028501840190955284845261010c9436949293602493"
    "928401919081908401838280828437509497506103999650505050505050565b005b34801561011"
    "a57600080fd5b5061010c60ff60043516610435565b34801561013557600080fd5b5061010c60ff"
    "60043516602435604435606435608435610527565b34801561015c57600080fd5b5061010c60ff6"
    "00435166024356044356105e4565b34801561017d57600080fd5b50604080516020600480358082"
    "0135838102808601850190965280855261010c95369593946024949385019291829185019084908"
    "082843750506040805187358901803560208181028481018201909552818452989b9a9989019892"
    "975090820195509350839250850190849080828437509497506106b49650505050505050565b348"
    "01561020b57600080fd5b5061010c60ff6004351660243560443560643561076d565b3480156102"
    "2f57600080fd5b5061010c60ff60043516602435610818565b34801561024d57600080fd5b50604"
    "0805160206004803580820135601f810184900484028501840190955284845261010c9436949293"
    "6024939284019190819084018382808284375050604080516020601f89358b01803591820183900"
    "4830284018301909452808352979a99988101979196509182019450925082915084018382808284"
    "37509497506108ca9650505050505050565b3480156102e457600080fd5b5061010c73fffffffff"
    "fffffffffffffffffffffffffffffff600435811690602435166109bb565b348015610318576000"
    "80fd5b506040805160206004803580820135601f810184900484028501840190955284845261010"
    "c943694929360249392840191908190840183828082843750949750610a0d965050505050505056"
    "5b34801561037157600080fd5b5061010c73ffffffffffffffffffffffffffffffffffffffff600"
    "43581169060243516610a6b565b7fa95e6e2a182411e7a6f9ed114a85c3761d87f9b8f453d842c7"
    "1235aa64fff99f81604051808060200182810382528381815181526020019150805190602001908"
    "0838360005b838110156103f85781810151838201526020016103e0565b50505050905090810190"
    "601f1680156104255780820380516001836020036101000a031916815260200191505b509250505"
    "060405180910390a150565b600181601181111561044357fe5b1415610477576040517f1e86022f"
    "78f8d04f8e3dfd13a2bdb280403e6632877c0dbee5e4eeb259908a5c90600090a1610524565b600"
    "081601181111561048557fe5b141561049757604051600090a0610524565b604080517f08c379a0"
    "0000000000000000000000000000000000000000000000000000000081526020600482015260266"
    "0248201527f4469646e2774206d6174636820616e7920616c6c6f7761626c65206576656e746044"
    "8201527f20696e64657800000000000000000000000000000000000000000000000000006064820"
    "15290519081900360840190fd5b50565b600585601181111561053557fe5b141561058757604080"
    "51858152602081018590528082018490526060810183905290517ff039d147f23fe975a4254bdf6"
    "b1502b8c79132ae1833986b7ccef2638e73fdf99181900360800190a16105dd565b600b85601181"
    "111561059557fe5b14156104975780827fa30ece802b64cd2b7e57dabf4010aabf5df26d1556977"
    "affb07b98a77ad955b58686604051808381526020018281526020019250505060405180910390a3"
    "5b5050505050565b60038360118111156105f257fe5b14156106385760408051838152602081018"
    "3905281517fdf0cb1dea99afceb3ea698d62e705b736f1345a7eee9eb07e63d1f8f556c1bc59291"
    "81900390910190a16106af565b600983601181111561064657fe5b1415610687576040805183815"
    "2905182917f057bc32826fbe161da1c110afcdcae7c109a8b69149f727fc37a603c60ef94ca9190"
    "81900360200190a26106af565b600883601181111561069557fe5b1415610497576040805183815"
    "29051829181900360200190a15b505050565b816040518082805190602001906020028083836000"
    "5b838110156106e25781810151838201526020016106ca565b50505050905001915050604051809"
    "10390207fdbc4c1d1d2f0d84e58d36ca767ec9ba2ec2f933c055e50e5ccdd57697f7b58b0826040"
    "518080602001828103825283818151815260200191508051906020019060200280838360005b838"
    "1101561075657818101518382015260200161073e565b5050505090500192505050604051809103"
    "90a25050565b600484601181111561077b57fe5b14156107c657604080518481526020810184905"
    "280820183905290517f4a25b279c7c585f25eda9788ac9420ebadae78ca6b206a0e6ab488fd81f5"
    "50629181900360600190a1610812565b600a8460118111156107d457fe5b1415610497576040805"
    "18481529051829184917ff16c999b533366ca5138d78e85da51611089cd05749f098d6c225d4cd4"
    "2ee6ec9181900360200190a35b50505050565b600282601181111561082657fe5b1415610864576"
    "040805182815290517f56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce9"
    "05d49181900360200190a16108c6565b600782601181111561087257fe5b14156108a8576040518"
    "1907ff70fe689e290d8ce2b2a388ac28db36fbb0e16a6d89c6804c461f65a1b40bb1590600090a2"
    "6108c6565b60068260118111156108b657fe5b1415610497576040518190600090a15b5050565b8"
    "16040518082805190602001908083835b602083106108fa5780518252601f199092019160209182"
    "0191016108db565b51815160209384036101000a600019018019909216911617905260408051929"
    "09401829003822081835287518383015287519096507fe77cf33df73da7bc2e253a2dae617e6f15"
    "e4e337eaa462a108903af4643d1b7595508794929350839283019185019080838360005b8381101"
    "561097d578181015183820152602001610965565b50505050905090810190601f1680156109aa57"
    "80820380516001836020036101000a031916815260200191505b509250505060405180910390a25"
    "050565b6040805173ffffffffffffffffffffffffffffffffffffffff8381168252915191841691"
    "7ff922c215689548d72c3d2fe4ea8dafb2a30c43312c9b43fe5d10f713181f991c9181900360200"
    "190a25050565b7f532fd6ea96cfb78bb46e09279a26828b8b493de1a2b8b1ee1face527978a15a5"
    "8160405180806020018281038252838181518152602001915080519060200190808383600083811"
    "0156103f85781810151838201526020016103e0565b6040805173ffffffffffffffffffffffffff"
    "ffffffffffffff80851682528316602082015281517f06029e18f16caae06a69281f35b00ed3fcf"
    "47950e6c99dafa1bdd8c4b93479a0929181900390910190a150505600a165627a7a72305820962b"
    "b0d0c7c052407e6ad0911da133e939baa8783fbd0220169b97b54160a89e0029"
)

CONTRACT_EMITTER_ABI_OLD = [
    {
        "constant": False,
        "inputs": [
            {
                "name": "v",
                "type": "string"
            }
        ],
        "name": "logString",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "name": "which",
                "type": "uint8"
            }
        ],
        "name": "logNoArgs",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "name": "which",
                "type": "uint8"
            },
            {
                "name": "arg0",
                "type": "uint256"
            },
            {
                "name": "arg1",
                "type": "uint256"
            },
            {
                "name": "arg2",
                "type": "uint256"
            },
            {
                "name": "arg3",
                "type": "uint256"
            }
        ],
        "name": "logQuadruple",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "name": "which",
                "type": "uint8"
            },
            {
                "name": "arg0",
                "type": "uint256"
            },
            {
                "name": "arg1",
                "type": "uint256"
            }
        ],
        "name": "logDouble",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "name": "arg0",
                "type": "bytes2[]"
            },
            {
                "name": "arg1",
                "type": "bytes2[]"
            }
        ],
        "name": "logListArgs",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "name": "which",
                "type": "uint8"
            },
            {
                "name": "arg0",
                "type": "uint256"
            },
            {
                "name": "arg1",
                "type": "uint256"
            },
            {
                "name": "arg2",
                "type": "uint256"
            }
        ],
        "name": "logTriple",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "name": "which",
                "type": "uint8"
            },
            {
                "name": "arg0",
                "type": "uint256"
            }
        ],
        "name": "logSingle",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "name": "arg0",
                "type": "string"
            },
            {
                "name": "arg1",
                "type": "string"
            }
        ],
        "name": "logDynamicArgs",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "name": "arg0",
                "type": "address"
            },
            {
                "name": "arg1",
                "type": "address"
            }
        ],
        "name": "logAddressIndexedArgs",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "name": "v",
                "type": "bytes"
            }
        ],
        "name": "logBytes",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "name": "arg0",
                "type": "address"
            },
            {
                "name": "arg1",
                "type": "address"
            }
        ],
        "name": "logAddressNotIndexedArgs",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "anonymous": True,
        "inputs": [],
        "name": "LogAnonymous",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [],
        "name": "LogNoArguments",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "name": "arg0",
                "type": "uint256"
            }
        ],
        "name": "LogSingleArg",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "name": "arg0",
                "type": "uint256"
            },
            {
                "indexed": False,
                "name": "arg1",
                "type": "uint256"
            }
        ],
        "name": "LogDoubleArg",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "name": "arg0",
                "type": "uint256"
            },
            {
                "indexed": False,
                "name": "arg1",
                "type": "uint256"
            },
            {
                "indexed": False,
                "name": "arg2",
                "type": "uint256"
            }
        ],
        "name": "LogTripleArg",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "name": "arg0",
                "type": "uint256"
            },
            {
                "indexed": False,
                "name": "arg1",
                "type": "uint256"
            },
            {
                "indexed": False,
                "name": "arg2",
                "type": "uint256"
            },
            {
                "indexed": False,
                "name": "arg3",
                "type": "uint256"
            }
        ],
        "name": "LogQuadrupleArg",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "name": "v",
                "type": "string"
            }
        ],
        "name": "LogString",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "name": "v",
                "type": "bytes"
            }
        ],
        "name": "LogBytes",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "name": "arg0",
                "type": "uint256"
            }
        ],
        "name": "LogSingleWithIndex",
        "type": "event"
    },
    {
        "anonymous": True,
        "inputs": [
            {
                "indexed": True,
                "name": "arg0",
                "type": "uint256"
            }
        ],
        "name": "LogSingleAnonymous",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "name": "arg0",
                "type": "uint256"
            },
            {
                "indexed": True,
                "name": "arg1",
                "type": "uint256"
            }
        ],
        "name": "LogDoubleWithIndex",
        "type": "event"
    },
    {
        "anonymous": True,
        "inputs": [
            {
                "indexed": False,
                "name": "arg0",
                "type": "uint256"
            },
            {
                "indexed": True,
                "name": "arg1",
                "type": "uint256"
            }
        ],
        "name": "LogDoubleAnonymous",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "name": "arg0",
                "type": "uint256"
            },
            {
                "indexed": True,
                "name": "arg1",
                "type": "uint256"
            },
            {
                "indexed": True,
                "name": "arg2",
                "type": "uint256"
            }
        ],
        "name": "LogTripleWithIndex",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "name": "arg0",
                "type": "uint256"
            },
            {
                "indexed": False,
                "name": "arg1",
                "type": "uint256"
            },
            {
                "indexed": True,
                "name": "arg2",
                "type": "uint256"
            },
            {
                "indexed": True,
                "name": "arg3",
                "type": "uint256"
            }
        ],
        "name": "LogQuadrupleWithIndex",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "name": "arg0",
                "type": "string"
            },
            {
                "indexed": False,
                "name": "arg1",
                "type": "string"
            }
        ],
        "name": "LogDynamicArgs",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "name": "arg0",
                "type": "bytes2[]"
            },
            {
                "indexed": False,
                "name": "arg1",
                "type": "bytes2[]"
            }
        ],
        "name": "LogListArgs",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "name": "arg0",
                "type": "address"
            },
            {
                "indexed": False,
                "name": "arg1",
                "type": "address"
            }
        ],
        "name": "LogAddressIndexed",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "name": "arg0",
                "type": "address"
            },
            {
                "indexed": False,
                "name": "arg1",
                "type": "address"
            }
        ],
        "name": "LogAddressNotIndexed",
        "type": "event"
    }
]


EMITTER_ENUM_OLD = {
    'LogAnonymous': 0,
    'LogNoArguments': 1,
    'LogSingleArg': 2,
    'LogDoubleArg': 3,
    'LogTripleArg': 4,
    'LogQuadrupleArg': 5,
    'LogSingleAnonymous': 6,
    'LogSingleWithIndex': 7,
    'LogDoubleAnonymous': 8,
    'LogDoubleWithIndex': 9,
    'LogTripleWithIndex': 10,
    'LogQuadrupleWithInde': 11,
}
