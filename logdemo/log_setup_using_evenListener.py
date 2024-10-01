from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.events import EventFiringWebDriver
from logger import LogEventListener


def navigate_to_python_link():

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')

    driver = EventFiringWebDriver(
        webdriver.Chrome(options), LogEventListener())
    driver.get("http://www.apress.com")
    driver.maximize_window()

    WebDriverWait(driver, 5).until(
        EC.visibility_of_any_elements_located((By.XPATH, "//dialog[@class='cc-banner']")))
    reject_cookies_btn = driver.find_element(
        By.XPATH, "//div/button[@class='cc-button cc-button--secondary cc-button--contrast cc-banner__button cc-banner__button-accept']")
    reject_cookies_btn.click()

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
    except Exception:
        pass


if __name__ == '__main__':
    navigate_to_python_link()
