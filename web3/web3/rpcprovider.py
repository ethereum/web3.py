import requests
from web3.web3.provider import Provider


class RPCProvider(Provider):

    def __init__(self, host="127.0.0.1", port="8545", *args, **kwargs):
        self.host = host
        self.port = port
        self.session = requests.session()

        super(RPCProvider, self).__init__(*args, **kwargs)

    def _make_request(self, request):
        response = self.session.post(
            "http://{host}:{port}/".format(host=self.host, port=self.port),
            data=request
        )

        return response.text
