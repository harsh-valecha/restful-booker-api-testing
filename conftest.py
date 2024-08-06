import pytest
import requests
import json

@pytest.fixture(scope='session')
def base_url():
    return "https://restful-booker.herokuapp.com"

@pytest.fixture(scope='session')
def session():
    with requests.Session() as session:
        yield session


@pytest.fixture(scope='session')
def token():
   r = requests.post(url='https://restful-booker.herokuapp.com/auth',data={'username':'admin','password':'password123'})
   if r.status_code==200:
    return r.text
   return r


@pytest.fixture(scope='session')
def shared():
   return {}