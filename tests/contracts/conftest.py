import pytest
import json
import textwrap


CONTRACT_CODE = b"606060405261022e806100126000396000f360606040523615610074576000357c01000000000000000000000000000000000000000000000000000000009004806316216f391461007657806361bc221a146100995780637cf5dab0146100bc578063a5f3c23b146100e8578063d09de08a1461011d578063dcf537b11461014057610074565b005b610083600480505061016c565b6040518082815260200191505060405180910390f35b6100a6600480505061017f565b6040518082815260200191505060405180910390f35b6100d26004808035906020019091905050610188565b6040518082815260200191505060405180910390f35b61010760048080359060200190919080359060200190919050506101ea565b6040518082815260200191505060405180910390f35b61012a6004805050610201565b6040518082815260200191505060405180910390f35b6101566004808035906020019091905050610217565b6040518082815260200191505060405180910390f35b6000600d9050805080905061017c565b90565b60006000505481565b6000816000600082828250540192505081905550600060005054905080507f3496c3ede4ec3ab3686712aa1c238593ea6a42df83f98a5ec7df9834cfa577c5816040518082815260200191505060405180910390a18090506101e5565b919050565b6000818301905080508090506101fb565b92915050565b600061020d6001610188565b9050610214565b90565b60006007820290508050809050610229565b91905056"


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
