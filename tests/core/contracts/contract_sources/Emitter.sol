pragma solidity ^0.4.21;


contract Emitter {
    event LogAnonymous() anonymous;
    event LogNoArguments();
    event LogSingleArg(uint arg0);
    event LogDoubleArg(uint arg0, uint arg1);
    event LogTripleArg(uint arg0, uint arg1, uint arg2);
    event LogQuadrupleArg(uint arg0, uint arg1, uint arg2, uint arg3);
    event LogString(string v);
    event LogBytes(bytes v);

    // Indexed
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
        LogAddressNotIndexed
    }

    function logNoArgs(WhichEvent which) public {
        if (which == WhichEvent.LogNoArguments) emit LogNoArguments();
        else if (which == WhichEvent.LogAnonymous) emit LogAnonymous();
        else revert("Didn't match any allowable event index");
    }

    function logSingle(WhichEvent which, uint arg0) public {
        if (which == WhichEvent.LogSingleArg) emit LogSingleArg(arg0);
        else if (which == WhichEvent.LogSingleWithIndex) emit LogSingleWithIndex(arg0);
        else if (which == WhichEvent.LogSingleAnonymous) emit LogSingleAnonymous(arg0);
        else revert("Didn't match any allowable event index");
    }

    function logDouble(WhichEvent which, uint arg0, uint arg1) public {
        if (which == WhichEvent.LogDoubleArg) emit LogDoubleArg(arg0, arg1);
        else if (which == WhichEvent.LogDoubleWithIndex) emit LogDoubleWithIndex(arg0, arg1);
        else if (which == WhichEvent.LogDoubleAnonymous) emit LogDoubleAnonymous(arg0, arg1);
        else revert("Didn't match any allowable event index");
    }

    function logTriple(WhichEvent which, uint arg0, uint arg1, uint arg2) public {
        if (which == WhichEvent.LogTripleArg) emit LogTripleArg(arg0, arg1, arg2);
        else if (which == WhichEvent.LogTripleWithIndex) emit LogTripleWithIndex(arg0, arg1, arg2);
        else revert("Didn't match any allowable event index");
    }

    function logQuadruple(WhichEvent which, uint arg0, uint arg1, uint arg2, uint arg3) public {
        if (which == WhichEvent.LogQuadrupleArg) emit LogQuadrupleArg(arg0, arg1, arg2, arg3);
        else if (which == WhichEvent.LogQuadrupleWithIndex) emit LogQuadrupleWithIndex(arg0, arg1, arg2, arg3);
        else revert("Didn't match any allowable event index");
    }
    function logDynamicArgs(string arg0, string arg1) public {
        emit LogDynamicArgs(arg0, arg1);
    }
    function logListArgs(bytes2[] arg0, bytes2[] arg1) public {
        emit LogListArgs(arg0, arg1);
    }
    function logAddressIndexedArgs(address arg0, address arg1) public {
        emit LogAddressIndexed(arg0, arg1);
    }
    function logAddressNotIndexedArgs(address arg0, address arg1) public {
        emit LogAddressNotIndexed(arg0, arg1);
    }
}
