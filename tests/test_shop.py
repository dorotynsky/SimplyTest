from tests.conftest import open_home_page
from pages.home_page import HomePage


def test_shop_title(open_home_page):
    home_page = HomePage(open_home_page)
    actual_page_title_text = home_page.get_page_title_text()
    expected_page_title_text = "Shop"
    assert actual_page_title_text == expected_page_title_text, (f"Page title should be: {expected_page_title_text}."
                                                                f" Actual result is: {actual_page_title_text}")
