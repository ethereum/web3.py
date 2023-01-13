from eth_utils import (
    ValidationError,
)


class EthPMException(Exception):
    """
    Base class for all Py-EthPM errors.
    """

    pass


class InsufficientAssetsError(EthPMException):
    """
    Raised when a Manifest or Package does not contain the required
    assets to do something.
    """

    pass


class EthPMValidationError(EthPMException, ValidationError):
    """
    Raised when something does not pass a validation check.
    """

    pass


class CannotHandleURI(EthPMException):
    """
    Raised when the given URI cannot be served by any of the available backends.
    """

    pass


class FailureToFetchIPFSAssetsError(EthPMException):
    """
    Raised when an attempt to fetch a Package's assets via IPFS failed.
    """

    pass


class BytecodeLinkingError(EthPMException):
    """
    Raised when an attempt to link a contract factory's bytecode failed.
    """

    pass


class ManifestBuildingError(EthPMException):
    """
    Raised when an attempt to build a manifest failed.
    """

    pass


class ManifestValidationError(EthPMException):
    """
    Raised when a provided manifest cannot be published, since it's invalid.
    """

    pass
