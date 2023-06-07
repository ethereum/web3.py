pragma solidity >=0.8.0;

contract PanicErrorsContract {
    // --- setup --- //

    enum ErrorCode21 { A }

    bytes[] public emptyArray = new bytes[](0);

    bytes public x = "abc";
    bytes public y;

    function() internal private err51;

    // --- error code test functions --- //

    function errorCode01() public pure {
        // assert evaluates to false
        assert (false);
    }

    function errorCode11() public pure {
        // arithmetic underflow outside of unchecked block
        uint err11 = 0;
        err11--;
    }

    function errorCode12(uint zero) public pure {
        // division by zero
        uint err = 5 / zero;
    }

    function errorCode21(int negativeInt) public pure {
        // convert invalid value into enum
        ErrorCode21 err = ErrorCode21(negativeInt);
    }

    function errorCode22() public {
        // access storage byte array that is incorrectly encoded
        // source: https://github.com/ethereum/solidity/pull/10239/files
        assembly { sstore(x.slot, 64) }
        delete y;
        x.pop();
    }

    function errorCode31() public {
        // pop on empty array
        emptyArray.pop();
    }

    function errorCode32() public {
        // array index out of bounds
        emptyArray[1];
    }

    function errorCode41() public pure {
        // allocation of too much memory or array too large
        uint256 l = 2**256 / 32;
        uint256[] memory x = new uint256[](l);
    }

    function errorCode51() public {
        // call to zero-initialized variable of internal function type
        err51();
    }
}
