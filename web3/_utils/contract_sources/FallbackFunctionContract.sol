pragma solidity >=0.5.4;

contract FallbackFunctionContract {
    uint data;
    constructor() payable { data = 0; }
    function getData() public view returns (uint r) { return data; }
    fallback() external { data = 1; }
}
