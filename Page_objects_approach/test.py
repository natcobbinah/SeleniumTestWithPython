import unittest
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
import pages
from logger import LogEventListener

class ApressCookieConsentScreen(unittest.TestCase):
    #sample test case using page object model

    @classmethod
    def setUpClass(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')

        self.driver = EventFiringWebDriver(webdriver.Chrome(options), LogEventListener())
        self.driver.get("http://www.apress.com")
        self.driver.maximize_window()

    """ def test_navigate_to_python_link(self):
        consent_screen = pages.CookiePopupScreenPage(self.driver)
        consent_screen.click_reject_cookies_btn()

        categories_menu = pages.HomePageScreenPage(self.driver)
        categories_menu.click_categories_menu()

        python_books_page = pages.HomePageScreenPage(self.driver)
        python_books_page.click_redirect_to_python_page() """

    def test_apress_consent_screen(self):
        consent_screen = pages.CookiePopupScreenPage(self.driver)
        consent_screen.click_reject_cookies_btn()

    def test_categories_menu(self):
        categories_menu = pages.HomePageScreenPage(self.driver)
        categories_menu.click_categories_menu()

    def test_redirect_to_python_page(self):
        python_books_page = pages.HomePageScreenPage(self.driver)
        python_books_page.click_redirect_to_python_page() 

    
    @classmethod
    def tearDownClass(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
