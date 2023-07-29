import time

from behave import given, when, then
from selenium.webdriver.common.by import By



# @given("the search results page is open")
# def open_cureskin(context):
#     context.app.base_page.open_url('https://shop.cureskin.com/search?q=cure')
#
#
# @when("user clicks 'More Filters'")
# def click_filters(context):
#     context.app.search_results_page.click_filters()
#
#
# @when("select 'Face Wash' filter")
# def select_face_wash(context):
#     context.app.search_results_page.select_face_wash()
#
#
# @when("click 'Apply' button")
# def click_apply_button(context):
#     context.app.search_results_page.click_apply_button()
#
#
# @then("verify filter is set and 'Face Wash' appears under filters")
# def verify_face_wash_selected(context):
#     context.app.search_results_page.verify_face_wash_selected()
#
#
# @when("user clicks 'Clear all'")
# def click_clear_all(context):
#     context.app.search_results_page.click_clear_all()
#
#
# @then("verify filter is removed")
# def verify_filter_removed(context):
#     context.app.search_results_page.verify_filter_removed()
