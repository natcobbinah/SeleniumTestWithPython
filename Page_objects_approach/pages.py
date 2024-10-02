from elements import BasePageElement
from locators import CoookieScreenLocators, HomePageLocators
from selenium.webdriver.common.action_chains import ActionChains

class CookieDialogScreen(BasePageElement):
    locator = CoookieScreenLocators.POP_UP_DIALOG_WINDOW

class HomePageScreen(BasePageElement):
    locator = HomePageLocators.PYTHON_LINK_TEXT


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class CookiePopupScreenPage(BasePage):
    #Actions items for CookiePopScreen

    def click_reject_cookies_btn(self):
        element = self.driver.find_element(*CoookieScreenLocators.REJECT_COOKIES_BUTTON)
        element.click()

class HomePageScreenPage(BasePage):
    #Action items happening on homepage screen

    def click_categories_menu(self):
        element = self.driver.find_element(*HomePageLocators.CATEGORIES_MENU)
        ActionChains(self.driver).move_to_element(
            element
        ).pause(2).click().perform()

    def click_redirect_to_python_page(self):
        element = self.driver.find_element(*HomePageLocators.PYTHON_PAGE_URL)
        ActionChains(self.driver).move_to_element(
            element
        ).pause(2).click().perform()

