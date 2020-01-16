def test_del_dict(dct):
    del dct['Will']
    assert 'Will' not in dct
