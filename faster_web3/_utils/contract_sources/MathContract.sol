pragma solidity >=0.7.0;

contract MathContract {
    uint256 public counter = 0;

    event Increased(uint256 value);

    function incrementCounter() public payable returns(uint256 result) {
        counter = counter + 1;
        emit Increased(1);
        return counter;
    }

    function incrementCounter(uint256 amount) public payable returns(uint256 result) {
        counter = counter + amount;
        emit Increased(amount);
        return counter;
    }

    function return13() public returns(int256 result) {
        return 13;
    }

    function multiply7(int256 a) public payable returns(int256 result) {
        return a * 7;
    }

    function add(int256 a, int256 b) public payable returns(int256 result) {
        return a + b;
    }
}
