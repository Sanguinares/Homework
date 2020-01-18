import pytest


def test_insert_element(lst):
    lst.insert(5, 25)
    assert 25 in lst


def test_remove_element(lst):
    del lst[0]
    assert 0 not in lst


def test_extend_list(lst, lst1):
    lst.extend(lst1)
    assert len(lst) == 9


def test_reverse_list(lst):
    lst.reverse()
    assert lst[0] == 20


@pytest.mark.parametrize("num1,num2", [
    (0, 100),
    (5, 200),
    (10, 300),
    (15, 300),
])
def test_remove_with_param(lst, lst1, num1, num2):
    lst.remove(num1)
    lst1.remove(num2)
    assert len(lst) == 4
    assert lst1[2] == 400
