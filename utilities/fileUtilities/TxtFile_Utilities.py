import os
import sys
from platform import python_version
from framework.BaseClass import BaseClass
import selenium


class TxtFileUtils(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    def add_env_detailto_file(self, browser, url, user):
        envfile = sys.path[0] + os.sep + "reports"+os.sep+"allureReport"+os.sep+"reports"+os.sep+"environment.properties"

        if browser == "ff":
            browser = "Firefox"

        with open(envfile, 'w') as f4:
            f4.write("URL="+url+"\n")
            f4.write("User="+user+"\n")
            f4.write("Browser=" + browser + " " + str(self.driver.capabilities['browserVersion']) + "\n")
            f4.write("Python ="+python_version()+"\n")
            f4.write("Selenium ="+selenium.__version__)
        f4.closed

