import pytest


def test_sets_int(st, st1):
    assert len(st.union(st1)) == 8


def test_sets_union(st, st1):
    assert len(st.intersection(st1)) == 1


def test_sets_diff(st, st1):
    assert 'zero' not in st.difference(st1)


def test_sets_idj(st, st1):
    assert st.isdisjoint(st1) is False


@pytest.mark.parametrize("arr", [
    {'zero', 1, 'two', 3, 'four', 5, 'six'},
    {'zero', 1, 'two', 3, 'four', 5, 6, 7, 'eight', 'nine'},
])
def test_superset(st, st1, arr):
    assert arr.issuperset(st) is True

