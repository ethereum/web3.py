def test_import_and_version():
    import web3

    assert isinstance(web3.__version__, str)
