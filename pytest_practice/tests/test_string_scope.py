import pytest


def test_str_find(stg):
    assert stg.find('Строка') == 0


def test_str_islower(stg):
    assert stg.islower() is False


def test_str_isspace(stg):
    assert stg.isspace() is False


def test_str_add(stg, stg1):
    assert len(stg+stg1) == 87


@pytest.mark.parametrize("up", [
    'ЭТО ВЕРХНИЙ РЕГИСТР',
    'а это не верхний регистр'
])
def test_is_upper(up):
    assert up.isupper() is True

