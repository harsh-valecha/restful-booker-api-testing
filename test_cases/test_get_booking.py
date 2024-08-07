import pytest
import requests

@pytest.mark.order(2)
@pytest.mark.parametrize('firstname',[("jim")])
def test_get_booking(session,base_url,firstname):
    url = f'{base_url}/booking'
    response = session.get(url=url,params={'firstname':firstname})
    assert response.status_code == 200
    print(response)


@pytest.mark.order(3)
@pytest.mark.parametrize("booking_data", [
    {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2023-01-05"
        },
        "additionalneeds": "Breakfast"
    }
])
def test_get_booking_by_id(session,base_url,shared,booking_data):
    url = f'{base_url}/booking/{shared["bookingid"]}'
    response = session.get(url)
    response_data = response.json()
    assert response.status_code==200
    assert response_data["firstname"] == booking_data["firstname"]
    assert response_data["lastname"] == booking_data["lastname"]
    assert response_data["totalprice"] == booking_data["totalprice"]
    assert response_data["depositpaid"] == booking_data["depositpaid"]
    assert response_data["bookingdates"]["checkin"] == booking_data["bookingdates"]["checkin"]
    assert response_data["bookingdates"]["checkout"] == booking_data["bookingdates"]["checkout"]
    assert response_data["additionalneeds"] == booking_data["additionalneeds"]
