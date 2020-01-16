import pytest


@pytest.fixture()
def stg():
    return 'Строка - очень полезный в работе тип'


@pytest.fixture()
def stg1():
    return 'поэтому её обязательно стоит всячески потестировать'
