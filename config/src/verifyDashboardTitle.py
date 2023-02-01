import json
import sys
from framework.BaseClass import BaseClass
from utilities.reporting.startLogging import Logging
from selenium.webdriver.common.by import By
from utilities.reporting.startExtentReporting import StartReporting

from utilities.fileUtilities.ReadJson import ReadJson


class DashboardTitle(BaseClass):

    def __init__(self, driver, jsonfilepath, parent):
        self.jsonfilepath = jsonfilepath
        self.driver = driver
        self.parent = parent

        self.LogStatus = StartReporting.LogStatus

    wUITitle = (By.XPATH, "//*[@class='header']")
    wFrame = (By.XPATH, "//iframe[@id='Web-web-widget']")

    def getiframe(self):
        return self.driver.find_element(*DashboardTitle.wFrame)

    def verifyDashtitle(self):
        try:
            # Expected value from json
            obj = json.loads(ReadJson.readJson(sys.path[0] + self.jsonfilepath))
            ExpectedTitle = (obj['dashBoard']['dashboardTitle'])
            ExpectedTooltip = (obj['dashBoard']['dashboardTitle'])

            # Actual value from GUI
            wActualTitle = self.driver.find_element(*DashboardTitle.wUITitle)
            sActualTitle = wActualTitle.text
            sActualTooltip = wActualTitle.get_attribute("title")

            self.parent.log(self.LogStatus.INFO, "Expected dashboard title : " + ExpectedTitle)
            self.parent.log(self.LogStatus.INFO, "Actual dashboard title : " + sActualTitle)
            self.allureLogs("Expected dashboard title : " + ExpectedTitle)
            self.allureLogs("Actual dashboard title : " + sActualTitle)

            # logging and reporting
            try:
                assert ExpectedTitle == sActualTitle
            except AssertionError:
                print("DashBoard Title did not matched with expected")
                self.parent.log(self.LogStatus.FAIL, "DashBoard Title did not matched with expected")
                self.allureLogs("DashBoard Title did not matched with expected")
            else:
                print("DashBoard Title matched expected")
                self.parent.log(self.LogStatus.PASS, "DashBoard Title matched expected")
                self.allureLogs("DashBoard Title matched expected")

            self.allureLogs("")
            self.parent.log(self.LogStatus.INFO,"")
            self.parent.log(self.LogStatus.INFO, "Expected dashboard tooltip : " + ExpectedTooltip)
            self.parent.log(self.LogStatus.INFO, "Actual dashboard tooltip : " + sActualTooltip)
            self.allureLogs("Expected dashboard tooltip : " + ExpectedTooltip)
            self.allureLogs("Actual dashboard tooltip : " + sActualTooltip)

            try:
                assert ExpectedTooltip == sActualTooltip
            except AssertionError:
                print("DashBoard title Tooltip did not matched with expected")
                self.parent.log(self.LogStatus.FAIL, "DashBoard title Tooltip did not matched with expected")
                self.allureLogs("DashBoard title Tooltip did not matched with expected")
            else:
                print("Dashboard title Tooltip matched with expected")
                self.parent.log(self.LogStatus.PASS, "Dashboard title Tooltip matched with expected")
                self.allureLogs("Dashboard title Tooltip matched with expected")

        except Exception as e:
            print(e)
            self.parent.log(self.LogStatus.FAIL, e)
            self.allureLogs(e)
            Logging.logInfo("%s", e)
