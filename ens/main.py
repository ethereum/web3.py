
from eth_utils import (
    is_address,
    to_checksum_address,
)

from ens import abis

from ens.constants import (
    EMPTY_ADDR_HEX,
    REVERSE_REGISTRAR_DOMAIN,
)

from ens.exceptions import (
    AddressMismatch,
    UnauthorizedError,
    UnownedName,
)

from ens.registrar import Registrar

from ens.utils import (
    Web3,
    address_in,
    address_to_reverse_domain,
    dict_copy,
    dot_eth_name,
    dot_eth_namehash,
    init_web3,
    label_to_hash,
    normalize_name,
)

ENS_MAINNET_ADDR = '0x314159265dd8dbb310642f98f50c066173c1259b'

default = object()


class ENS:
    '''
    Quick access to common Ethereum Name Service functions,
    like getting the address for a name.

    Unless otherwise specified, all addresses are assumed to be a ``str`` in
    `checksum format <https://github.com/ethereum/EIPs/blob/master/EIPS/eip-155.md>`_,
    like: ``"0x314159265dD8dbb310642f98f50C066173C1259b"``
    '''

    labelhash = staticmethod(label_to_hash)
    namehash = staticmethod(dot_eth_namehash)
    nameprep = staticmethod(normalize_name)
    reverse_domain = staticmethod(address_to_reverse_domain)

    def __init__(self, providers=None, addr=None):
        '''
        :param providers: a list or single provider used to connect to Ethereum
        :type providers: instance of `web3.providers.base.BaseProvider`
        :param hex-string addr: the address of the ENS registry on-chain. If not provided,
            ENS.py will default to the mainnet ENS registry address.
        '''
        self.web3 = init_web3(providers)

        ens_addr = addr if addr else ENS_MAINNET_ADDR
        self.ens = self.web3.eth.contract(abi=abis.ENS, address=ens_addr)
        self._resolverContract = self.web3.eth.contract(abi=abis.RESOLVER)
        self.registrar = Registrar(self)

    @classmethod
    def fromWeb3(cls, web3, addr=None):
        '''
        Generate an ENS instance with web3

        :param `web3.Web3` web3: to infer connection information
        :param hex-string addr: the address of the ENS registry on-chain. If not provided,
            ENS.py will default to the mainnet ENS registry address.
        '''
        return cls(web3.manager.providers, addr=addr)

    def address(self, name):
        '''
        Look up the Ethereum address that name currently points to.

        :param str name: an ENS name to look up
        :raises InvalidName: if ``name`` has invalid syntax
        '''
        return self.resolve(name, 'addr')

    def name(self, address):
        '''
        Look up the name that the address points to, using a
        reverse lookup. Reverse lookup is opt-in for name owners.

        :param address:
        :type address: hex string
        '''
        reversed_domain = address_to_reverse_domain(address)
        return self.resolve(reversed_domain, get='name')
    reverse = name

    @dict_copy
    def setup_address(self, name, address=default, transact={}):
        '''
        Set up the name to point to the supplied address.
        The sender of the transaction must own the name, or
        its parent name.

        Example: If the caller owns ``parentname.eth`` with no subdomains
        and calls this method with ``sub.parentname.eth``,
        then ``sub`` will be created as part of this call.

        :param str name: ENS name to set up
        :param address: name will point to this address. If ``None``, set resolver to empty addr.
            If not specified, name will point to the owner's address.
        :param dict transact: the transaction configuration, like in
            `web3.eth.sendTransaction`
        :raises InvalidName: if ``name`` has invalid syntax
        :raises UnauthorizedError: if ``from`` in ``transact`` does not own ``name``
        '''
        owner = self.setup_owner(name, transact=transact)
        self._assert_control(owner, name)
        if address is default:
            address = owner
        elif not address:
            address = EMPTY_ADDR_HEX
        if self.address(name) == to_checksum_address(address):
            return None
        transact['from'] = owner
        resolver = self._set_resolver(name, transact=transact)
        if isinstance(address, str):
            address = Web3().toBytes(hexstr=address)
        else:
            address = Web3().toBytes(address)
        return resolver.setAddr(dot_eth_namehash(name), address, transact=transact)

    @dict_copy
    def setup_name(self, name, address=None, transact={}):
        '''
        Set up the address for reverse lookup, aka "caller ID".
        After successful setup, the method `~ens.main.ENS.name` will return
        ``name`` when supplied with ``address``.

        :param str name: ENS name that address will point to
        :param address: to set up
        :param dict transact: the transaction configuration, like in
            `web3.eth.sendTransaction`
        :raises AddressMismatch: if the name does not already point to the address
        :raises InvalidName: if ``name`` has invalid syntax
        :raises UnauthorizedError: if ``'from'`` in `transact` does not own `name`
        :raises UnownedName: if no one owns `name`
        '''
        if not name:
            self._assert_control(address, 'the reverse record')
            return self._setup_reverse(None, address, transact=transact)
        else:
            resolved = self.address(name)
            if not address:
                address = resolved
            elif resolved and address != resolved:
                raise AddressMismatch(
                    "Could not set address %r to point to name, because the name resolves to %r. "
                    "To change the name for an existing address, call setup_address() first." % (
                        address, resolved
                    )
                )
            if not address:
                address = self.owner(name)
            if not address:
                raise UnownedName("claim subdomain using setup_address() first")
            self._assert_control(address, name)
            if not resolved:
                self.setup_address(name, address, transact=transact)
            return self._setup_reverse(name, address, transact=transact)

    def resolve(self, name, get='addr'):
        resolver = self.resolver(name)
        if resolver:
            lookup_function = getattr(resolver, get)
            resolved = lookup_function(dot_eth_namehash(name))
            if is_address(resolved):
                resolved = to_checksum_address(resolved)
            return resolved
        else:
            return None

    def resolver(self, name):
        resolver_addr = self.ens.resolver(dot_eth_namehash(name))
        if not resolver_addr:
            return None
        return self._resolverContract(address=resolver_addr)

    def reverser(self, target_address):
        reversed_domain = address_to_reverse_domain(target_address)
        return self.resolver(reversed_domain)

    def owner(self, name):
        '''
        Get the owner of a name. Note that this may be different from the
        deed holder in the '.eth' registrar. To find out the deed owner,
        see :meth:`ens.registrar.Registrar.entries`. Learn more about the difference
        between deed and name ownership in the ENS `Managing Ownership docs
        <http://docs.ens.domains/en/latest/userguide.html#managing-ownership>`_

        :param str name: ENS name to look up
        :return: owner address
        :rtype: str
        '''
        node = dot_eth_namehash(name)
        return self.ens.owner(node)

    @dict_copy
    def setup_owner(self, name, new_owner=default, transact={}):
        '''
        Set the owner of the supplied name to ``new_owner``.

        For typical scenarios, you'll never need to call this method directly,
        simply call :meth:`setup_name` or :meth:`setup_address`. This method does *not*
        set up the name to point to an address.

        If ``new_owner`` is not supplied, then this will assume you
        want the same owner as the parent domain.

        If the caller owns ``parentname.eth`` with no subdomains
        and calls this method with ``sub.parentname.eth``,
        then ``sub`` will be created as part of this call.

        :param str name: ENS name to set up
        :param new_owner: account that will own ``name``. If ``None``, set owner to empty addr.
            If not specified, name will point to the parent domain owner's address.
        :param dict transact: the transaction configuration, like in
            :meth:`web3.eth.Eth.sendTransaction`
        :raises InvalidName: if ``name`` has invalid syntax
        :raises UnauthorizedError: if ``from`` in ``transact`` does not own ``name``
        :returns: the new owner's address
        '''
        (super_owner, unowned, owned) = self._first_owner(name)
        if new_owner is default:
            new_owner = super_owner
        elif not new_owner:
            new_owner = EMPTY_ADDR_HEX
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

    def _assert_control(self, account, name, parent_owned=None):
        if not address_in(account, self.web3.eth.accounts):
            raise UnauthorizedError(
                "in order to modify %r, you must control account %r, which owns %r" % (
                    name, account, parent_owned or name
                )
            )

    def _first_owner(self, name):
        '''
        Takes a name, and returns the owner of the deepest subdomain that has an owner

        :returns: (owner or None, list(unowned_subdomain_labels), first_owned_domain)
        '''
        owner = None
        unowned = []
        pieces = dot_eth_name(name).split('.')
        while pieces and not owner:
            name = '.'.join(pieces)
            owner = self.owner(name)
            if not owner:
                unowned.append(pieces.pop(0))
        return (owner, unowned, name)

    @dict_copy
    def _claim_ownership(self, owner, unowned, owned, old_owner=None, transact={}):
        transact['from'] = old_owner or owner
        for label in reversed(unowned):
            self.ens.setSubnodeOwner(
                dot_eth_namehash(owned),
                label_to_hash(label),
                owner,
                transact=transact
            )
            owned = "%s.%s" % (label, owned)

    @dict_copy
    def _set_resolver(self, name, resolver_addr=None, transact={}):
        if not resolver_addr:
            resolver_addr = self.address('resolver.eth')
        namehash = dot_eth_namehash(name)
        if self.ens.resolver(namehash) != resolver_addr:
            self.ens.setResolver(
                namehash,
                Web3().toBytes(hexstr=resolver_addr),
                transact=transact
            )
        return self._resolverContract(address=resolver_addr)

    @dict_copy
    def _setup_reverse(self, name, address, transact={}):
        if name:
            name = dot_eth_name(name)
        else:
            name = ''
        transact['from'] = address
        return self._reverse_registrar().setName(name, transact=transact)

    def _reverse_registrar(self):
        addr = self.ens.owner(dot_eth_namehash(REVERSE_REGISTRAR_DOMAIN))
        return self.web3.eth.contract(address=addr, abi=abis.REVERSE_REGISTRAR)
