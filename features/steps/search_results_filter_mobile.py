import time

from behave import given, when, then
from selenium.webdriver.common.by import By



@given("the search results page is open")
def open_cureskin(context):
    context.app.base_page.open_url('https://shop.cureskin.com/search?q=cure')


@when("user taps 'Filter and Sort'")
def tap_filters(context):
    context.app.search_results_mobile_page.tap_filters()


@when("tap 'Product type'")
def tap_product_type(context):
    context.app.search_results_mobile_page.tap_product_type()


@when("navigate to the target page")
def navigate_to_target_page(context):
    context.app.search_results_mobile_page.navigate_to_target_page()


@when("user taps 'Clear all'")
def tap_clear_all(context):
    context.app.search_results_mobile_page.tap_clear_all()


@then("verify filter is removed")
def verify_filter_removed(context):
    context.app.search_results_mobile_page.verify_filter_removed()

