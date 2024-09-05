import allure


def test_complete_flow(home_page, cart_page):
    check_shop_title(home_page)
    check_empty_cart(home_page)
    add_item_to_cart_and_view(home_page, cart_page)
    check_item_quantity_and_subtotal(cart_page)


@allure.step("Check shop page title")
def check_shop_title(home_page):
    actual_page_title_text = home_page.get_page_title_text()
    expected_page_title_text = "Shop"
    assert actual_page_title_text == expected_page_title_text, (
        f"Page title should be: {expected_page_title_text}."
        f" Actual result is: {actual_page_title_text}")


@allure.step("Check if cart is empty")
def check_empty_cart(home_page):
    actual_amount = home_page.get_amount_of_items_in_cart()
    expected_amount = "0 items"
    assert actual_amount == expected_amount, (
        f"Expected amount of items is {expected_amount}."
        f" Actual result is: {actual_amount}")

    home_page.hover_over_cart()
    assert home_page.get_empty_message_visibility()

    actual_empty_message_text = home_page.get_empty_message_text()
    expected_empty_message_text = "No products in the cart."
    assert actual_empty_message_text == expected_empty_message_text, (
        f"Expected empty message text is {expected_empty_message_text}."
        f" Actual result is: {actual_empty_message_text}")


@allure.step("Add item 'Album' to cart and view cart")
def add_item_to_cart_and_view(home_page, cart_page):
    home_page.add_item_to_cart("Album")
    home_page.click_view_cart_btn()
    actual_page_title_text = cart_page.get_page_title_text()
    expected_page_title_text = "Cart"
    assert actual_page_title_text == expected_page_title_text, (
        f"Page title should be: {expected_page_title_text}. "
        f"Actual result is: {actual_page_title_text}"
    )


@allure.step("Check item quantity and subtotal")
def check_item_quantity_and_subtotal(cart_page):
    cart_page.change_item_quantity("2")
    cart_page.click_update_cart()

    actual_subtotal = cart_page.get_product_subtotal_text()

    # Screenshot example
    screenshot = cart_page.make_screenshot()
    allure.attach(screenshot, name="Check subtotal screenshot", attachment_type=allure.attachment_type.PNG)

    expected_subtotal = "30,00 €"
    assert actual_subtotal == expected_subtotal, (
        f"Expected subtotal text is {expected_subtotal}. "
        f"Actual result is: {actual_subtotal}"
    )
