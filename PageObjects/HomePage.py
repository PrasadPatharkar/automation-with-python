from selenium.webdriver.common.by import By

from Core.Config import ConfigData
from PageObjects.BasePage import BasePage
from PageObjects.SearchResultsPage import SearchResultsPage


class HomePage(BasePage):
    search_box = (By.ID, "twotabsearchtextbox")
    first_from_suggestion_list = (By.CSS_SELECTOR, "div#suggestions div:nth-of-type(1)")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(ConfigData.Home_URL)

    def product_search(self, search_text):
        self.send_keys(self.search_box, search_text)
        self.click(self.first_from_suggestion_list)
        return SearchResultsPage(self.driver)


