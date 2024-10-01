from config import log_error, log_msg
from LocatorType import LocatorType
from WebDriver_module import WebDriverSetup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from logging_config import LOG_CONFIG
import logging.config
import logging
logging.config.dictConfig(LOG_CONFIG)


def navigate_to_python_link():
    logger = logging.getLogger("example_app")

    web_driver_setup = WebDriverSetup()

    driver = web_driver_setup.setup_chrome_browser()
    driver.get("http://www.apress.com")
    driver.maximize_window()

    try:
        web_element = web_driver_setup.expected_conditions_presence_of_element_located(
            driver, 5, LocatorType.XPATH, "//dialog[@class='cc-banner']")
        if web_element:
            reject_cookies_btn = driver.find_element(
                By.XPATH, "//div/button[@class='cc-button cc-button--secondary cc-button--contrast cc-banner__button cc-banner__button-accept']")
            reject_cookies_btn.click()
    except Exception as e:
        log_error(logger, e)

    try:
        # main screen access operations
        main_menu = driver.find_element(By.XPATH, "//nav/ul/li/a[@href='#']")
        ActionChains(driver).move_to_element(main_menu).perform()

        # wait for submenu to be displayed
        web_driver_setup.expected_conditions_visibility_of_element_located(
            driver, 3, LocatorType.LINK_TEXT, "Python")
        sub_menu = driver.find_element(
            By.XPATH, "//ul/li/a[@href='/gp/python']")
        ActionChains(driver).move_to_element(
            sub_menu).pause(2).click().perform()
    except Exception as e:
        log_error(logger, e)

    log_msg(logger, '----------------------Logging using try/catch completed from webmodule completed-------------------')


if __name__ == '__main__':
    navigate_to_python_link()
