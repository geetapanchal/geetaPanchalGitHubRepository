import pytest

from framework.BaseClass import BaseClass
from framework.openDashboard import OpenDashboard


@pytest.mark.topApplications
class TestTopApplications(BaseClass):

    def test_topApplications(self):
        print("Top appli")
        t = OpenDashboard("")
        t.dashboardName = 'Top Applications'
        t.openDashboard()
