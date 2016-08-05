import pytest
import json
import textwrap
from sha3 import sha3_256

assert sha3_256(b'').hexdigest() == 'c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470'


@pytest.fixture(autouse=True)
def skip_testrpc_and_wait_for_mining_start(web3_empty, wait_for_block,
                                           skip_if_testrpc):
    skip_if_testrpc(web3_empty)  # TODO: enable testrpc
    wait_for_block(web3_empty)


CONTRACT_EMITTER_SOURCE = textwrap.dedent(("""
contract Emitter {
    event LogAnonymous() anonymous;
    event LogNoArguments();
    event LogSingleArg(uint arg0);
    event LogDoubleArg(uint arg0, uint arg1);
    event LogTripleArg(uint arg0, uint arg1, uint arg2);
    event LogQuadrupleArg(uint arg0, uint arg1, uint arg2, uint arg3);

    // Indexed
    event LogSingleWithIndex(uint indexed arg0);
    event LogDoubleWithIndex(uint arg0, uint indexed arg1);
    event LogTripleWithIndex(uint arg0, uint indexed arg1, uint indexed arg2);
    event LogQuadrupleWithIndex(uint arg0, uint arg1, uint indexed arg2, uint indexed arg3);

    enum WhichEvent {
        LogAnonymous,
        LogNoArguments,
        LogSingleArg,
        LogDoubleArg,
        LogTripleArg,
        LogQuadrupleArg,
        LogSingleWithIndex,
        LogDoubleWithIndex,
        LogTripleWithIndex,
        LogQuadrupleWithIndex
    }

    function logNoArgs(WhichEvent which) public {
        if (which == WhichEvent.LogNoArguments) LogNoArguments();
        else if (which == WhichEvent.LogAnonymous) LogAnonymous();
        else throw;
    }

    function logSingle(WhichEvent which, uint arg0) public {
        if (which == WhichEvent.LogSingleArg) LogSingleArg(arg0);
        else if (which == WhichEvent.LogSingleWithIndex) LogSingleWithIndex(arg0);
        else throw;
    }

    function logDouble(WhichEvent which, uint arg0, uint arg1) public {
        if (which == WhichEvent.LogDoubleArg) LogDoubleArg(arg0, arg1);
        else if (which == WhichEvent.LogDoubleWithIndex) LogDoubleWithIndex(arg0, arg1);
        else throw;
    }

    function logTriple(WhichEvent which, uint arg0, uint arg1, uint arg2) public {
        if (which == WhichEvent.LogTripleArg) LogTripleArg(arg0, arg1, arg2);
        else if (which == WhichEvent.LogTripleWithIndex) LogTripleWithIndex(arg0, arg1, arg2);
        else throw;
    }

    function logQuadruple(WhichEvent which, uint arg0, uint arg1, uint arg2, uint arg3) public {
        if (which == WhichEvent.LogQuadrupleArg) LogQuadrupleArg(arg0, arg1, arg2, arg3);
        else if (which == WhichEvent.LogQuadrupleWithIndex) LogQuadrupleWithIndex(arg0, arg1, arg2, arg3);
        else throw;
    }
}
"""))

CONTRACT_EMITTER_CODE = "0x60606040526102c0806100126000396000f3606060405260e060020a600035046317c0c180811461004757806320f0256e1461008057806390b41d8b146100da5780639c37705314610125578063aa6fd82214610177575b005b61004560043560018114156101b9577f1e86022f78f8d04f8e3dfd13a2bdb280403e6632877c0dbee5e4eeb259908a5c60006060a15b50565b61004560043560243560443560643560843560058514156101d1576060848152608084815260a084905260c08390527ff039d147f23fe975a4254bdf6b1502b8c79132ae1833986b7ccef2638e73fdf991a15b5050505050565b610045600435602435604435600383141561021357606082815260808290527fdf0cb1dea99afceb3ea698d62e705b736f1345a7eee9eb07e63d1f8f556c1bc590604090a15b505050565b610045600435602435604435606435600484141561024e576060838152608083905260a08290527f4a25b279c7c585f25eda9788ac9420ebadae78ca6b206a0e6ab488fd81f550629080a15b50505050565b610045600435602435600282141561028b5760608181527f56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d490602090a15b5050565b60008114156101cc5760006060a061007d565b610002565b60098514156101cc5760608481526080849052819083907fa30ece802b64cd2b7e57dabf4010aabf5df26d1556977affb07b98a77ad955b590604090a36100d3565b60078314156101cc57606082815281907f057bc32826fbe161da1c110afcdcae7c109a8b69149f727fc37a603c60ef94ca90602090a2610120565b60088414156101cc576060838152819083907ff16c999b533366ca5138d78e85da51611089cd05749f098d6c225d4cd42ee6ec90602090a3610171565b60068214156101cc57807ff70fe689e290d8ce2b2a388ac28db36fbb0e16a6d89c6804c461f65a1b40bb1560006060a26101b556"

CONTRACT_EMITTER_RUNTIME = "0x606060405260e060020a600035046317c0c180811461004757806320f0256e1461008057806390b41d8b146100da5780639c37705314610125578063aa6fd82214610177575b005b61004560043560018114156101b9577f1e86022f78f8d04f8e3dfd13a2bdb280403e6632877c0dbee5e4eeb259908a5c60006060a15b50565b61004560043560243560443560643560843560058514156101d1576060848152608084815260a084905260c08390527ff039d147f23fe975a4254bdf6b1502b8c79132ae1833986b7ccef2638e73fdf991a15b5050505050565b610045600435602435604435600383141561021357606082815260808290527fdf0cb1dea99afceb3ea698d62e705b736f1345a7eee9eb07e63d1f8f556c1bc590604090a15b505050565b610045600435602435604435606435600484141561024e576060838152608083905260a08290527f4a25b279c7c585f25eda9788ac9420ebadae78ca6b206a0e6ab488fd81f550629080a15b50505050565b610045600435602435600282141561028b5760608181527f56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d490602090a15b5050565b60008114156101cc5760006060a061007d565b610002565b60098514156101cc5760608481526080849052819083907fa30ece802b64cd2b7e57dabf4010aabf5df26d1556977affb07b98a77ad955b590604090a36100d3565b60078314156101cc57606082815281907f057bc32826fbe161da1c110afcdcae7c109a8b69149f727fc37a603c60ef94ca90602090a2610120565b60088414156101cc576060838152819083907ff16c999b533366ca5138d78e85da51611089cd05749f098d6c225d4cd42ee6ec90602090a3610171565b60068214156101cc57807ff70fe689e290d8ce2b2a388ac28db36fbb0e16a6d89c6804c461f65a1b40bb1560006060a26101b556"

CONTRACT_EMITTER_ABI = json.loads('[{"constant":false,"inputs":[{"name":"which","type":"uint8"}],"name":"logNoArgs","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"which","type":"uint8"},{"name":"arg0","type":"uint256"},{"name":"arg1","type":"uint256"},{"name":"arg2","type":"uint256"},{"name":"arg3","type":"uint256"}],"name":"logQuadruple","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"which","type":"uint8"},{"name":"arg0","type":"uint256"},{"name":"arg1","type":"uint256"}],"name":"logDouble","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"which","type":"uint8"},{"name":"arg0","type":"uint256"},{"name":"arg1","type":"uint256"},{"name":"arg2","type":"uint256"}],"name":"logTriple","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"which","type":"uint8"},{"name":"arg0","type":"uint256"}],"name":"logSingle","outputs":[],"type":"function"},{"anonymous":true,"inputs":[],"name":"LogAnonymous","type":"event"},{"anonymous":false,"inputs":[],"name":"LogNoArguments","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"arg0","type":"uint256"}],"name":"LogSingleArg","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"arg0","type":"uint256"},{"indexed":false,"name":"arg1","type":"uint256"}],"name":"LogDoubleArg","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"arg0","type":"uint256"},{"indexed":false,"name":"arg1","type":"uint256"},{"indexed":false,"name":"arg2","type":"uint256"}],"name":"LogTripleArg","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"arg0","type":"uint256"},{"indexed":false,"name":"arg1","type":"uint256"},{"indexed":false,"name":"arg2","type":"uint256"},{"indexed":false,"name":"arg3","type":"uint256"}],"name":"LogQuadrupleArg","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"arg0","type":"uint256"}],"name":"LogSingleWithIndex","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"arg0","type":"uint256"},{"indexed":true,"name":"arg1","type":"uint256"}],"name":"LogDoubleWithIndex","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"arg0","type":"uint256"},{"indexed":true,"name":"arg1","type":"uint256"},{"indexed":true,"name":"arg2","type":"uint256"}],"name":"LogTripleWithIndex","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"arg0","type":"uint256"},{"indexed":false,"name":"arg1","type":"uint256"},{"indexed":true,"name":"arg2","type":"uint256"},{"indexed":true,"name":"arg3","type":"uint256"}],"name":"LogQuadrupleWithIndex","type":"event"}]')


@pytest.fixture()
def EMITTER_SOURCE():
    return CONTRACT_EMITTER_SOURCE


@pytest.fixture()
def EMITTER_CODE():
    return CONTRACT_EMITTER_CODE


@pytest.fixture()
def EMITTER_RUNTIME():
    return CONTRACT_EMITTER_RUNTIME


@pytest.fixture()
def EMITTER_ABI():
    return CONTRACT_EMITTER_ABI


@pytest.fixture()
def EMITTER(EMITTER_CODE,
            EMITTER_RUNTIME,
            EMITTER_ABI,
            EMITTER_SOURCE):
    return {
        'code': EMITTER_CODE,
        'code_runtime': EMITTER_RUNTIME,
        'source': EMITTER_SOURCE,
        'abi': EMITTER_ABI,
    }


@pytest.fixture()
def Emitter(web3_empty, EMITTER):
    web3 = web3_empty
    return web3.eth.contract(**EMITTER)


@pytest.fixture()
def emitter(web3_empty, Emitter, wait_for_transaction, wait_for_block):
    web3 = web3_empty

    wait_for_block(web3)
    deploy_txn_hash = Emitter.deploy({'from': web3.eth.coinbase, 'gas': 1000000})
    deploy_receipt = wait_for_transaction(web3, deploy_txn_hash)
    contract_address = deploy_receipt['contractAddress']

    code = web3.eth.getCode(contract_address)
    assert code == Emitter.code_runtime
    return Emitter(address=contract_address)


class LogFunctions(object):
    LogAnonymous = 0
    LogNoArguments = 1
    LogSingleArg = 2
    LogDoubleArg = 3
    LogTripleArg = 4
    LogQuadrupleArg = 5
    LogSingleWithIndex = 6
    LogDoubleWithIndex = 7
    LogTripleWithIndex = 8
    LogQuadrupleWithIndex = 9


@pytest.fixture()
def emitter_event_ids():
    return LogFunctions


def event_topic(event_signature):
    from web3.utils.string import force_bytes
    return force_bytes("0x" + sha3_256(force_bytes(event_signature)).hexdigest())


class LogTopics(object):
    LogAnonymous = event_topic("LogAnonymous()")
    LogNoArguments = event_topic("LogNoArguments()")
    LogSingleArg = event_topic("LogSingleArg(uint256)")
    LogSingleWithIndex = event_topic("LogSingleWithIndex(uint256)")
    LogDoubleArg = event_topic("LogDoubleArg(uint256,uint256)")
    LogDoubleWithIndex = event_topic("LogDoubleWithIndex(uint256,uint256)")
    LogTripleArg = event_topic("LogTripleArg(uint256,uint256,uint256)")
    LogTripleWithIndex = event_topic("LogTripleWithIndex(uint256,uint256,uint256)")
    LogQuadrupleArg = event_topic("LogQuadrupleArg(uint256,uint256,uint256,uint256)")
    LogQuadrupleWithIndex = event_topic("LogQuadrupleWithIndex(uint256,uint256,uint256,uint256)")


@pytest.fixture()
def emitter_log_topics():
    return LogTopics
