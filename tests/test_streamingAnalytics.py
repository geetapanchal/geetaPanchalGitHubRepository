import pytest
from framework.BaseClass import BaseClass
from framework.openDashboard import OpenDashboard
from config import constants
from src.verifyDashboardTitle import DashboardTitle

@pytest.mark.streamingAnalytics
class TestStreamingAnalytics(BaseClass):

    def test_streamingAnalytics(self):
        OD = OpenDashboard(constants.StreamAnalytic)
        OD.openDashboard()
        DT = DashboardTitle(self.driver, constants.JSONFILESTREAMANALYTICS)

