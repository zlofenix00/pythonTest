from selenium.webdriver.chrome.webdriver import WebDriver

from utils.driver import Driver


class MainPage:

    @property
    def driver(self) -> WebDriver:
        return Driver()
