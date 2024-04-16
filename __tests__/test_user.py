# libraries
import pytest
import json
import requests
from utils.utils import ler_csv

# classes
# atributtes and variables

user_id = 150
username = "stefanyteixeira"
firstName = "Stefany"
email = "stefanytaniateixeira@projetochama.com.br"
password = "BxTYs9HLca"
phone = "81984585948"

# common information
url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}

# function and method
def test_post_user():

    # configuration 
    user = open('./fixtures/json/user1.json')
    data = json.loads(user.read())
    
    # execution
    response = requests.post(
        url=url,
        headers=headers,
        data=json.dumps(data),
        timeout=5
    )

    response_body = response.json()
    
    # validation
    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == str(user_id)

def test_get_user():
    response = requests.get(
        url=f'{url}/{username}',
        headers=headers
    )

    response_body = response.json()
    assert response.status_code == 200
    assert response_body['username'] == username
    assert response_body['firstName'] == firstName
    assert response_body['phone'] == phone

def test_put_user():
    user = open('./fixtures/json/user2.json')
    data = json.loads(user.read())
    
    response = requests.put(
        url=f'{url}/{username}',
        headers=headers,
        data = json.dumps(data),
        timeout=5
    )

    response_body = response.json()
    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == str(user_id)

def test_delete_user():     
    response = requests.delete(
        url=f'{url}/{username}',
        headers=headers
    )

    response_body = response.json()
    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == str(username)

@pytest.mark.parametrize('user_id,username,firstName,lastName,email,password,phone,userStatus',
                         ler_csv('./fixtures/csv/user.csv')
                         )
def test_post_user_dynamic(user_id,username,firstName,lastName,email,password,phone,userStatus):
    user = {}    
    user['id'] = int(user_id)  
    user['username'] = username
    user['firstName'] = firstName
    user['lastName'] = lastName
    user['email'] = email
    user['password'] = password
    user['phone'] = phone
    user['userStatus'] = int(userStatus)

    user = json.dumps(obj=user, indent=4)
    print('\n' + user) 

    response = requests.post(
        url=url,
        headers=headers,
        data=user,
        timeout=5
    )

    response_body = response.json()
    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == str(user_id)


@pytest.mark.parametrize('user_id,username,firstName,lastName,email,password,phone,userStatus',
                         ler_csv('./fixtures/csv/user.csv')
                         )
def test_delete_user_dynamic(user_id,username,firstName,lastName,email,password,phone,userStatus):
    user = {}
    user['id'] = int(user_id)  
    user['username'] = username
    user['firstName'] = firstName
    user['lastName'] = lastName
    user['email'] = email
    user['password'] = password
    user['phone'] = phone
    user['userStatus'] = int(userStatus)

    user = json.dumps(obj=user, indent=4)
    print('\n' + user) 

    response = requests.delete(
        url=f'{url}/{username}',
        headers=headers,
        timeout=5
    )

    response_body = response.json()
    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == str(username)