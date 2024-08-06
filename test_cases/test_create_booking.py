import pytest
import json

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
def test_create_booking(session, base_url,shared,booking_data):
    url = f"{base_url}/booking"
    headers = {"Content-Type": "application/json"}
    response = session.post(url, data=json.dumps(booking_data), headers=headers)
    
    assert response.status_code == 200
    response_data = response.json()
    assert "bookingid" in response_data
    assert response_data["booking"]["firstname"] == booking_data["firstname"]
    assert response_data["booking"]["lastname"] == booking_data["lastname"]
    assert response_data["booking"]["totalprice"] == booking_data["totalprice"]
    assert response_data["booking"]["depositpaid"] == booking_data["depositpaid"]
    assert response_data["booking"]["bookingdates"]["checkin"] == booking_data["bookingdates"]["checkin"]
    assert response_data["booking"]["bookingdates"]["checkout"] == booking_data["bookingdates"]["checkout"]
    assert response_data["booking"]["additionalneeds"] == booking_data["additionalneeds"]
    shared['bookingid'] = response_data['bookingid']
