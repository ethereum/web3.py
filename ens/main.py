
from ens import abis

from ens.constants import EMPTY_SHA3_BYTES

from ens.exceptions import (
    AddressMismatch,
    UnauthorizedError,
    UnownedName,
)

from ens.registrar import Registrar

from ens.utils import (
    dict_copy,
    ensure_hex,
    init_web3,
    prepare_name,
)

DEFAULT_TLD = 'eth'
RECOGNIZED_TLDS = [DEFAULT_TLD, 'reverse', 'test']

ENS_MAINNET_ADDR = '0x314159265dd8dbb310642f98f50c066173c1259b'

REVERSE_REGISTRAR_DOMAIN = 'addr.reverse'


def Web3():
    from web3 import Web3
    return Web3


class ENS:
    '''
    Quick access to common Ethereum Name Service functions,
    like getting the address for a name.

    Unless otherwise specified, all addresses are assumed to be a ``str`` in
    `checksum format <https://github.com/ethereum/EIPs/blob/master/EIPS/eip-155.md>`_,
    like: ``"0x314159265dD8dbb310642f98f50C066173C1259b"``
    '''

    nameprep = staticmethod(prepare_name)

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
    def fromWeb3(cls, web3):
        '''
        Generate an ENS instance with web3

        :param `web3.Web3` web3: to infer connection information
        '''
        return cls(web3.manager.providers)

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
        reversed_domain = self.reverse_domain(address)
        return self.resolve(reversed_domain, get='name')
    reverse = name

    @dict_copy
    def setup_address(self, name, address=None, transact={}):
        '''
        Set up the name to point to the supplied address.
        The sender if the transaction must own the name, or
        its parent name.

        Example: If the caller owns ``parentname.eth`` with no subdomains
        and calls this method with ``sub.parentname.eth``,
        then ``sub`` will be created as part of this call.

        :param str name: ENS name to set up
        :param address: name will point to this
        :param dict transact: the transaction configuration, like in
            `web3.eth.sendTransaction`
        :raises InvalidName: if ``name`` has invalid syntax
        :raises UnauthorizedError: if ``from`` in ``transact`` does not own ``name``
        '''
        (owner, unowned, owned) = self._first_owner(name)
        if not address:
            address = owner
        if self.address(name) == ensure_hex(address):
            return None
        self._assert_control(owner, name, owned)
        if unowned:
            self._claim_ownership(owner, unowned, owned, transact=transact)
        transact['from'] = owner
        resolver = self._set_resolver(name, transact=transact)
        if isinstance(address, str):
            address = Web3().toBytes(hexstr=address)
        else:
            address = Web3().toBytes(address)
        return resolver.setAddr(self.namehash(name), address, transact=transact)

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
        :raises UnauthorizedError: if ``from`` in ``transact`` does not own ``name``
        '''
        resolved = self.address(name)
        if not address:
            address = resolved
        elif resolved and address != resolved:
            raise AddressMismatch(
                "To change the name for an existing address, call setup_address() first"
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
            resolved = lookup_function(self.namehash(name))
            if self.web3.isAddress(resolved):
                resolved = self.web3.toChecksumAddress(resolved)
            return resolved
        else:
            return None

    @classmethod
    def namehash(cls, name):
        '''
        Generate the namehash. In normal operation, this is handled
        behind the scenes. For advanced usage, it is a helpful utility.

        Will add '.eth' to name if no TLD given. Also, normalizes the name with
        `nameprep
        <https://github.com/ethereum/EIPs/blob/master/EIPS/eip-137.md#name-syntax>`_
        before hashing.

        :param str name: ENS name to hash
        :return: the namehash
        :rtype: bytes
        :raises InvalidName: if ``name`` has invalid syntax
        '''
        name = cls._full_name(name)
        node = EMPTY_SHA3_BYTES
        if name:
            labels = name.split(".")
            for label in reversed(labels):
                labelhash = cls.labelhash(label)
                assert isinstance(labelhash, bytes)
                assert isinstance(node, bytes)
                sha_hex = Web3().sha3(node + labelhash)
                node = Web3().toBytes(hexstr=sha_hex)
        return node

    def resolver(self, name):
        resolver_addr = self.ens.resolver(self.namehash(name))
        if not resolver_addr:
            return None
        return self._resolverContract(address=resolver_addr)

    def reverser(self, target_address):
        reversed_domain = self.reverse_domain(target_address)
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
        node = self.namehash(name)
        return self.ens.owner(node)

    @classmethod
    def labelhash(cls, label):
        prepped = cls.nameprep(label)
        label_bytes = prepped.encode()
        sha_hex = Web3().sha3(label_bytes)
        return Web3().toBytes(hexstr=sha_hex)

    def reverse_domain(self, address):
        address = ensure_hex(address)
        if address.startswith('0x'):
            address = address[2:]
        address = address.lower()
        return address + '.' + REVERSE_REGISTRAR_DOMAIN

    def _reverse_node(self, address):
        domain = self.reverse_domain(address)
        return self.namehash(domain)

    def _assert_control(self, account, name, parent_owned=None):
        if account not in self.web3.eth.accounts:
            raise UnauthorizedError(
                "in order to modify %r, you must control account %r, which owns %r" % (
                    name, account, parent_owned or name
                )
            )

    def _first_owner(self, name):
        '@returns (owner or None, list(unowned_subdomain_labels), first_owned_domain)'
        owner = None
        unowned = []
        pieces = self._full_name(name).split('.')
        while not owner and pieces:
            name = '.'.join(pieces)
            owner = self.owner(name)
            if not owner:
                unowned.append(pieces.pop(0))
        return (owner, unowned, name)

    @dict_copy
    def _claim_ownership(self, owner, unowned, owned, transact={}):
        transact['from'] = owner
        for label in reversed(unowned):
            self.ens.setSubnodeOwner(
                self.namehash(owned),
                self.labelhash(label),
                owner,
                transact=transact
            )
            owned = "%s.%s" % (label, owned)

    @dict_copy
    def _set_resolver(self, name, resolver_addr=None, transact={}):
        if not resolver_addr:
            resolver_addr = self.address('resolver.eth')
        namehash = self.namehash(name)
        if self.ens.resolver(namehash) != resolver_addr:
            self.ens.setResolver(
                namehash,
                Web3().toBytes(hexstr=resolver_addr),
                transact=transact
            )
        return self._resolverContract(address=resolver_addr)

    @dict_copy
    def _setup_reverse(self, name, address, transact={}):
        name = self._full_name(name)
        transact['from'] = address
        return self._reverse_registrar().setName(name, transact=transact)

    def _reverse_registrar(self):
        addr = self.ens.owner(self.namehash(REVERSE_REGISTRAR_DOMAIN))
        return self.web3.eth.contract(address=addr, abi=abis.REVERSE_REGISTRAR)

    @classmethod
    def _full_name(cls, name):
        if isinstance(name, (bytes, bytearray)):
            name = Web3().toText(name)
        name = cls.nameprep(name)
        pieces = name.split('.')
        if pieces[-1] not in RECOGNIZED_TLDS:
            pieces.append(DEFAULT_TLD)
        return '.'.join(pieces)
