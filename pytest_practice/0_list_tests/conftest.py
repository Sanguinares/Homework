import pytest


@pytest.fixture()
def lst():
    return [0, 5, 10, 15, 20]


@pytest.fixture()
def lst1():
    return [100, 200, 300, 400]


