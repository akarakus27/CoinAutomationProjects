import time

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from config.config_file import BASE_TITLE
from pages.base_page import BaseClass
import undetected_chromedriver as uc


class HomePage(BaseClass):
    SIGN_IN = (By.ID, "nav-link-accountList")
    SEARCH_BAR = (By.ID, "twotabsearchtextbox")
    SIGN_OUT_BUTTON = (By.ID, "nav-item-signout")
    HEADER_MENU = (By.CLASS_NAME, "header-menu")
    MARKETS_PAGE = (By.XPATH, "//a[contains(text(),'Piyasalar')]")
    EASY_BUY_SELL_PAGE = (By.XPATH, "//a[contains(text(),'Kolay Al/Sat')")
    FOOTER = (By.CSS_SELECTOR, ".footer .col-md-6 ")
    LINKS= "li"

    def __init__(self, driver):
        super().__init__(driver)
        self.methods = BaseClass(self.driver)

    def check(self):
        (self.methods.element_is_visible(self.HEADER_MENU), 'No "Header Menu"  on the page!')
        (self.methods.element_is_visible(self.MARKETS_PAGE), 'No "Piyasalar" button on the page!')
        (self.methods.element_is_visible(self.EASY_BUY_SELL_PAGE), 'No "Kolay Al/Sat"  on the page!')

    def user_is_on_homepage(self, site):
        """ Go to "piyasalar" page """
        self.wait_for_load()
        print(self.driver.current_url)
        self.url_contains(site)

    def verify_page_title(self):
        """ Go to "piyasalar" page """
        print(self.driver.title)
        self.title_contains(BASE_TITLE)
        assert BASE_TITLE in self.driver.title

    def go_to_markets_page(self):
        """ Go to "piyasalar" page """
        self.clickable_and_click(self.MARKETS_PAGE)

    def verify_page_links(self):
        """ Go to "piyasalar" page """
        # section = driver.find_element(By.CSS_SELECTOR, "footer")
        section = self.get_web_element(self.FOOTER)

        # Get all the links in the section
        links = section.find_element(By.CSS_SELECTOR, self.LINKS)
        # Iterate through each link and check if it is working
        for link in links:
            href = link.get_attribute("href")
            driver = uc.Chrome(use_subprocess=True)
            driver.get(href)

            if self.driver.title == "":
                print(f"Error: The link {href} is not working.")
            else:
                print(f"The link {href} is working.")



