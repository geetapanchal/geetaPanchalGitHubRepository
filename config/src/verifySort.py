import json
import sys
from framework.BaseClass import BaseClass
from selenium.webdriver.common.by import By
from utilities.fileUtilities.ReadJson import ReadJson
from utilities.reporting.startLogging import Logging
from utilities.reporting.startExtentReporting import StartReporting


class SortGridColumnData(BaseClass):
    """
    This class verify data in columns of grid is sorted in ascending or descending order.
    Sorting on alphanumeric and numeric column data
    """

    def __init__(self, driver, jsonfilepath, parent):
        self.jsonfilepath = jsonfilepath
        self.driver = driver
        self.parent = parent
        self.LogStatus = StartReporting.LogStatus

    wGridTitle = (By.XPATH, "//tr/th")
    wGridColumnData = (By.XPATH, "//tr/td")

    def verifySort(self):
        try:
            sGridTitle = self.driver.find_elements(*SortGridColumnData.wGridTitle)
            sGridColumnData = self.driver.find_elements(*SortGridColumnData.wGridColumnData)

            obj = json.loads(ReadJson.readJson(sys.path[0] + self.jsonfilepath))
            sExpectedTitle = (obj['gridTitle']['displaynames'])

            if len(sGridColumnData) > 0:
                for i in len(sGridTitle):
                    pass

        except Exception as e:
            print(e)
            self.extentnode.log(self.LogStatus.FAIL, e)
            self.allureLogs(e)
            Logging.logInfo("%s", e)
