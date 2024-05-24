# API Testing With Pytest

## Getting started

* To download and install `pytest`, run this command from the terminal : `pip install pytest`
* To download and install `requests`, run this command from the terminal : `pip install requests`

To ensure all dependencies are resolved in a CI environment, in one go, add them to a `requirements.txt` file.
* Then run the following command : `pip install -r requirements.txt`
* run `bash setup.sh` to install and configure everything at one place

By default pytest only identifies the file names starting with `test_` or ending with `_test` as the test files.

Pytest requires the test method names to start with `test`. All other method names will be ignored even if we explicitly ask to run those methods.

A sample test below :

```python
def test_get_all_products():
    response=retrive_products()
    assert response.status_code == 200

```

### Test step functionality : 

* A detailed explanation of each step has been mentioned in test file.

## Running tests

### Run All test case

If your tests are contained inside a folder 'tests', then run the following command : `pytest tests` 

### Run All API test case

If your tests are contained inside a folder 'tests', then run the following command : `pytest tests/apitest` 

### Run All task warrior test case

If your tests are contained inside a folder 'tests', then run the following command : `pytest tests/taskwarriortest` 

### Run specific testcase/suite

run the following command for read_operation tests : `pytest tests_read_operation.py` 

## Report

To generate html report, run the following command : `pytest tests --html=report.html -s`

## CI intigration
* Intigrated github action to run test on each push and pull request. code can be found in .github/workflow/push.yml

## Findings and issues:

* Few test case will return wrong response code due to Test API. example: creating new user should returns 201 but it returns 200



