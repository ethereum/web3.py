pragma solidity >=0.7.0;

contract StringContract {
    string const = "never used";
    string value;

    constructor (string memory _value) {
        value = _value;
    }

    function constValue() public payable returns(string memory) {
        return const;
    }

    function getValue() public payable returns(string memory) {
        return value;
    }

    function setValue(string memory _value) public {
        value = _value;
    }
}
