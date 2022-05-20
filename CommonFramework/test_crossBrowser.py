# as we are using method directly without class ,hence no need to add self keyword
# this will be executed 3 times, because in the conftest fixture file we are passing 3 arguments


import pytest


@pytest.mark.usefixtures()

def test_crossBrowser(crossBrowserTesting): # as we are not using class , hence fixture name should be given in the argumnet

    print(crossBrowserTesting[1])