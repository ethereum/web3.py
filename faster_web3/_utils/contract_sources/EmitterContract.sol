pragma solidity >=0.8.0;


contract EmitterContract {
    event LogAnonymous() anonymous;
    event LogNoArguments();
    event LogSingleArg(uint arg0);
    event LogDoubleArg(uint arg0, uint arg1);
    event LogTripleArg(uint arg0, uint arg1, uint arg2);
    event LogQuadrupleArg(uint arg0, uint arg1, uint arg2, uint arg3);
    event LogString(string v);
    event LogBytes(bytes v);
    event LogSingleWithIndex(uint indexed arg0);
    event LogSingleAnonymous(uint indexed arg0) anonymous;
    event LogDoubleWithIndex(uint arg0, uint indexed arg1);
    event LogDoubleAnonymous(uint arg0, uint indexed arg1) anonymous;
    event LogTripleWithIndex(uint arg0, uint indexed arg1, uint indexed arg2);
    event LogQuadrupleWithIndex(uint arg0, uint arg1, uint indexed arg2, uint indexed arg3);
    event LogDynamicArgs(string indexed arg0, string arg1);
    event LogListArgs(bytes2[] indexed arg0, bytes2[] arg1);
    event LogAddressIndexed(address indexed arg0, address arg1);
    event LogAddressNotIndexed(address arg0, address arg1);

    struct NestedTestTuple {
        uint c;
    }
    struct TestTuple {
        uint a;
        uint b;
        NestedTestTuple nested;
    }
    event LogStructArgs(uint arg0, TestTuple arg1);

    event LogIndexedAndNotIndexed(
        address indexed indexedAddress,
        uint256 indexed indexedUint256,
        address nonIndexedAddress,
        uint256 nonIndexedUint256,
        string nonIndexedString
    );

    enum WhichEvent {
        LogAnonymous,
        LogNoArguments,
        LogSingleArg,
        LogDoubleArg,
        LogTripleArg,
        LogQuadrupleArg,
        LogSingleAnonymous,
        LogSingleWithIndex,
        LogDoubleAnonymous,
        LogDoubleWithIndex,
        LogTripleWithIndex,
        LogQuadrupleWithIndex,
        LogBytes,
        LogString,
        LogDynamicArgs,
        LogListArgs,
        LogAddressIndexed,
        LogAddressNotIndexed,
        LogStructArgs,
        LogIndexedAndNotIndexed
    }

    function logNoArgs(WhichEvent which) external {
        if (which == WhichEvent.LogNoArguments) emit LogNoArguments();
        else if (which == WhichEvent.LogAnonymous) emit LogAnonymous();
        else revert("Didn't match any allowable event index");
    }

    function logSingle(WhichEvent which, uint arg0) external {
        if (which == WhichEvent.LogSingleArg) emit LogSingleArg(arg0);
        else if (which == WhichEvent.LogSingleWithIndex) emit LogSingleWithIndex(arg0);
        else if (which == WhichEvent.LogSingleAnonymous) emit LogSingleAnonymous(arg0);
        else revert("Didn't match any allowable event index");
    }

    function logDouble(WhichEvent which, uint arg0, uint arg1) external {
        if (which == WhichEvent.LogDoubleArg) emit LogDoubleArg(arg0, arg1);
        else if (which == WhichEvent.LogDoubleWithIndex) emit LogDoubleWithIndex(arg0, arg1);
        else if (which == WhichEvent.LogDoubleAnonymous) emit LogDoubleAnonymous(arg0, arg1);
        else revert("Didn't match any allowable event index");
    }

    function logTriple(WhichEvent which, uint arg0, uint arg1, uint arg2) external {
        if (which == WhichEvent.LogTripleArg) emit LogTripleArg(arg0, arg1, arg2);
        else if (which == WhichEvent.LogTripleWithIndex) emit LogTripleWithIndex(arg0, arg1, arg2);
        else revert("Didn't match any allowable event index");
    }

    function logQuadruple(WhichEvent which, uint arg0, uint arg1, uint arg2, uint arg3) external {
        if (which == WhichEvent.LogQuadrupleArg) emit LogQuadrupleArg(arg0, arg1, arg2, arg3);
        else if (which == WhichEvent.LogQuadrupleWithIndex) emit LogQuadrupleWithIndex(arg0, arg1, arg2, arg3);
        else revert("Didn't match any allowable event index");
    }

    function logDynamicArgs(string memory arg0, string memory arg1) external {
        emit LogDynamicArgs(arg0, arg1);
    }

    function logListArgs(bytes2[] memory arg0, bytes2[] memory arg1) external {
        emit LogListArgs(arg0, arg1);
    }

    function logAddressIndexedArgs(address arg0, address arg1) external {
        emit LogAddressIndexed(arg0, arg1);
    }

    function logAddressNotIndexedArgs(address arg0, address arg1) external {
        emit LogAddressNotIndexed(arg0, arg1);
    }

    function logBytes(bytes memory v) external {
        emit LogBytes(v);
    }

    function logString(string memory v) external {
        emit LogString(v);
    }

    function logStruct(uint arg0, TestTuple memory arg1) external {
        emit LogStructArgs(arg0, arg1);
    }

    function logIndexedAndNotIndexedArgs(
        address indexedAddress,
        uint256 indexedUint256,
        address nonIndexedAddress,
        uint256 nonIndexedUint256,
        string memory nonIndexedString
    ) external {
        emit LogIndexedAndNotIndexed(
            indexedAddress,
            indexedUint256,
            nonIndexedAddress,
            nonIndexedUint256,
            nonIndexedString
        );
    }
}
