from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePageElement(object):
    #used in every page

    # can be extended to define various various for timeouts and polling
    # polling is essential to prevent WebDriverWait to wait explicitly for
    # a target element which can not be located and continue with other tests

    def __init__(self):
        self.timeout_and_poll = {
            "timeout_100": 100,
            "polling_10": 10
        }


    def __set__(self, obj, value):
        #here we can pass values if its a text element using send_keys(value)

        driver = obj.driver
        WebDriverWait(driver, self.timeout_and_poll["timeout_100"],
                      self.timeout_and_poll["polling_10"]).until(
            EC.visibility_of_element_located(self.locator)
        )
        #driver.find_element(self.locator).send_keys(value)
    
    

