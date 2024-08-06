import pytest
import requests

@pytest.mark.parametrize('firstname',[("jim")])
def test_get_booking(session,base_url,firstname):
    url = f'{base_url}/booking'
    response = session.get(url=url,params={'firstname':firstname})
    assert response.status_code == 200
    print(response)
