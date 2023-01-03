import os
import sys
import pytest
from config import constants
from framework.login import Login
from framework.BaseClass import BaseClass
from selenium.webdriver.common.by import By
from framework.framework import Framework
from src.VerifyTabTitle import DashTabTitle
from framework.openDashboard import OpenDashboard
from src.verifyDashboardTitle import DashboardTitle
from utilities.reporting.startExtentReporting import StartReporting


@pytest.mark.sites
class TestSites(BaseClass):
    # store extent function
    ExtentReport = StartReporting
    reportpath = sys.path[0] + os.sep + "reports" + os.sep + "extentReport" + os.sep + "Sites" + '.html'
    extent = StartReporting.ExtentReports(reportpath)
    LogStatus = ExtentReport.LogStatus
    logindash = extent.startTest("Login")
    parent = extent.startTest("Sites")
    DashTabTitle = extent.startTest("Verify Dash Tab title")
    DashTitle = extent.startTest("Verify Dashboard title")

    def test_login(self):
        # Login to the application
        tl = Login(TestSites.logindash, self.driver)

        # tl = TestLogin(TestSites.logindash)
        tl.login()
        # tl = TestLogin()
        # tl.parent = TestSites.logindash

        # Check if first screen available and user logged in
        fw = Framework(self.driver, TestSites.logindash)
        # fw = Framework(TestSites.logindash)
        fw.check_user_loggendIn()

    def test_open_dashboard(self):
        # Open dashboard sites
        OD = OpenDashboard(self.driver, constants.ConfigSites, TestSites.parent)
        #OD = OpenDashboard(constants.ConfigSites, TestSites.parent)
        OD.openDashboard()

    def test_dash_tab_title(self):
        # Verify dash tab title
        DT = DashTabTitle(self.driver, constants.JSONFILESITES, TestSites.DashTabTitle)
        DT.verifyDashTabtitle()

    def test_dashboard_title(self):
        # Switch frame
        DT = DashboardTitle(self.driver, constants.JSONFILESITES, TestSites.DashTitle)
        self.wait_visibility_of_element_located(By.XPATH, "//iframe[@id='Web-web-widget']")
        self.driver.switch_to.frame(DT.getiframe())

        # Check dashboard visible
        fw = Framework(self.driver, self.parent)
        fw.check_dashboard_visible()

        # Verify dashboard title
        DT.verifyDashtitle()

    def test_generate_xtentReport(self):
        # push data to report
        TestSites.extent.endTest(TestSites.logindash)
        TestSites.extent.endTest(TestSites.parent)
        TestSites.extent.endTest(TestSites.DashTabTitle)
        TestSites.extent.endTest(TestSites.DashTitle)
        TestSites.extent.flush()
