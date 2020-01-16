import pytest


@pytest.fixture()
def dct():
    return {'John': 20, 'Kate': 23, 'Sam': 35, "Will": 19}
