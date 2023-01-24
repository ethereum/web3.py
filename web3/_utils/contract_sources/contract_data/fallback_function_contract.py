"""
Generated by `compile_contracts.py` script.
Compiled with Solidity v0.8.17.
"""

# source: web3/_utils/contract_sources/FallbackFunctionContract.sol:FallbackFunctionContract  # noqa: E501
FALLBACK_FUNCTION_CONTRACT_BYTECODE = "0x60806040526000808190555060be806100196000396000f3fe6080604052348015600f57600080fd5b5060043610602b5760003560e01c80633bc5de3014603557602c565b5b60016000819055005b603b604f565b60405160469190606f565b60405180910390f35b60008054905090565b6000819050919050565b6069816058565b82525050565b6000602082019050608260008301846062565b9291505056fea2646970667358221220e68e49e1327532e8eeed55e60110d01e6d3f2ea93607400e02eb7d30766f3c3e64736f6c63430008110033"  # noqa: E501
FALLBACK_FUNCTION_CONTRACT_RUNTIME = "0x6080604052348015600f57600080fd5b5060043610602b5760003560e01c80633bc5de3014603557602c565b5b60016000819055005b603b604f565b60405160469190606f565b60405180910390f35b60008054905090565b6000819050919050565b6069816058565b82525050565b6000602082019050608260008301846062565b9291505056fea2646970667358221220e68e49e1327532e8eeed55e60110d01e6d3f2ea93607400e02eb7d30766f3c3e64736f6c63430008110033"  # noqa: E501
FALLBACK_FUNCTION_CONTRACT_ABI = [
    {"inputs": [], "stateMutability": "payable", "type": "constructor"},
    {"stateMutability": "nonpayable", "type": "fallback"},
    {
        "inputs": [],
        "name": "getData",
        "outputs": [{"internalType": "uint256", "name": "r", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
]
FALLBACK_FUNCTION_CONTRACT_DATA = {
    "bytecode": FALLBACK_FUNCTION_CONTRACT_BYTECODE,
    "bytecode_runtime": FALLBACK_FUNCTION_CONTRACT_RUNTIME,
    "abi": FALLBACK_FUNCTION_CONTRACT_ABI,
}
