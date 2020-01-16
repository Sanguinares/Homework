import pytest


@pytest.mark.parametrize("up", [
    'ЭТО ВЕРХНИЙ РЕГИСТР',
    'а это не верхний регистр'
])
def test_is_upper(up):
    assert up.isupper()
