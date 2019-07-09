pragma solidity ^0.4.24;

contract Owned {
    address owner;
    
    modifier onlyOwner { require(msg.sender == owner); _; }

    constructor() public {
        owner = msg.sender;
    }
}
