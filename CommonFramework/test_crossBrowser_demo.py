# as we are using method directly without class ,hence no need to add self keyword
# this will be executed 3 times, because in the conftest fixture file we are passing 3 arguments
# here crossBrowserTesting is a tuple

import pytest
from CommonFramework.baseclass import baseClass



@pytest.mark.usefixtures("crossBrowserTesting")
class Test_browser(baseClass):
    def test_crossBrowser(self,crossBrowserTesting ):  # as we are now using class , hence fixture name should be given in the argumnet
        log = self.test_logs()
        log.info(crossBrowserTesting)
        print(crossBrowserTesting[1])