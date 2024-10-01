from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from LocatorType import LocatorType


class WebDriverSetup:

    def __init__(self):
        #empty constructor
        pass

    def setup_chrome_browser(self, browser_arg_list=[]):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')

        for option_args in browser_arg_list:
            options.add_argument(option_args)

        driver = webdriver.Chrome(options)
        return driver


    def _return_locator_type_element_search(self, driver, timeout,  path_locator_type, search_element_value):
        web_element = None

        if path_locator_type == LocatorType.CLASS_NAME:
            web_element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_any_elements_located((By.CLASS_NAME, search_element_value)))
            
        elif path_locator_type == LocatorType.CSS_SELECTOR:
            web_element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_any_elements_located((By.CSS_SELECTOR, search_element_value)))
            
        elif path_locator_type == LocatorType.ID:
            web_element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_any_elements_located((By.ID, search_element_value)))
            
        elif path_locator_type == LocatorType.NAME:
            web_element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_any_elements_located((By.NAME, search_element_value)))
            
        elif path_locator_type == LocatorType.LINK_TEXT:
            web_element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_any_elements_located((By.LINK_TEXT, search_element_value)))
        
        elif path_locator_type == LocatorType.PARTIAL_LINK_TEXT:
            web_element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_any_elements_located((By.PARTIAL_LINK_TEXT, search_element_value)))
            
        elif path_locator_type == LocatorType.TAG_NAME:
            web_element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_any_elements_located((By.TAG_NAME, search_element_value)))
        
        return web_element

    def expected_conditions_visibility_of_element_located(self, driver, timeout,  path_locator_type, search_element_value):
        return self._return_locator_type_element_search(driver, timeout,  path_locator_type, search_element_value)

    def expected_conditions_presence_of_element_located(self, driver, timeout,  path_locator_type, search_element_value):
        return self._return_locator_type_element_search(driver, timeout,  path_locator_type, search_element_value)

   
       