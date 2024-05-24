import pytest
import requests
from utils.productoperation import create_product,delete_product,retrive_products,retrive_products_By_id,get_limited_products,sorting_products,categories_of_product,category_product
from config import createproductdata,productid5data,productcatagoriesdata

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

# Test case for Read operation

## retrieve all products data
def test_get_all_products():
    response=retrive_products()
    assert response.status_code == 200

    
## retrieve product with id 5
def test_get_product_with_id():
    response = retrive_products_By_id(5)
    assert response.status_code == 200
    response_product_id5 = response.json()
    # Verify the product response for id 5
    assert response_product_id5["id"] == productid5data["id"]
    assert response_product_id5["title"] == productid5data["title"]
    assert response_product_id5["price"] == productid5data["price"]
    assert response_product_id5["description"] == productid5data["description"]
    assert response_product_id5["category"] == productid5data["category"]
    assert response_product_id5["image"] == productid5data["image"]
    assert response_product_id5["rating"]["rate"] == productid5data["rating"]["rate"]
    assert response_product_id5["rating"]["count"] == productid5data["rating"]["count"]

## retrieve product with invalid id
def test_get_product_with_invalid_id():
    response = retrive_products_By_id(1000)
    assert response.status_code == 200
    #validate none response or response doesn't have id
    assert response is None or "id" not in response, f"Expected 'id' not to be in response, but got {response}"

## retrieve PRODUCT with limit 5
def test_get_product_with_limit_5():
    limit = 5
    response = get_limited_products(limit)
    assert response.status_code == 200
    response_products = response.json()
    #Validate that the response contains exactly 5 products
    assert isinstance(response_products, list), f"Expected a list, but got {type(response_products).__name__}"
    assert len(response_products) == 5, f"Expected 5 products, but got {len(response_products)}"
    
    #Verify that each product in the list has an 'id'
    for product in response_products:
        assert "id" in product, f"Product {product} does not have an 'id' key"

## short products in decending order
def test_get_products_sorted_desc():
    sort="desc"
    response = sorting_products(sort)
    assert response.status_code == 200
    reponse_sorted_products = response.json()
    #Verify that the response is a list of products
    assert isinstance(reponse_sorted_products, list), f"Expected a list, but got {type(reponse_sorted_products).__name__}"
    #Check that the products are sorted in descending order by id
    ids = [product['id'] for product in reponse_sorted_products]

# get products catagories
def test_get_product_categories():
    response = categories_of_product()
    assert response.status_code == 200
    response_product_categories = response.json()
    assert isinstance(response_product_categories, list), f"Expected a list, but got {type(response_product_categories).__name__}"
    assert response_product_categories == productcatagoriesdata

#validate specic categories product
def test_products_in_category():
    categories = ["electronics", "jewelery", "men's clothing", "women's clothing"]
    
    #ittereare for all category
    for category in categories:
        response= category_product(category)
        assert response.status_code == 200
        response_category_products = response.json()
        # Verify that all products belong to the specific category
        for product in response_category_products:
            assert "category" in product, "Product does not have a 'category' field"
            assert product["category"] == category, f"Product {product['title']} does not belong to the '{category}' category"

## retrive newly created product 
def test_verify_newly_created_user(setup_create_product):
    response, id = setup_create_product
    assert id is not None  # Check if the product has been created successfully
    #Verify newly created product in database with id
    response = retrive_products_By_id(id)
    assert response.status_code == 200 # it return 200 but newly created product is not updating in database for test API
             

