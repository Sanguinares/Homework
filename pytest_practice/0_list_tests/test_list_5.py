import pytest


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
