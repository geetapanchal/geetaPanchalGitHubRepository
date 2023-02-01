import json
import sys
from framework.BaseClass import BaseClass
from utilities.reporting.startLogging import Logging
from selenium.webdriver.common.by import By
from framework.framework import  Framework
from utilities.reporting.startExtentReporting import StartReporting

from utilities.fileUtilities.ReadJson import ReadJson


class GridTitle(BaseClass):

    def __init__(self, driver, jsonfilepath, extentnode):
        self.driver = driver
        self.jsonfilepath = jsonfilepath
        self.extentnode = extentnode
        self.LogStatus = StartReporting.LogStatus

    wRefreshButton = (By.XPATH, "//*[@title='Refresh']")
    wGridtitle = (By.CSS_SELECTOR,".bx--table-header-label")
    wGridtitletooltip = (By.XPATH,"//table//th//*[@title]")

    def verifyGridTitle(self):
        try:
            # Expected value from json
            obj = json.loads(ReadJson.readJson(sys.path[0] + self.jsonfilepath))
            sExpectedTitle = (obj['gridTitle']['displaynames'])
            sExpectedTooltip = (obj['gridTitle']['displaynames'])
            ExpectedTitle = []
            for i in sExpectedTitle:
                 ExpectedTitle.append(i.split(":")[0])

            ExpectedTooltip = []
            for i in sExpectedTooltip:
                 ExpectedTooltip.append(i.split(":")[0])

            # Actual value from GUI - GRID TITLE
            self.wait_visibility_of_element_located(By.CSS_SELECTOR,".bx--table-header-label")
            wActualTitle = self.driver.find_elements(*GridTitle.wGridtitle)
            sActualTitle = []
            for i in wActualTitle:
                sActualTitle.append(i.text)

            # Actual value from GUI - GRID TTTLE Tooltip
            wActualTooltip = self.driver.find_elements(*GridTitle.wGridtitletooltip)

            sActualTooltip = []
            for i in wActualTooltip:
                sActualTooltip.append(i.text)

            GridTitleSize = len(wActualTitle)

            if GridTitleSize > 0 and len(ExpectedTitle) > 0:
                f = Framework(self.driver, self.extentnode)
                f.comparingArrays(ExpectedTitle,sActualTitle)

            elif GridTitleSize > 0 and len(ExpectedTitle) == 0:
                self.extentnode.log(self.LogStatus.FAIL, "Grid titles are visible, Expected values are blank")
                self.allureLogs("Grid titles are visible, Expected values are blank")
            elif GridTitleSize == 0 and len(ExpectedTitle) >0:
                self.extentnode.log(self.LogStatus.FAIL, "Grid titles are blank, Expected values are not blank")
                self.allureLogs("Grid titles are blank, Expected values are not blank")
            elif GridTitleSize == 0 and len(ExpectedTitle) == 0:
                self.extentnode.log(self.LogStatus.PASS, "Grid titles are blank, Expected values are blank")
                self.allureLogs("Grid titles are blank, Expected values are blank")
            else:
                self.extentnode.log(self.LogStatus.FAIL, "Unknown result")
                self.allureLogs("Unknown result")

        except Exception as e:
            print(e)
            self.extentnode.log(self.LogStatus.FAIL, e)
            self.allureLogs(e)
            Logging.logInfo("%s", e)



