pragma solidity >=0.7.0;

contract ContractCallerTester {
    int public count;

    function add(int256 a, int256 b) public payable returns (int256) {
        return a + b;
    }

    function increment() public returns (int256) {
        return count += 1;
    }

    function counter() public payable returns (int256) {
        return count;
    }

    function returnMeta() public payable returns (address, bytes memory, uint256, uint, uint) {
        return (msg.sender, msg.data, gasleft(), msg.value, block.number);
    }
}
