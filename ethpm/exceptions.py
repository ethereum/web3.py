class PyEthPMException(Exception):
    """
    Base class for all Py-EthPM errors.
    """

    pass


class InsufficientAssetsError(PyEthPMException):
    """
    Raised when a Manifest or Package does not contain the required
    assets to do something.
    """

    pass


class EthPMValidationError(PyEthPMException):
    """
    Raised when something does not pass a validation check.
    """

    pass


class CannotHandleURI(PyEthPMException):
    """
    Raised when the given URI cannot be served by any of the available backends.
    """

    pass


class FailureToFetchIPFSAssetsError(PyEthPMException):
    """
    Raised when an attempt to fetch a Package's assets via IPFS failed.
    """

    pass


class BytecodeLinkingError(PyEthPMException):
    """
    Raised when an attempt to link a contract factory's bytecode failed.
    """

    pass


class ManifestBuildingError(PyEthPMException):
    """
    Raised when an attempt to build a manifest failed.
    """

    pass
