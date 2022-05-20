# fixtures can be used to make the test case executable first. Like launching a browser etc
# class name should always start with Camel Case
# if you ever create a class , then method must have 'self' argument
# the fixture defined in conftest will get executed before each method . if given at class leve;
# But if you want to run the fixture only once , then go to conftest file and add scope == class
# class name should always start with keyword Test , otherwise pytest will not run
# method name should have start with test 
import pytest


@pytest.mark.usefixtures("openBrowser")
class TestExample:

    def test_later(self):
        print("will be executed after setup mehtod 1")  # here we can do all the coding

    def test_later1(self):
        print("will be executed after setup mehtod 2 ")

    def test_later2(self):
        print("will be executed after setup mehtod 3")
