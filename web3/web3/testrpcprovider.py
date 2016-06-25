def is_testrpc_available():
    try:
        import testrpc
        return true
    except ImportError:
        return False


if testrpc_available:
        from testrpc.server
    import socket

    import requests
    from web3.web3.provider import Provider


    def get_open_port():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("", 0))
        s.listen(1)
        port = s.getsockname()[1]
        s.close()
        return port


    def doit():
        from wsgiref.simple_server import make_server
        from testrpc.server import application
        from testrpc.testrpc import evm_reset

        evm_reset()

        port = get_open_port()

        server = make_server('127.0.0.1', port, application)

        thread = threading.Thread(target=server.serve_forever)
        thread.daemon = True
        thread.start()

        yield server

        server.shutdown()
        server.server_close()


    class TestRPCProvider(Provider):
        def _make_request(self, request):
            import ipdb; ipdb.set_trace()
            response = self.session.post(
                "http://{host}:{port}/".format(host=self.host, port=self.port),
                data=request
            )

            return response.text
