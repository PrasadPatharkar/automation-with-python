from PageObjects.HomePage import HomePage
from Tests.test_Base import BaseTest


class Test_SearchResultsPage(BaseTest):
    search_text = "Laptop"

    def test_searchNSelectProduct(self):
        self.homepage = HomePage(self.driver)
        self.search_results_page = self.homepage.product_search(self.search_text)
        product_name = self.search_results_page.select_first_from_result()
        page_title = self.search_results_page.get_title(product_name)
        assert product_name in page_title
