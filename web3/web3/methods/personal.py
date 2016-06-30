import getpass


class Personal(object):
    """
    https://github.com/ethereum/go-ethereum/wiki/Management-APIs#personal
    """
    def __init__(self, request_manager):
        self.request_manager = request_manager

    def importRawKey(self, private_key, passphrase):
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

    def signAndSendTransaction(self, *args, **kwargs):
        raise NotImplementedError()

    def lockAccount(self, *args, **kwargs):
        raise NotImplementedError()

    def unlockAccount(self, account, passphrase):
        return self.request_manager.request_blocking(
            "personal_listAccounts",
            [account, passphrase],
        )
