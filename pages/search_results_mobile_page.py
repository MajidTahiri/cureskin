import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


class SearchResultsMobilePage(Page):

    # Mobile version locators
    FILTERS_BTN = (By.CSS_SELECTOR, ".mobile-facets__wrapper")
    PRODUCT_TYPE = (By.CSS_SELECTOR, ".mobile-facets__summary")
    CLEAR_ALL = (By.CSS_SELECTOR, ".active-facets")
    SEARCH_RESULTS = (By.ID, "ProductCount")

    def tap_filters(self):
        self.wait_for_element_click(*self.FILTERS_BTN)


    def tap_product_type(self):
        self.click_element_by_index(*self.PRODUCT_TYPE, index=0)


    def navigate_to_target_page(self):
        self.driver.get("https://shop.cureskin.com/search?filter.p.product_type=Face+Wash&filter.v.price.gte=&filter"
                        ".v.price.lte=&sort_by=relevance&q=cure")

    def tap_clear_all(self):
        self.click_element_by_index(*self.CLEAR_ALL, index=0)


    def verify_filter_removed(self):
        expected_text = '19 results found for “cure”'
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_RESULTS))
        actual_text = self.driver.find_element(*self.SEARCH_RESULTS).text
        assert actual_text == expected_text, f"Element text mismatch. Expected: '{expected_text}', Actual: '{actual_text}'"
        print("Element text verification successful.")


