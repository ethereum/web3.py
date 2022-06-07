from copy import (
    deepcopy,
)
from functools import (
    wraps,
)
from typing import (
    TYPE_CHECKING,
    Optional,
    Sequence,
    Tuple,
    Union,
    cast,
)
import warnings

from eth_typing import (
    Address,
    ChecksumAddress,
    HexAddress,
)
from eth_utils import (
    is_binary_address,
    is_checksum_address,
    to_checksum_address,
)
from eth_utils.toolz import (
    merge,
)
from hexbytes import (
    HexBytes,
)

from ens import abis
from ens.constants import (
    EMPTY_ADDR_HEX,
    ENS_MAINNET_ADDR,
    REVERSE_REGISTRAR_DOMAIN,
)
from ens.exceptions import (
    AddressMismatch,
    UnauthorizedError,
    UnownedName,
)
from ens.utils import (
    address_in,
    address_to_reverse_domain,
    default,
    init_web3,
    is_none_or_zero_address,
    is_valid_name,
    label_to_hash,
    normal_name_to_hash,
    normalize_name,
    raw_name_to_hash,
)

if TYPE_CHECKING:
    from web3 import Web3  # noqa: F401
    from web3.contract import (  # noqa: F401
        Contract,
    )
    from web3.providers import (  # noqa: F401
        BaseProvider,
    )
    from web3.types import (  # noqa: F401
        Middleware,
        TxParams,
    )


class ENS:
    """
    Quick access to common Ethereum Name Service functions,
    like getting the address for a name.

    Unless otherwise specified, all addresses are assumed to be a `str` in
    `checksum format <https://github.com/ethereum/EIPs/blob/master/EIPS/eip-155.md>`_,
    like: ``"0x314159265dD8dbb310642f98f50C066173C1259b"``
    """

    @staticmethod
    @wraps(label_to_hash)
    def labelhash(label: str) -> HexBytes:
        return label_to_hash(label)

    @staticmethod
    @wraps(raw_name_to_hash)
    def namehash(name: str) -> HexBytes:
        return raw_name_to_hash(name)

    @staticmethod
    @wraps(normalize_name)
    def nameprep(name: str) -> str:
        return normalize_name(name)

    @staticmethod
    @wraps(is_valid_name)
    def is_valid_name(name: str) -> bool:
        return is_valid_name(name)

    @staticmethod
    @wraps(address_to_reverse_domain)
    def reverse_domain(address: ChecksumAddress) -> str:
        return address_to_reverse_domain(address)

    def __init__(
        self,
        provider: 'BaseProvider' = cast('BaseProvider', default),
        addr: ChecksumAddress = None,
        middlewares: Optional[Sequence[Tuple['Middleware', str]]] = None,
    ) -> None:
        """
        :param provider: a single provider used to connect to Ethereum
        :type provider: instance of `web3.providers.base.BaseProvider`
        :param hex-string addr: the address of the ENS registry on-chain. If not provided,
            ENS.py will default to the mainnet ENS registry address.
        """
        self.web3 = init_web3(provider, middlewares)

        ens_addr = addr if addr else ENS_MAINNET_ADDR
        self.ens = self.web3.eth.contract(abi=abis.ENS, address=ens_addr)
        self._resolverContract = self.web3.eth.contract(abi=abis.RESOLVER)

    @classmethod
    def fromWeb3(cls, web3: 'Web3', addr: ChecksumAddress = None) -> 'ENS':
        """
        Generate an ENS instance with web3

        :param `web3.Web3` web3: to infer connection information
        :param hex-string addr: the address of the ENS registry on-chain. If not provided,
            ENS.py will default to the mainnet ENS registry address.
        """
        provider = web3.manager.provider
        middlewares = web3.middleware_onion.middlewares
        return cls(provider, addr=addr, middlewares=middlewares)

    def address(self, name: str) -> Optional[ChecksumAddress]:
        """
        Look up the Ethereum address that `name` currently points to.

        :param str name: an ENS name to look up
        :raises InvalidName: if `name` has invalid syntax
        """
        return cast(ChecksumAddress, self.resolve(name, 'addr'))

    def name(
        self,
        address: ChecksumAddress,
        strict: bool = False
    ) -> Optional[str]:
        """
        Look up the name that the address points to, using a
        reverse lookup. Reverse lookup is opt-in for name owners.

        :param hex-string address: the address to look up
        :param bool strict: perform a strict check which will confirm that forward and
            reverse resolution matches
        """
        reversed_domain = address_to_reverse_domain(address)
        name = self.resolve(reversed_domain, get="name")

        if strict:
            return name if to_checksum_address(address) == self.address(name) else None

        return name

    def setup_address(
        self,
        name: str,
        address: Union[Address, ChecksumAddress, HexAddress] = cast(ChecksumAddress, default),
        transact: Optional["TxParams"] = None
    ) -> HexBytes:
        """
        Set up the name to point to the supplied address.
        The sender of the transaction must own the name, or
        its parent name.

        Example: If the caller owns ``parentname.eth`` with no subdomains
        and calls this method with ``sub.parentname.eth``,
        then ``sub`` will be created as part of this call.

        :param str name: ENS name to set up
        :param str address: name will point to this address, in checksum format. If ``None``,
            erase the record. If not specified, name will point to the owner's address.
        :param dict transact: the transaction configuration, like in
            :meth:`~web3.eth.Eth.send_transaction`
        :raises InvalidName: if ``name`` has invalid syntax
        :raises UnauthorizedError: if ``'from'`` in `transact` does not own `name`
        """
        if not transact:
            transact = {}
        transact = deepcopy(transact)
        owner = self.setup_owner(name, transact=transact)
        self._assert_control(owner, name)
        if is_none_or_zero_address(address):
            address = None
        elif address is default:
            address = owner
        elif is_binary_address(address):
            address = to_checksum_address(cast(str, address))
        elif not is_checksum_address(address):
            raise ValueError("You must supply the address in checksum format")
        if self.address(name) == address:
            return None
        if address is None:
            address = EMPTY_ADDR_HEX
        transact['from'] = owner
        resolver: 'Contract' = self._set_resolver(name, transact=transact)
        return resolver.functions.setAddr(raw_name_to_hash(name), address).transact(transact)

    def setup_name(
        self,
        name: str,
        address: Optional[ChecksumAddress] = None,
        transact: Optional["TxParams"] = None
    ) -> HexBytes:
        """
        Set up the address for reverse lookup, aka "caller ID".
        After successful setup, the method :meth:`~ens.main.ENS.name` will return
        `name` when supplied with `address`.

        :param str name: ENS name that address will point to
        :param str address: to set up, in checksum format
        :param dict transact: the transaction configuration, like in
            :meth:`~web3.eth.send_transaction`
        :raises AddressMismatch: if the name does not already point to the address
        :raises InvalidName: if `name` has invalid syntax
        :raises UnauthorizedError: if ``'from'`` in `transact` does not own `name`
        :raises UnownedName: if no one owns `name`
        """
        if not transact:
            transact = {}
        transact = deepcopy(transact)
        if not name:
            self._assert_control(address, 'the reverse record')
            return self._setup_reverse(None, address, transact=transact)
        else:
            resolved = self.address(name)
            if is_none_or_zero_address(address):
                address = resolved
            elif resolved and address != resolved and resolved != EMPTY_ADDR_HEX:
                raise AddressMismatch(
                    "Could not set address %r to point to name, because the name resolves to %r. "
                    "To change the name for an existing address, call setup_address() first." % (
                        address, resolved
                    )
                )
            if is_none_or_zero_address(address):
                address = self.owner(name)
            if is_none_or_zero_address(address):
                raise UnownedName("claim subdomain using setup_address() first")
            if is_binary_address(address):
                address = to_checksum_address(address)
            if not is_checksum_address(address):
                raise ValueError("You must supply the address in checksum format")
            self._assert_control(address, name)
            if not resolved:
                self.setup_address(name, address, transact=transact)
            return self._setup_reverse(name, address, transact=transact)

    def resolve(self, name: str, get: str = 'addr') -> Optional[Union[ChecksumAddress, str]]:
        warnings.warn(
            "In v6, the `ENS.resolve()` method will be made internal and renamed to "
            "`_resolve()`. It is recommended to use the abstracted resolve functionality of "
            "`ENS.address()` for forward resolution, and `ENS.name()` for reverse resolution "
            "instead.",
            category=DeprecationWarning,
        )

        normal_name = normalize_name(name)
        resolver = self.resolver(normal_name)
        if resolver:
            lookup_function = getattr(resolver.functions, get)
            namehash = normal_name_to_hash(normal_name)
            address = lookup_function(namehash).call()
            if is_none_or_zero_address(address):
                return None
            return address
        else:
            return None

    def resolver(self, normal_name: str = None, name: str = None) -> Optional['Contract']:
        if not name:
            warnings.warn(
                "The function signature for resolver() will change in v6 to accept `name` as a "
                "the positional argument, over `normal_name`, and the method will instead "
                "normalize the name internally. You may migrate to using `name` by passing it in "
                "as a keyword, e.g. resolver(name=\"ensname.eth\").",
                category=FutureWarning,
            )
        else:
            if normal_name:
                raise TypeError(
                    "Only supply one positional argument or the `name` keyword, e.g. "
                    "resolver(\"ensname.eth\") or resolver(name=\"ensname.eth\")."
                )
            normal_name = normalize_name(name)

        resolver_addr = self.ens.caller.resolver(normal_name_to_hash(normal_name))
        if is_none_or_zero_address(resolver_addr):
            return None
        return self._resolverContract(address=resolver_addr)

    def reverser(self, target_address: ChecksumAddress) -> Optional['Contract']:
        reversed_domain = address_to_reverse_domain(target_address)
        return self.resolver(reversed_domain)

    def owner(self, name: str) -> ChecksumAddress:
        """
        Get the owner of a name. Note that this may be different from the
        deed holder in the '.eth' registrar. Learn more about the difference
        between deed and name ownership in the ENS `Managing Ownership docs
        <http://docs.ens.domains/en/latest/userguide.html#managing-ownership>`_

        :param str name: ENS name to look up
        :return: owner address
        :rtype: str
        """
        node = raw_name_to_hash(name)
        return self.ens.caller.owner(node)

    def get_text(self, name: str, key: str) -> str:
        """
        Get the value of a text record by key from an ENS name.

        :param str name: ENS name to look up
        :param str key: ENS name's text record key
        :return:  ENS name's text record value
        :rtype: str
        :raises UnownedName: if no one owns `name`
        """
        node = raw_name_to_hash(name)
        normal_name = normalize_name(name)

        r = self.resolver(normal_name)
        if r:
            return r.caller.text(node, key)
        else:
            raise UnownedName("claim domain using setup_address() first")

    def set_text(
        self,
        name: str,
        key: str,
        value: str,
        transact: "TxParams" = {}
    ) -> HexBytes:
        """
        Set the value of a text record of an ENS name.

        :param str name: ENS name
        :param str key: Name of the attribute to set
        :param str value: Value to set the attribute to
        :param dict transact: the transaction configuration, like in
            :meth:`~web3.eth.Eth.send_transaction`
        :return: Transaction hash
        :rtype: HexBytes
        :raises UnownedName: if no one owns `name`
        """
        owner = self.owner(name)
        node = raw_name_to_hash(name)
        normal_name = normalize_name(name)

        transaction_dict = merge({'from': owner}, transact)

        r = self.resolver(normal_name)
        if r:
            return r.functions.setText(node, key, value).transact(transaction_dict)
        else:
            raise UnownedName("claim domain using setup_address() first")

    def setup_owner(
        self,
        name: str,
        new_owner: ChecksumAddress = cast(ChecksumAddress, default),
        transact: Optional["TxParams"] = None
    ) -> ChecksumAddress:
        """
        Set the owner of the supplied name to `new_owner`.

        For typical scenarios, you'll never need to call this method directly,
        simply call :meth:`setup_name` or :meth:`setup_address`. This method does *not*
        set up the name to point to an address.

        If `new_owner` is not supplied, then this will assume you
        want the same owner as the parent domain.

        If the caller owns ``parentname.eth`` with no subdomains
        and calls this method with ``sub.parentname.eth``,
        then ``sub`` will be created as part of this call.

        :param str name: ENS name to set up
        :param new_owner: account that will own `name`. If ``None``, set owner to empty addr.
            If not specified, name will point to the parent domain owner's address.
        :param dict transact: the transaction configuration, like in
            :meth:`~web3.eth.Eth.send_transaction`
        :raises InvalidName: if `name` has invalid syntax
        :raises UnauthorizedError: if ``'from'`` in `transact` does not own `name`
        :returns: the new owner's address
        """
        if not transact:
            transact = {}
        transact = deepcopy(transact)
        (super_owner, unowned, owned) = self._first_owner(name)
        if new_owner is default:
            new_owner = super_owner
        elif not new_owner:
            new_owner = ChecksumAddress(EMPTY_ADDR_HEX)
        else:
            new_owner = to_checksum_address(new_owner)
        current_owner = self.owner(name)
        if new_owner == EMPTY_ADDR_HEX and not current_owner:
            return None
        elif current_owner == new_owner:
            return current_owner
        else:
            self._assert_control(super_owner, name, owned)
            self._claim_ownership(new_owner, unowned, owned, super_owner, transact=transact)
            return new_owner

    def _assert_control(self, account: ChecksumAddress, name: str,
                        parent_owned: Optional[str] = None) -> None:
        if not address_in(account, self.web3.eth.accounts):
            raise UnauthorizedError(
                "in order to modify %r, you must control account %r, which owns %r" % (
                    name, account, parent_owned or name
                )
            )

    def _first_owner(self, name: str) -> Tuple[Optional[ChecksumAddress], Sequence[str], str]:
        """
        Takes a name, and returns the owner of the deepest subdomain that has an owner

        :returns: (owner or None, list(unowned_subdomain_labels), first_owned_domain)
        """
        owner = None
        unowned = []
        pieces = normalize_name(name).split('.')
        while pieces and is_none_or_zero_address(owner):
            name = '.'.join(pieces)
            owner = self.owner(name)
            if is_none_or_zero_address(owner):
                unowned.append(pieces.pop(0))
        return (owner, unowned, name)

    def _claim_ownership(
        self,
        owner: ChecksumAddress,
        unowned: Sequence[str],
        owned: str,
        old_owner: Optional[ChecksumAddress] = None,
        transact: Optional["TxParams"] = None
    ) -> None:
        if not transact:
            transact = {}
        transact = deepcopy(transact)
        transact['from'] = old_owner or owner
        for label in reversed(unowned):
            self.ens.functions.setSubnodeOwner(
                raw_name_to_hash(owned),
                label_to_hash(label),
                owner
            ).transact(transact)
            owned = "%s.%s" % (label, owned)

    def _set_resolver(
        self,
        name: str,
        resolver_addr: Optional[ChecksumAddress] = None,
        transact: Optional["TxParams"] = None
    ) -> 'Contract':
        if not transact:
            transact = {}
        transact = deepcopy(transact)
        if is_none_or_zero_address(resolver_addr):
            resolver_addr = self.address('resolver.eth')
        namehash = raw_name_to_hash(name)
        if self.ens.caller.resolver(namehash) != resolver_addr:
            self.ens.functions.setResolver(
                namehash,
                resolver_addr
            ).transact(transact)
        return self._resolverContract(address=resolver_addr)

    def _setup_reverse(
        self, name: str, address: ChecksumAddress, transact: Optional["TxParams"] = None
    ) -> HexBytes:
        if not transact:
            transact = {}
        transact = deepcopy(transact)
        if name:
            name = normalize_name(name)
        else:
            name = ''
        transact['from'] = address
        return self._reverse_registrar().functions.setName(name).transact(transact)

    def _reverse_registrar(self) -> 'Contract':
        addr = self.ens.caller.owner(normal_name_to_hash(REVERSE_REGISTRAR_DOMAIN))
        return self.web3.eth.contract(address=addr, abi=abis.REVERSE_REGISTRAR)
