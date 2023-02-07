from selenium.webdriver import ActionChains, Keys

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from config.config_file import BASE_TITLE


class BaseClass:
    """This class is the parent of all pages
    it contains all the generic methods and utilities for all pages"""

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(self.driver, timeout=5)

    def get_web_element(self, locator):
        element = self.driver.find_elements(locator[0], locator[1])
        return element

    def get_web_elements(self, locator):
        element_list = self.driver.find_elements(locator[0], locator[1])
        return element_list
    #Kullanulmadı
    def force_click(self, locator):
        element = self.get_web_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    # Kullanulmadı
    def page_scroll(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def implicit_wait(self, time):
        self.driver.implicitly_wait(time)

    def visible_and_click(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator)).click()

    def send_key(self, locator, text):
        self.wait.until(expected_conditions.presence_of_element_located(locator)).send_keys(text)

    def get_element_text(self, locator):
        return self.wait.until(expected_conditions.presence_of_element_located(locator)).text

    def get_element(self, locator):
        return self.wait.until(expected_conditions.presence_of_element_located(locator))

    def element_is_presence(self, locator):
        try:
            return bool(self.wait.until(expected_conditions.presence_of_element_located(locator)))
        except:
            return False

    def elements_are_presence(self, locator):
        try:
            return bool(self.wait.until(expected_conditions.presence_of_all_elements_located(locator)))
        except:
            return False

    def element_is_visible(self, locator):
        try:
            return bool(self.wait.until(expected_conditions.visibility_of_element_located(locator)))
        except:
            return False

    def element_visible(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))

    def element_is_displayed(self, locator):
        try:
            return self.wait.until(expected_conditions.element_to_be_clickable(locator)).is_displayed()
        except:
            return False

    def element_is_enabled(self, locator):
        return self.wait.until(expected_conditions.element_to_be_clickable(locator)).is_enabled()

    def element_is_selected(self, locator):
        return self.wait.until(expected_conditions.element_to_be_clickable(locator)).is_selected()

    def get_title(self):
        return self.driver.title

    def wait_for_load(self):
        page_state = self.driver.execute_script('return document.readyState;')
        return page_state == 'complete'

    def wait_for_jquery_load(self):
        self.driver.execute_script("return jQuery.active==0")

    def scroll_in_the_middle_of_locator(self, locator):
        element = self.get_web_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'})", element)

    def scroll_in_the_middle_of_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'})", element)

    def clickable_and_click(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator)).click()

    def element_is_presence(self, locator):
        self.wait.until(expected_conditions.presence_of_element_located(locator))

    def text_is_presence(self, text):
        self.wait.until(expected_conditions.text_to_be_present_in_element(text))

    def element_is_invisible(self, locator):
        self.wait.until(expected_conditions.invisibility_of_element(locator))

    def title_contains(self, title):
        self.wait.until(expected_conditions.title_contains(title), "Expected title:" + BASE_TITLE)

    def visibility_of_all_elements_located(self, locators):
        self.wait.until(expected_conditions.visibility_of_all_elements_located(locators))

    def url_contains(self, url):
        self.wait.until(expected_conditions.url_contains(url), "Expected url: " + self.driver.current_url)
#kullanulknadu
    def url_to_be(self, url):
        self.wait.until(expected_conditions.url_to_be(url), "Expected url: " + self.driver.current_url)
