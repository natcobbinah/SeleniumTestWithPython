from selenium.webdriver.support.events import AbstractEventListener
import logging
import logging.config
from logging_config import LOG_CONFIG
import logging.handlers


logger = logging.getLogger("example_app")
logging.config.dictConfig(LOG_CONFIG)


class LogEventListener(AbstractEventListener):

    logger = logger

    def after_navigate_to(self, url: str, driver):
        logger.info(f"{url} opened in browser")

    def after_find(self, by, value, driver):
        logger.info(f"Found element by={by}  and value={value}")

    def after_click(self, element, driver):
        logger.info(f"{element} visible and clicked in browser")

    def after_quit(self, driver):
        logger.info("------Logging completed------")

    def on_exception(self, exception, driver):
        logger.error(f"{exception.msg}")
        
        

        
        
