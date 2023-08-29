from eth_utils import (
    ValidationError,
)
import idna


class ENSException(Exception):
    """
    Base class for all ENS Errors
    """

    pass


class AddressMismatch(ENSException):
    """
    In order to set up reverse resolution correctly, the ENS name should first
    point to the address. This exception is raised if the name does
    not currently point to the address.
    """

    pass


class InvalidName(idna.IDNAError, ENSException):
    """
    This exception is raised if the provided name does not meet
    the normalization standards specified in `ENSIP-15
    <https://docs.ens.domains/ens-improvement-proposals/ensip-15-normalization-standard>`_.
    """

    pass


class UnauthorizedError(ENSException):
    """
    Raised if the sending account is not the owner of the name
    you are trying to modify. Make sure to set ``from`` in the
    ``transact`` keyword argument to the owner of the name.
    """

    pass


class UnownedName(ENSException):
    """
    Raised if you are trying to modify a name that no one owns.

    If working on a subdomain, make sure the subdomain gets created
    first with :meth:`~ens.ENS.setup_address`.
    """

    pass


class ResolverNotFound(ENSException):
    """
    Raised if no resolver was found for the name you are trying to resolve.
    """

    pass


class UnsupportedFunction(ENSException):
    """
    Raised if a resolver does not support a particular method.
    """

    pass


class BidTooLow(ENSException):
    """
    Raised if you bid less than the minimum amount
    """

    pass


class InvalidBidHash(ENSException):
    """
    Raised if you supply incorrect data to generate the bid hash.
    """

    pass


class InvalidLabel(ENSException):
    """
    Raised if you supply an invalid label
    """

    pass


class OversizeTransaction(ENSException):
    """
    Raised if a transaction you are trying to create would cost so
    much gas that it could not fit in a block.

    For example: when you try to start too many auctions at once.
    """

    pass


class UnderfundedBid(ENSException):
    """
    Raised if you send less wei with your bid than you declared
    as your intent to bid.
    """

    pass


class ENSValidationError(ENSException, ValidationError):
    """
    Raised if there is a validation error
    """
