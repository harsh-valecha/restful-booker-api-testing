import pytest
import requests
import json



@pytest.mark.order(5)
@pytest.mark.parametrize("partial_data",[{
    "firstname" : "James",
    "lastname" : "Brown"
}])
def test_partial_update(session,base_url,token,shared,partial_data):
    bookingid = shared['bookingid']
    token = json.loads(token)["token"]
    
    response= session.patch(f'{base_url}/booking/{bookingid}',headers={'Cookie':f'token={token}'},json=partial_data)
    print('response is '+response.text)
    assert response.status_code==200
    response_data = response.json()
    assert response_data["firstname"] == partial_data["firstname"]
    assert response_data["lastname"] == partial_data["lastname"]
    