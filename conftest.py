import pytest
from selenium import webdriver
from pages.main_page import MainPageScooter
from urls import URL

@pytest.fixture(scope="function")
def driver():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get(URL)
    yield browser
    browser.quit()

@pytest.fixture
def home_page(driver):
    home_page = MainPageScooter(driver)
    home_page.close_cookie_window()
    return home_page