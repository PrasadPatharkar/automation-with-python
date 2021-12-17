from PageObjects.BasePage import BasePage
from selenium.webdriver.common.by import By


class SearchResultsPage(BasePage):
    first_search_result = (By.CSS_SELECTOR, "[data-component-type='s-search-results'] div[data-index='2'][data-component-type] img")
    search_box = (By.ID, "twotabsearchtextbox")

    def __init__(self, driver):
        super().__init__(driver)

    def select_first_from_result(self):
        product_name = self.get_text(self.first_search_result)
        self.click(self.first_search_result)
        return product_name

    def get_search_text(self):
        return self.get_text(self.search_box)