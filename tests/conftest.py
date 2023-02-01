import os
import sys
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import configuration
from utilities.reporting.startLogging import Logging
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from utilities.fileUtilities.TxtFile_Utilities import TxtFileUtils

# Command line arguments
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Environment to run tests against",
        choices=("chrome", "ff", "edge"),
    )
    parser.addoption(
        "--url",
        action="store",
        help="Environment to run tests against",
    )


# prepare list of tests to run / dashboard to verify
def pytest_collection_modifyitems(session, config, items):
    """ prepare list of tests to run / dashboard to verify"""
    toRun = configuration.dashboardsToExecute
    toRunCopy = []
    for i in toRun:
        for item in items.copy():
            if item.get_closest_marker(i):
                toRunCopy.append(item)

    items.clear()
    for i in toRunCopy:
        items.append(i)


@pytest.fixture(scope="class")
def setup(request):
    """ Browser and url setup and login to the application"""
    # Browser setup
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        opt=Options()
        opt.add_argument("--headless")

        s = Service(sys.path[0] + os.sep + "lib" + os.sep + "chromedriver.exe")
        driver = webdriver.Chrome(service=s)
    elif browser_name == "ff":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name == 'edge':
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        print("Invalid browser type")

    # Maximize window and open URL
    driver.maximize_window()
    driver.get(request.config.getoption("url"))
    request.cls.driver = driver

    # log detail to txt file
    Logging.logInfo("%s", "Browser - " + browser_name)
    Logging.logInfo("%s", "URL - " + request.config.getoption("url"))
    Logging.logInfo("%s", "Username - " + configuration.username)

    # add detail to environment.properties for the allure reporting
    t = TxtFileUtils(driver)
    t.add_env_detailto_file(browser_name, request.config.getoption("url"), configuration.username)

    yield
    driver.close()
