import requests
import uuid
from assertpy.assertpy import assert_that

BASE_URI = "http://deeksha-test-system:8080"
AUTH_API = BASE_URI + "/api/auth/token" 
USERS_API = BASE_URI + "/api/users"
auth_username = 'api_tester'
auth_password = 'admin123'

def test_register_new_user():
    unique_username = register_new_user()
    # After user is registered, review all the users to find if the new registered user is present in the list
    response = requests.get(USERS_API).json()
    usernames = response['payload']
    assert_that(usernames).contains(unique_username)
    print(f"{unique_username} is sucessfully registered!!", end="\n\n")
    return unique_username

def register_new_user():
    # Ensure that unique username is created everytime the test runs
    unique_username = f'User {str(uuid.uuid4())}'
    payload = {
    'username' :  unique_username,
    'firstname': 'tester',
    'lastname' : 'admin',
    'password' : 'admin123',
    'phone'    :  466646787
    }
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.post(url=USERS_API, headers=headers, json=payload).json()
    assert_that(response['status'], description=response['message']).is_equal_to('SUCCESS')
    return unique_username

def test_review_users():
    response = requests.get(USERS_API).json()
    assert_that(response['status']).is_equal_to('SUCCESS')
    registered_users = ", ".join(response['payload'])
    print(f"""Registered Users:
          {registered_users}
          """)
    
def is_authenticated():
    #After successfull HTTP basic authentication, return token to include in headers for subsequent endpoints
    response = requests.get(AUTH_API, auth=(auth_username, auth_password)).json()
    assert_that(response['status']).is_equal_to('SUCCESS')
    return response['token']

def test_get_specific_user(username):
    access_token = is_authenticated()
    headers = {'Content-Type':'application/json',
               'token': f'{access_token}'
              }
    response = requests.get(USERS_API + "/" + f"{username}", headers=headers).json()
    assert_that(response['status'], description=response['message']).is_equal_to('SUCCESS')
    print(f"""Successfully retrieved the details for {username}
          firstname = {response['payload']['firstname']}
          lastname  = {response['payload']['lastname']}
          phone     = {response['payload']['phone']}
          """)


def test_put_specific_user(username):
    access_token = is_authenticated()
    headers = {'Content-Type':'application/json',
               'token': f'{access_token}'
              }
    update_payload = {'firstname': 'Deeksha', 'lastname': '1234'}
    response = requests.put(USERS_API + "/" + f"{username}",  headers=headers, json=update_payload).json()
    assert_that(response['status'], description=response['message']).is_equal_to('SUCCESS')
    print(f"""Requested update Info:firstname={update_payload['firstname']} and lastname={update_payload['lastname']} for {username}
          API response - {response['message']}""")
    


def test_flasky_apis():
    print("----------------Running the test automation of Flasky API----------------")
    print("1. Test register new users")
    registered_user = test_register_new_user()
    print("2. Review users")
    test_review_users()
    print("3. Get Details of specific user")
    test_get_specific_user(registered_user)
    print("4. Update Details of specific user")
    test_put_specific_user(registered_user)

if __name__ == "__main__":
    test_flasky_apis()
