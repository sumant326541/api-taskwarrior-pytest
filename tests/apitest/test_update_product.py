import pytest
import requests
from utils.productoperation import create_product,delete_product,update_product,retrive_products_By_id
from config import createproductdata,updateproductdata

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



# Test case for Update operation
## update product details
def test_update_product(setup_create_product):
    response, id = setup_create_product
    id = 1
    response = update_product(id,updateproductdata)  # > newly created product was not updating in database hence trying to update existing product with id = 1
    #Verify that the user has been updated succefully
    assert response.status_code == 200
    updated_product_response = response.json()
   
    #Verify the id in response body = 1
    assert updated_product_response["id"] == id
    assert updated_product_response["title"] == updateproductdata["title"]
    assert updated_product_response["price"] == updateproductdata["price"]
    assert updated_product_response["description"] == updateproductdata["description"]
    assert updated_product_response["image"] == updateproductdata["image"]
    assert updated_product_response["category"] == updateproductdata["category"]

    #Verify product has been updated in data base with id 1
    id=1
    retrive_products_By_id(id)
    assert response.status_code == 200
    #assert response.json()["title"] == updateproduct["title"]  # >  product has not been upadted in database because of test API

## update an non existing product details
def test_update_nonexisting_products():
    id = 1000
    response = update_product(id,updateproductdata)
    #assert response.status_code == 404 # to check, there is no product with id=1000, but it returns 200 because of test API
    assert response.status_code == 200 