class PytestEthereumError(Exception):
    """
    Base class for all Pytest-Ethereum errors.
    """

    pass


class DeployerError(PytestEthereumError):
    """
    Raised when the Deployer is unable to deploy a contract type.
    """

    pass


class LinkerError(PytestEthereumError):
    """
    Raised when the Linker is unable to link two contract types.
    """

    pass
