import unittest
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from logging_config import LOG_CONFIG
import logging.config
import logging
from selenium.common.exceptions import TimeoutException
logging.config.dictConfig(LOG_CONFIG)

# Get the parent directory of the current file (one level up)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Add the parent directory to Python path
sys.path.append(parent_dir)
from logdemo.config import log_error, log_msg

class LogSetupWithUnitTest(unittest.TestCase):



    def setUp(self):
        self.logger = logging.getLogger("example_app")

        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')

        self.driver = webdriver.Chrome(options)
        try:
            self.driver.get("http://www.apress.com")
            self.driver.maximize_window()
        except TimeoutException as t:
            print(t.msg)


    def test_reject_cookies_and_click_main_screen_link(self):

        try:
            # wait for dialog box to be displayed and reject cookies
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_any_elements_located((By.XPATH, "//dialog[@class='cc-banner']")))
            reject_cookies_btn = self.driver.find_element(
                By.XPATH, "//div/button[@class='cc-button cc-button--secondary cc-button--contrast cc-banner__button cc-banner__button-accept']")
            reject_cookies_btn.click()
        except Exception as e:
            log_error(self.logger, e)

        try:
            # main screen access operations
            main_menu = self.driver.find_element(
                By.XPATH, "//nav/ul/li/a[@href='#']")
            ActionChains(self.driver).move_to_element(main_menu).perform()

            # wait for submenu to be displayed
            WebDriverWait(self.driver, 3).until(
                EC.visibility_of_any_elements_located((By.LINK_TEXT, "Python")))

            sub_menu = self.driver.find_element(
                By.XPATH, "//ul/li/a[@href='/gp/python']")
            ActionChains(self.driver).move_to_element(
                sub_menu).pause(2).click().perform()
        except Exception as e:
            log_error(self.logger, e)

    
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
