// SPDX-License-Identifier: MIT
pragma solidity ^0.6.8;

contract Owned {
    address owner;
    
    modifier onlyOwner { require(msg.sender == owner); _; }

    constructor() public {
        owner = msg.sender;
    }
}
