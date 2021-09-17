from enum import IntEnum


class ChainID(IntEnum):
    # Ethereum L1 networks

    MAINNET = 1
    ROPSTEN = 3
    RINKEBY = 4
    GOERLI = 5
    KOVAN = 42

    # Layer 2 networks
    OPTIMISM = 10
    XDAI = 100
    MATIC = 137

    BINANCE = 56
    RSK = 30
    TOMO = 88

