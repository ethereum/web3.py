from web3.utils.functional import replace_key


def test_replacing_key():
    original = {
        'a': 1,
        'b': 2,
    }

    result = replace_key(original, 'a', 3)

    assert result['a'] == 3
    assert result['b'] == 2

    assert original['a'] == 1
    assert original['b'] == 2
