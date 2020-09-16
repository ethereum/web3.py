
IND_EVENT_CONTRACT_CODE = (
    "6080604052348015600f57600080fd5b506101018061001f6000396000f30060806040526004361"
    "0603f576000357c0100000000000000000000000000000000000000000000000000000000900463"
    "ffffffff1680635818fad7146044575b600080fd5b348015604f57600080fd5b50606c600480360"
    "38101908080359060200190929190505050606e565b005b807ff70fe689e290d8ce2b2a388ac28d"
    "b36fbb0e16a6d89c6804c461f65a1b40bb1560405160405180910390a27f56d2ef3c5228bf5d885"
    "73621e325a4672ab50e033749a601e4f4a5e1dce905d48160405180828152602001915050604051"
    "80910390a1505600a165627a7a72305820afa2dc55cd3a55a914793a583c3284fc5f8dc8ebec94e"
    "6ec7fe1ad6d604daf350029"
)


IND_EVENT_CONTRACT_RUNTIME = (
    "608060405260043610603f576000357c01000000000000000000000000000000000000000000000"
    "00000000000900463ffffffff1680635818fad7146044575b600080fd5b348015604f57600080fd"
    "5b50606c60048036038101908080359060200190929190505050606e565b005b807ff70fe689e29"
    "0d8ce2b2a388ac28db36fbb0e16a6d89c6804c461f65a1b40bb1560405160405180910390a27f56"
    "d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d481604051808281526"
    "0200191505060405180910390a1505600a165627a7a72305820afa2dc55cd3a55a914793a583c32"
    "84fc5f8dc8ebec94e6ec7fe1ad6d604daf350029"
)


IND_EVENT_CONTRACT_ABI = [
    {
        "constant": False,
        "inputs": [
            {
                "name": "arg0",
                "type": "uint256"
            }
        ],
        "name": "logTwoEvents",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "name": "arg0",
                "type": "uint256"
            }
        ],
        "name": "LogSingleWithIndex",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "name": "arg0",
                "type": "uint256"
            }
        ],
        "name": "LogSingleArg",
        "type": "event"
    }
]
