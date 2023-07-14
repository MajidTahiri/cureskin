from pages.base_page import Page
from pages.search_results_page import SearchResultsPage


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.base_page = Page(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
