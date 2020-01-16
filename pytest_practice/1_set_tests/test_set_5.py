import pytest


@pytest.mark.parametrize("arr", [
    {'zero', 1, 'two', 3, 'four', 5, 'six'},
    {'zero', 1, 'two', 3, 'four', 5, 6, 7, 'eight', 'nine'},
])
def test_superset(st, st1, arr):
    assert arr.issuperset(st) is True

