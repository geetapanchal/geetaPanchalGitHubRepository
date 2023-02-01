from selenium.webdriver.common.by import By

from config import configuration
from framework.BaseClass import BaseClass
from utilities.reporting.startLogging import Logging
from utilities.reporting.startExtentReporting import StartReporting


class Framework(BaseClass):

    def __init__(self, driver, parent):
        self.driver = driver
        self.parent = parent
        self.LogStatus = StartReporting.LogStatus

    def check_user_loggendIn(self):
        # check if user loggend in successfully
        element = self.wait_visibility_of_element_returnEle(By.CLASS_NAME, "username")
        try:
            assert element.text == configuration.username
        except AssertionError:
            Logging.logInfo("%s", "Username - " + configuration.username + " not visible")
            self.parent.log(self.LogStatus.FAIL, "Username - " + configuration.username + " not visible")
            self.allureLogs("Username - " + configuration.username + " not visible")
        else:
            Logging.logInfo("%s", "User - " + element.text + "  visible on welcome screen")
            self.parent.log(self.LogStatus.PASS, "User - " + element.text + "  visible on welcome screen")
            self.allureLogs("User - " + element.text + " visible on welcome screen")

    def check_dashboard_visible(self):
        # Verify dashboard opened

        DashTitle = self.wait_visibility_of_element_returnEle(By.CLASS_NAME, "header")

        try:
            assert DashTitle.text != ""
        except AssertionError:
            Logging.logInfo("%s", "Dashboard title not visible")
            self.parent.log(self.LogStatus.FAIL, "Dashboard title not visible")
            self.allureLogs("Dashboard title not visible")
        else:
            Logging.logInfo("%s", "Dashboard title : " + DashTitle.text)
            self.parent.log(self.LogStatus.INFO, "Dashboard title : " + DashTitle.text)
            self.allureLogs("Dashboard title : " + DashTitle.text)

    def clickAndWait(self, webElement, txt):
        webElement.click()
        msg = txt + " clicked successfully"
        print(txt + " clicked successfully")
        Logging.logInfo("%s", msg)
        self.parent.log(self.LogStatus.INFO, msg)

    def comparingArrays(self, jsonvalues, UIValues):
        self.parent.log(self.LogStatus.INFO, "Expected values from json : " + str(jsonvalues))
        self.parent.log(self.LogStatus.INFO, "Actual values from UI : " + str(jsonvalues))
        self.parent.log(self.LogStatus.INFO, "")

        self.parent.log(self.LogStatus.INFO, "Started comapring Json and UI values")
        self.allureLogs("Started comapring Json and UI values")

        comparingList = []
        for i in range(len(jsonvalues)):
            comparingList.append(0)

        for i in range(len(jsonvalues)):
            try:
                if UIValues[i].__contains__(jsonvalues[i]):
                    comparingList[i] = 1
                    self.parent.log(self.LogStatus.INFO, "UI value - " + UIValues[i])
                    self.parent.log(self.LogStatus.INFO, "Verified with json value '" + jsonvalues[
                        i] + "' !! Matched counter value 	 '" + str(comparingList))
                else:
                    Logging.logInfo("%s", "Values are not as per expectation.")

                try:
                    assert jsonvalues[i] == UIValues[i]
                except AssertionError:
                    Logging.logInfo("%s", "values from both array " + jsonvalues[i] + " , " + UIValues[i])
                    self.parent.log(self.LogStatus.FAIL, "Testcase FAIL - Json & UI values not matched")
                    self.parent.log(self.LogStatus.INFO, "Expected - " + jsonvalues[i])
                    self.parent.log(self.LogStatus.INFO, "Actual - " + UIValues[i])
                    self.allureLogs("Testcase FAIL - Json & UI values not matched")
                    self.allureLogs("Expected - " + jsonvalues[i])
                    self.allureLogs("Actual - " + UIValues[i])
                else:
                    Logging.logInfo("%s", "values from both array " + jsonvalues[i] + " , " + UIValues[i])
                    self.parent.log(self.LogStatus.PASS, "Testcase PASS - Json & UI values matched")
                    self.allureLogs("Expected - " + jsonvalues[i] + " , Actual - " + UIValues[i]+ " !!! \n Testcase PASS - values matched ")

                self.parent.log(self.LogStatus.INFO, "")
            except Exception as e:
                print(e)
                self.parent.log(self.LogStatus.FAIL, e)
                self.allureLogs(e)
                Logging.logInfo("%s", e)
