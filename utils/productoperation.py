import requests
from config import BASE_URL,resourceproducts,resourcecategories,resourcecategory

#function to create products
def create_product(createproduct):
    response = requests.post(f"{BASE_URL}/{resourceproducts}", json=createproduct)
    return response

#function to update product with id and update data
def update_product(id,updateproductdata):
    response = requests.put(f"{BASE_URL}/{resourceproducts}/{id}", json=updateproductdata)  # > newly created product was not updating in database hence trying to update existing product with id = 1
    return response
#function for retrive all products
def retrive_products():
    response = requests.get(f"{BASE_URL}/{resourceproducts}")
    return response 

#function for retrive products with id
def retrive_products_By_id(id):
    response = requests.get(f"{BASE_URL}/{resourceproducts}/{id}")
    return response 

# function to retrive limited product 
def get_limited_products(limit):
    response = requests.get(f"{BASE_URL}/{resourceproducts}?limit={limit}")
    return response

# function to sortproducts
def sorting_products(sort):
    response = requests.get(f"{BASE_URL}/{resourceproducts}?sort={sort}")
    return response

#function to get "all categories" of product
def categories_of_product():
    response = requests.get(f"{BASE_URL}/{resourcecategories}")
    return response

#function to get product by category
def category_product(category):
    response = requests.get(f"{BASE_URL}/{resourcecategory}/{category}")
    return response

#delete product function with id
def delete_product(id):
    response = requests.delete(f"{BASE_URL}/{resourceproducts}/{id}")
    assert response.status_code == 200
    return response