from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from tests.conftest import driver


class HomePage:
    def __init__(self, driver):
        self.browser = driver
        # Locators
        self.page_title_locator = (By.TAG_NAME, "h1")
        self.cart_btn_locator = (By.CLASS_NAME, "cart-contents")
        self.empty_message_locator = (By.CLASS_NAME, "woocommerce-mini-cart__empty-message")
        self.view_cart_btn_locator = (By.LINK_TEXT, "View cart")

    def add_item_to_cart(self, item: str):
        return self.browser.find_element(By.CSS_SELECTOR, f"a[aria-label='Add “{item}” to your cart']").click()

    def click_view_cart_btn(self):
        return self.browser.find_element(*self.view_cart_btn_locator).click()

    def get_page_title_text(self):
        return self.browser.find_element(*self.page_title_locator).text

    def click_cart_btn(self):
        return self.browser.find_element(*self.cart_btn_locator).click()

    def get_amount_of_items_in_cart(self):
        cart_btn_el = self.browser.find_element(*self.cart_btn_locator)
        count_element = cart_btn_el.find_element(By.CLASS_NAME, "count")
        return count_element.text

    def hover_over_cart(self):
        cart_btn_el = self.browser.find_element(*self.cart_btn_locator)
        actions = ActionChains(self.browser)
        actions.move_to_element(cart_btn_el).perform()

    def get_empty_message_visibility(self):
        return self.browser.find_element(*self.empty_message_locator).is_displayed()

    def get_empty_message_text(self):
        return self.browser.find_element(*self.empty_message_locator).text
