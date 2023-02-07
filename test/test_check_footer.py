import unittest

import pytest
from config.config_file import PAGE_NAME
from pages.base_page import BaseClass
from pages.home_page import HomePage


@pytest.mark.usefixtures("test_setup")
class TestCheckFooter(unittest.TestCase):

    def test_check_footer(self):
        self.method = BaseClass(self.driver)
        paribu_home = HomePage(self.driver)
        paribu_home.user_is_on_homepage(PAGE_NAME)
        paribu_home.verify_page_links()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()