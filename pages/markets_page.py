import csv

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base_page import BaseClass
from config.config_file import PRICE


class MarketsPage(BaseClass):
    MARKET_PAGE = (By.CLASS_NAME, "market-page")
    BUY = (By.XPATH, "//a[contains(text(),'ALIŞ')]")
    SELL = (By.XPATH, "//a[contains(text(),'SATIŞ')]")
    MARKETS_TL = (By.XPATH, "//a[contains(@href, '#crypto-tl')]")
    MARKETS_ALL = (By.XPATH, "//a[contains(@href, '#all')]")
    MARKETS_USD = (By.XPATH, "//a[contains(@href, '#crypto-usdt')]")
    MARKETS_FAN = (By.XPATH, "//a[contains(@href, '#fantoken-chz')]")
    MARKETS_BOX = (By.XPATH, "//a[contains(@href, '#box-tl')]")
    SORTING_BUTTON = (By.CLASS_NAME, "icon-preferences1")
    ALFABETIK_SORTING = (By.XPATH, "//label[contains(.,'Alfabetik')]")
    HACME_GORE_SORTING = (By.XPATH, "//label[contains(.,'Hacme göre')]")
    FIYATA_GORE_SORTING = (By.XPATH, "//label[contains(.,'Fiyata göre')]")
    DEGISIME_GORE_SORTING = (By.XPATH, "//label[contains(.,'Değişime göre')]")
    SELECT_COIN = './/*[contains(@class, "market-picker-col-name")]//*[contains(text(), "{}")]'
    WAVES_COIN = (By.XPATH, "//span[contains(.,'Waves')]")
    AL_SAT_PIYASALAR = (By.XPATH, '//span[text()="PİYASA"]')
    TOPLAM_TL_AL = (By.XPATH, '//label[text()="Toplam (TL)"]')
    ALIS_EMRI_VER = (By.XPATH, "//span[contains(.,'Alış Emrİ Ver')]")
    ALL_COIN= (By.CLASS_NAME, "market-picker")
    ALL_COINS = "market-picker + div"
    COIN_NAME = ".market-picker-row .market-picker-col-name"
    COIN_PRICE = ".market-picker-row .market-picker-col-price"
    COIN_CHANGE_RATE = ".market-picker-row .market-picker-percentage"

    def __init__(self, driver):
        super().__init__(driver)
        self.methods = BaseClass(self.driver)

    def check(self):
        (self.methods.element_is_visible(self.MARKET_PAGE), 'No "Market Page"  on the page!')
        (self.methods.element_is_visible(self.BUY), 'No "Alış"  on the page!')
        (self.methods.element_is_visible(self.SELL), 'No "Satış"  on the page!')

    def click_piyasalar(self, type):
        """
        Click
        :param type:
        """
        if type =="all":
            self.clickable_and_click(self.MARKETS_ALL)
        elif type =="tl":
            self.clickable_and_click(self.MARKETS_TL)
        elif type =="usdt":
            self.clickable_and_click(self.MARKETS_USD)
        elif type =="fan":
            self.clickable_and_click(self.MARKETS_FAN)
        else:
            self.clickable_and_click(self.MARKETS_BOX)
        return self

    def click_sorting_coin(self, sorting):
        """
        Click sorting coin

        """
        self.clickable_and_click(self.SORTING_BUTTON)
        if sorting =="Alfabetik":
            self.clickable_and_click(self.ALFABETIK_SORTING)
        elif sorting =="Hacme Göre":
            self.clickable_and_click(self.HACME_GORE_SORTING)
        elif sorting =="Fiyata göre":
            self.clickable_and_click(self.FIYATA_GORE_SORTING)
        else:
            self.clickable_and_click(self.DEGISIME_GORE_SORTING)
        return self

    def select_coin(self, coin):
        """
        Select Coin

        """
        self.clickable_and_click(self.WAVES_COIN)

    def click_al_sat_piyasalar(self):
        """
        """
        self.clickable_and_click(self.AL_SAT_PIYASALAR)

    def click_tl_al(self):
        """  """
        self.clickable_and_click(self.TOPLAM_TL_AL)
        self.clickable_and_click(self.TOPLAM_TL_AL).clear.send_keys(PRICE + Keys.ENTER)

    def click_alis_emri_ver(self):
        """

        :return:
        """
        self.clickable_and_click(self.ALIS_EMRI_VER)

    def write_coin_excel(self):
        # Find all the rows in the table
        rows = self.get_web_elements(self.ALL_COIN)

        # Write the data to a CSV file
        with open('coin_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Coin Name', 'Price', 'Change Rate'])
            for row in rows:
                coin_name = row.find_element(By.CSS_SELECTOR, self.COIN_NAME).text
                price = row.find_element(By.CSS_SELECTOR, self.COIN_PRICE).text
                change_rate = row.find_element(By.CSS_SELECTOR, self.COIN_CHANGE_RATE,).text
                writer.writerow([coin_name, price, change_rate])
