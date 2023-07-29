import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from app.application import Application
from support.logger import logger



def browser_init(context, test_name):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """

    # Set up Chrome driver with mobile emulation
    mobile_emulation = {"deviceName": "iPhone 12 Pro"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    # Create the driver instance and set up wait
    chromedriver_path = '/Users/macbookpro/Desktop/QA_automation_program/cureskin/chromedriver'
    context.driver = webdriver.Chrome(executable_path=chromedriver_path, options=chrome_options)
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)

    # Assign the driver to the application context
    context.app = Application(context.driver)

    # ------------------------------------------------------------------------#


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'Step failed: {step}')
        print('\nStep failed: ', step)
        # Mark test case as FAILED on BrowserStack:
        # Documentation: https://www.browserstack.com/docs/automate/selenium/view-test-results/mark-tests-as-pass-fail
        # context.driver.execute_script(
        #     'browserstack_executor: {"action": "setSessionStatus", "arguments": '
        #     '{"status":"failed", "reason": "Step failed"}}'
        # )


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.close()
