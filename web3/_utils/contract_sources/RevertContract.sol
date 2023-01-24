pragma solidity >=0.6.1;

contract RevertContract {
  function normalFunction() public pure returns (bool) {
      return true;
  }

  function revertWithMessage() public pure {
      revert('Function has been reverted.');
  }

  function revertWithoutMessage() public pure {
      revert();
  }
}
