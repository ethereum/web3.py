import json

REVERT_CONTRACT_BYTECODE = "608060405234801561001057600080fd5b5060f08061001f6000396000f3fe6080604052348015600f57600080fd5b5060043610603c5760003560e01c8063185c38a4146041578063c06a97cb146049578063d67e4b8414604f575b600080fd5b60476069565b005b6047603c565b605560b6565b604080519115158252519081900360200190f35b6040805162461bcd60e51b815260206004820152601b60248201527f46756e6374696f6e20686173206265656e2072657665727465642e0000000000604482015290519081900360640190fd5b60019056fea265627a7a723158202b5d1c5df2d5450324be8ee1af3ef7098f4b4acf5df16b1cb3cc86d4c48aa95664736f6c63430005100032"


REVERT_CONTRACT_RUNTIME_CODE = "6080604052348015600f57600080fd5b5060043610603c5760003560e01c8063185c38a4146041578063c06a97cb146049578063d67e4b8414604f575b600080fd5b60476069565b005b6047603c565b605560b6565b604080519115158252519081900360200190f35b6040805162461bcd60e51b815260206004820152601b60248201527f46756e6374696f6e20686173206265656e2072657665727465642e0000000000604482015290519081900360640190fd5b60019056fea26469706673582212204e6819701a04acfefd5a4b75221d095cac98d0a467116e264d73f1b3dc239b9064736f6c63430006010033"  # noqa: E501


_REVERT_CONTRACT_ABI = json.loads('''[
    {
        "constant": true,
        "inputs": [],
        "name": "normalFunction",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "revertWithMessage",
        "outputs": [],
        "payable": false,
        "stateMutability": "pure",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "revertWithoutMessage",
        "outputs": [],
        "payable": false,
        "stateMutability": "pure",
        "type": "function"
    }
]''')


REVERT_CONTRACT_SOURCE = """
pragma solidity ^0.6.1;

contract RevertContract {
  function normalFunction() public pure returns (bool) {
      return true;
  }

  function revertWithMessage() public pure {
      revert('Function has been reverted.');
  }

  function revertWithoutMessage() public pure {
      revert();
  }
}
"""
