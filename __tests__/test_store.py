# Libraries
import json
import requests

# Classes
# Atributtes, variables and common information
store_id = "11"
store_petId = 11198 
store_quantity = 3
store_shipDate = "2024-04-15T18:17:55.144Z"
store_status = "placed"
store_complete = True


url = 'https://petstore.swagger.io/v2/store/order'
headers = {'Content-Type': 'application/json'}

# Functions and methods 
def test_post_store():
    store = open('./fixtures/json/order.json')    
    data = json.loads(store.read())        
 
    response = requests.post(
        url=url,
        headers=headers,
        data=json.dumps(data),
        timeout=5
    )

    response_body = response.json()
    assert response.status_code == 200
    assert response_body['petId'] == store_petId
    assert response_body['quantity'] == store_quantity
    assert response_body['complete'] == store_complete

def test_get_store():
    response = requests.get(
        url=f'{url}/{store_id}',
        headers=headers
    )
    
    response_body = response.json()
    assert response.status_code == 200
    assert response_body['petId'] == store_petId
    assert response_body['quantity'] == store_quantity
    assert response_body['complete'] == store_complete

def test_delete_store():
    response = requests.delete(
        url=f'{url}/{store_id}',
        headers=headers
    )

    response_body = response.json()
    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == str(store_id)
