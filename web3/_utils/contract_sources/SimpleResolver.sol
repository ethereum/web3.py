pragma solidity ^0.8.13;

contract SimpleResolver {
    function supportsInterface(bytes4 interfaceID) public returns (bool) {
        return interfaceID == 0x3b3b57de;
    }

    function addr(bytes32 nodeID) public returns (address) {
        return address(this);
    }
}
