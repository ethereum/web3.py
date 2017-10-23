from __future__ import absolute_import

import getpass
import warnings

from web3.module import (
    Module,
)

from eth_utils import (
    coerce_return_to_text,
    remove_0x_prefix,
    encode_hex,
)


class Personal(Module):
    """
    https://github.com/ethereum/go-ethereum/wiki/Management-APIs#personal
    """
    @coerce_return_to_text
    def importRawKey(self, private_key, passphrase):
        if len(private_key) == 66:
            private_key = remove_0x_prefix(private_key)
        elif len(private_key) == 32:
            private_key = remove_0x_prefix(encode_hex(private_key))
        elif len(private_key) == 64:
            pass
        else:
            raise ValueError("Unknown private key format")
        return self.web3.manager.request_blocking(
            "personal_importRawKey",
            [private_key, passphrase],
        )

    @coerce_return_to_text
    def newAccount(self, password=None):
        if password is None:
            warnings.warn(DeprecationWarning(
                "Prompting for a password has been deprecated.  Please update "
                "your code to provide a password"
            ))
            password1 = getpass.getpass("Passphrase:")
            password2 = getpass.getpass("Repeat passphrase:")
            if password1 != password2:
                raise ValueError("Passwords do not match")

            password = password1

        if not password:
            raise ValueError("Cannot have an empty password")

        return self.web3.manager.request_blocking(
            "personal_newAccount", [password],
        )

    @property
    @coerce_return_to_text
    def listAccounts(self):
        return self.web3.manager.request_blocking(
            "personal_listAccounts", [],
        )

    @coerce_return_to_text
    def getListAccounts(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")

    @coerce_return_to_text
    def sendTransaction(self, transaction, passphrase):
        return self.web3.manager.request_blocking(
            "personal_sendTransaction",
            [transaction, passphrase],
        )

    def signAndSendTransaction(self, *args, **kwargs):
        warnings.warn(DeprecationWarning(
            "The `web3.personal.signAndSendTransaction` has been renamed to "
            "`web3.personal.sendTransaction`.  Please update your code to use "
            "the new method as this one will be removed in a subsequent release"
        ))
        return self.sendTransaction(*args, **kwargs)

    def lockAccount(self, account):
        return self.web3.manager.request_blocking(
            "personal_lockAccount",
            [account],
        )

    def unlockAccount(self, account, passphrase, duration=None):
        try:
            return self.web3.manager.request_blocking(
                "personal_unlockAccount",
                [account, passphrase, duration],
            )
        except ValueError as err:
            if "could not decrypt" in str(err):
                # Hack to handle go-ethereum error response.
                return False
            else:
                raise

    def sign(self, message, signer, passphrase):
        return self.web3.manager.request_blocking(
            'personal_sign',
            [message, signer, passphrase],
        )

    def ecRecover(self, message, signature):
        return self.web3.manager.request_blocking(
            'personal_ecRecover',
            [message, signature],
        )
