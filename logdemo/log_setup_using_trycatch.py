from config import log_error, log_msg
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from logging_config import LOG_CONFIG
import logging.config
import logging
logging.config.dictConfig(LOG_CONFIG)


def navigate_to_python_link():
    logger = logging.getLogger("example_app")

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')

    driver = webdriver.Chrome(options)
    driver.get("http://www.apress.com")
    driver.maximize_window()

    try:
        # wait for dialog box to be displayed and reject cookies
        WebDriverWait(driver, 5).until(
            EC.visibility_of_any_elements_located((By.XPATH, "//dialog[@class='cc-banner']")))
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
        WebDriverWait(driver, 3).until(
            EC.visibility_of_any_elements_located((By.LINK_TEXT, "Python")))

        sub_menu = driver.find_element(
            By.XPATH, "//ul/li/a[@href='/gp/python']")
        ActionChains(driver).move_to_element(
            sub_menu).pause(2).click().perform()
    except Exception as e:
        log_error(logger, e)

    log_msg(logger, '----------------------Logging using try/catch completed-------------------')


if __name__ == '__main__':
    navigate_to_python_link()
