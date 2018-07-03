import functools
import json
import pytest

from eth_utils import (
    apply_key_map,
    encode_hex,
    event_signature_to_log_topic,
)


@pytest.fixture(autouse=True)
def wait_for_mining_start(web3, wait_for_block):
    wait_for_block(web3)


CONTRACT_EMITTER_CODE = "0x60606040526104ae806100126000396000f3606060405236156100615760e060020a60003504630bb563d6811461006357806317c0c1801461013657806320f0256e1461017057806390b41d8b146101ca5780639c37705314610215578063aa6fd82214610267578063e17bf956146102a9575b005b60206004803580820135601f810184900490930260809081016040526060848152610061946024939192918401918190838280828437509496505050505050507fa95e6e2a182411e7a6f9ed114a85c3761d87f9b8f453d842c71235aa64fff99f8160405180806020018281038252838181518152602001915080519060200190808383829060006004602084601f0104600f02600301f150905090810190601f1680156101255780820380516001836020036101000a031916815260200191505b509250505060405180910390a15b50565b610061600435600181141561037a577f1e86022f78f8d04f8e3dfd13a2bdb280403e6632877c0dbee5e4eeb259908a5c60006060a1610133565b6100616004356024356044356064356084356005851415610392576060848152608084815260a084905260c08390527ff039d147f23fe975a4254bdf6b1502b8c79132ae1833986b7ccef2638e73fdf991a15b5050505050565b61006160043560243560443560038314156103d457606082815260808290527fdf0cb1dea99afceb3ea698d62e705b736f1345a7eee9eb07e63d1f8f556c1bc590604090a15b505050565b6100616004356024356044356064356004841415610428576060838152608083905260a08290527f4a25b279c7c585f25eda9788ac9420ebadae78ca6b206a0e6ab488fd81f550629080a15b50505050565b61006160043560243560028214156104655760608181527f56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d490602090a15b5050565b60206004803580820135601f810184900490930260809081016040526060848152610061946024939192918401918190838280828437509496505050505050507f532fd6ea96cfb78bb46e09279a26828b8b493de1a2b8b1ee1face527978a15a58160405180806020018281038252838181518152602001915080519060200190808383829060006004602084601f0104600f02600301f150905090810190601f1680156101255780820380516001836020036101000a03191681526020019150509250505060405180910390a150565b600081141561038d5760006060a0610133565b610002565b600b85141561038d5760608481526080849052819083907fa30ece802b64cd2b7e57dabf4010aabf5df26d1556977affb07b98a77ad955b590604090a36101c3565b600983141561040f57606082815281907f057bc32826fbe161da1c110afcdcae7c109a8b69149f727fc37a603c60ef94ca90602090a2610210565b600883141561038d5760608281528190602090a1610210565b600a84141561038d576060838152819083907ff16c999b533366ca5138d78e85da51611089cd05749f098d6c225d4cd42ee6ec90602090a3610261565b600782141561049a57807ff70fe689e290d8ce2b2a388ac28db36fbb0e16a6d89c6804c461f65a1b40bb1560006060a26102a5565b600682141561038d578060006060a16102a556"  # noqa: E501

CONTRACT_EMITTER_RUNTIME = "0x606060405236156100615760e060020a60003504630bb563d6811461006357806317c0c1801461013657806320f0256e1461017057806390b41d8b146101ca5780639c37705314610215578063aa6fd82214610267578063e17bf956146102a9575b005b60206004803580820135601f810184900490930260809081016040526060848152610061946024939192918401918190838280828437509496505050505050507fa95e6e2a182411e7a6f9ed114a85c3761d87f9b8f453d842c71235aa64fff99f8160405180806020018281038252838181518152602001915080519060200190808383829060006004602084601f0104600f02600301f150905090810190601f1680156101255780820380516001836020036101000a031916815260200191505b509250505060405180910390a15b50565b610061600435600181141561037a577f1e86022f78f8d04f8e3dfd13a2bdb280403e6632877c0dbee5e4eeb259908a5c60006060a1610133565b6100616004356024356044356064356084356005851415610392576060848152608084815260a084905260c08390527ff039d147f23fe975a4254bdf6b1502b8c79132ae1833986b7ccef2638e73fdf991a15b5050505050565b61006160043560243560443560038314156103d457606082815260808290527fdf0cb1dea99afceb3ea698d62e705b736f1345a7eee9eb07e63d1f8f556c1bc590604090a15b505050565b6100616004356024356044356064356004841415610428576060838152608083905260a08290527f4a25b279c7c585f25eda9788ac9420ebadae78ca6b206a0e6ab488fd81f550629080a15b50505050565b61006160043560243560028214156104655760608181527f56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d490602090a15b5050565b60206004803580820135601f810184900490930260809081016040526060848152610061946024939192918401918190838280828437509496505050505050507f532fd6ea96cfb78bb46e09279a26828b8b493de1a2b8b1ee1face527978a15a58160405180806020018281038252838181518152602001915080519060200190808383829060006004602084601f0104600f02600301f150905090810190601f1680156101255780820380516001836020036101000a03191681526020019150509250505060405180910390a150565b600081141561038d5760006060a0610133565b610002565b600b85141561038d5760608481526080849052819083907fa30ece802b64cd2b7e57dabf4010aabf5df26d1556977affb07b98a77ad955b590604090a36101c3565b600983141561040f57606082815281907f057bc32826fbe161da1c110afcdcae7c109a8b69149f727fc37a603c60ef94ca90602090a2610210565b600883141561038d5760608281528190602090a1610210565b600a84141561038d576060838152819083907ff16c999b533366ca5138d78e85da51611089cd05749f098d6c225d4cd42ee6ec90602090a3610261565b600782141561049a57807ff70fe689e290d8ce2b2a388ac28db36fbb0e16a6d89c6804c461f65a1b40bb1560006060a26102a5565b600682141561038d578060006060a16102a556"  # noqa: E501

CONTRACT_EMITTER_ABI = json.loads('[{"constant":false,"inputs":[{"name":"v","type":"string"}],"name":"logString","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"which","type":"uint8"}],"name":"logNoArgs","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"which","type":"uint8"},{"name":"arg0","type":"uint256"},{"name":"arg1","type":"uint256"},{"name":"arg2","type":"uint256"},{"name":"arg3","type":"uint256"}],"name":"logQuadruple","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"which","type":"uint8"},{"name":"arg0","type":"uint256"},{"name":"arg1","type":"uint256"}],"name":"logDouble","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"which","type":"uint8"},{"name":"arg0","type":"uint256"},{"name":"arg1","type":"uint256"},{"name":"arg2","type":"uint256"}],"name":"logTriple","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"which","type":"uint8"},{"name":"arg0","type":"uint256"}],"name":"logSingle","outputs":[],"type":"function"},{"constant":false,"inputs":[{"name":"v","type":"bytes"}],"name":"logBytes","outputs":[],"type":"function"},{"anonymous":true,"inputs":[],"name":"LogAnonymous","type":"event"},{"anonymous":false,"inputs":[],"name":"LogNoArguments","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"arg0","type":"uint256"}],"name":"LogSingleArg","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"arg0","type":"uint256"},{"indexed":false,"name":"arg1","type":"uint256"}],"name":"LogDoubleArg","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"arg0","type":"uint256"},{"indexed":false,"name":"arg1","type":"uint256"},{"indexed":false,"name":"arg2","type":"uint256"}],"name":"LogTripleArg","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"arg0","type":"uint256"},{"indexed":false,"name":"arg1","type":"uint256"},{"indexed":false,"name":"arg2","type":"uint256"},{"indexed":false,"name":"arg3","type":"uint256"}],"name":"LogQuadrupleArg","type":"event"},{"anonymous":true,"inputs":[{"indexed":true,"name":"arg0","type":"uint256"}],"name":"LogSingleAnonymous","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"arg0","type":"uint256"}],"name":"LogSingleWithIndex","type":"event"},{"anonymous":true,"inputs":[{"indexed":false,"name":"arg0","type":"uint256"},{"indexed":true,"name":"arg1","type":"uint256"}],"name":"LogDoubleAnonymous","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"arg0","type":"uint256"},{"indexed":true,"name":"arg1","type":"uint256"}],"name":"LogDoubleWithIndex","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"arg0","type":"uint256"},{"indexed":true,"name":"arg1","type":"uint256"},{"indexed":true,"name":"arg2","type":"uint256"}],"name":"LogTripleWithIndex","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"arg0","type":"uint256"},{"indexed":false,"name":"arg1","type":"uint256"},{"indexed":true,"name":"arg2","type":"uint256"},{"indexed":true,"name":"arg3","type":"uint256"}],"name":"LogQuadrupleWithIndex","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"v","type":"bytes"}],"name":"LogBytes","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"v","type":"string"}],"name":"LogString","type":"event"}]')  # noqa: E501


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
            EMITTER_ABI):
    return {
        'bytecode': EMITTER_CODE,
        'bytecode_runtime': EMITTER_RUNTIME,
        'abi': EMITTER_ABI,
    }


@pytest.fixture()
def Emitter(web3, EMITTER):
    return web3.eth.contract(**EMITTER)


@pytest.fixture()
def emitter(web3, Emitter, wait_for_transaction, wait_for_block, address_conversion_func):
    wait_for_block(web3)
    deploy_txn_hash = Emitter.constructor().transact({'from': web3.eth.coinbase, 'gas': 1000000})
    deploy_receipt = wait_for_transaction(web3, deploy_txn_hash)
    contract_address = address_conversion_func(deploy_receipt['contractAddress'])

    bytecode = web3.eth.getCode(contract_address)
    assert bytecode == Emitter.bytecode_runtime
    _emitter = Emitter(address=contract_address)
    assert _emitter.address == contract_address
    return _emitter


class LogFunctions:
    LogAnonymous = 0
    LogNoArguments = 1
    LogSingleArg = 2
    LogDoubleArg = 3
    LogTripleArg = 4
    LogQuadrupleArg = 5
    LogSingleAnonymous = 6
    LogSingleWithIndex = 7
    LogDoubleAnonymous = 8
    LogDoubleWithIndex = 9
    LogTripleWithIndex = 10
    LogQuadrupleWithIndex = 11


@pytest.fixture()
def emitter_event_ids():
    return LogFunctions


class LogTopics:
    LogAnonymous = encode_hex(event_signature_to_log_topic("LogAnonymous()"))
    LogNoArguments = encode_hex(event_signature_to_log_topic("LogNoArguments()"))
    LogSingleArg = encode_hex(event_signature_to_log_topic("LogSingleArg(uint256)"))
    LogSingleAnonymous = encode_hex(event_signature_to_log_topic("LogSingleAnonymous(uint256)"))
    LogSingleWithIndex = encode_hex(event_signature_to_log_topic("LogSingleWithIndex(uint256)"))
    LogDoubleArg = encode_hex(event_signature_to_log_topic("LogDoubleArg(uint256,uint256)"))
    LogDoubleAnonymous = encode_hex(event_signature_to_log_topic("LogDoubleAnonymous(uint256,uint256)"))  # noqa: E501
    LogDoubleWithIndex = encode_hex(event_signature_to_log_topic("LogDoubleWithIndex(uint256,uint256)"))  # noqa: E501
    LogTripleArg = encode_hex(event_signature_to_log_topic("LogTripleArg(uint256,uint256,uint256)"))
    LogTripleWithIndex = encode_hex(event_signature_to_log_topic("LogTripleWithIndex(uint256,uint256,uint256)"))  # noqa: E501
    LogQuadrupleArg = encode_hex(event_signature_to_log_topic("LogQuadrupleArg(uint256,uint256,uint256,uint256)"))  # noqa: E501
    LogQuadrupleWithIndex = encode_hex(event_signature_to_log_topic("LogQuadrupleWithIndex(uint256,uint256,uint256,uint256)"))  # noqa: E501
    LogBytes = encode_hex(event_signature_to_log_topic("LogBytes(bytes)"))
    LogString = encode_hex(event_signature_to_log_topic("LogString(string)"))


@pytest.fixture()
def emitter_log_topics():
    return LogTopics


def return_filter_by_api(
        api_style=None,
        contract=None,
        args=[]):
    if api_style == 'v3':
        with pytest.deprecated_call():
            return contract.eventFilter(*args)
    elif api_style == 'v4':
        event_name = args[0]
        kwargs = apply_key_map({'filter': 'argument_filters'}, args[1])
        if 'fromBlock' not in kwargs:
            kwargs['fromBlock'] = 'latest'
        return contract.events[event_name].createFilter(**kwargs)
    else:
        raise ValueError("api_style must be 'v3 or v4'")


@pytest.fixture(params=['v3', 'v4'])
def create_filter(request):
    return functools.partial(return_filter_by_api, request.param)
