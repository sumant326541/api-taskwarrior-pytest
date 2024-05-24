import pytest
import requests
from utils.productoperation import create_product,delete_product
from config import createproductdata

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


# Test case for Create operation
## Create a new product with valid data
def test_create_post(setup_create_product):
    response, id = setup_create_product
    assert id is not None  # Check if the user has been created successfully

    # Verify that the response body contains the created product data 
    created_product = response.json()
    assert created_product["title"] == createproductdata["title"]
    assert created_product["price"] == createproductdata["price"]
    assert created_product["description"] == createproductdata["description"]
    assert created_product["image"] == createproductdata["image"]
    assert created_product["category"] == createproductdata["category"]
   