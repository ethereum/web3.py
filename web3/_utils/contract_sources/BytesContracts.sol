pragma solidity >=0.7.0;

contract BytesContract {
    bytes const = hex"0123";
    bytes value;

    constructor (bytes memory _value) {
        value = _value;
    }

    function constValue() public view returns(bytes memory) {
        return const;
    }

    function getValue() public view returns(bytes memory) {
        return value;
    }

    function setValue(bytes memory _value) public {
        value = _value;
    }
}

contract Bytes32Contract {
    bytes32 const = hex"0123012301230123012301230123012301230123012301230123012301230123";
    bytes32 value;

    constructor (bytes32 _value) {
        value = _value;
    }

    function constValue() public view returns(bytes32) {
        return const;
    }

    function getValue() public view returns(bytes32) {
        return value;
    }

    function setValue(bytes32 _value) public {
        value = _value;
    }
}
