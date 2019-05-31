
EVNT_CONTRACT_CODE = (
    "6080604052348015600f57600080fd5b5061010b8061001f6000396000f30060806040526004361"
    "0603f576000357c0100000000000000000000000000000000000000000000000000000000900463"
    "ffffffff1680635818fad7146044575b600080fd5b348015604f57600080fd5b50606c600480360"
    "38101908080359060200190929190505050606e565b005b7ff70fe689e290d8ce2b2a388ac28db3"
    "6fbb0e16a6d89c6804c461f65a1b40bb15816040518082815260200191505060405180910390a17"
    "f56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce905d481604051808281"
    "5260200191505060405180910390a1505600a165627a7a72305820ff79430a04cf654d7b46edc52"
    "9ccaa5d7f77607f54bb58210be0c48455292c810029"
)


EVNT_CONTRACT_RUNTIME = (
    "608060405260043610603f576000357c01000000000000000000000000000000000000000000000"
    "00000000000900463ffffffff1680635818fad7146044575b600080fd5b348015604f57600080fd"
    "5b50606c60048036038101908080359060200190929190505050606e565b005b7ff70fe689e290d"
    "8ce2b2a388ac28db36fbb0e16a6d89c6804c461f65a1b40bb158160405180828152602001915050"
    "60405180910390a17f56d2ef3c5228bf5d88573621e325a4672ab50e033749a601e4f4a5e1dce90"
    "5d4816040518082815260200191505060405180910390a1505600a165627a7a72305820ff79430a"
    "04cf654d7b46edc529ccaa5d7f77607f54bb58210be0c48455292c810029"
)


EVNT_CONTRACT_ABI = [
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
                "indexed": False,
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
