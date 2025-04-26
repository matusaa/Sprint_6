import pytest
from selenium import webdriver
from constants import Constants
from pages.main_page import MainPageScooter
from pages.order_page import OrderPage

@pytest.fixture(scope="function")
def driver():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get(Constants.URL)
    yield browser
    browser.quit()

@pytest.fixture
def home_page(driver):
    home_page = MainPageScooter(driver)
    home_page.close_cookie_window()
    return home_page

@pytest.fixture
def order_page(driver):
    order_page = OrderPage(driver)
    return order_page