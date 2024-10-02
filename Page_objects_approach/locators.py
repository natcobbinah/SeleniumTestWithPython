from selenium.webdriver.common.by import By


class CoookieScreenLocators:
    # should contain all locators from main page
    POP_UP_DIALOG_WINDOW = (By.XPATH, "//dialog[@class='cc-banner']")
    REJECT_COOKIES_BUTTON = (
        By.XPATH, "//div/button[@class='cc-button cc-button--secondary cc-button--contrast cc-banner__button cc-banner__button-accept']")


class HomePageLocators:
    # should contain locators from homepage
    CATEGORIES_MENU = (By.XPATH, "//nav/ul/li/a[@href='#']")
    PYTHON_LINK_TEXT = (By.LINK_TEXT, "Python")
    PYTHON_PAGE_URL = (
        By.XPATH, "//ul/li/a[@href='/gp/python']")
