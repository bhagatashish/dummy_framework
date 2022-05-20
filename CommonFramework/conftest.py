'''everything written here will always
# get executed for all the files. The file is mandatory to have a name as "conftest"
# fixtures can be used to make the test case executable first. Like launching a browser etc
# data driven and parameterizartion can be done with return statements in tuple format
# when we define fixture to class only then it will run only once

'''
import pytest


@pytest.fixture(scope="class")
def openBrowser():
    print("Browser is open")
    yield
    print("browser closed")


@pytest.fixture()
def usersData():
    return 'ashish', 'bhagat', 'ashish.bhagat@gmail.com'


@pytest.fixture(params=[('chrome', 'ashish', 'bhagat'), ('firefox', 'mohit', 'bhagat'), ('ie', 'neeru')])
def crossBrowserTesting(request):  # here request is default keyword and it should never be changed
    return request.param
