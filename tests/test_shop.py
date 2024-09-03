import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_open_google(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title