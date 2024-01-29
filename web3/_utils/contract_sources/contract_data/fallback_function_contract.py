"""
Generated by `compile_contracts.py` script.
Compiled with Solidity v0.8.24.
"""

# source: web3/_utils/contract_sources/FallbackFunctionContract.sol:FallbackFunctionContract  # noqa: E501
FALLBACK_FUNCTION_CONTRACT_BYTECODE = "0x60806040525f808190555060b7806100165f395ff3fe6080604052348015600e575f80fd5b50600436106029575f3560e01c80633bc5de3014603257602a565b5b60015f819055005b6038604c565b60405160439190606a565b60405180910390f35b5f8054905090565b5f819050919050565b6064816054565b82525050565b5f602082019050607b5f830184605d565b9291505056fea2646970667358221220d54b66543e94ad7d67032bda2a75a2eaa02da9e34bb7346516e2800efc239d4364736f6c63430008180033"  # noqa: E501
FALLBACK_FUNCTION_CONTRACT_RUNTIME = "0x6080604052348015600e575f80fd5b50600436106029575f3560e01c80633bc5de3014603257602a565b5b60015f819055005b6038604c565b60405160439190606a565b60405180910390f35b5f8054905090565b5f819050919050565b6064816054565b82525050565b5f602082019050607b5f830184605d565b9291505056fea2646970667358221220d54b66543e94ad7d67032bda2a75a2eaa02da9e34bb7346516e2800efc239d4364736f6c63430008180033"  # noqa: E501
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
