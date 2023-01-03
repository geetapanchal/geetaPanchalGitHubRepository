from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from framework.BaseClass import BaseClass


class LoginPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    username = (By.NAME, "j_username")
    password = (By.NAME, "j_password")
    login_btn = (By.ID, "login_btn")
    advance_btn = (By.ID, "details-button")
    proceed_lnk = (By.ID, "proceed-link")
    usernameOnWelcomePage = (By.CSS_SELECTOR, ".username")

    def getUserName(self):
        return self.driver.find_element(*LoginPage.username)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def getLogin_btn(self):
        return self.driver.find_element(*LoginPage.login_btn)

    def getAdvance_btn(self):
        try:
            self.driver.find_element(*LoginPage.advance_btn)
        except NoSuchElementException:
            return "None"
        else:
            print("try catch else")
            return self.driver.find_element(*LoginPage.advance_btn)

    def getProceed_lnk(self):
        return self.driver.find_element(*LoginPage.proceed_lnk)

    def getUserNameAfterLogin(self):
        return self.driver.find_element(*LoginPage.usernameOnWelcomePage)
