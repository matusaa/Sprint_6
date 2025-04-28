import allure
import pytest
from locators.order_page_locators import TestOrderPageLocators
from constants import Constants
from conftest import driver, home_page
from pages.order_page import OrderPage


class TestOrderForm:

    @allure.title('Проверка флоу позитивного сценария оформления заказа через кнопку "Заказать" в шапке' )
    @allure.description('Переход в форму заказа через кнопку "Заказать" в шапке и успешное оформление заказа')
    @pytest.mark.parametrize('name, last_name, address, station, number, comment', [Constants.user_1])
    def test_order_via_header_button(self, driver, home_page, name, last_name, address,station, number,
                                     comment):
        home_page.click_order_button_header()
        order_page = OrderPage(home_page.driver)
        order_page.personal_information_input(name, last_name, address, station, number)
        order_page.rental_information_input(comment)
        order_page.click_yes_button_confirmation_pop_up()
        assert order_page.is_order_confirmation_displayed()

    @allure.title('Проверка флоу позитивного сценария оформления заказа через нижнюю кнопку "Заказать')
    @allure.description('Переход в форму заказа через нажатие кнопки "Заказать" в теле и успешного оформления заказа')
    @pytest.mark.parametrize('name, last_name, address, station, number, comment', [Constants.user_2])
    def test_complete_order_form_order_button_body(self, driver, home_page, name, last_name, address,
                                                   station, number, comment):
        home_page.click_order_button_body()
        order_page = OrderPage(driver)
        order_page.personal_information_input(name, last_name, address, station, number)
        order_page.rental_information_input(comment)
        order_page.click_yes_button_confirmation_pop_up()
        assert order_page.is_order_confirmation_displayed()