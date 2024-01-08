def test_import_and_version():
    import web3

    version = web3.__version__
    assert isinstance(version, str)
