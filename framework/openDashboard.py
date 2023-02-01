from utilities.reporting.startExtentReporting import StartReporting
from selenium.webdriver.common.action_chains import ActionChains
from utilities.fileUtilities.ReadJson import ReadJson
from utilities.reporting.startLogging import Logging
from selenium.webdriver.common.by import By
from framework.BaseClass import BaseClass
from framework.framework import Framework
import time
import json
import sys
import os


class OpenDashboard(BaseClass):

    def __init__(self, driver, dashboardName, parent):
        self.dashboardName = dashboardName
        self.driver = driver
        self.parent = parent
        self.LogStatus = StartReporting.LogStatus

    sMainMenu = (By.XPATH, "//*[contains(@class,'parentMenus')]")
    # sSubMenu0 = (By.XPATH, "//div[@id='cdk-overlay-0']//button")
    # sSubMenu1 = (By.XPATH, "//div[@id='cdk-overlay-1']//button")
    sSubMenu0 = (By.XPATH, "//h5")
    sSubMenu1 = (By.XPATH, "// h5 /../ div")

    def openDashboard(self):
        f = Framework(self.driver, self.parent)
        action = ActionChains(self.driver)

        # Read menu json
        obj = json.loads(ReadJson.readJson(sys.path[0] + os.sep + "json" + os.sep + "Menu.json"))
        if obj:
            self.parent.log(self.LogStatus.PASS, "Menu.json read successfully")
            Logging.logInfo("%s", "Menu.json read successfully")
            assert True
            self.allureLogs("Menu.json read successfully")
        else:
            self.parent.log(self.LogStatus.FAIL, "Menu.json read failed")
            Logging.logInfo("%s", "Fail to read Menu.json")
            assert False
            self.allureLogs("Fail to read menu.json")

        # Create Hierarchy string
        if obj:
            a = (obj['menu'])
            hierarchyString = ""
            parentID = ""
            for i in a:
                if i['dashboardTitle'] == self.dashboardName:
                    hierarchyString = i['menuTitle'] + ":" + i['dashboardTitle']
                    parentID = i['parentId']
                    break

            while parentID != "":
                for i in a:
                    if i['id'] == parentID:
                        hierarchyString = i['menuTitle'] + ":" + hierarchyString
                        parentID = i['parentId']

            HierachyArray = hierarchyString.split(":")
            self.parent.log(self.LogStatus.INFO, "Menu hierarchy for the dashboard  ->  " + hierarchyString)
            self.parent.log(self.LogStatus.INFO, "")
            Logging.logInfo("%s", "Menu hierarchy for the dashboard : " + hierarchyString)

            self.wait_visibility_of_element_located(By.CLASS_NAME, "parentMenus")

            # Open Dashboard
            try:
                for i in range(len(HierachyArray) - 1):
                    if i == 0:
                        wEachMenu = self.driver.find_elements(*OpenDashboard.sMainMenu)
                        for wMainMenu in wEachMenu:
                            action.move_to_element(wMainMenu).perform()
                            if wMainMenu.text == HierachyArray[0]:
                                f.clickAndWait(wMainMenu, wMainMenu.text)
                    elif i == 1:
                        print("PH")
                        # self.wait_visibility_of_element_located(By.XPATH, "//h5")
                        # wSubMenu = self.driver.find_elements(*OpenDashboard.sSubMenu0)
                        # for lSubMenu in wSubMenu:
                        #     #time.sleep(1)
                        #     if lSubMenu.text == HierachyArray[i]:
                        #         f.clickAndWait(lSubMenu, lSubMenu.text)

                    elif i == 2:
                        # self.wait_visibility_of_element_located(By.XPATH, "//div[@id='cdk-overlay-1']//button")
                        wSubMenu = self.driver.find_elements(*OpenDashboard.sSubMenu1)
                        for lSubMenu in wSubMenu:
                            # time.sleep(1)
                            if lSubMenu.text == HierachyArray[i]:
                                f.clickAndWait(lSubMenu, lSubMenu.text)
                                break
                    else:
                        pass


            except Exception as e:
                print("excetion in open dashboard ---", e)
                Logging.logInfo("%s", "Error occured in OpenDashboard")
                self.parent.log(self.LogStatus.FAIL, "Error occured in OpenDashboard")
                # assert False
                self.allureLogs("Error occured in OpenDashboard")
            else:
                Logging.logInfo("%s", "Open Dashboard pass")
                self.parent.log(self.LogStatus.PASS, "Open Dashboard pass")
                # assert TRUE
                self.allureLogs("Open Dashboard pass")
