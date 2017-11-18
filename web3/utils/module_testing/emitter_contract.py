
EMITTER_BYTECODE = (
    "60606040526104ae806100126000396000f3606060405236156100615760e060020a60003504630b"
    "b563d6811461006357806317c0c1801461013657806320f0256e1461017057806390b41d8b146101"
    "ca5780639c37705314610215578063aa6fd82214610267578063e17bf956146102a9575b005b6020"
    "6004803580820135601f810184900490930260809081016040526060848152610061946024939192"
    "918401918190838280828437509496505050505050507fa95e6e2a182411e7a6f9ed114a85c3761d"
    "87f9b8f453d842c71235aa64fff99f81604051808060200182810382528381815181526020019150"
    "80519060200190808383829060006004602084601f0104600f02600301f150905090810190601f16"
    "80156101255780820380516001836020036101000a031916815260200191505b5092505050604051"
    "80910390a15b50565b610061600435600181141561037a577f1e86022f78f8d04f8e3dfd13a2bdb2"
    "80403e6632877c0dbee5e4eeb259908a5c60006060a1610133565b61006160043560243560443560"
    "64356084356005851415610392576060848152608084815260a084905260c08390527ff039d147f2"
    "3fe975a4254bdf6b1502b8c79132ae1833986b7ccef2638e73fdf991a15b5050505050565b610061"
    "60043560243560443560038314156103d457606082815260808290527fdf0cb1dea99afceb3ea698"
    "d62e705b736f1345a7eee9eb07e63d1f8f556c1bc590604090a15b505050565b6100616004356024"
    "356044356064356004841415610428576060838152608083905260a08290527f4a25b279c7c585f2"
    "5eda9788ac9420ebadae78ca6b206a0e6ab488fd81f550629080a15b50505050565b610061600435"
    "60243560028214156104655760608181527f56d2ef3c5228bf5d88573621e325a4672ab50e033749"
    "a601e4f4a5e1dce905d490602090a15b5050565b60206004803580820135601f8101849004909302"
    "60809081016040526060848152610061946024939192918401918190838280828437509496505050"
    "505050507f532fd6ea96cfb78bb46e09279a26828b8b493de1a2b8b1ee1face527978a15a5816040"
    "51808060200182810382528381815181526020019150805190602001908083838290600060046020"
    "84601f0104600f02600301f150905090810190601f16801561012557808203805160018360200361"
    "01000a03191681526020019150509250505060405180910390a150565b600081141561038d576000"
    "6060a0610133565b610002565b600b85141561038d5760608481526080849052819083907fa30ece"
    "802b64cd2b7e57dabf4010aabf5df26d1556977affb07b98a77ad955b590604090a36101c3565b60"
    "0983141561040f57606082815281907f057bc32826fbe161da1c110afcdcae7c109a8b69149f727f"
    "c37a603c60ef94ca90602090a2610210565b600883141561038d5760608281528190602090a16102"
    "10565b600a84141561038d576060838152819083907ff16c999b533366ca5138d78e85da51611089"
    "cd05749f098d6c225d4cd42ee6ec90602090a3610261565b600782141561049a57807ff70fe689e2"
    "90d8ce2b2a388ac28db36fbb0e16a6d89c6804c461f65a1b40bb1560006060a26102a5565b600682"
    "141561038d578060006060a16102a556"
)


EMITTER_ABI = [
    {
        "constant": False,
        "inputs": [{"name": "v", "type": "string"}],
        "name": "logString",
        "outputs": [],
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [{"name": "which", "type": "uint8"}],
        "name": "logNoArgs",
        "outputs": [],
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"name": "which", "type": "uint8"},
            {"name": "arg0", "type": "uint256"},
            {"name": "arg1", "type": "uint256"},
            {"name": "arg2", "type": "uint256"},
            {"name": "arg3", "type": "uint256"},
        ],
        "name": "logQuadruple",
        "outputs": [],
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"name": "which", "type": "uint8"},
            {"name": "arg0", "type": "uint256"},
            {"name": "arg1", "type": "uint256"},
        ],
        "name": "logDouble",
        "outputs": [],
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"name": "which", "type": "uint8"},
            {"name": "arg0", "type": "uint256"},
            {"name": "arg1", "type": "uint256"},
            {"name": "arg2", "type": "uint256"},
        ],
        "name": "logTriple",
        "outputs": [],
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [
            {"name": "which", "type": "uint8"},
            {"name": "arg0", "type": "uint256"},
        ],
        "name": "logSingle",
        "outputs": [],
        "type": "function",
    },
    {
        "constant": False,
        "inputs": [{"name": "v", "type": "bytes"}],
        "name": "logBytes",
        "outputs": [],
        "type": "function",
    },
    {
        "anonymous": True,
        "inputs": [],
        "name": "LogAnonymous",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [],
        "name": "LogNoArguments",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [{"indexed": False, "name": "arg0", "type": "uint256"}],
        "name": "LogSingleArg",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": False, "name": "arg0", "type": "uint256"},
            {"indexed": False, "name": "arg1", "type": "uint256"},
        ],
        "name": "LogDoubleArg",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": False, "name": "arg0", "type": "uint256"},
            {"indexed": False, "name": "arg1", "type": "uint256"},
            {"indexed": False, "name": "arg2", "type": "uint256"},
        ],
        "name": "LogTripleArg",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": False, "name": "arg0", "type": "uint256"},
            {"indexed": False, "name": "arg1", "type": "uint256"},
            {"indexed": False, "name": "arg2", "type": "uint256"},
            {"indexed": False, "name": "arg3", "type": "uint256"},
        ],
        "name": "LogQuadrupleArg",
        "type": "event",
    },
    {
        "anonymous": True,
        "inputs": [{"indexed": True, "name": "arg0", "type": "uint256"}],
        "name": "LogSingleAnonymous",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [{"indexed": True, "name": "arg0", "type": "uint256"}],
        "name": "LogSingleWithIndex",
        "type": "event",
    },
    {
        "anonymous": True,
        "inputs": [
            {"indexed": False, "name": "arg0", "type": "uint256"},
            {"indexed": True, "name": "arg1", "type": "uint256"},
        ],
        "name": "LogDoubleAnonymous",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": False, "name": "arg0", "type": "uint256"},
            {"indexed": True, "name": "arg1", "type": "uint256"},
        ],
        "name": "LogDoubleWithIndex",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": False, "name": "arg0", "type": "uint256"},
            {"indexed": True, "name": "arg1", "type": "uint256"},
            {"indexed": True, "name": "arg2", "type": "uint256"},
        ],
        "name": "LogTripleWithIndex",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": False, "name": "arg0", "type": "uint256"},
            {"indexed": False, "name": "arg1", "type": "uint256"},
            {"indexed": True, "name": "arg2", "type": "uint256"},
            {"indexed": True, "name": "arg3", "type": "uint256"},
        ],
        "name": "LogQuadrupleWithIndex",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [{"indexed": False, "name": "v", "type": "bytes"}],
        "name": "LogBytes",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [{"indexed": False, "name": "v", "type": "string"}],
        "name": "LogString",
        "type": "event",
    },
]


EMITTER_ENUM = {
    'LogAnonymous': 0,
    'LogNoArguments': 1,
    'LogSingleArg': 2,
    'LogDoubleArg': 3,
    'LogTripleArg': 4,
    'LogQuadrupleArg': 5,
    'LogSingleAnonymous': 6,
    'LogSingleWithIndex': 7,
    'LogDoubleAnonymous': 8,
    'LogDoubleWithIndex': 9,
    'LogTripleWithIndex': 10,
    'LogQuadrupleWithInde': 11,
}
