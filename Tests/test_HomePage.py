from PageObjects.HomePage import HomePage
from Tests.test_Base import BaseTest


class Test_HomePage(BaseTest):
    search_text = "Laptop"

    def test_search_for_product(self):
        self.home = HomePage(self.driver)
        search_results_page = self.home.product_search(self.search_text)
        product_name = search_results_page.get_search_text()
        page_title = search_results_page.get_title(product_name)
        assert product_name in page_title
