pragma solidity >=0.6.0;

contract EventContract {
    event LogSingleArg(uint256 arg0);
    event LogSingleWithIndex(uint256 arg0);

    function logTwoEvents(uint256 _arg0) public {
        emit LogSingleWithIndex(_arg0);
        emit LogSingleArg(_arg0);
    }
}

contract IndexedEventContract {
    event LogSingleArg(uint256 arg0);
    event LogSingleWithIndex(uint256 indexed arg0);

    function logTwoEvents(uint256 _arg0) public {
        emit LogSingleWithIndex(_arg0);
        emit LogSingleArg(_arg0);
    }
}
