

class Transaction(object):
    IMMUTABILITY_WARNING = "Transactions are immutable, create a new one instead of modifying this"

    def __init__(self, values):
        '''
        @param values a dictionary of transaction values
        '''
        self.__dict__ = values
        try:
            self._unique_txid()
        except AttributeError as e:
            assert False, "Transaction must be uniquely defined. Failed because: %s" % e
        self._locked = True

    def _unique_txid(self):
        'currently the hash works as a unique identifier, but someday maybe not'
        return getattr(self, 'hash')

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, val):
        raise NotImplementedError(Transaction.IMMUTABILITY_WARNING)

    def __delitem__(self, key):
        raise NotImplementedError(Transaction.IMMUTABILITY_WARNING)

    def __iter__(self):
        return iter(self.__dict__)

    def todict(self):
        return dict(self.__dict__)

    def items(self):
        return self.__dict__.items()

    def iteritems(self):
        return self.__dict__.iteritems()

    def __setattr__(self, key, val):
        if hasattr(self, '_locked'):
            raise NotImplementedError(Transaction.IMMUTABILITY_WARNING)
        super(type(self), self).__setattr__(key, val)

    def __delattr__(self, key):
        raise NotImplementedError(Transaction.IMMUTABILITY_WARNING)

    def __contains__(self, key):
        return key in self.__dict__

    def __eq__(self, other):
        return hasattr(other, '_unique_txid') and self._unique_txid() == other._unique_txid()

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        return hash(self._unique_txid())

    def __str__(self):
        return "Tx:" + self._unique_txid()

    def __repr__(self):
        return "Transaction(%r)" % self.__dict__
