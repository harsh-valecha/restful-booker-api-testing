import pytest
import requests
import json

data = {
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


def test_update_booking(session,base_url,token,shared):
    token = json.loads(token)["token"]

    headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Cookie": f"token={token}"
    }
    response = session.put(url=f'{base_url}/booking/{shared["bookingid"]}',headers=headers,json=data)
    print(response)
    assert response.status_code==200
    print(response.json())