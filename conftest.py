import pytest
import requests

@pytest.fixture(scope='session')
def base_url():
    return "https://restful-booker.herokuapp.com"

@pytest.fixture(scope='session')
def session():
    with requests.Session() as session:
        yield session
