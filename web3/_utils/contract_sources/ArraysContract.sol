pragma solidity >=0.7.0;

contract ArraysContract {
        bytes32[] public bytes32Value;
        bytes32[] public bytes32ConstValue = [keccak256('A'), keccak256('B')];
        bytes1[] public byteValue;
        bytes1[] public byteConstValue = [bytes1(hex"00"), bytes1(hex"01")];

        constructor(bytes32[] memory  _bytes32Value, bytes1[] memory _byteValue) {
            bytes32Value = _bytes32Value;
            byteValue = _byteValue;
        }

        function getBytes32ConstValue() public view returns (bytes32[] memory) {
            return bytes32ConstValue;
        }

        function getByteConstValue()  public view  returns (bytes1[] memory){
            return byteConstValue;
        }

        function setBytes32Value(bytes32[] memory _bytes32Value) public {
            bytes32Value = _bytes32Value;
        }

        function getBytes32Value() public view returns (bytes32[] memory) {
            return bytes32Value;
        }

        function setByteValue(bytes1[] memory _byteValue) public {
            byteValue = _byteValue;
        }

        function getByteValue() public view returns (bytes1[] memory) {
            return byteValue;
        }
}
