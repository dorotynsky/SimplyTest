from selenium.webdriver.common.by import By
from tests.conftest import driver


class CartPage:
    def __init__(self, driver):
        self.browser = driver
        # Locators
        self.page_title_locator = (By.TAG_NAME, "h1")

    def get_page_title_text(self):
        return self.browser.find_element(*self.page_title_locator).text
