from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BaseClass


class LoginPopup(BaseClass):
    PHONE_NUMBER_TEXT_AREA = (By.XPATH, '//label[text()="Cep Telefonu"]')
    PASSWORD_TEXT_AREA = (By.XPATH, '//label[text()="Parola"]')
    SIGN_IN_BUTTON = (By.XPATH, "//span[contains(.,' GİRİŞ YAP')]")
    SIGN_IN_ALERT = (By.CLASS_NAME, "v-messages__message")

    def __init__(self, driver):
        super().__init__(driver)
        self.methods = BaseClass(self.driver)

    def check(self):
        (self.methods.element_is_visible(self.PHONE_NUMBER_TEXT_AREA), 'No "Cep Telefonu" area on the page!')
        (self.methods.element_is_visible(self.PASSWORD_TEXT_AREA), 'No "Parola" area on the page!')
        (self.methods.element_is_visible(self.SIGN_IN_BUTTON), 'No "Sign in" button on the page!')

    def sign_in(self):
        """
        Fills login information
        :param PASSWORD:
        :param PHONE_NUMBER:

        """
        #self.methods.visible_and_click(self.PHONE_NUMBER_TEXT_AREA).send_keys(PHONE_NUMBER)
        #self.element_is_visible(self.PHONE_NUMBER_TEXT_AREA)
        #self.send_key(self.PHONE_NUMBER_TEXT_AREA, PHONE_NUMBER)
        #self.send_key(self.PHONE_NUMBER_TEXT_AREA, Keys.ENTER)
        #self.methods.clickable_and_click(self.PASSWORD_TEXT_AREA).send_keys(PASSWORD)
        #self.element_is_visible(self.PASSWORD_TEXT_AREA)
        #self.send_key(self.PASSWORD_TEXT_AREA, PASSWORD)
        self.methods.clickable_and_click(self.SIGN_IN_BUTTON)

    @staticmethod
    def select_login_alert(column):
        """
        Select alert
        :param str column:

        """
        column_name_list = {
            "phone number": "0",
            "password": "1"
        }
        index = column_name_list.get(column)
        return int(index)

    def is_alert_present(self, input_index=0):
        """
        Returns alert

        """
        return self.get_element_text(self.SIGN_IN_ALERT)[input_index]
