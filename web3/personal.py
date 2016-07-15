from __future__ import absolute_import
import getpass

from web3.utils.encoding import (
    remove_0x_prefix,
    encode_hex,
)


class Personal(object):
    """
    https://github.com/ethereum/go-ethereum/wiki/Management-APIs#personal
    """
    def __init__(self, request_manager):
        self.request_manager = request_manager

    def importRawKey(self, private_key, passphrase):
        if len(private_key) == 66:
            private_key = remove_0x_prefix(private_key)
        elif len(private_key) == 32:
            private_key = remove_0x_prefix(encode_hex(private_key))
        elif len(private_key) == 64:
            pass
        else:
            raise ValueError("Unknown private key format")
        return self.request_manager.request_blocking(
            "personal_importRawKey",
            [private_key, passphrase],
        )

    def newAccount(self, password=None):
        if password is None:
            password1 = getpass.getpass("Passphrase:")
            password2 = getpass.getpass("Repeat passphrase:")
            if password1 != password2:
                raise ValueError("Passwords do not match")

            password = password1

        if not password:
            raise ValueError("Cannot have an empty password")

        return self.request_manager.request_blocking("personal_newAccount", [password])

    @property
    def listAccounts(self):
        return self.request_manager.request_blocking("personal_listAccounts", [])

    def getListAccounts(self, *args, **kwargs):
        raise NotImplementedError("Async calling has not been implemented")

    def signAndSendTransaction(self, tx, passphrase):
        return self.request_manager.request_blocking(
            # "personal_sendTransaction",
            "personal_signAndSendTransaction",
            [tx, passphrase],
        )

    def lockAccount(self, account):
        return self.request_manager.request_blocking(
            "personal_lockAccount",
            [account],
        )

    def unlockAccount(self, account, passphrase, duration=None):
        return self.request_manager.request_blocking(
            "personal_unlockAccount",
            [account, passphrase, duration],
        )
