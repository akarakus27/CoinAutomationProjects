import time
import pytest
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver import DesiredCapabilities

from config.config_file import BASE_URL
from pages.base_page import BaseClass


@pytest.fixture(autouse=True, scope="class")
def test_setup(request):
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument('disable-infobars')
    options.add_argument("--disable-extensions")
    options.add_experimental_option('useAutomationExtension', False)
    driver = uc.Chrome(use_subprocess=True)

    BaseClass.implicit_wait(3)
    driver.get(BASE_URL)
    driver.maximize_window()
    driver.delete_all_cookies()
    request.cls.driver = driver
