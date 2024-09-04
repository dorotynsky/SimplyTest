import time
from conftest import home_page


def test_shop_title(home_page):
    actual_page_title_text = home_page.get_page_title_text()
    expected_page_title_text = "Shop"
    assert actual_page_title_text == expected_page_title_text, (
        f"Page title should be: {expected_page_title_text}."
        f" Actual result is: {actual_page_title_text}")


def test_empty_cart(home_page):
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


def test_add_item(home_page, cart_page):
    home_page.add_item_to_cart("Album")
    home_page.click_view_cart_btn()
    actual_page_title_text = cart_page.get_page_title_text()
    expected_page_title_text = "Cart"
    assert actual_page_title_text == expected_page_title_text, (
        f"Page title should be: {expected_page_title_text}."
        f" Actual result is: {actual_page_title_text}")
