
from collections import namedtuple
from enum import IntEnum

from ens import abis

from ens.exceptions import (
    BidTooLow,
    InvalidBidHash,
    OversizeTransaction,
    UnderfundedBid,
)

from ens.utils import (
    Web3,
    dict_copy,
    dot_eth_label,
    estimate_auction_start_gas,
    assert_signer_in_modifier_kwargs,
    label_to_hash,
    sha3_text,
    to_utc_datetime,
)

REGISTRAR_NAME = 'eth'

MIN_BID = 10000000000000000  # 0.01 ether

AuctionEntry = namedtuple('AuctionEntry', 'status, deed, close_at, deposit, top_bid')
'''
A namedtuple with various attributes about an auction for a .eth name.

    See :meth:`Registrar.entries`
'''


class Status(IntEnum):
    '''
    Current status of the auction for a label. For more info,
    see the `ENS documentation
    <http://docs.ens.domains/en/latest/userguide.html#starting-an-auction>`_

    The status names mirror those in the `Solidity contract
    <https://github.com/ethereum/ens/blob/master/contracts/HashRegistrarSimplified.sol#L110>`_.
    A couple are modified to be gramatically consistent with each other.
    '''

    Open = 0
    '''The associated name is available for anyone to start an auction.'''

    Auctioning = 1
    '''
    An auction on the name has begun. The .eth Registrar is accepting bids.

    In the `registrar contract
    <https://github.com/ethereum/ens/blob/master/contracts/HashRegistrarSimplified.sol#L110>`_
    this is called ``Auction``
    '''

    Owned = 2
    '''The name has been auctioned, and the top bidder was determined'''

    Forbidden = 3
    '''Reserved for later use'''

    Revealing = 4
    '''
    The .eth Registrar is no longer accepting bids. All bidders must reveal during this period.

    In the `registrar contract
    <https://github.com/ethereum/ens/blob/master/contracts/HashRegistrarSimplified.sol#L110>`_
    this is called ``Reveal``
    '''

    NotYetAvailable = 5
    '''
    When ENS first launched, there was a slow rollout of names. This status was
    used for names that had not yet been released.

    It should no longer apply to any names, until the next major release of sub-7 character
    names.
    '''


class Registrar:
    """
    .. WARNING:: The registrar functionality is Alpha-quality. Use at your own risk!

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

    def entries(self, label):
        '''
        Returns a :class:`~collections.namedtuple` with information about the auction for `label`.

        See these attributes on the returned value:

         * `status` the auction state, one of :class:`Status`
         * `deed` the contract storing the deposit, a :class:`~web3.contract.ConciseContract`
         * `close_at` the time that the auction reveals end, a :class:`datetime.datetime`
         * `deposit` amount in wei that is held on deposit for the auction winner
         * `top_bid` amount in wei that the highest bidder placed as the top bid

        You can also retrieve these attributes one at a time with these method calls on
        ENS.registrar:

         * :meth:`status`
         * :meth:`deed`
         * :meth:`close_at`
         * :meth:`deposit`
         * :meth:`top_bid`

        :rtype: AuctionEntry
        :raise InvalidName: if ``label`` is not a valid ENS label
        :raise ValueError: if ``label`` is shorter than 7 characters
        '''
        label = dot_eth_label(label)
        label_hash = self.ens.labelhash(label)
        return self.entries_by_hash(label_hash)

    @dict_copy
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
                transact_dict['gas'] = estimate_auction_start_gas(labels)
            if transact_dict['gas'] > self._last_gaslimit():
                raise OversizeTransaction('This call includes too many auctions to fit in a block.')
        labels = [dot_eth_label(label) for label in labels]
        label_hashes = [self.ens.labelhash(label) for label in labels]
        return self.core.startAuctions(label_hashes, **modifier_dict)

    @dict_copy
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
        label = dot_eth_label(label)
        sender = assert_signer_in_modifier_kwargs(modifier_dict)
        if amount < MIN_BID:
            raise BidTooLow("You must bid at least %s ether" % Web3().fromWei(MIN_BID, 'ether'))
        bid_hash = self._bid_hash(label, sender, amount, secret)
        return self.core.newBid(bid_hash, **modifier_dict)

    @dict_copy
    def reveal(self, label, amount, secret, **modifier_dict):
        if not modifier_dict:
            modifier_dict = {'transact': {}}
        sender = assert_signer_in_modifier_kwargs(modifier_dict)
        label = dot_eth_label(label)
        bid_hash = self._bid_hash(label, sender, amount, secret)
        if not self.core.sealedBids(sender, bid_hash):
            raise InvalidBidHash
        label_hash = self.ens.labelhash(label)
        secret_hash = sha3_text(secret)
        return self.core.unsealBid(label_hash, amount, secret_hash, **modifier_dict)
    unseal = reveal

    @dict_copy
    def finalize(self, label, **modifier_dict):
        if not modifier_dict:
            modifier_dict = {'transact': {}}
        label = dot_eth_label(label)
        label_hash = self.ens.labelhash(label)
        return self.core.finalizeAuction(label_hash, **modifier_dict)

    def entries_by_hash(self, label_hash):
        assert isinstance(label_hash, (bytes, bytearray))
        entries = self.core.entries(label_hash)
        return AuctionEntry(
            Status(entries[0]),
            self._deedContract(entries[1]) if entries[1] else None,
            to_utc_datetime(entries[2]),
            entries[3],
            entries[4],
        )

    @property
    def core(self):
        if not self._core:
            self._core = self._coreContract(address=self.ens.owner(REGISTRAR_NAME))
        return self._core

    def _last_gaslimit(self):
        last_block = self.web3.eth.getBlock('latest')
        return last_block.gasLimit

    def _bid_hash(self, label, bidder, bid_amount, secret):
        label_hash = label_to_hash(label)
        secret_hash = sha3_text(secret)
        bid_hash = self.core.shaBid(label_hash, bidder, bid_amount, secret_hash)
        # deal with web3.py returning a string instead of bytes:
        if isinstance(bid_hash, str):
            bid_hash = bytes(bid_hash, encoding='latin-1')
        return bid_hash

    def status(self, label):
        '''
        Get the current status of the auction for `label`

        :param str label: the .eth name you want to look up
        :rtype: Status
        '''
        return self.entries(label).status

    def deed(self, label):
        '''
        Get the contract holding the deposit for the current
        winner of the auction for `label`

        :param str label: the .eth name you want to look up
        :rtype: ~web3.contract.ConciseContract
        :returns: `Deed contract
            <https://github.com/ethereum/ens/blob/master/contracts/HashRegistrarSimplified.sol>`_
        '''
        return self.entries(label).deed

    def close_at(self, label):
        '''
        Get the time that reveals must be submitted by for the auction for `label`

        :param str label: the .eth name you want to look up
        :rtype: datetime.datetime
        :return: timezone-aware end time (may be in past or future)
        '''
        return self.entries(label).close_at

    def deposit(self, label):
        '''
        Get the amount of wei deposited by the current winner of the auction for `label`

        This number may not be final if :meth:`close_at` is in the future.

        :param str label: the .eth name you want to look up
        :rtype: int
        :returns: wei deposited
        '''
        return self.entries(label).deposit

    def top_bid(self, label):
        '''
        Get the amount of wei bid by the current winner of the auction for `label`

        This number may not be final if :meth:`close_at` is in the future.

        :param str label: the .eth name you want to look up
        :rtype: int
        :returns: wei bid
        '''
        return self.entries(label).top_bid
