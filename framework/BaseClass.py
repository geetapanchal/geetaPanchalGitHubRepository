'''
Created on Jun 22, 2022
@author: Geeta
'''
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def allureLogs(self, text):
        with allure.step(text):
            pass

    def allureLogsfail(self, text):
        with allure.step(text):
            pass

    def allureattach(self,text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)

    def wait_presense_of_element_located(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((locator_type, locator)))

    def wait_visibility_of_element_located(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.visibility_of_element_located((locator_type, locator)))

    def wait_frame_to_be_available_and_switch_to_it(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.frame_to_be_available_and_switch_to_it((locator_type, locator)))

    def wait_visibility_of_element_returnEle(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 20)
        return  wait.until(EC.visibility_of_element_located((locator_type, locator)))





