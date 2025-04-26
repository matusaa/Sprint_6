import allure
from locators.order_page_locators import TestOrderPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
from selenium.webdriver.common.by import By

class OrderPage(BasePage):

    @allure.step('Заполнить поле "Имя"')
    def set_first_name(self, name):
        self.set_text_to_elm(TestOrderPageLocators.FIRST_NAME_INPUT, name)
        return self

    @allure.step('Заполнить поле "Фамилия"')
    def set_last_name(self, last_name):
        self.set_text_to_elm(TestOrderPageLocators.LAST_NAME_INPUT, last_name)
        return self

    @allure.step('Заполнить поле "Адрес"')
    def set_address(self, address):
        self.set_text_to_elm(TestOrderPageLocators.ADDRESS_INPUT, address)
        return self

    @allure.step('Заполнить поле "Метро"')
    def set_metro(self, station):
        self.click_on_element(TestOrderPageLocators.METRO_STATION_INPUT)
        self.set_text_to_elm(TestOrderPageLocators.METRO_STATION_INPUT, station)
        self.click_on_element(TestOrderPageLocators.SELECTED_STATION)
        return self

    def check_metro_value(self, station):
        field = self.find_element_with_wait(TestOrderPageLocators.METRO_STATION_INPUT)
        expected_value = station
        assert field.get_attribute('value') == expected_value

    @allure.step('Заполнить поле "Телефон"')
    def set_phone(self, number):
        self.set_text_to_elm(TestOrderPageLocators.PHONE_NUMBER_INPUT, number)
        return self

    @allure.step('Нажать кнопку "Далее"')
    def click_next_button(self):
        self.click_on_element(TestOrderPageLocators.CONTINUE_BUTTON)

    @allure.step('Проверка отображения заголовка второй формы')
    def check_the_title_of_second_form_displaying(self):
        self.check_displaying_of_element(TestOrderPageLocators.TITLE_ABOUT_RENT_FORM)

    @allure.step('Заполнить поле "Дата аренды"')
    def set_rental_date(self):
        self.click_on_element(TestOrderPageLocators.RENTAL_DATE_INPUT)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(TestOrderPageLocators.CALENDAR))
        today = datetime.date.today()
        available_days = self.driver.find_elements(*TestOrderPageLocators.AVAILABLE_DAYS)
        for day_element in available_days:
            text = day_element.text.strip()
            if not text.isdigit():
                continue
            day = int(text)
            current_year = today.year
            current_month = today.month
            try:
                date_to_compare = datetime.date(current_year, current_month, day)
            except ValueError:
                continue
            if date_to_compare > today:
                day_element.click()
                return
        raise Exception("Не удалось найти дату больше текущей")

    @allure.step('Заполнить поле "Срок аренды"')
    def set_rental_duration(self):
        self.click_on_element(TestOrderPageLocators.RENTAL_DURATION_INPUT)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(TestOrderPageLocators.RENTAL_DURATION_LIST))
        self.click_on_element(TestOrderPageLocators.DROPDOWN_ITEM_RENTAL_PERIOD)


    def set_color_field(self):
        self.click_on_element(TestOrderPageLocators.CHECKBOX_GREY)
        return self

    def set_comment_field(self, comment):
        self.set_text_to_elm(TestOrderPageLocators.COMMENT_FIELD, comment)
        return self

    @allure.step('Нажать кнопку "Заказать"')
    def click_order_button(self):
        self.click_on_element(TestOrderPageLocators.ORDER_BUTTON)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(TestOrderPageLocators.POP_UP_CONFIRM_ORDER)
        )
        return self

    @allure.step('Проверка отображения окна подтверждения после нажатия кнопки Заказать')
    def check_displaying_of_confirm_window(self):
        self.check_displaying_of_element(TestOrderPageLocators.POP_UP_CONFIRM_ORDER)

    @allure.step('Нажать кнопку "Да" в окне подтверждения заказа')
    def click_yes_button_confirmation_pop_up(self):
        self.click_on_element(TestOrderPageLocators.YES_BUTTON_POP_UP_CONFIRM_ORDER)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(TestOrderPageLocators.POP_UP_COMPLETE_ORDER))
        return self


    @allure.step('Заполнение первой части формы и нажатие кнопки "Далее"')
    def personal_information_input(self, name, last_name, address, station, number):
        self.set_first_name(name)
        self.set_last_name(last_name)
        self.set_address(address)
        self.set_metro(station)
        self.check_metro_value(station)
        self.set_phone(number)
        self.click_next_button()
        self.check_the_title_of_second_form_displaying()

    @allure.step('Заполнение второй части формы и окно подтверждения')
    def rental_information_input(self, comment):
        self.set_rental_date()
        self.set_rental_duration()
        self.set_color_field()
        self.set_comment_field(comment)
        self.click_order_button()
        self.check_displaying_of_confirm_window()