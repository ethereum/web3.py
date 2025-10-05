pragma solidity >=0.6.0;

contract StringContract {
    string public value;

    constructor (string memory _value) {
        value = _value;
    }

    function getValue() external payable returns(string memory) {
        return value;
    }

    function setValue(string memory _value) external {
        value = _value;
    }

    // for testing contract call to unknown function selector
    fallback(bytes calldata _calldata) external returns(bytes memory) {
        return _calldata;
    }
}
