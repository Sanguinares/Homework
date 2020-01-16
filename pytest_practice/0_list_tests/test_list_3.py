def test_extend_list(lst, lst1):
    lst.extend(lst1)
    assert len(lst) == 9
