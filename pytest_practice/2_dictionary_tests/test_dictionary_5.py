import pytest


@pytest.mark.parametrize("upd", [
    {'Jack': 31, 'George': 85, 'Bill': 43},
    {'Olga': 20, 'Jack': 23, 'Peter': 37},
])
def test_update(dct, upd):
    dct.update(upd)
    assert 'Jack' in dct


