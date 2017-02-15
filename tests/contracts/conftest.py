import pytest
import json
import textwrap

from eth_utils import (
    encode_hex,
    event_signature_to_log_topic,
)


CONTRACT_CODE = "0x606060405261022e806100126000396000f360606040523615610074576000357c01000000000000000000000000000000000000000000000000000000009004806316216f391461007657806361bc221a146100995780637cf5dab0146100bc578063a5f3c23b146100e8578063d09de08a1461011d578063dcf537b11461014057610074565b005b610083600480505061016c565b6040518082815260200191505060405180910390f35b6100a6600480505061017f565b6040518082815260200191505060405180910390f35b6100d26004808035906020019091905050610188565b6040518082815260200191505060405180910390f35b61010760048080359060200190919080359060200190919050506101ea565b6040518082815260200191505060405180910390f35b61012a6004805050610201565b6040518082815260200191505060405180910390f35b6101566004808035906020019091905050610217565b6040518082815260200191505060405180910390f35b6000600d9050805080905061017c565b90565b60006000505481565b6000816000600082828250540192505081905550600060005054905080507f3496c3ede4ec3ab3686712aa1c238593ea6a42df83f98a5ec7df9834cfa577c5816040518082815260200191505060405180910390a18090506101e5565b919050565b6000818301905080508090506101fb565b92915050565b600061020d6001610188565b9050610214565b90565b60006007820290508050809050610229565b91905056"


CONTRACT_RUNTIME = "0x60606040523615610074576000357c01000000000000000000000000000000000000000000000000000000009004806316216f391461007657806361bc221a146100995780637cf5dab0146100bc578063a5f3c23b146100e8578063d09de08a1461011d578063dcf537b11461014057610074565b005b610083600480505061016c565b6040518082815260200191505060405180910390f35b6100a6600480505061017f565b6040518082815260200191505060405180910390f35b6100d26004808035906020019091905050610188565b6040518082815260200191505060405180910390f35b61010760048080359060200190919080359060200190919050506101ea565b6040518082815260200191505060405180910390f35b61012a6004805050610201565b6040518082815260200191505060405180910390f35b6101566004808035906020019091905050610217565b6040518082815260200191505060405180910390f35b6000600d9050805080905061017c565b90565b60006000505481565b6000816000600082828250540192505081905550600060005054905080507f3496c3ede4ec3ab3686712aa1c238593ea6a42df83f98a5ec7df9834cfa577c5816040518082815260200191505060405180910390a18090506101e5565b919050565b6000818301905080508090506101fb565b92915050565b600061020d6001610188565b9050610214565b90565b60006007820290508050809050610229565b91905056"


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
def MathContract(web3, MATH_ABI, MATH_CODE, MATH_RUNTIME, MATH_SOURCE):
    return web3.eth.contract(
        abi=MATH_ABI,
        bytecode=MATH_CODE,
        bytecode_runtime=MATH_RUNTIME,
        source=MATH_SOURCE,
    )


CONTRACT_SIMPLE_CONSTRUCTOR_SOURCE = "contract WithNoArgumentConstructor { uint public data; function WithNoArgumentConstructor() { data = 3; }}"
CONTRACT_SIMPLE_CONSTRUCTOR_CODE = '0x60606040526003600055602c8060156000396000f3606060405260e060020a600035046373d4a13a8114601a575b005b602260005481565b6060908152602090f3'
CONTRACT_SIMPLE_CONSTRUCTOR_RUNTIME = '0x606060405260e060020a600035046373d4a13a8114601a575b005b602260005481565b6060908152602090f3'
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
def SimpleConstructorContract(web3,
                              SIMPLE_CONSTRUCTOR_SOURCE,
                              SIMPLE_CONSTRUCTOR_CODE,
                              SIMPLE_CONSTRUCTOR_RUNTIME,
                              SIMPLE_CONSTRUCTOR_ABI):
    return web3.eth.contract(
        abi=SIMPLE_CONSTRUCTOR_ABI,
        bytecode=SIMPLE_CONSTRUCTOR_CODE,
        bytecode_runtime=SIMPLE_CONSTRUCTOR_RUNTIME,
        source=SIMPLE_CONSTRUCTOR_SOURCE,
    )


CONTRACT_WITH_CONSTRUCTOR_ARGUMENTS_SOURCE =  "contract WithConstructorArguments { uint public data_a; bytes32 public data_b; function WithConstructorArguments(uint a, bytes32 b) { data_a = a; data_b = b; }}"

CONTRACT_WITH_CONSTRUCTOR_ARGUMENTS_CODE = "0x60606040818152806066833960a09052516080516000918255600155603e908190602890396000f3606060405260e060020a600035046388ec134681146024578063d4c46c7614602c575b005b603460005481565b603460015481565b6060908152602090f3"
CONTRACT_WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME = "0x606060405260e060020a600035046388ec134681146024578063d4c46c7614602c575b005b603460005481565b603460015481565b6060908152602090f3"
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
def WithConstructorArgumentsContract(web3,
                                     WITH_CONSTRUCTOR_ARGUMENTS_SOURCE,
                                     WITH_CONSTRUCTOR_ARGUMENTS_CODE,
                                     WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME,
                                     WITH_CONSTRUCTOR_ARGUMENTS_ABI):
    return web3.eth.contract(
        abi=WITH_CONSTRUCTOR_ARGUMENTS_ABI,
        bytecode=WITH_CONSTRUCTOR_ARGUMENTS_CODE,
        bytecode_runtime=WITH_CONSTRUCTOR_ARGUMENTS_RUNTIME,
        source=WITH_CONSTRUCTOR_ARGUMENTS_SOURCE,
    )


CONTRACT_WITH_CONSTRUCTOR_ADDRESS_SOURCE = "contract WithAddrArg { address public testAddr; function WithAddrArg(address _testAddr){ testAddr = _testAddr; }}"
CONTRACT_WITH_CONSTRUCTOR_ADDRESS_CODE = "0x6060604052604051602080607683395060806040525160008054600160a060020a031916821790555060428060346000396000f3606060405260e060020a600035046334664e3a8114601a575b005b603860005473ffffffffffffffffffffffffffffffffffffffff1681565b6060908152602090f3"
CONTRACT_WITH_CONSTRUCTOR_ADDRESS_RUNTIME = "0x606060405260e060020a600035046334664e3a8114601a575b005b603860005473ffffffffffffffffffffffffffffffffffffffff1681565b6060908152602090f3"
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
def WithConstructorAddressArgumentsContract(web3,
                                            WITH_CONSTRUCTOR_ADDRESS_SOURCE,
                                            WITH_CONSTRUCTOR_ADDRESS_CODE,
                                            WITH_CONSTRUCTOR_ADDRESS_RUNTIME,
                                            WITH_CONSTRUCTOR_ADDRESS_ABI):
    return web3.eth.contract(
        abi=WITH_CONSTRUCTOR_ADDRESS_ABI,
        bytecode=WITH_CONSTRUCTOR_ADDRESS_CODE,
        bytecode_runtime=WITH_CONSTRUCTOR_ADDRESS_RUNTIME,
        source=WITH_CONSTRUCTOR_ADDRESS_SOURCE,
    )


CONTRACT_STRING_SOURCE = textwrap.dedent(("""
contract StringContract {
    string constant c_value = '\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff';

    function constValue() public returns (string) {
        return c_value;
    }

    string public value;

    function StringContract(string _value) {
        value = _value;
    }

    function setValue(string _value) public {
        value = _value;
    }

    function getValue() public returns (string) {
        return value;
    }
}
"""))

CONTRACT_STRING_CODE = "0x6060604052604051610496380380610496833981016040528051018060006000509080519060200190828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f10608d57805160ff19168380011785555b50607c9291505b8082111560ba57838155600101606b565b5050506103d8806100be6000396000f35b828001600101855582156064579182015b828111156064578251826000505591602001919060010190609e565b509056606060405260e060020a600035046320965255811461003c57806330de3cee1461009f5780633fa4f245146100c457806393a0935214610121575b005b6101c7600060608181528154602060026001831615610100026000190190921691909104601f810182900490910260a0908101604052608082815292939190828280156102605780601f1061023557610100808354040283529160200191610260565b6101c7600060609081526101a06040526101006080818152906102d860a03990505b90565b6101c760008054602060026001831615610100026000190190921691909104601f810182900490910260809081016040526060828152929190828280156102975780601f1061026c57610100808354040283529160200191610297565b60206004803580820135601f81018490049093026080908101604052606084815261003a946024939192918401918190838280828437509496505050505050508060006000509080519060200190828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061029f57805160ff19168380011785555b506102cf9291505b808211156102d4578381556001016101b4565b60405180806020018281038252838181518152602001915080519060200190808383829060006004602084601f0104600f02600301f150905090810190601f1680156102275780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b820191906000526020600020905b81548152906001019060200180831161024357829003601f168201915b505050505090506100c1565b820191906000526020600020905b81548152906001019060200180831161027a57829003601f168201915b505050505081565b828001600101855582156101ac579182015b828111156101ac5782518260005055916020019190600101906102b1565b505050565b509056000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f303132333435363738393a3b3c3d3e3f404142434445464748494a4b4c4d4e4f505152535455565758595a5b5c5d5e5f606162636465666768696a6b6c6d6e6f707172737475767778797a7b7c7d7e7f808182838485868788898a8b8c8d8e8f909192939495969798999a9b9c9d9e9fa0a1a2a3a4a5a6a7a8a9aaabacadaeafb0b1b2b3b4b5b6b7b8b9babbbcbdbebfc0c1c2c3c4c5c6c7c8c9cacbcccdcecfd0d1d2d3d4d5d6d7d8d9dadbdcdddedfe0e1e2e3e4e5e6e7e8e9eaebecedeeeff0f1f2f3f4f5f6f7f8f9fafbfcfdfeff"

CONTRACT_STRING_RUNTIME = "0x606060405260e060020a600035046320965255811461003c57806330de3cee1461009f5780633fa4f245146100c457806393a0935214610121575b005b6101c7600060608181528154602060026001831615610100026000190190921691909104601f810182900490910260a0908101604052608082815292939190828280156102605780601f1061023557610100808354040283529160200191610260565b6101c7600060609081526101a06040526101006080818152906102d860a03990505b90565b6101c760008054602060026001831615610100026000190190921691909104601f810182900490910260809081016040526060828152929190828280156102975780601f1061026c57610100808354040283529160200191610297565b60206004803580820135601f81018490049093026080908101604052606084815261003a946024939192918401918190838280828437509496505050505050508060006000509080519060200190828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061029f57805160ff19168380011785555b506102cf9291505b808211156102d4578381556001016101b4565b60405180806020018281038252838181518152602001915080519060200190808383829060006004602084601f0104600f02600301f150905090810190601f1680156102275780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b820191906000526020600020905b81548152906001019060200180831161024357829003601f168201915b505050505090506100c1565b820191906000526020600020905b81548152906001019060200180831161027a57829003601f168201915b505050505081565b828001600101855582156101ac579182015b828111156101ac5782518260005055916020019190600101906102b1565b505050565b509056000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f303132333435363738393a3b3c3d3e3f404142434445464748494a4b4c4d4e4f505152535455565758595a5b5c5d5e5f606162636465666768696a6b6c6d6e6f707172737475767778797a7b7c7d7e7f808182838485868788898a8b8c8d8e8f909192939495969798999a9b9c9d9e9fa0a1a2a3a4a5a6a7a8a9aaabacadaeafb0b1b2b3b4b5b6b7b8b9babbbcbdbebfc0c1c2c3c4c5c6c7c8c9cacbcccdcecfd0d1d2d3d4d5d6d7d8d9dadbdcdddedfe0e1e2e3e4e5e6e7e8e9eaebecedeeeff0f1f2f3f4f5f6f7f8f9fafbfcfdfeff"

CONTRACT_STRING_ABI = json.loads('[{"constant":false,"inputs":[],"name":"getValue","outputs":[{"name":"","type":"string"}],"type":"function"},{"constant":false,"inputs":[],"name":"constValue","outputs":[{"name":"","type":"string"}],"type":"function"},{"constant":true,"inputs":[],"name":"value","outputs":[{"name":"","type":"string"}],"type":"function"},{"constant":false,"inputs":[{"name":"_value","type":"string"}],"name":"setValue","outputs":[],"type":"function"},{"inputs":[{"name":"_value","type":"string"}],"type":"constructor"}]')


@pytest.fixture()
def STRING_SOURCE():
    return CONTRACT_STRING_SOURCE


@pytest.fixture()
def STRING_CODE():
    return CONTRACT_STRING_CODE


@pytest.fixture()
def STRING_RUNTIME():
    return CONTRACT_STRING_RUNTIME


@pytest.fixture()
def STRING_ABI():
    return CONTRACT_STRING_ABI


@pytest.fixture()
def STRING_CONTRACT(STRING_SOURCE, STRING_CODE, STRING_RUNTIME, STRING_ABI):
    return {
        'bytecode': STRING_CODE,
        'bytecode_runtime': STRING_RUNTIME,
        'abi': STRING_ABI,
        'source': STRING_SOURCE,
    }

@pytest.fixture()
def StringContract(web3, STRING_CONTRACT):
    return web3.eth.contract(**STRING_CONTRACT)


CONTRACT_EMITTER_SOURCE = textwrap.dedent(("""
contract Emitter {
    event LogAnonymous() anonymous;
    event LogNoArguments();
    event LogSingleArg(uint arg0);
    event LogDoubleArg(uint arg0, uint arg1);
    event LogTripleArg(uint arg0, uint arg1, uint arg2);
    event LogQuadrupleArg(uint arg0, uint arg1, uint arg2, uint arg3);

    // Indexed
    event LogSingleAnonymous(uint indexed arg0) anonymous;
    event LogSingleWithIndex(uint indexed arg0);
    event LogDoubleAnonymous(uint arg0, uint indexed arg1) anonymous;
    event LogDoubleWithIndex(uint arg0, uint indexed arg1);
    event LogTripleWithIndex(uint arg0, uint indexed arg1, uint indexed arg2);
    event LogQuadrupleWithIndex(uint arg0, uint arg1, uint indexed arg2, uint indexed arg3);
    event LogDynamicArgs(string indexed arg0, string arg1);

    // Bytes and String
    event LogBytes(bytes v);
    event LogString(string v);

    enum WhichEvent {
        LogAnonymous,
        LogNoArguments,
        LogSingleArg,
        LogDoubleArg,
        LogTripleArg,
        LogQuadrupleArg,
        LogSingleAnonymous,
        LogSingleWithIndex,
        LogDoubleAnonymous,
        LogDoubleWithIndex,
        LogTripleWithIndex,
        LogQuadrupleWithIndex
    }

    function logBytes(bytes v) {
        LogBytes(v);
    }

    function logString(string v) {
        LogString(v);
    }

    function logNoArgs(WhichEvent which) public {
        if (which == WhichEvent.LogNoArguments) LogNoArguments();
        else if (which == WhichEvent.LogAnonymous) LogAnonymous();
        else throw;
    }

    function logSingle(WhichEvent which, uint arg0) public {
        if (which == WhichEvent.LogSingleArg) LogSingleArg(arg0);
        else if (which == WhichEvent.LogSingleWithIndex) LogSingleWithIndex(arg0);
        else if (which == WhichEvent.LogSingleAnonymous) LogSingleAnonymous(arg0);
        else throw;
    }

    function logDouble(WhichEvent which, uint arg0, uint arg1) public {
        if (which == WhichEvent.LogDoubleArg) LogDoubleArg(arg0, arg1);
        else if (which == WhichEvent.LogDoubleWithIndex) LogDoubleWithIndex(arg0, arg1);
        else if (which == WhichEvent.LogDoubleAnonymous) LogDoubleAnonymous(arg0, arg1);
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

    function logDynamicArgs(string arg0, string arg1) public {
        LogDynamicArgs(arg0, arg1);
    }
}
"""))

CONTRACT_EMITTER_CODE = "0x606060405234610000575b610772806100186000396000f36060604052361561006c5760e060020a60003504630bb563d6811461007157806317c0c180146100c657806320f0256e146100d857806390b41d8b146100f65780639c3770531461010e578063aa6fd82214610129578063acabb9ed1461013e578063e17bf956146101d0575b610000565b34610000576100c4600480803590602001908201803590602001908080601f0160208091040260200160405190810160405280939291908181526020018383808284375094965061022595505050505050565b005b34610000576100c46004356102b8565b005b34610000576100c460043560243560443560643560843561031e565b005b34610000576100c46004356024356044356103e0565b005b34610000576100c46004356024356044356064356104b3565b005b34610000576100c4600435602435610563565b005b34610000576100c4600480803590602001908201803590602001908080601f0160208091040260200160405190810160405280939291908181526020018383808284375050604080516020601f89358b0180359182018390048302840183019094528083529799988101979196509182019450925082915084018382808284375094965061061895505050505050565b005b34610000576100c4600480803590602001908201803590602001908080601f016020809104026020016040519081016040528093929190818152602001838380828437509496506106df95505050505050565b005b7fa95e6e2a182411e7a6f9ed114a85c3761d87f9b8f453d842c71235aa64fff99f8160405180806020018281038252838181518152602001915080519060200190808383829060006004602084601f0104600302600f01f150905090810190601f1680156102a75780820380516001836020036101000a031916815260200191505b509250505060405180910390a15b50565b600181600b81116100005714156102f7576040517f1e86022f78f8d04f8e3dfd13a2bdb280403e6632877c0dbee5e4eeb259908a5c90600090a16102b5565b600081600b811161000057141561006c57604051600090a06102b5565b610000565b5b5b50565b600585600b811161000057141561037b5760408051858152602081018590528082018490526060810183905290517ff039d147f23fe975a4254bdf6b1502b8c79132ae1833986b7ccef2638e73fdf99181900360800190a16103d7565b600b85600b811161000057141561006c5780827fa30ece802b64cd2b7e57dabf4010aabf5df26d1556977affb07b98a77ad955b58686604051808381526020018281526020019250505060405180910390a36103d7565b610000565b5b5b5050505050565b600383600b811161000057141561043157604080518381526020810183905281517fdf0cb1dea99afceb3ea698d62e705b736f1345a7eee9eb07e63d1f8f556c1bc5929181900390910190a16104ab565b600983600b811161000057141561047d5760408051838152905182917f057bc32826fbe161da1c110afcdcae7c109a8b69149f727fc37a603c60ef94ca919081900360200190a26104ab565b600883600b811161000057141561006c57604080518381529051829181900360200190a16104ab565b610000565b5b5b5b505050565b600484600b811161000057141561050957604080518481526020810184905280820183905290517f4a25b279c7c585f25eda9788ac9420ebadae78ca6b206a0e6ab488fd81f550629181900360600190a161055b565b600a84600b811161000057141561006c57604080518481529051829184917ff16c999b533366ca5138d78e85da51611089cd05749f098d6c225d4cd42ee6ec9181900360200190a361055b565b610000565b5b5b50505050565b600282600b81116100005714156105ac576040805182815290517f56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d49181900360200190a1610611565b600782600b81116100005714156105ed5760405181907ff70fe689e290d8ce2b2a388ac28db36fbb0e16a6d89c6804c461f65a1b40bb1590600090a2610611565b600682600b811161000057141561006c576040518190600090a1610611565b610000565b5b5b5b5050565b81604051808280519060200190808383829060006004602084601f0104600302600f01f15090500191505060405180910390207fe77cf33df73da7bc2e253a2dae617e6f15e4e337eaa462a108903af4643d1b758260405180806020018281038252838181518152602001915080519060200190808383829060006004602084601f0104600302600f01f150905090810190601f1680156106cd5780820380516001836020036101000a031916815260200191505b509250505060405180910390a25b5050565b7f532fd6ea96cfb78bb46e09279a26828b8b493de1a2b8b1ee1face527978a15a58160405180806020018281038252838181518152602001915080519060200190808383829060006004602084601f0104600302600f01f150905090810190601f1680156102a75780820380516001836020036101000a031916815260200191505b509250505060405180910390a15b5056"

CONTRACT_EMITTER_RUNTIME = "0x6060604052361561006c5760e060020a60003504630bb563d6811461007157806317c0c180146100c657806320f0256e146100d857806390b41d8b146100f65780639c3770531461010e578063aa6fd82214610129578063acabb9ed1461013e578063e17bf956146101d0575b610000565b34610000576100c4600480803590602001908201803590602001908080601f0160208091040260200160405190810160405280939291908181526020018383808284375094965061022595505050505050565b005b34610000576100c46004356102b8565b005b34610000576100c460043560243560443560643560843561031e565b005b34610000576100c46004356024356044356103e0565b005b34610000576100c46004356024356044356064356104b3565b005b34610000576100c4600435602435610563565b005b34610000576100c4600480803590602001908201803590602001908080601f0160208091040260200160405190810160405280939291908181526020018383808284375050604080516020601f89358b0180359182018390048302840183019094528083529799988101979196509182019450925082915084018382808284375094965061061895505050505050565b005b34610000576100c4600480803590602001908201803590602001908080601f016020809104026020016040519081016040528093929190818152602001838380828437509496506106df95505050505050565b005b7fa95e6e2a182411e7a6f9ed114a85c3761d87f9b8f453d842c71235aa64fff99f8160405180806020018281038252838181518152602001915080519060200190808383829060006004602084601f0104600302600f01f150905090810190601f1680156102a75780820380516001836020036101000a031916815260200191505b509250505060405180910390a15b50565b600181600b81116100005714156102f7576040517f1e86022f78f8d04f8e3dfd13a2bdb280403e6632877c0dbee5e4eeb259908a5c90600090a16102b5565b600081600b811161000057141561006c57604051600090a06102b5565b610000565b5b5b50565b600585600b811161000057141561037b5760408051858152602081018590528082018490526060810183905290517ff039d147f23fe975a4254bdf6b1502b8c79132ae1833986b7ccef2638e73fdf99181900360800190a16103d7565b600b85600b811161000057141561006c5780827fa30ece802b64cd2b7e57dabf4010aabf5df26d1556977affb07b98a77ad955b58686604051808381526020018281526020019250505060405180910390a36103d7565b610000565b5b5b5050505050565b600383600b811161000057141561043157604080518381526020810183905281517fdf0cb1dea99afceb3ea698d62e705b736f1345a7eee9eb07e63d1f8f556c1bc5929181900390910190a16104ab565b600983600b811161000057141561047d5760408051838152905182917f057bc32826fbe161da1c110afcdcae7c109a8b69149f727fc37a603c60ef94ca919081900360200190a26104ab565b600883600b811161000057141561006c57604080518381529051829181900360200190a16104ab565b610000565b5b5b5b505050565b600484600b811161000057141561050957604080518481526020810184905280820183905290517f4a25b279c7c585f25eda9788ac9420ebadae78ca6b206a0e6ab488fd81f550629181900360600190a161055b565b600a84600b811161000057141561006c57604080518481529051829184917ff16c999b533366ca5138d78e85da51611089cd05749f098d6c225d4cd42ee6ec9181900360200190a361055b565b610000565b5b5b50505050565b600282600b81116100005714156105ac576040805182815290517f56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d49181900360200190a1610611565b600782600b81116100005714156105ed5760405181907ff70fe689e290d8ce2b2a388ac28db36fbb0e16a6d89c6804c461f65a1b40bb1590600090a2610611565b600682600b811161000057141561006c576040518190600090a1610611565b610000565b5b5b5b5050565b81604051808280519060200190808383829060006004602084601f0104600302600f01f15090500191505060405180910390207fe77cf33df73da7bc2e253a2dae617e6f15e4e337eaa462a108903af4643d1b758260405180806020018281038252838181518152602001915080519060200190808383829060006004602084601f0104600302600f01f150905090810190601f1680156106cd5780820380516001836020036101000a031916815260200191505b509250505060405180910390a25b5050565b7f532fd6ea96cfb78bb46e09279a26828b8b493de1a2b8b1ee1face527978a15a58160405180806020018281038252838181518152602001915080519060200190808383829060006004602084601f0104600302600f01f150905090810190601f1680156102a75780820380516001836020036101000a031916815260200191505b509250505060405180910390a15b5056"

CONTRACT_EMITTER_ABI = json.loads('[{"constant":false,"inputs":[{"name":"v","type":"string"}],"name":"logString","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"which","type":"uint8"}],"name":"logNoArgs","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"which","type":"uint8"},{"name":"arg0","type":"uint256"},{"name":"arg1","type":"uint256"},{"name":"arg2","type":"uint256"},{"name":"arg3","type":"uint256"}],"name":"logQuadruple","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"which","type":"uint8"},{"name":"arg0","type":"uint256"},{"name":"arg1","type":"uint256"}],"name":"logDouble","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"which","type":"uint8"},{"name":"arg0","type":"uint256"},{"name":"arg1","type":"uint256"},{"name":"arg2","type":"uint256"}],"name":"logTriple","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"which","type":"uint8"},{"name":"arg0","type":"uint256"}],"name":"logSingle","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"arg0","type":"string"},{"name":"arg1","type":"string"}],"name":"logDynamicArgs","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"v","type":"bytes"}],"name":"logBytes","outputs":[],"payable":false,"type":"function"},{"anonymous":true,"inputs":[],"name":"LogAnonymous","type":"event"},{"anonymous":false,"inputs":[],"name":"LogNoArguments","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"arg0","type":"uint256"}],"name":"LogSingleArg","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"arg0","type":"uint256"},{"indexed":false,"name":"arg1","type":"uint256"}],"name":"LogDoubleArg","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"arg0","type":"uint256"},{"indexed":false,"name":"arg1","type":"uint256"},{"indexed":false,"name":"arg2","type":"uint256"}],"name":"LogTripleArg","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"arg0","type":"uint256"},{"indexed":false,"name":"arg1","type":"uint256"},{"indexed":false,"name":"arg2","type":"uint256"},{"indexed":false,"name":"arg3","type":"uint256"}],"name":"LogQuadrupleArg","type":"event"},{"anonymous":true,"inputs":[{"indexed":true,"name":"arg0","type":"uint256"}],"name":"LogSingleAnonymous","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"arg0","type":"uint256"}],"name":"LogSingleWithIndex","type":"event"},{"anonymous":true,"inputs":[{"indexed":false,"name":"arg0","type":"uint256"},{"indexed":true,"name":"arg1","type":"uint256"}],"name":"LogDoubleAnonymous","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"arg0","type":"uint256"},{"indexed":true,"name":"arg1","type":"uint256"}],"name":"LogDoubleWithIndex","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"arg0","type":"uint256"},{"indexed":true,"name":"arg1","type":"uint256"},{"indexed":true,"name":"arg2","type":"uint256"}],"name":"LogTripleWithIndex","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"arg0","type":"uint256"},{"indexed":false,"name":"arg1","type":"uint256"},{"indexed":true,"name":"arg2","type":"uint256"},{"indexed":true,"name":"arg3","type":"uint256"}],"name":"LogQuadrupleWithIndex","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"arg0","type":"string"},{"indexed":false,"name":"arg1","type":"string"}],"name":"LogDynamicArgs","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"v","type":"bytes"}],"name":"LogBytes","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"v","type":"string"}],"name":"LogString","type":"event"}]')


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
def EMITTER(EMITTER_CODE,
            EMITTER_RUNTIME,
            EMITTER_ABI,
            EMITTER_SOURCE):
    return {
        'bytecode': EMITTER_CODE,
        'bytecode_runtime': EMITTER_RUNTIME,
        'source': EMITTER_SOURCE,
        'abi': EMITTER_ABI,
    }


@pytest.fixture()
def Emitter(web3_empty, EMITTER):
    web3 = web3_empty
    return web3.eth.contract(**EMITTER)


@pytest.fixture()
def emitter(web3_empty, Emitter, wait_for_transaction, wait_for_block):
    web3 = web3_empty

    wait_for_block(web3)
    deploy_txn_hash = Emitter.deploy({'from': web3.eth.coinbase, 'gas': 1000000})
    deploy_receipt = wait_for_transaction(web3, deploy_txn_hash)
    contract_address = deploy_receipt['contractAddress']

    bytecode = web3.eth.getCode(contract_address)
    assert bytecode == Emitter.bytecode_runtime
    return Emitter(address=contract_address)


class LogFunctions(object):
    LogAnonymous = 0
    LogNoArguments = 1
    LogSingleArg = 2
    LogDoubleArg = 3
    LogTripleArg = 4
    LogQuadrupleArg = 5
    LogSingleAnonymous = 6
    LogSingleWithIndex = 7
    LogDoubleAnonymous = 8
    LogDoubleWithIndex = 9
    LogTripleWithIndex = 10
    LogQuadrupleWithIndex = 11


@pytest.fixture()
def emitter_event_ids():
    return LogFunctions


class LogTopics(object):
    LogAnonymous = encode_hex(event_signature_to_log_topic("LogAnonymous()"))
    LogNoArguments = encode_hex(event_signature_to_log_topic("LogNoArguments()"))
    LogSingleArg = encode_hex(event_signature_to_log_topic("LogSingleArg(uint256)"))
    LogSingleAnonymous = encode_hex(event_signature_to_log_topic("LogSingleAnonymous(uint256)"))
    LogSingleWithIndex = encode_hex(event_signature_to_log_topic("LogSingleWithIndex(uint256)"))
    LogDoubleArg = encode_hex(event_signature_to_log_topic("LogDoubleArg(uint256,uint256)"))
    LogDoubleAnonymous = encode_hex(event_signature_to_log_topic("LogDoubleAnonymous(uint256,uint256)"))
    LogDoubleWithIndex = encode_hex(event_signature_to_log_topic("LogDoubleWithIndex(uint256,uint256)"))
    LogTripleArg = encode_hex(event_signature_to_log_topic("LogTripleArg(uint256,uint256,uint256)"))
    LogTripleWithIndex = encode_hex(event_signature_to_log_topic("LogTripleWithIndex(uint256,uint256,uint256)"))
    LogQuadrupleArg = encode_hex(event_signature_to_log_topic("LogQuadrupleArg(uint256,uint256,uint256,uint256)"))
    LogQuadrupleWithIndex = encode_hex(event_signature_to_log_topic("LogQuadrupleWithIndex(uint256,uint256,uint256,uint256)"))
    LogBytes = encode_hex(event_signature_to_log_topic("LogBytes(bytes)"))
    LogString = encode_hex(event_signature_to_log_topic("LogString(string)"))
    LogDynamicArgs = encode_hex(event_signature_to_log_topic("LogDynamicArgs(string,string)"))


@pytest.fixture()
def emitter_log_topics():
    return LogTopics
