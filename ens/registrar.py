
from collections import namedtuple
from datetime import datetime
from enum import IntEnum

import pytz

from ens import abis
from ens.exceptions import (
    BidTooLow,
    InvalidBidHash,
    InvalidLabel,
    UnderfundedBid,
)


def Web3():
    from web3 import Web3
    return Web3


REGISTRAR_NAME = 'eth'

AUCTION_START_GAS_CONSTANT = 25000
AUCTION_START_GAS_MARGINAL = 39000

MIN_BID = 10000000000000000  # 0.01 ether
MIN_NAME_LENGTH = 7

AuctionEntries = namedtuple('AuctionEntries', 'status, deed, close_at, deposit, top_bid')


class Status(IntEnum):
    '''
    Current status of the auction for a label. For more info:
    http://docs.ens.domains/en/latest/userguide.html#starting-an-auction

    Names taken from Solidity contract, but modified so they are gramatically parallel
    '''
    Open = 0
    Auctioning = 1        # original name was 'Auction' in HashRegistrarSimplified contract
    Owned = 2
    Forbidden = 3
    Revealing = 4         # original name was 'Reveal' in HashRegistrarSimplified contract
    NotYetAvailable = 5


class Registrar:
    """
    Provides access to the production ``'.eth'`` registrar, to buy names at auction.

    Terminology
        * Name: a fully qualified ENS name. For example: 'tickets.eth'
        * Label: a single word available under the .eth domain, via auction. For example: 'tickets'

    The registrar does not directly manage subdomains multiple layers down, like: 'fotc.tickets.eth'
    Each domain owner is individually responsible for that.
    """

    def __init__(self, ens):
        self.ens = ens
        self.web3 = ens.web3
        self._coreContract = self.web3.eth.contract(abi=abis.AUCTION_REGISTRAR)
        # delay generating this contract so that this class can be created before web3 is online
        self._core = None
        self._deedContract = self.web3.eth.contract(abi=abis.DEED)
        self._short_invalid = True

    def entries(self, label):
        '''
        Returns a tuple of data about the status of the auction for ``label``.

        Alternatively, you can request individual parts of the tuple. For example,
        get the :attr:`~ens.registrar.AuctionEntries.top_bid` value
        with a call like ``ns.registrar.top_bid(label)``.

        See these attributes on the returned value:

         * ``status`` the auction state, one of :class:`Status`
         * ``deed`` the contract storing the deposit, type :class:`web3.contract.ConciseContract`
         * ``close_at`` the time that the auction reveals end, type :class:`datetime.datetime`
         * ``deposit`` amount in wei that is held on deposit for the auction winner
         * ``top_bid`` amount in wei that the highest bidder placed as the top bid

        :rtype: AuctionEntries
        '''
        label = self._to_label(label)
        label_hash = self.ens.labelhash(label)
        return self.entries_by_hash(label_hash)

    def start(self, labels, **modifier_dict):
        if not labels:
            return
        if isinstance(labels, (str, bytes)):
            labels = [labels]
        if not modifier_dict:
            modifier_dict = {'transact': {}}
        if 'transact' in modifier_dict:
            transact_dict = modifier_dict['transact']
            if 'gas' not in transact_dict:
                transact_dict['gas'] = self._estimate_start_gas(labels)
            if transact_dict['gas'] > self._last_gaslimit():
                raise ValueError('There are too many auctions to fit in a block -- start fewer.')
        labels = [self._to_label(label) for label in labels]
        label_hashes = [self.ens.labelhash(label) for label in labels]
        return self.core.startAuctions(label_hashes, **modifier_dict)

    def bid(self, label, amount, secret, **modifier_dict):
        """
        :param str label: to bid on
        :param int amount: wei to bid
        :param secret: You **MUST keep a copy of this** to avoid burning your entire deposit!
        :type secret: bytes, str or int
        """
        if not modifier_dict:
            modifier_dict = {'transact': {}}
        if 'transact' in modifier_dict:
            transact = modifier_dict['transact']
            if 'value' not in transact:
                transact['value'] = amount
            elif transact['value'] < amount:
                raise UnderfundedBid("Bid of %s ETH was only funded with %s ETH" % (
                                     Web3().fromWei(amount, 'ether'),
                                     Web3().fromWei(transact['value'], 'ether')))
        label = self._to_label(label)
        sender = self.__require_sender(modifier_dict)
        if amount < MIN_BID:
            raise BidTooLow("You must bid at least %s ether" % Web3().fromWei(MIN_BID, 'ether'))
        bid_hash = self._bid_hash(label, sender, amount, secret)
        return self.core.newBid(bid_hash, **modifier_dict)

    def reveal(self, label, amount, secret, **modifier_dict):
        if not modifier_dict:
            modifier_dict = {'transact': {}}
        sender = self.__require_sender(modifier_dict)
        label = self._to_label(label)
        bid_hash = self._bid_hash(label, sender, amount, secret)
        if not self.core.sealedBids(sender, bid_hash):
            raise InvalidBidHash
        label_hash = self.ens.labelhash(label)
        secret_hash = self._secret_hash(secret)
        return self.core.unsealBid(label_hash, amount, secret_hash, **modifier_dict)
    unseal = reveal

    def finalize(self, label, **modifier_dict):
        if not modifier_dict:
            modifier_dict = {'transact': {}}
        label = self._to_label(label)
        label_hash = self.ens.labelhash(label)
        return self.core.finalizeAuction(label_hash, **modifier_dict)

    def entries_by_hash(self, label_hash):
        assert isinstance(label_hash, (bytes, bytearray))
        entries = self.core.entries(label_hash)
        return AuctionEntries(
            Status(entries[0]),
            self._deedContract(entries[1]) if entries[1] else None,
            datetime.fromtimestamp(entries[2], pytz.utc) if entries[2] else None,
            entries[3],
            entries[4],
        )

    @property
    def core(self):
        if not self._core:
            self._core = self._coreContract(address=self.ens.owner(REGISTRAR_NAME))
        return self._core

    def _estimate_start_gas(self, labels):
        return AUCTION_START_GAS_CONSTANT + AUCTION_START_GAS_MARGINAL * len(labels)

    def __require_sender(self, modifier_dict):
        modifier_vals = modifier_dict[list(modifier_dict).pop()]
        if 'from' not in modifier_vals:
            raise TypeError("You must specify the sending account")
        return modifier_vals['from']

    def _last_gaslimit(self):
        last_block = self.web3.eth.getBlock('latest')
        return last_block.gasLimit

    def _bid_hash(self, label, bidder, bid_amount, secret):
        label_hash = self.ens.labelhash(label)
        secret_hash = self._secret_hash(secret)
        bid_hash = self.core.shaBid(label_hash, bidder, bid_amount, secret_hash)
        # deal with web3.py returning a string instead of bytes:
        if isinstance(bid_hash, str):
            bid_hash = bytes(bid_hash, encoding='latin-1')
        return bid_hash

    @staticmethod
    def _secret_hash(secret):
        if isinstance(secret, str):
            secret = secret.encode()
        secret_hash = Web3().sha3(secret)
        return Web3().toBytes(hexstr=secret_hash)

    def _to_label(self, name):
        '''
        Convert from a name, like 'ethfinex.eth', to a label, like 'ethfinex'
        If name is already a label, this should be a noop, except for converting to a string
        '''
        if isinstance(name, (bytes, bytearray)):
            name = name.decode()
        name = self.ens.nameprep(name)
        if '.' not in name:
            label = name
        else:
            pieces = name.split('.')
            if len(pieces) != 2:
                raise ValueError(
                    "You must specify a label, like 'tickets' "
                    "or a fully-qualified name, like 'tickets.eth'"
                )
            if pieces[-1] != REGISTRAR_NAME:
                raise ValueError("This interface only manages names under .%s " % REGISTRAR_NAME)
            label = pieces[-2]
        if self._short_invalid and len(label) < MIN_NAME_LENGTH:
            raise InvalidLabel('name %r is too shart' % label)
        return label

    def __entry_lookup(self, label, entry_attr):
        entries = self.entries(label)
        return getattr(entries, entry_attr)

    def __getattr__(self, attr):
        if attr in AuctionEntries._fields:
            return lambda label: self.__entry_lookup(label, attr)
        else:
            raise AttributeError
