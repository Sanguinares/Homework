def test_insert_element(lst):
    lst.insert(5, 25)
    assert 25 in lst
