import pytest


@pytest.fixture()
def lst():
    return [0, 5, 10, 15, 20]


@pytest.fixture()
def lst1():
    return [100, 200, 300, 400]


@pytest.fixture()
def st():
    return {'zero', 1, 'two', 3, 'four'}


@pytest.fixture()
def st1():
    return {5, 6, 7, 'zero'}


@pytest.fixture()
def dct():
    return {'John': 20, 'Kate': 23, 'Sam': 35, "Will": 19}


@pytest.fixture()
def stg():
    return 'Строка - очень полезный в работе тип'


@pytest.fixture()
def stg1():
    return 'поэтому её обязательно стоит всячески потестировать'
