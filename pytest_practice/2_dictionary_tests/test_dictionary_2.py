def test_clear_dict(dct):
    dct.clear()
    assert len(dct) == 0
