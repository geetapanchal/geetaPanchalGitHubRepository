import json
import sys
from framework.BaseClass import BaseClass
from utilities.reporting.startLogging import Logging
from selenium.webdriver.common.by import By
from utilities.reporting.startExtentReporting import StartReporting

from utilities.fileUtilities.ReadJson import ReadJson


class Refresh(BaseClass):

    def __init__(self, driver, jsonfilepath, parent):
        self.jsonfilepath = jsonfilepath
        self.driver = driver
        self.parent = parent
        self.LogStatus = StartReporting.LogStatus

    wRefreshButton = (By.XPATH, "//*[@title='Refresh']")

    def verifyRefresh(self):
        try:
            # Expected value from json
            obj = json.loads(ReadJson.readJson(sys.path[0] + self.jsonfilepath))
            ExpectedTitle = (obj['dashBoard']['dashboardButtons']['autoRefresh']['tabTitle'])
            ExpectedTooltip = (obj['dashBoard']['dashboardButtons']['autoRefresh']['tooltip'])

            # Actual value from GUI
            self.wait_visibility_of_element_located(By.XPATH,"//*[@title='Refresh']")
            wActualTitle = self.driver.find_element(*Refresh.wRefreshButton)
            sActualTitle = wActualTitle.get_attribute("title")
            sActualTooltip = wActualTitle.get_attribute("title")

            # isDiplayed from UI and json
            uiDisplayed = wActualTitle.is_displayed()
            jsDisplayed = (obj['dashBoard']['dashboardButtons']['autoRefresh']['isdisplayed'])

            if uiDisplayed and jsDisplayed:

                self.parent.log(self.LogStatus.INFO, "Expected value : " + ExpectedTitle)
                self.parent.log(self.LogStatus.INFO, "Actual value : " + sActualTitle)
                self.allureLogs("Expected value : " + ExpectedTitle)
                self.allureLogs("Actual value : " + sActualTitle)

                # assertion and logging
                try:
                    assert ExpectedTitle == sActualTitle
                except AssertionError:
                    print("Refresh Title did not matched with expected")
                    self.parent.log(self.LogStatus.FAIL, "Refresh Title did not matched with expected")
                    self.allureLogs("Refresh Title did not matched with expected")
                else:
                    print("Refresh Title matched expected")
                    self.parent.log(self.LogStatus.PASS, "Refresh Title matched expected")
                    self.allureLogs("Refresh Title matched expected")

                self.allureLogs("")
                self.parent.log(self.LogStatus.INFO, "")
                self.parent.log(self.LogStatus.INFO, "Expected tooltip : " + ExpectedTooltip)
                self.parent.log(self.LogStatus.INFO, "Actual tooltip : " + sActualTooltip)
                self.allureLogs("Expected tooltip : " + ExpectedTooltip)
                self.allureLogs("Actual tooltip : " + sActualTooltip)

                try:
                    assert ExpectedTooltip == sActualTooltip
                except AssertionError:
                    print("Refresh button Tooltip did not matched with expected")
                    self.parent.log(self.LogStatus.FAIL, "Refresh button Tooltip did not matched with expected")
                    self.allureLogs("Refresh button Tooltip did not matched with expected")
                else:
                    print("Refresh button Tooltip matched with expected")
                    self.parent.log(self.LogStatus.PASS, "Refresh button Tooltip matched with expected")
                    self.allureLogs("Refresh button Tooltip matched with expected")

            elif uiDisplayed and not jsDisplayed:
                self.parent.log(self.LogStatus.FAIL, ExpectedTitle + " is visible and expected is blank")
                self.allureLogs(ExpectedTitle + " is visible and expected is blank")
            elif not uiDisplayed and jsDisplayed:
                self.parent.log(self.LogStatus.FAIL, ExpectedTitle + " is not visible and expected is visible")
                self.allureLogs(ExpectedTitle + " is not visible and expected is visible")
            elif not uiDisplayed and not jsDisplayed:
                self.parent.log(self.LogStatus.PASS, ExpectedTitle + " is not visible and expected is blank")
                self.allureLogs(ExpectedTitle + " is not visible and expected is blank")
            else:
                self.parent.log(self.LogStatus.FAIL, "Unknown result")
                self.allureLogs("Unknown result")

        except Exception as e:
            print(e)
            self.parent.log(self.LogStatus.FAIL, e)
            self.allureLogs(e)
            Logging.logInfo("%s", e)



