

def test_fake_hash(fake_hash):
    assert fake_hash(b'rainstorms') == b"HASH(brainstorms)"
