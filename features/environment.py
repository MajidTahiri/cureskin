import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from app.application import Application
# from support.logger import logger
import logging
logger = logging.getLogger(__name__)


def browser_init(context, test_name):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)
    # ------------------------------------------------------------------------#


    #### HEADLESS MODE ####
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    context.driver = webdriver.Chrome(
        chrome_options=options,
        service=service
    )
    # ------------------------------------------------------------------------#


    # Firefox Browser #
    geckodriver_path = "/Users/macbookpro/Desktop/QA_automation_program/python-selenium-automation/geckodriver"
    context.driver = webdriver.Firefox(executable_path=geckodriver_path)

    # ------------------------------------------------------------------------#



    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)
    # ------------------------------------------------------------------------#


def before_scenario(context, scenario):
    # print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    # print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'Step failed: {step}')
        print('\nStep failed: ', step)
        # Mark test case as FAILED on BrowserStack:
        # Documentation: https://www.browserstack.com/docs/automate/selenium/view-test-results/mark-tests-as-pass-fail
        context.driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": '
            '{"status":"failed", "reason": "Step failed"}}'
        )


def after_scenario(context, feature):
    context.driver.close()
