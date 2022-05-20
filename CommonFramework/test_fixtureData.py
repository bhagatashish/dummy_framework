import pytest
# class name should always start with keyword Test , otherwise pytest will not run
# method name should have start with test

@pytest.mark.usefixtures("usersData")
class Testdata:

    def test_later(self):
        print("will be executed after setup mehtod 1")  # here we can do all the coding
