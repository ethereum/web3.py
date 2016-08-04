import pytest
import json
import textwrap


CONTRACT_CODE = b"0x606060405261022e806100126000396000f360606040523615610074576000357c01000000000000000000000000000000000000000000000000000000009004806316216f391461007657806361bc221a146100995780637cf5dab0146100bc578063a5f3c23b146100e8578063d09de08a1461011d578063dcf537b11461014057610074565b005b610083600480505061016c565b6040518082815260200191505060405180910390f35b6100a6600480505061017f565b6040518082815260200191505060405180910390f35b6100d26004808035906020019091905050610188565b6040518082815260200191505060405180910390f35b61010760048080359060200190919080359060200190919050506101ea565b6040518082815260200191505060405180910390f35b61012a6004805050610201565b6040518082815260200191505060405180910390f35b6101566004808035906020019091905050610217565b6040518082815260200191505060405180910390f35b6000600d9050805080905061017c565b90565b60006000505481565b6000816000600082828250540192505081905550600060005054905080507f3496c3ede4ec3ab3686712aa1c238593ea6a42df83f98a5ec7df9834cfa577c5816040518082815260200191505060405180910390a18090506101e5565b919050565b6000818301905080508090506101fb565b92915050565b600061020d6001610188565b9050610214565b90565b60006007820290508050809050610229565b91905056"


CONTRACT_RUNTIME = b"0x60606040523615610074576000357c01000000000000000000000000000000000000000000000000000000009004806316216f391461007657806361bc221a146100995780637cf5dab0146100bc578063a5f3c23b146100e8578063d09de08a1461011d578063dcf537b11461014057610074565b005b610083600480505061016c565b6040518082815260200191505060405180910390f35b6100a6600480505061017f565b6040518082815260200191505060405180910390f35b6100d26004808035906020019091905050610188565b6040518082815260200191505060405180910390f35b61010760048080359060200190919080359060200190919050506101ea565b6040518082815260200191505060405180910390f35b61012a6004805050610201565b6040518082815260200191505060405180910390f35b6101566004808035906020019091905050610217565b6040518082815260200191505060405180910390f35b6000600d9050805080905061017c565b90565b60006000505481565b6000816000600082828250540192505081905550600060005054905080507f3496c3ede4ec3ab3686712aa1c238593ea6a42df83f98a5ec7df9834cfa577c5816040518082815260200191505060405180910390a18090506101e5565b919050565b6000818301905080508090506101fb565b92915050565b600061020d6001610188565b9050610214565b90565b60006007820290508050809050610229565b91905056"


CONTRACT_SOURCE = textwrap.dedent(("""
    contract Math {
        uint public counter;

        event Increased(uint value);

        function increment() public returns (uint) {
            return increment(1);
        }

        function increment(uint amt) public returns (uint result) {
            counter += amt;
            result = counter;
            Increased(result);
            return result;
        }

        function add(int a, int b) public returns (int result) {
            result = a + b;
            return result;
        }

        function multiply7(int a) public returns (int result) {
            result = a * 7;
            return result;
        }

        function return13() public returns (int result) {
            result = 13;
            return result;
        }
    }
""")).strip()

CONTRACT_ABI = json.loads('[{"constant":false,"inputs":[],"name":"return13","outputs":[{"name":"result","type":"int256"}],"type":"function"},{"constant":true,"inputs":[],"name":"counter","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"amt","type":"uint256"}],"name":"increment","outputs":[{"name":"result","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"a","type":"int256"},{"name":"b","type":"int256"}],"name":"add","outputs":[{"name":"result","type":"int256"}],"type":"function"},{"constant":false,"inputs":[],"name":"increment","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":false,"inputs":[{"name":"a","type":"int256"}],"name":"multiply7","outputs":[{"name":"result","type":"int256"}],"type":"function"},{"anonymous":false,"inputs":[{"indexed":false,"name":"value","type":"uint256"}],"name":"Increased","type":"event"}]')  # NOQA


@pytest.fixture(scope="session")
def MATH_CODE():
    return CONTRACT_CODE


@pytest.fixture(scope="session")
def MATH_RUNTIME():
    return CONTRACT_RUNTIME


@pytest.fixture(scope="session")
def MATH_SOURCE():
    return CONTRACT_SOURCE


@pytest.fixture(scope="session")
def MATH_ABI():
    return CONTRACT_ABI


@pytest.fixture()
def MathContract(web3_tester, MATH_ABI, MATH_CODE, MATH_RUNTIME, MATH_SOURCE):
    return web3_tester.eth.contract(
        abi=MATH_ABI,
        code=MATH_CODE,
        code_runtime=MATH_RUNTIME,
        source=MATH_SOURCE,
    )


CONTRACT_SIMPLE_CONSTRUCTOR_SOURCE = "contract WithNoArgumentConstructor { uint public data; function WithNoArgumentConstructor() { data = 3; }}"
CONTRACT_SIMPLE_CONSTRUCTOR_CODE = b'0x60606040526003600055602c8060156000396000f3606060405260e060020a600035046373d4a13a8114601a575b005b602260005481565b6060908152602090f3'
CONTRACT_SIMPLE_CONSTRUCTOR_RUNTIME = b'0x606060405260e060020a600035046373d4a13a8114601a575b005b602260005481565b6060908152602090f3'
CONTRACT_SIMPLE_CONSTRUCTOR_ABI = json.loads('[{"constant":true,"inputs":[],"name":"data","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"inputs":[],"type":"constructor"}]')


@pytest.fixture(scope="session")
def SIMPLE_CONSTRUCTOR_SOURCE():
    return CONTRACT_SIMPLE_CONSTRUCTOR_SOURCE


@pytest.fixture(scope="session")
def SIMPLE_CONSTRUCTOR_CODE():
    return CONTRACT_SIMPLE_CONSTRUCTOR_CODE


@pytest.fixture(scope="session")
def SIMPLE_CONSTRUCTOR_RUNTIME():
    return CONTRACT_SIMPLE_CONSTRUCTOR_RUNTIME


@pytest.fixture(scope="session")
def SIMPLE_CONSTRUCTOR_ABI():
    return CONTRACT_SIMPLE_CONSTRUCTOR_ABI


@pytest.fixture()
def SimpleConstructorContract(web3_tester,
                              SIMPLE_CONSTRUCTOR_SOURCE,
                              SIMPLE_CONSTRUCTOR_CODE,
                              SIMPLE_CONSTRUCTOR_RUNTIME,
                              SIMPLE_CONSTRUCTOR_ABI):
    return web3_tester.eth.contract(
        abi=SIMPLE_CONSTRUCTOR_ABI,
        code=SIMPLE_CONSTRUCTOR_CODE,
        code_runtime=SIMPLE_CONSTRUCTOR_RUNTIME,
        source=SIMPLE_CONSTRUCTOR_SOURCE,
    )


CONTRACT_WITH_CONSTRUCTOR_ARGUMENTS_SOURCE =  "contract WithConstructorArguments { uint public data_a; bytes32 public data_b; function WithConstructorArguments(uint a, bytes32 b) { data_a = a; data_b = b; }}"

CONTRACT_WITH_CONSTRUCTOR_ARGUMENTS_CODE = b"0x60606040818152806066833960a09052516080516000918255600155603e908190602890396000f3606060405260e060020a600035046388ec134681146024578063d4c46c7614602c575b005b603460005481565b603460015481565b6060908152602090f3"
CONTRACT_WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME = b"0x606060405260e060020a600035046388ec134681146024578063d4c46c7614602c575b005b603460005481565b603460015481565b6060908152602090f3"
CONTRACT_WITH_CONSTRUCTOR_ARGUMENTS_ABI = json.loads('[{"constant":true,"inputs":[],"name":"data_a","outputs":[{"name":"","type":"uint256"}],"type":"function"},{"constant":true,"inputs":[],"name":"data_b","outputs":[{"name":"","type":"bytes32"}],"type":"function"},{"inputs":[{"name":"a","type":"uint256"},{"name":"b","type":"bytes32"}],"type":"constructor"}]')


@pytest.fixture()
def WITH_CONSTRUCTOR_ARGUMENTS_SOURCE():
    return CONTRACT_WITH_CONSTRUCTOR_ARGUMENTS_SOURCE


@pytest.fixture()
def WITH_CONSTRUCTOR_ARGUMENTS_CODE():
    return CONTRACT_WITH_CONSTRUCTOR_ARGUMENTS_CODE


@pytest.fixture()
def WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME():
    return CONTRACT_WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME


@pytest.fixture()
def WITH_CONSTRUCTOR_ARGUMENTS_ABI():
    return CONTRACT_WITH_CONSTRUCTOR_ARGUMENTS_ABI


@pytest.fixture()
def WithConstructorArgumentsContract(web3_tester,
                                     WITH_CONSTRUCTOR_ARGUMENTS_SOURCE,
                                     WITH_CONSTRUCTOR_ARGUMENTS_CODE,
                                     WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME,
                                     WITH_CONSTRUCTOR_ARGUMENTS_ABI):
    return web3_tester.eth.contract(
        abi=WITH_CONSTRUCTOR_ARGUMENTS_ABI,
        code=WITH_CONSTRUCTOR_ARGUMENTS_CODE,
        code_runtime=WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME,
        source=WITH_CONSTRUCTOR_ARGUMENTS_SOURCE,
    )


CONTRACT_WITH_CONSTRUCTOR_ADDRESS_SOURCE = "contract WithAddrArg { address public testAddr; function WithAddrArg(address _testAddr){ testAddr = _testAddr; }}"
CONTRACT_WITH_CONSTRUCTOR_ADDRESS_CODE = b"0x6060604052604051602080607683395060806040525160008054600160a060020a031916821790555060428060346000396000f3606060405260e060020a600035046334664e3a8114601a575b005b603860005473ffffffffffffffffffffffffffffffffffffffff1681565b6060908152602090f3"
CONTRACT_WITH_CONSTRUCTOR_ADDRESS_RUNTIME = b"0x606060405260e060020a600035046334664e3a8114601a575b005b603860005473ffffffffffffffffffffffffffffffffffffffff1681565b6060908152602090f3"
CONTRACT_WITH_CONSTRUCTOR_ADDRESS_ABI = json.loads('[{"constant":true,"inputs":[],"name":"testAddr","outputs":[{"name":"","type":"address"}],"type":"function"},{"inputs":[{"name":"_testAddr","type":"address"}],"type":"constructor"}]')


@pytest.fixture()
def WITH_CONSTRUCTOR_ADDRESS_SOURCE():
    return CONTRACT_WITH_CONSTRUCTOR_ADDRESS_SOURCE


@pytest.fixture()
def WITH_CONSTRUCTOR_ADDRESS_CODE():
    return CONTRACT_WITH_CONSTRUCTOR_ADDRESS_CODE


@pytest.fixture()
def WITH_CONSTRUCTOR_ADDRESS_RUNTIME():
    return CONTRACT_WITH_CONSTRUCTOR_ADDRESS_RUNTIME


@pytest.fixture()
def WITH_CONSTRUCTOR_ADDRESS_ABI():
    return CONTRACT_WITH_CONSTRUCTOR_ADDRESS_ABI


@pytest.fixture()
def WithConstructorAddressArgumentsContract(web3_tester,
                                     WITH_CONSTRUCTOR_ADDRESS_SOURCE,
                                     WITH_CONSTRUCTOR_ADDRESS_CODE,
                                     WITH_CONSTRUCTOR_ADDRESS_RUNTIME,
                                     WITH_CONSTRUCTOR_ADDRESS_ABI):
    return web3_tester.eth.contract(
        abi=WITH_CONSTRUCTOR_ADDRESS_ABI,
        code=WITH_CONSTRUCTOR_ADDRESS_CODE,
        code_runtime=WITH_CONSTRUCTOR_ADDRESS_RUNTIME,
        source=WITH_CONSTRUCTOR_ADDRESS_SOURCE,
    )


STRING_CONTRACT_ABI_DEF = """
    {
        "abi": [
            {
                "constant": false,
                "inputs": [],
                "name": "getValue",
                "outputs": [
                    {
                        "name": "result",
                        "type": "string"
                    }
                ],
                "type": "function"
            },
            {
                "constant": true,
                "inputs": [],
                "name": "constString",
                "outputs": [
                    {
                        "name": "",
                        "type": "string"
                    }
                ],
                "type": "function"
            },
            {
                "constant": true,
                "inputs": [],
                "name": "value",
                "outputs": [
                    {
                        "name": "",
                        "type": "string"
                    }
                ],
                "type": "function"
            },
            {
                "constant": false,
                "inputs": [
                    {
                        "name": "_value",
                        "type": "string"
                    }
                ],
                "name": "setValue",
                "outputs": [],
                "type": "function"
            },
            {
                "inputs": [
                    {
                        "name": "_value",
                        "type": "string"
                    }
                ],
                "type": "constructor"
            }
        ],
        "code": "0x60a0604052600f6060527f546f686f6c616d7069c385c384c39600000000000000000000000000000000006080526001805460008290527f546f686f6c616d7069c385c384c396000000000000000000000000000000001e82556100b4907fb10e2d527612073b26eecdfd717e6a320cf44b4afac2b0732d9fcbe2b7fa0cf66020600283861615610100026000190190931692909204601f01919091048101905b8082111561012c57600081556001016100a0565b505060405161047e38038061047e833981016040528080518201919060200150508060006000509080519060200190828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061013057805160ff19168380011785555b506101609291506100a0565b5090565b82800160010185558215610120579182015b82811115610120578251826000505591602001919060010190610142565b50505061030d806101716000396000f3606060405260e060020a600035046320965255811461003c5780632f3556771461009f5780633fa4f245146100fb57806393a0935214610158575b005b6101fe600060608181528154602060026001831615610100026000190190921691909104601f810182900490910260a0908101604052608082815292939190828280156102975780601f1061026c57610100808354040283529160200191610297565b6101fe600180546020600282841615610100026000190190921691909104601f810182900490910260809081016040526060828152929190828280156102cc5780601f106102a1576101008083540402835291602001916102cc565b6101fe60008054602060026001831615610100026000190190921691909104601f810182900490910260809081016040526060828152929190828280156102cc5780601f106102a1576101008083540402835291602001916102cc565b60206004803580820135601f81018490049093026080908101604052606084815261003a946024939192918401918190838280828437509496505050505050508060006000509080519060200190828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106102d457805160ff19168380011785555b506103049291505b80821115610309578381556001016101eb565b60405180806020018281038252838181518152602001915080519060200190808383829060006004602084601f0104600f02600301f150905090810190601f16801561025e5780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b820191906000526020600020905b81548152906001019060200180831161027a57829003601f168201915b5050505050905090565b820191906000526020600020905b8154815290600101906020018083116102af57829003601f168201915b505050505081565b828001600101855582156101e3579182015b828111156101e35782518260005055916020019190600101906102e6565b505050565b509056",
        "code_runtime": "0x606060405260e060020a600035046320965255811461003c5780632f3556771461009f5780633fa4f245146100fb57806393a0935214610158575b005b6101fe600060608181528154602060026001831615610100026000190190921691909104601f810182900490910260a0908101604052608082815292939190828280156102975780601f1061026c57610100808354040283529160200191610297565b6101fe600180546020600282841615610100026000190190921691909104601f810182900490910260809081016040526060828152929190828280156102cc5780601f106102a1576101008083540402835291602001916102cc565b6101fe60008054602060026001831615610100026000190190921691909104601f810182900490910260809081016040526060828152929190828280156102cc5780601f106102a1576101008083540402835291602001916102cc565b60206004803580820135601f81018490049093026080908101604052606084815261003a946024939192918401918190838280828437509496505050505050508060006000509080519060200190828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106102d457805160ff19168380011785555b506103049291505b80821115610309578381556001016101eb565b60405180806020018281038252838181518152602001915080519060200190808383829060006004602084601f0104600f02600301f150905090810190601f16801561025e5780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b820191906000526020600020905b81548152906001019060200180831161027a57829003601f168201915b5050505050905090565b820191906000526020600020905b8154815290600101906020018083116102af57829003601f168201915b505050505081565b828001600101855582156101e3579182015b828111156101e35782518260005055916020019190600101906102e6565b505050565b509056",
        "meta": {
            "compilerVersion": "0.3.5-371690f0",
            "language": "Solidity",
            "languageVersion": "0"
        },
        "source": null
    }
"""

@pytest.fixture(scope="session")
def string_contract_abi_def():
    return json.loads(STRING_CONTRACT_ABI_DEF)


@pytest.fixture()
def StringContract(web3_tester, string_contract_abi_def):
    return web3_tester.eth.contract(
        abi=string_contract_abi_def["abi"],
        code=string_contract_abi_def["code"],
        code_runtime=string_contract_abi_def["code_runtime"],
        source=string_contract_abi_def["source"],
    )


CONTRACT_EMITTER_SOURCE = textwrap.dedent(("""
contract Emitter {
    event LogAnonymous() anonymous;
    event LogNoArguments();
    event LogSingleArg(uint arg0);
    event LogDoubleArg(uint arg0, uint arg1);
    event LogTripleArg(uint arg0, uint arg1, uint arg2);
    event LogQuadrupleArg(uint arg0, uint arg1, uint arg2, uint arg3);

    // Indexed
    event LogSingleWithIndex(uint indexed arg0);
    event LogDoubleWithIndex(uint arg0, uint indexed arg1);
    event LogTripleWithIndex(uint arg0, uint indexed arg1, uint indexed arg2);
    event LogQuadrupleWithIndex(uint arg0, uint arg1, uint indexed arg2, uint indexed arg3);

    enum WhichEvent {
        LogAnonymous,
        LogNoArguments,
        LogSingleArg,
        LogDoubleArg,
        LogTripleArg,
        LogQuadrupleArg,
        LogSingleWithIndex,
        LogDoubleWithIndex,
        LogTripleWithIndex,
        LogQuadrupleWithIndex
    }

    function logNoArgs(WhichEvent which) public {
        if (which == WhichEvent.LogNoArguments) LogNoArguments();
        else if (which == WhichEvent.LogAnonymous) LogAnonymous();
        else throw;
    }

    function logSingle(WhichEvent which, uint arg0) public {
        if (which == WhichEvent.LogSingleArg) LogSingleArg(arg0);
        else if (which == WhichEvent.LogSingleWithIndex) LogSingleWithIndex(arg0);
        else throw;
    }

    function logDouble(WhichEvent which, uint arg0, uint arg1) public {
        if (which == WhichEvent.LogDoubleArg) LogDoubleArg(arg0, arg1);
        else if (which == WhichEvent.LogDoubleWithIndex) LogDoubleWithIndex(arg0, arg1);
        else throw;
    }

    function logTriple(WhichEvent which, uint arg0, uint arg1, uint arg2) public {
        if (which == WhichEvent.LogTripleArg) LogTripleArg(arg0, arg1, arg2);
        else if (which == WhichEvent.LogTripleWithIndex) LogTripleWithIndex(arg0, arg1, arg2);
        else throw;
    }

    function logQuadruple(WhichEvent which, uint arg0, uint arg1, uint arg2, uint arg3) public {
        if (which == WhichEvent.LogQuadrupleArg) LogQuadrupleArg(arg0, arg1, arg2, arg3);
        else if (which == WhichEvent.LogQuadrupleWithIndex) LogQuadrupleWithIndex(arg0, arg1, arg2, arg3);
        else throw;
    }
}
"""))

CONTRACT_EMITTER_CODE = "0x60606040526102c0806100126000396000f3606060405260e060020a600035046317c0c180811461004757806320f0256e1461008057806390b41d8b146100da5780639c37705314610125578063aa6fd82214610177575b005b61004560043560018114156101b9577f1e86022f78f8d04f8e3dfd13a2bdb280403e6632877c0dbee5e4eeb259908a5c60006060a15b50565b61004560043560243560443560643560843560058514156101d1576060848152608084815260a084905260c08390527ff039d147f23fe975a4254bdf6b1502b8c79132ae1833986b7ccef2638e73fdf991a15b5050505050565b610045600435602435604435600383141561021357606082815260808290527fdf0cb1dea99afceb3ea698d62e705b736f1345a7eee9eb07e63d1f8f556c1bc590604090a15b505050565b610045600435602435604435606435600484141561024e576060838152608083905260a08290527f4a25b279c7c585f25eda9788ac9420ebadae78ca6b206a0e6ab488fd81f550629080a15b50505050565b610045600435602435600282141561028b5760608181527f56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d490602090a15b5050565b60008114156101cc5760006060a061007d565b610002565b60098514156101cc5760608481526080849052819083907fa30ece802b64cd2b7e57dabf4010aabf5df26d1556977affb07b98a77ad955b590604090a36100d3565b60078314156101cc57606082815281907f057bc32826fbe161da1c110afcdcae7c109a8b69149f727fc37a603c60ef94ca90602090a2610120565b60088414156101cc576060838152819083907ff16c999b533366ca5138d78e85da51611089cd05749f098d6c225d4cd42ee6ec90602090a3610171565b60068214156101cc57807ff70fe689e290d8ce2b2a388ac28db36fbb0e16a6d89c6804c461f65a1b40bb1560006060a26101b556"

CONTRACT_EMITTER_RUNTIME = "0x606060405260e060020a600035046317c0c180811461004757806320f0256e1461008057806390b41d8b146100da5780639c37705314610125578063aa6fd82214610177575b005b61004560043560018114156101b9577f1e86022f78f8d04f8e3dfd13a2bdb280403e6632877c0dbee5e4eeb259908a5c60006060a15b50565b61004560043560243560443560643560843560058514156101d1576060848152608084815260a084905260c08390527ff039d147f23fe975a4254bdf6b1502b8c79132ae1833986b7ccef2638e73fdf991a15b5050505050565b610045600435602435604435600383141561021357606082815260808290527fdf0cb1dea99afceb3ea698d62e705b736f1345a7eee9eb07e63d1f8f556c1bc590604090a15b505050565b610045600435602435604435606435600484141561024e576060838152608083905260a08290527f4a25b279c7c585f25eda9788ac9420ebadae78ca6b206a0e6ab488fd81f550629080a15b50505050565b610045600435602435600282141561028b5760608181527f56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d490602090a15b5050565b60008114156101cc5760006060a061007d565b610002565b60098514156101cc5760608481526080849052819083907fa30ece802b64cd2b7e57dabf4010aabf5df26d1556977affb07b98a77ad955b590604090a36100d3565b60078314156101cc57606082815281907f057bc32826fbe161da1c110afcdcae7c109a8b69149f727fc37a603c60ef94ca90602090a2610120565b60088414156101cc576060838152819083907ff16c999b533366ca5138d78e85da51611089cd05749f098d6c225d4cd42ee6ec90602090a3610171565b60068214156101cc57807ff70fe689e290d8ce2b2a388ac28db36fbb0e16a6d89c6804c461f65a1b40bb1560006060a26101b556"

CONTRACT_EMITTER_ABI = json.loads('[{"constant":false,"inputs":[{"name":"which","type":"uint8"}],"name":"logNoArgs","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"which","type":"uint8"},{"name":"arg0","type":"uint256"},{"name":"arg1","type":"uint256"},{"name":"arg2","type":"uint256"},{"name":"arg3","type":"uint256"}],"name":"logQuadruple","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"which","type":"uint8"},{"name":"arg0","type":"uint256"},{"name":"arg1","type":"uint256"}],"name":"logDouble","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"which","type":"uint8"},{"name":"arg0","type":"uint256"},{"name":"arg1","type":"uint256"},{"name":"arg2","type":"uint256"}],"name":"logTriple","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"which","type":"uint8"},{"name":"arg0","type":"uint256"}],"name":"logSingle","outputs":[],"type":"function"},{"anonymous":true,"inputs":[],"name":"LogAnonymous","type":"event"},{"anonymous":false,"inputs":[],"name":"LogNoArguments","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"arg0","type":"uint256"}],"name":"LogSingleArg","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"arg0","type":"uint256"},{"indexed":false,"name":"arg1","type":"uint256"}],"name":"LogDoubleArg","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"arg0","type":"uint256"},{"indexed":false,"name":"arg1","type":"uint256"},{"indexed":false,"name":"arg2","type":"uint256"}],"name":"LogTripleArg","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"arg0","type":"uint256"},{"indexed":false,"name":"arg1","type":"uint256"},{"indexed":false,"name":"arg2","type":"uint256"},{"indexed":false,"name":"arg3","type":"uint256"}],"name":"LogQuadrupleArg","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"arg0","type":"uint256"}],"name":"LogSingleWithIndex","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"arg0","type":"uint256"},{"indexed":true,"name":"arg1","type":"uint256"}],"name":"LogDoubleWithIndex","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"arg0","type":"uint256"},{"indexed":true,"name":"arg1","type":"uint256"},{"indexed":true,"name":"arg2","type":"uint256"}],"name":"LogTripleWithIndex","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"arg0","type":"uint256"},{"indexed":false,"name":"arg1","type":"uint256"},{"indexed":true,"name":"arg2","type":"uint256"},{"indexed":true,"name":"arg3","type":"uint256"}],"name":"LogQuadrupleWithIndex","type":"event"}]')


@pytest.fixture()
def EMITTER_SOURCE():
    return CONTRACT_EMITTER_SOURCE


@pytest.fixture()
def EMITTER_CODE():
    return CONTRACT_EMITTER_CODE


@pytest.fixture()
def EMITTER_RUNTIME():
    return CONTRACT_EMITTER_RUNTIME


@pytest.fixture()
def EMITTER_ABI():
    return CONTRACT_EMITTER_ABI


@pytest.fixture()
def EmitterContract(web3_tester,
                    EMITTER_SOURCE,
                    EMITTER_CODE,
                    EMITTER_RUNTIME,
                    EMITTER_ABI):
    return web3_tester.eth.contract(
        abi=EMITTER_ABI,
        code=EMITTER_CODE,
        code_runtime=EMITTER_RUNTIME,
        source=EMITTER_SOURCE,
    )
