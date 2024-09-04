from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.browser = driver
        # Locators
        self.page_title_locator = (By.TAG_NAME, "h1")
        self.cart_btn_locator = (By.CLASS_NAME, "cart-contents")
        self.empty_message_locator = (By.CLASS_NAME, "woocommerce-mini-cart__empty-message")
        self.view_cart_btn_locator = (By.LINK_TEXT, "View cart")

    # ---Universal methods---
    # Universal method to find an element
    def find(self, locator):
        return self.browser.find_element(*locator)

    # Universal method to click an element
    def click(self, locator):
        self.find(locator).click()

    # Universal method to get text from an element
    def get_text(self, locator):
        return self.find(locator).text

    def get_page_title_text(self):
        return self.get_text(self.page_title_locator)

    # -----------------------

    # ---Cart---
    def click_cart_btn(self):
        self.click(self.cart_btn_locator)

    def get_amount_of_items_in_cart(self):
        cart_btn_el = self.find(self.cart_btn_locator)
        count_element = cart_btn_el.find_element(By.CLASS_NAME, "count")
        return count_element.text

    def hover_over_cart(self):
        cart_btn_el = self.find(self.cart_btn_locator)
        actions = ActionChains(self.browser)
        actions.move_to_element(cart_btn_el).perform()

    def get_empty_message_visibility(self):
        return self.find(self.empty_message_locator).is_displayed()

    def get_empty_message_text(self):
        return self.get_text(self.empty_message_locator)

    def add_item_to_cart(self, item: str):
        self.browser.find_element(By.CSS_SELECTOR, f"a[aria-label='Add “{item}” to your cart']").click()

    def click_view_cart_btn(self):
        self.click(self.view_cart_btn_locator)
