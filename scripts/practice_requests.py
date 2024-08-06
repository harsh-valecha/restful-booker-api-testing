import requests

base_url = 'https://restful-booker.herokuapp.com/'
userdata = {
    'username':'admin',
    'password':'password123'
}
def create_token():
    response = requests.post(f'{base_url}auth',data = userdata)
    return response.json()['token']
token  = create_token()

data = {
    "firstname" : "kamlesh",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
def create_booking():
    response = requests.post(f'{base_url}booking',json = data)
    if response.status_code==200:
        return response.json()['bookingid']
    
booking_id = create_booking()


def get_booking():
    response =requests.get(f'{base_url}booking/{booking_id}')
    return response.json()

# print(get_booking())


firstname = 'kamlesh'
lastname='chaturvedi'

def get_booking_ids(**kwargs):
    response = requests.get(f'{base_url}booking',params={'firstname':kwargs['firstname']})
    print(response.status_code,response.json()[0]['bookingid'])
# create_token()
#get_booking_ids(firstname = firstname) # example of getting a booking id using firstname


update_data = {
    "firstname" : "James",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}

def update_booking():
    response = requests.put(f'{base_url}booking/{booking_id}',json=update_data,headers={"Cookie":f"token={token}"})
    if response.status_code==200:
        return response.json()
    

# print(update_booking())

partial_data = {
    "firstname" : "Jaktap",
    "lastname" : "Bengali"
}
def partial_update_booking():
    response = requests.patch(f'{base_url}booking/{booking_id}',headers={'Cookie':f'token={token}'},json=partial_data)
    if response.status_code==200:
        return response.json()
    

# print(partial_update_booking())


def delete_booking():
    response = requests.delete(f'{base_url}booking/{booking_id}',headers={'Cookie':f'token={token}'})
    print(response.status_code,response.text)

# delete_booking()