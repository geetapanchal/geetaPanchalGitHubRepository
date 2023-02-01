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
from config.src.verifyGridtitle_ConfigUI import GridTitle
from config.src.verifyRefresh import Refresh
from utilities.reporting.startExtentReporting import StartReporting


@pytest.mark.Streaminganalytics
class TestStreamingAnalytics(BaseClass):
    # store extent function
    ExtentReport = StartReporting
    reportpath = sys.path[0] + os.sep + "reports" + os.sep + "extentReport" + os.sep + "StreamingAnalytics" + '.html'
    extent = StartReporting.ExtentReports(reportpath)
    LogStatus = ExtentReport.LogStatus
    logindash = extent.startTest("Login")
    parent = extent.startTest("Streaming Analytics")
    DashTabTitle = extent.startTest("Verify Dash Tab title")
    DashTitle = extent.startTest("Verify Dashboard title")
    Refresh = extent.startTest("Verify Refresh")
    GridTitle = extent.startTest("Verify Grid title")

    def test_login(self):
        # Login to the application
        tl = Login(TestStreamingAnalytics.logindash, self.driver)
        tl.login()

        # Check if first screen available and user logged in
        fw = Framework(self.driver, TestStreamingAnalytics.logindash)
        fw.check_user_loggendIn()
        TestStreamingAnalytics.extent.endTest(TestStreamingAnalytics.logindash)

    def test_open_dashboard(self):
        # Open dashboard
        OD = OpenDashboard(self.driver, constants.ConfigStreamingAnalytics, TestStreamingAnalytics.parent)
        OD.openDashboard()
        TestStreamingAnalytics.extent.endTest(TestStreamingAnalytics.parent)

    def test_dash_tab_title(self):
        # Verify dash tab title
        DT = DashTabTitle(self.driver, constants.JSONSTREAMINGANALYTICS, TestStreamingAnalytics.DashTabTitle)
        DT.verifyDashTabtitle()
        TestStreamingAnalytics.extent.endTest(TestStreamingAnalytics.DashTabTitle)

    def test_dashboard_title(self):
        # Switch frame
        DT = DashboardTitle(self.driver, constants.JSONSTREAMINGANALYTICS, TestStreamingAnalytics.DashTitle)
        self.wait_visibility_of_element_located(By.XPATH, "//iframe[@id='Web-web-widget']")
        self.driver.switch_to.frame(DT.getiframe())

        # Check dashboard visible
        fw = Framework(self.driver, self.parent)
        fw.check_dashboard_visible()

        # Verify dashboard title
        DT.verifyDashtitle()
        TestStreamingAnalytics.extent.endTest(TestStreamingAnalytics.DashTitle)

    def test_refresh(self):
        r = Refresh(self.driver, constants.JSONSTREAMINGANALYTICS, TestStreamingAnalytics.Refresh)
        r.verifyRefresh()
        TestStreamingAnalytics.extent.endTest(TestStreamingAnalytics.Refresh)

    def test_grid_title(self):
        GT = GridTitle(self.driver, constants.JSONSTREAMINGANALYTICS, TestStreamingAnalytics.GridTitle)
        GT.verifyGridTitle()
        TestStreamingAnalytics.extent.endTest(TestStreamingAnalytics.GridTitle)

    def teardown_class(self):
        TestStreamingAnalytics.extent.flush()
