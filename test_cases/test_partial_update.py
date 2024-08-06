import pytest
import requests
import json

partial_data = {
    "firstname" : "James",
    "lastname" : "Brown"
}

def test_partial_update(session,base_url,token,shared):
    bookingid = shared['bookingid']
    token = json.loads(token)["token"]
    
    response= session.patch(f'{base_url}/booking/{bookingid}',headers={'Cookie':f'token={token}'},json=partial_data)
    print('response is '+response.text)
    assert response.status_code==200