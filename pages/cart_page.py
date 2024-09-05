from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class CartPage:
    def __init__(self, driver):
        self.browser = driver
        # Locators
        self.page_title_locator = (By.TAG_NAME, "h1")
        self.quantity_input_locator = (By.CSS_SELECTOR, "input[type=number]")
        self.update_cart_locator = (By.XPATH, "//button[contains(., 'Update cart')]")
        self.product_subtotal_locator = (By.CSS_SELECTOR, ".product-subtotal bdi")

    def get_page_title_text(self):
        return self.browser.find_element(*self.page_title_locator).text

    def change_item_quantity(self, quantity: str):
        item_quantity_el = self.browser.find_element(*self.quantity_input_locator)
        item_quantity_el.clear()
        item_quantity_el.send_keys(quantity)

    def click_update_cart(self):
        return self.browser.find_element(*self.update_cart_locator).click()

    def get_product_subtotal_text(self, timeout=10):
        subtotal_before = self.browser.find_element(*self.product_subtotal_locator).text
        WebDriverWait(self.browser, timeout).until(
            lambda driver: self.browser.find_element(*self.product_subtotal_locator).text != subtotal_before
        )
        return self.browser.find_element(*self.product_subtotal_locator).text
