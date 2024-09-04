from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from tests.conftest import driver


class HomePage:
    def __init__(self, driver):
        self.browser = driver
        # Locators
        self.page_title_locator = (By.CLASS_NAME, "page-title")
        self.cart_button_locator = (By.CLASS_NAME, "cart-contents")
        self.empty_message_locator = (By.CLASS_NAME, "woocommerce-mini-cart__empty-message")

    def get_page_title_text(self):
        return self.browser.find_element(*self.page_title_locator).text

    def click_cart_button(self):
        return self.browser.find_element(*self.cart_button_locator).click()

    def get_amount_of_items_in_cart(self):
        cart_button_el = self.browser.find_element(*self.cart_button_locator)
        count_element = cart_button_el.find_element(By.CLASS_NAME, "count")
        return count_element.text

    def hover_over_cart(self):
        cart_button_el = self.browser.find_element(*self.cart_button_locator)
        actions = ActionChains(self.browser)
        actions.move_to_element(cart_button_el).perform()

    def get_empty_message_visibility(self):
        return self.browser.find_element(*self.empty_message_locator).is_displayed()

    def get_empty_message_text(self):
        return self.browser.find_element(*self.empty_message_locator).text
