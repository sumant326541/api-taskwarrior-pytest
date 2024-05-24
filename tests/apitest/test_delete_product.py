import pytest
import requests
from utils.productoperation import create_product,delete_product
from config import createproductdata,productid5data

# Fixture for setup actions (creating a new user)
@pytest.fixture
def setup_create_product(): 
    response = create_product(createproductdata)
    #assert response.status_code == 201 #it should return 201 in real api but will return you an object with a new id and response code 200. remember that nothing in real will insert into the database. so if you want to access the new id you will get a 404 error.
    assert response.status_code == 200
    id = response.json()["id"]
    
    #we can also consider below point in SetUP
    #If authentication or authorization mechanisms are in place, ensure that test users are authenticated and authorized to perform CRUD operations.
    #Obtain necessary access tokens or credentials to authenticate test requests.

    yield [response, id]  # Provide the response, id to the test function

    # Teardown: Delete the created user after the test completes
    delete_product(id)


# Test case for Delete operation
## test delete existing products with id 5
def test_delete_existing_product():
    response = delete_product(5)
    response_deleted_product_id5 = response.json() # it returns prducts details for id 5
    assert response_deleted_product_id5["id"] == productid5data["id"]
    assert response_deleted_product_id5["title"] == productid5data["title"]
    assert response_deleted_product_id5["price"] == productid5data["price"]
    assert response_deleted_product_id5["description"] == productid5data["description"]
    assert response_deleted_product_id5["category"] == productid5data["category"]
    assert response_deleted_product_id5["image"] == productid5data["image"]
    assert response_deleted_product_id5["rating"]["rate"] == productid5data["rating"]["rate"]
    assert response_deleted_product_id5["rating"]["count"] == productid5data["rating"]["count"]


## test delete newly created products
def test_delete_new_created_product(setup_create_product):
    response, id = setup_create_product
    response = delete_product(id)
    deleted_product = response.json()
    assert deleted_product is None


## test delete non-existing product
def test_delete_nonexisting_product():
    response = delete_product(21)
    response_deleted_product_id21 = response.json()
    assert response_deleted_product_id21 is None