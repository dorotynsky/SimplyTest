from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.conftest import driver


class HomePage:
    def __init__(self, driver):
        self.browser = driver
        # Elements
        self.page_title_el = self.browser.find_element(By.CLASS_NAME, "page-title")
        self.cart_button_el = self.browser.find_element(By.CLASS_NAME, "cart-contents")
        self.empty_message_el = self.browser.find_element(By.CLASS_NAME, "woocommerce-mini-cart__empty-message")

    def get_page_title_text(self):
        return self.page_title_el.text

    def click_cart_button(self):
        return self.cart_button_el.click()

    def get_amount_of_items_in_cart(self):
        # return self.cart_button_el.find_element(By.CLASS_NAME, "count").text

        # Find the cart button element every time you interact with it
        cart_button_el = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart-contents"))
        )
        # Find the 'count' element within the cart button element
        count_element = cart_button_el.find_element(By.CLASS_NAME, "count")
        return count_element.text

    def hover_over_cart(self):
        actions = ActionChains(self.browser)
        actions.move_to_element(self.cart_button_el).perform()

    def get_visibility_of_empty_message(self) :
        return self.empty_message_el.is_displayed()
