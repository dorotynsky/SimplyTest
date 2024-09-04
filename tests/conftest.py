import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.cart_page import CartPage


@pytest.fixture
def driver():
    # Create a ChromeOptions object for browser configuration
    chrome_options = webdriver.ChromeOptions()

    # Add arguments to disable pop-up windows
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    chrome_options.add_argument("--no-first-run")  # Disables the default search engine selection pop-up
    chrome_options.add_argument("--no-default-browser-check")  # Disables the default browser check
    chrome_options.add_argument("--disable-infobars")  # Disables information bars (optional)

    # Initialize WebDriver with the specified options
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture
def open_home_page(driver):
    driver.get("https://autoprojekt.simplytest.de/")
    return driver


@pytest.fixture
def home_page(open_home_page):
    # Create and return the HomePage object after opening the home page
    return HomePage(open_home_page)


@pytest.fixture
def cart_page(driver):
    # Create and return the CartPage object
    return CartPage(driver)
