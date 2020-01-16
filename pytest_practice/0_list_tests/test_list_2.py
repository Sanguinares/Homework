def test_remove_element(lst):
    del lst[0]
    assert 0 not in lst
