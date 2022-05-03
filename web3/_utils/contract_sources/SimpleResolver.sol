pragma solidity ^0.8.13;

contract SimpleResolver {
    // deployed on ropsten at address = 0xD4D522c96111679bF86220deFE75e0aA1df890b4

    function supportsInterface(bytes4 interfaceID) public returns (bool) {
        return interfaceID == 0x3b3b57de;
    }

    function addr(bytes32 nodeID) public returns (address) {
        return address(this);
    }
}
