import pytest
import requests
import json



@pytest.mark.order(4)
@pytest.mark.parametrize("update_data",[
     {
    "firstname" : "James",
    "lastname" : "Kachodi",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
])
def test_update_booking(session,base_url,token,shared,update_data):
    token = json.loads(token)["token"]

    headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Cookie": f"token={token}"
    }
    response = session.put(url=f'{base_url}/booking/{shared["bookingid"]}',headers=headers,json=update_data)
    print(response)
    assert response.status_code==200
    response_data = response.json()
    assert response_data["firstname"] == update_data["firstname"]
    assert response_data["lastname"] == update_data["lastname"]
    assert response_data["totalprice"] == update_data["totalprice"]
    assert response_data["depositpaid"] == update_data["depositpaid"]
    assert response_data["bookingdates"]["checkin"] == update_data["bookingdates"]["checkin"]
    assert response_data["bookingdates"]["checkout"] == update_data["bookingdates"]["checkout"]
    assert response_data["additionalneeds"] == update_data["additionalneeds"]