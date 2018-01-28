pragma solidity ^0.4.0;


contract Fallback {
    uint data;
    function() { data = 1; }
    function getData() returns (uint r) { return data; }
}