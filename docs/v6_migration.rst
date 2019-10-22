.. _migrating_v5_to_v6:

Migrating your code from v5 to v6
=================================

Web3.py follows `Semantic Versioning <http://semver.org>`_, which means
that version 6 introduced backwards-incompatible changes. If your
project depends on Web3.py v6, then you'll probably need to make some changes.

Here are the most common required updates:

Web3.py does not raise ValueError nor AttributeError instances anymore
----------------------------------------------------------------------

In v5, some Web3.py exceptions inherited from AttributeError, namely:

- NoABIFunctionsFound
- NoABIFound
- NoABIEventsFound

Others inherited from ValueError, namely:

- InvalidAddress
- NameNotFound
- LogTopicError
- InvalidEventABI

Now Web3.py exceptions now inherit from the same base Web3Exception.

As such, any code that was expecting a ValueError or an AttributeError from
Web3py must update to expecting one of the exception listed above, or
Web3Exception.
