# method name should start with test_
# file name should start with test_ or end with _test
import pytest as pytest


@pytest.mark.smoke
def test_case1():
    print('Hello')
@pytest.mark.xfail # xfail is used , when we want to execute the test case , but it shld not report pass or fail in o/p
def test_case2():
    print('jolly')