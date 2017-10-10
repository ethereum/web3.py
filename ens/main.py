
import idna

from ens import abis
from ens.constants import EMPTY_SHA3_BYTES
from ens.registrar import Registrar
from ens.utils import dict_copy, ensure_hex, init_web3

DEFAULT_TLD = 'eth'
RECOGNIZED_TLDS = [DEFAULT_TLD, 'reverse', 'test']

ENS_MAINNET_ADDR = '0x314159265dd8dbb310642f98f50c066173c1259b'

REVERSE_REGISTRAR_DOMAIN = 'addr.reverse'

GAS_DEFAULT = {
    'setAddr': 60001,
    'setResolver': 60002,
    'setSubnodeOwner': 60003,
}


def Web3():
    from web3 import Web3
    return Web3


class ENS:
    '''
    Unless otherwise specified, all addresses are assumed to be a str in hex format, like:
    "0x314159265dd8dbb310642f98f50c066173c1259b"
    '''

    def __init__(self, providers=None, addr=None):
        '''
        @param providers is a provider or list of providers for web3
        @param addr is the address of the ENS registry on-chain. If not provided,
            ENS.py will default to the mainnet ENS registry address.
        '''
        self.web3 = init_web3(providers)

        ens_addr = addr if addr else ENS_MAINNET_ADDR
        self.ens = self.web3.eth.contract(abi=abis.ENS, address=ens_addr)
        self._resolverContract = self.web3.eth.contract(abi=abis.RESOLVER)
        self.registrar = Registrar(self)

    def address(self, name):
        return self.resolve(name, 'addr')

    def name(self, address):
        reversed_domain = self.reverse_domain(address)
        return self.resolve(reversed_domain, get='name')
    reverse = name

    @dict_copy
    def setup_address(self, name, address=None, transact={}):
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
        transact['gas'] = GAS_DEFAULT['setAddr']
        if isinstance(address, str):
            address = Web3().toBytes(hexstr=address)
        else:
            address = Web3().toBytes(address)
        return resolver.setAddr(self.namehash(name), address, transact=transact)

    @dict_copy
    def setup_name(self, name, address=None, transact={}):
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

    def namehash(self, name):
        name = self._full_name(name)
        node = EMPTY_SHA3_BYTES
        if name:
            labels = name.split(".")
            for label in reversed(labels):
                labelhash = self.labelhash(label)
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
        node = self.namehash(name)
        return self.ens.owner(node)

    def labelhash(self, label):
        prepped = self.nameprep(label)
        label_bytes = prepped.encode()
        sha_hex = Web3().sha3(label_bytes)
        return Web3().toBytes(hexstr=sha_hex)

    def reverse_domain(self, address):
        address = ensure_hex(address)
        if address.startswith('0x'):
            address = address[2:]
        address = address.lower()
        return address + '.' + REVERSE_REGISTRAR_DOMAIN

    @staticmethod
    def nameprep(name):
        if not name:
            return name
        try:
            return idna.decode(name, uts46=True, std3_rules=True)
        except idna.IDNAError as exc:
            raise InvalidName("%s is an invalid name, because %s" % (name, exc)) from exc

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
        transact['gas'] = GAS_DEFAULT['setSubnodeOwner']
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
            transact['gas'] = GAS_DEFAULT['setResolver']
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


class AddressMismatch(ValueError):
    pass


class InvalidName(idna.IDNAError):
    pass


class UnauthorizedError(Exception):
    pass


class UnownedName(Exception):
    pass
