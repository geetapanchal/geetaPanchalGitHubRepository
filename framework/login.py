from utilities.reporting.startExtentReporting import StartReporting
from utilities.reporting.startLogging import Logging
from config import configuration
from framework.BaseClass import BaseClass
from framework.framework import Framework
from framework.verifyLoginPage import LoginPage


class Login(BaseClass):

    def __init__(self, parent, driver):
        self.driver = driver
        self.parent = parent
        self.LogStatus = StartReporting.LogStatus

    def login(self):
        lp = LoginPage(self.driver)
        if lp.getAdvance_btn() != "None":
            lp.getAdvance_btn().click()
            lp.getProceed_lnk().click()

        # user
        lp.getUserName().send_keys(configuration.username)
        Logging.logInfo("%s", "User " + configuration.username + " entered")
        self.parent.log(self.LogStatus.INFO, "User " + configuration.username + " entered")
        self.allureLogs("User " + configuration.username + " entered")

        # password
        lp.getPassword().send_keys(configuration.password)
        Logging.logInfo("%s", "Password entered")
        self.parent.log(self.LogStatus.INFO, "Password entered")
        self.allureLogs("Password entered")

        # submit button
        f = Framework(self.driver, self.parent)
        f.clickAndWait(lp.getLogin_btn(), 'submit button')
