pragma solidity ^0.8.4;

error Unauthorized();
error UnauthorizedWithMessage(string errorMessage);

contract RevertContract {
    function customErrorWithoutMessage() public pure {
        revert Unauthorized();
    }

    function customErrorWithMessage() public pure {
        revert UnauthorizedWithMessage("You are not authorized");
    }

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
