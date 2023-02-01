import os
import sys
import pytest
from config import constants
from framework.login import Login
from framework.BaseClass import BaseClass
from selenium.webdriver.common.by import By
from framework.framework import Framework
from config.src.verifyTabTitle import DashTabTitle
from framework.openDashboard import OpenDashboard
from config.src.verifyDashboardTitle import DashboardTitle
from config.src import Refresh
from utilities.reporting.startExtentReporting import StartReporting


def teardown_class():
    TestSites.extent.flush()


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
    Refresh = extent.startTest("Verify Refresh")

    def test_login(self):
        # Login to the application
        tl = Login(TestSites.logindash, self.driver)
        tl.login()

        # Check if first screen available and user logged in
        fw = Framework(self.driver, TestSites.logindash)
        fw.check_user_loggendIn()
        TestSites.extent.endTest(TestSites.logindash)

    def test_open_dashboard(self):
        # Open dashboard sites
        OD = OpenDashboard(self.driver, constants.ConfigSites, TestSites.parent)
        OD.openDashboard()
        TestSites.extent.endTest(TestSites.parent)

    def test_dash_tab_title(self):
        # Verify dash tab title
        DT = DashTabTitle(self.driver, constants.JSONSITES, TestSites.DashTabTitle)
        DT.verifyDashTabtitle()
        TestSites.extent.endTest(TestSites.DashTabTitle)

    def test_dashboard_title(self):
        # Switch frame
        DT = DashboardTitle(self.driver, constants.JSONSITES, TestSites.DashTitle)
        self.wait_visibility_of_element_located(By.XPATH, "//iframe[@id='Web-web-widget']")
        self.driver.switch_to.frame(DT.getiframe())

        # Check dashboard visible
        fw = Framework(self.driver, self.parent)
        fw.check_dashboard_visible()

        # Verify dashboard title
        DT.verifyDashtitle()
        TestSites.extent.endTest(TestSites.DashTitle)

    def test_refresh(self):
        r = Refresh(self.driver, constants.JSONSITES, TestSites.Refresh)
        r.verifyRefresh()
        TestSites.extent.endTest(TestSites.Refresh)
