import pytest
import sys
import os
from framework.BaseClass import BaseClass

from utilities.reporting.startExtentReporting import StartReporting
import jpype as jp


@pytest.mark.sites
class TestDummy(BaseClass):
    # store extent function
    ExtentReport = StartReporting
    reportpath = sys.path[0] + os.sep + "reports" + os.sep + "extentReport" + os.sep + "dummy"  + '.html'
    extent = StartReporting.ExtentReports(reportpath)

    LogStatus = ExtentReport.LogStatus
    # ext = ExtentReport.extent
    parent = extent.startTest("dummy")

    def test_login1(self):
        # Check if first screen available and user logged in
        TestDummy.parent.log(TestDummy.LogStatus.PASS, "Menu.json read failed")


    def test_shutdown1(self):
        # push data to report
        TestDummy.extent.endTest(TestDummy.parent)
        TestDummy.extent.flush()


