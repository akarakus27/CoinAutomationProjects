import unittest

import pytest
from config.config_file import PAGE_NAME, PHONE_NUMBER, PASSWORD
from pages.base_page import BaseClass
from pages.markets_page import MarketsPage
from pages.home_page import HomePage
from pages.login_popup import LoginPopup
from enums.enums_file import phone_error_text, password_error_text


@pytest.mark.usefixtures("test_setup")
class TestCheckLoginPopup(unittest.TestCase):
    """Test case is:
    1. Go Paribu and confirm
    2. open the login pages and log-in with your account
    3. type 'samsung' to the search box and click to the search button
    4. confirm that there are results for 'samsung'
    """
    tpye = dict(all='all', tl='tl', usdt='usdt', fan='fan', box="box")

    def test_check_login_popup(self):
        self.method = BaseClass(self.driver)
        paribu_home = HomePage(self.driver)
        paribu_home.user_is_on_homepage(PAGE_NAME)
        paribu_home.go_to_markets_page()
        category_page = MarketsPage(self.driver)
        category_page.click_piyasalar(self.tpye['all'])
        category_page.select_coin("Waves")
        category_page.click_al_sat_piyasalar()
        #category_page.click_tl_al()
        category_page.click_alis_emri_ver()
        loginpage = LoginPopup(self.driver)
        loginpage.sign_in()
        self.assertEqual(loginpage.is_alert_present('phone number'),
                         phone_error_text, "Text color can not be selected!")
        self.assertEqual(loginpage.is_alert_present('password'),
                         password_error_text, "Text color can not be selected!")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()