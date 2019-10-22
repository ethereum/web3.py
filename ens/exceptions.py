import idna


class ENSError(Exception):
    """
    Base class for all ENS Errors
    """

    pass


class AddressMismatch(ENSError):
    """
    In order to set up reverse resolution correctly, the ENS name should first
    point to the address. This exception is raised if the name does
    not currently point to the address.
    """

    pass


class InvalidName(idna.IDNAError, ENSError):
    """
    This exception is raised if the provided name does not meet
    the syntax standards specified in `EIP 137 name syntax
    <https://github.com/ethereum/EIPs/blob/master/EIPS/eip-137.md#name-syntax>`_.

    For example: names may not start with a dot, or include a space.
    """

    pass


class UnauthorizedError(ENSError):
    """
    Raised if the sending account is not the owner of the name
    you are trying to modify. Make sure to set ``from`` in the
    ``transact`` keyword argument to the owner of the name.
    """

    pass


class UnownedName(ENSError):
    """
    Raised if you are trying to modify a name that no one owns.

    If working on a subdomain, make sure the subdomain gets created
    first with :meth:`~ens.ENS.setup_address`.
    """

    pass


class ResolverNotFound(ENSError):
    """
    Raised if no resolver was found for the name you are trying to resolve.
    """

    pass


class UnsupportedFunction(ENSError):
    """
    Raised if a resolver does not support a particular method.
    """

    pass


class BidTooLow(ENSError):
    """
    Raised if you bid less than the minimum amount
    """

    pass


class InvalidBidHash(ENSError):
    """
    Raised if you supply incorrect data to generate the bid hash.
    """

    pass


class InvalidLabel(ENSError):
    """
    Raised if you supply an invalid label
    """

    pass


class OversizeTransaction(ENSError):
    """
    Raised if a transaction you are trying to create would cost so
    much gas that it could not fit in a block.

    For example: when you try to start too many auctions at once.
    """

    pass


class UnderfundedBid(ENSError):
    """
    Raised if you send less wei with your bid than you declared
    as your intent to bid.
    """

    pass
