def test_import_and_version():
    import faster_web3

    version = faster_web3.__version__
    assert isinstance(version, str)
