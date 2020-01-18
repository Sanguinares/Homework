import pytest


def test_dict_values(dct):
    assert dct['John'] == 20
    assert dct['Will'] == 19


def test_clear_dict(dct):
    dct.clear()
    assert len(dct) == 0


def test_del_dict(dct):
    del dct['Will']
    assert 'Will' not in dct


def test_set_dict(dct):
    dct['Kate'] = 25
    assert dct['Kate'] == 25


@pytest.mark.parametrize("upd", [
    {'Jack': 31, 'George': 85, 'Bill': 43},
    {'Olga': 20, 'Jack': 23, 'Peter': 37},
])
def test_update(dct, upd):
    dct.update(upd)
    assert 'Jack' in dct


