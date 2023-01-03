import json
import sys
from framework.BaseClass import BaseClass
from selenium.webdriver.common.by import By
from utilities.fileUtilities.ReadJson import ReadJson
from utilities.reporting.startExtentReporting import StartReporting


class DashTabTitle(BaseClass):

    def __init__(self, driver, jsonfilepath, parent):
        self.jsonfilepath = jsonfilepath
        self.driver = driver
        self.parent = parent
        self.LogStatus = StartReporting.LogStatus

    wtabTitle = (By.CSS_SELECTOR, ".tab-txt")

    def verifyDashTabtitle(self):
        # Expected value from json
        obj = json.loads(ReadJson.readJson(sys.path[0] + self.jsonfilepath))
        ExpectedTitle = (obj['dashBoard']['tabTitle'])
        ExpectedTooltip = (obj['dashBoard']['tabTitle'])

        # Actual value from GUI
        wActualTitle = self.driver.find_element(*DashTabTitle.wtabTitle)
        sActualTitle = (wActualTitle.text).strip()
        sActualTooltip = (wActualTitle.get_attribute("title")).strip()

        self.parent.log(self.LogStatus.INFO, "Expected dashboard title : " + ExpectedTitle)
        self.parent.log(self.LogStatus.INFO, "Actual dashboard title : " + sActualTitle)
        self.allureLogs("Expected dashboard title : " + ExpectedTitle)
        self.allureLogs("Actual dashboard title : " + sActualTitle)

        # logging and reporting
        try:
            assert ExpectedTitle == sActualTitle
        except AssertionError:
            print("Dash Tab title did not matched with expected")
            self.parent.log(self.LogStatus.FAIL, "Dash Tab title did not matched with expected")
            self.allureLogs("Dash Tab title did not matched with expected")
        else:
            print("Dash Tab title matched expected")
            self.parent.log(self.LogStatus.PASS, "Dash Tab title matched expected")
            self.allureLogs("Dash Tab title matched expected")

        self.parent.log(self.LogStatus.INFO,"")
        self.parent.log(self.LogStatus.INFO, "Expected dash tab tooltip : " + ExpectedTooltip)
        self.parent.log(self.LogStatus.INFO, "Actual dash tab tooltip : " + sActualTooltip)
        self.allureLogs("Expected dash tab tooltip : " + ExpectedTooltip)
        self.allureLogs("Actual dash tab tooltip : " + sActualTooltip)

        try:
            assert ExpectedTooltip == sActualTooltip
        except AssertionError:
            print("Dash tab title Tooltip did not matched with expected")
            self.parent.log(self.LogStatus.FAIL, "Dash tab title Tooltip did not matched with expected")
            self.allureLogs("Dash tab title Tooltip did not matched with expected")
        else:
            print("Dash tab title Tooltip matched with expected")
            self.parent.log(self.LogStatus.PASS, "Dash tab title Tooltip matched with expected")
            self.allureLogs("Dash tab title Tooltip matched with expected")

