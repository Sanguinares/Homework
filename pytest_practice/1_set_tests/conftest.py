import pytest


@pytest.fixture()
def st():
    return {'zero', 1, 'two', 3, 'four'}


@pytest.fixture()
def st1():
    return {5, 6, 7, 'zero'}


