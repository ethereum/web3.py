pragma solidity >=0.6.0;

contract EventContract {
    event LogSingleArg(uint256 arg0);
    event LogSingleWithIndex(uint256 arg0);

    function logTwoEvents(uint256 _arg0) external {
        emit LogSingleWithIndex(_arg0);
        emit LogSingleArg(_arg0);
    }
}

contract IndexedEventContract {
    event LogSingleArg(uint256 arg0);
    event LogSingleWithIndex(uint256 indexed arg0);

    function logTwoEvents(uint256 _arg0) external {
        emit LogSingleWithIndex(_arg0);
        emit LogSingleArg(_arg0);
    }
}

contract AmbiguousEventNameContract {
    event LogSingleArg(uint256 arg0);
    event LogSingleArg(bytes32 arg0);

    function logTwoEvents(uint256 _arg0) external {
        emit LogSingleArg(_arg0);
        emit LogSingleArg(bytes32(abi.encode(_arg0)));
    }
}
