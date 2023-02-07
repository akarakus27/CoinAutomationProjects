import unittest

import pytest
from selenium import webdriver

from config.config_file import PAGE_NAME
from pages.base_page import BaseClass
from pages.markets_page import MarketsPage
from pages.home_page import HomePage


@pytest.mark.usefixtures("test_setup")
class TestCheckCoinExchangeRate(unittest.TestCase):
    """Test case is:
    1. Go Paribu and confirm
    2. open the login pages and log-in with your account
    3. type 'samsung' to the search box and click to the search button
    4. confirm that there are results for 'samsung'
    """

    sorting = dict(alfabetik='Alfabetik', hacme_göre='Hacme Göre',
                   fiyata_göre='Fiyata Göre', degişime_göre='Degişime Göre')
    tpye = dict(all='all', tl='tl', usdt='usdt', fan='fan', box="box")

    def test_check_coin_exchange_rate(self):
        paribu_home = HomePage(self.driver)
        paribu_home.user_is_on_homepage(PAGE_NAME)
        paribu_home.go_to_markets_page()
        category_page = MarketsPage(self.driver)
        category_page.click_piyasalar(self.tpye["tl"])
        category_page.click_sorting_coin(self.sorting["hacme_göre"])
        category_page.write_coin_excel()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
