pragma solidity ^0.8.23;

contract FunctionNameTesterContract {
    function abi() public returns (bool) {
        return true;
    }

    function w3() public returns (bool) {
        return true;
    }

    // unused, this just needs to come after `w3` in the abi... so name it "z"
    function z() public returns (bool) {
        return false;
    }
}
