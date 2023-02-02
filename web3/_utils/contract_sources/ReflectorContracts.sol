pragma solidity >=0.4.0;

contract AddressReflectorContract {
    function reflect(address arg) public pure returns(address) {
        return arg;
    }

    function reflect(address[] memory arg) public pure returns(address[] memory) {
        return arg;
    }
}
