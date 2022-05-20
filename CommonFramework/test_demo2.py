import pytest
# if you want to skip any test case give pytest.mark.skip. it will not exectue the test case
# There can be some test cases which we want to skip or can be smoke .
# to run smoke test cases apply pytest -m smoke -v -s , here m stands for mark
# -v stands for verbose
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == 'Hi', 'The string does not match'
@pytest.mark.smoke
def test_Creditcard(openBrowser):
    a = 2
    b = 6
    assert a + 4 == b , 'Not matched'




