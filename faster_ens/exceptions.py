from typing import (
    final,
)

import idna
from mypy_extensions import (
    mypyc_attr,
)


@mypyc_attr(native_class=False)
class ENSException(Exception):
    """
    Base class for all ENS Errors
    """


@final
class ENSValueError(ENSException, ValueError):
    """
    An ENS exception wrapper for `ValueError`, for better control over
    exception handling.
    """


@final
@mypyc_attr(native_class=False)
class ENSTypeError(ENSException, TypeError):
    """
    An ENS exception wrapper for `TypeError`, for better control over
    exception handling.
    """


@final
class AddressMismatch(ENSException):
    """
    In order to set up reverse resolution correctly, the ENS name should first
    point to the address. This exception is raised if the name does
    not currently point to the address.
    """


@final
@mypyc_attr(native_class=False)
class InvalidName(idna.IDNAError, ENSException):
    """
    Raised if the provided name does not meet the normalization
    standards specified in `ENSIP-15`
    <https://docs.ens.domains/ens-improvement-proposals/ensip-15-normalization-standard>`_.
    """


@final
class UnauthorizedError(ENSException):
    """
    Raised if the sending account is not the owner of the name
    you are trying to modify. Make sure to set ``from`` in the
    ``transact`` keyword argument to the owner of the name.
    """


@final
class UnownedName(ENSException):
    """
    Raised if you are trying to modify a name that no one owns.

    If working on a subdomain, make sure the subdomain gets created
    first with :meth:`~ens.ENS.setup_address`.
    """


@final
class ResolverNotFound(ENSException):
    """
    Raised if no resolver was found for the name you are trying to resolve.
    """


@final
class UnsupportedFunction(ENSException):
    """
    Raised if a resolver does not support a particular method.
    """


@final
class BidTooLow(ENSException):
    """
    Raised if you bid less than the minimum amount
    """


@final
class InvalidBidHash(ENSException):
    """
    Raised if you supply incorrect data to generate the bid hash.
    """


@final
class InvalidLabel(ENSException):
    """
    Raised if you supply an invalid label
    """


@final
class OversizeTransaction(ENSException):
    """
    Raised if a transaction you are trying to create would cost so
    much gas that it could not fit in a block.

    For example: when you try to start too many auctions at once.
    """


@final
class UnderfundedBid(ENSException):
    """
    Raised if you send less wei with your bid than you declared
    as your intent to bid.
    """


@final
class ENSValidationError(ENSException):
    """
    Raised if there is a validation error
    """
