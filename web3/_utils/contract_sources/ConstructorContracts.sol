pragma solidity >=0.7.0;

contract SimpleConstructorContract {
    constructor() {}
}

contract ConstructorWithArgumentsContract {
    uint256 public data_a;
    bytes32 public data_b;

    constructor(uint256 a, bytes32 b) {
        data_a = a;
        data_b = b;
    }
}

contract ConstructorWithAddressArgumentContract {
    address public testAddr;

    constructor(address _testAddr) {
        testAddr = _testAddr;
    }
}
