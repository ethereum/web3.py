class Personal():
    """
    This API is not automatically available on a `web3` instance, rather it should be accessed
    through `web3.geth.personal` or `web3.parity.personal`.

    All RPC endpoints under the personal namespace should be added here, and NotImplementedErrors
    should be raised in subclasses if the endpoints are not supported by the respective client.
    """
    def importRawKey(self, private_key, passphrase):
        return self.web3.manager.request_blocking(
            "personal_importRawKey",
            [private_key, passphrase],
        )

    def newAccount(self, password):
        return self.web3.manager.request_blocking(
            "personal_newAccount", [password],
        )

    @property
    def listAccounts(self):
        return self.web3.manager.request_blocking(
            "personal_listAccounts", [],
        )

    def sendTransaction(self, transaction, passphrase):
        return self.web3.manager.request_blocking(
            "personal_sendTransaction",
            [transaction, passphrase],
        )

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
