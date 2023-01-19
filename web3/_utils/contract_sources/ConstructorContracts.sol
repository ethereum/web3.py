pragma solidity >=0.7.0;

contract SimpleConstructor {
    constructor() {}
}

contract ConstructorWithArguments {
    uint256 public data_a;
    bytes32 public data_b;

    constructor(uint256 a, bytes32 b) {
        data_a = a;
        data_b = b;
    }
}

contract ConstructorWithAddressArgument {
    address public testAddr;

    constructor(address _testAddr) {
        testAddr = _testAddr;
    }
}
