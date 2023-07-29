import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page


# class SearchResultsPage(Page):
#
#     FILTERS_BTN = (By.ID, "FacetDrawer")
#     CHECKBOX_FACE = (By.CSS_SELECTOR, ".facets__inner .facet-checkbox")
#     CHECKBOX_SELECTED = (By.CSS_SELECTOR, ".facets__inner [type='checkbox']")
#     APPLY_BTN = (By.CSS_SELECTOR, ".facets__inner [type='button']")
#     CLEAR_ALL = (By.CSS_SELECTOR, ".active-facets__button")
#
#
#     def click_filters(self):
#         self.wait_for_element_click(*self.FILTERS_BTN)
#
#
#     def select_face_wash(self):
#         self.wait_for_element_click(*self.CHECKBOX_FACE)
#
#
#     def verify_face_wash_selected(self):
#         checkbox = self.wait.until(EC.element_to_be_clickable(self.CHECKBOX_SELECTED))
#         assert checkbox.is_selected(), "The Face Wash filter is not selected."
#
#
#     def click_apply_button(self):
#         self.wait_for_element_click(*self.APPLY_BTN)
#
#     def click_clear_all(self):
#         self.click_element_by_index(*self.CLEAR_ALL, index=0)
#
#     def verify_filter_removed(self):
#         self.wait.until(EC.invisibility_of_element_located(self.CHECKBOX_SELECTED))
#         assert self.CHECKBOX_SELECTED, "The filter was not removed."
