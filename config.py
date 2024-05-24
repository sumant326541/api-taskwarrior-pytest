import json

# Read data from apidata.json file
with open('testdata/apidata.json', 'r') as file:
    apidata = json.load(file)

# Extract base URL, resource URL
BASE_URL = apidata.get('base_url')
resourceproducts = apidata.get('products')
resourcecategories = apidata.get('categories')
resourcecategory = apidata.get('category')

# Read data from updateproduct_data.json file
with open('testdata/updateproduct_data.json', 'r') as file:
    updateproductdata = json.load(file)

# Read data from createproduct_data.jsonfile
with open('testdata/createproduct_data.json', 'r') as file:
    createproductdata = json.load(file)

# Read productid5 data from apidata.json file
with open('testdata/productid5_data.json', 'r') as file:
    productid5data = json.load(file)


# Read product categories data from productcategories_data.json file
with open('testdata/productcategories_data.json', 'r') as file:
    productcatagoriesdata = json.load(file)