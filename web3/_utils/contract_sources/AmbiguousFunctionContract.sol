pragma solidity >=0.7.0;

contract AmbiguousFunctionContract {
    function isValidSignature() public view returns(string memory result) {
        return "valid";
    }

    function isValidSignature(bytes memory message, bytes memory signature) public view returns(uint256 result) {
        return 1;
    }

    function isValidSignature(bytes32 message, bytes memory signature) public view returns(uint256 result) {
        return 0;
    }
}
