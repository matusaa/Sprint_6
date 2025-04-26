import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import TestMainPageLocators
from pages.base_page import BasePage
from constants import Constants


class MainPageScooter(BasePage):

    @allure.step('Скролл до блока "Вопросы о важном"')
    def scroll_to_faq(self):
        locator = TestMainPageLocators.FAQ_QUESTION_8
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step('Нажатие на вопрос')
    def click_the_question(self, question_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(question_locator))
        self.click_on_element(question_locator)

    @allure.step('Получение текста ответа')
    def get_the_answer_text(self, answer_locator):
        self.find_element_with_wait(answer_locator)
        answer = self.get_text_on_element(answer_locator)
        return answer

    @allure.step('Нажатие на логотип "Яндекс"')
    def click_logo_yandex_open_dzen_page(self):
        self.find_element_with_wait(TestMainPageLocators.LOGO_YANDEX)
        self.click_on_element(TestMainPageLocators.LOGO_YANDEX)
        self.switch_to_next_tab()
        self.wait_url_to_be(Constants.DZEN_URL)

    @allure.step('Нажатие на логотип "Самокат"')
    def click_logo_open_home_page(self):
        self.find_element_with_wait(TestMainPageLocators.LOGO_SAMOKAT)
        self.click_on_element(TestMainPageLocators.LOGO_SAMOKAT)

    @allure.step('Нажатие кнопки "Заказать" в шапке')
    def click_order_button_header(self):
        self.find_element_with_wait(TestMainPageLocators.ORDER_BUTTON_HEADER)
        self.click_on_element(TestMainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step('Скролл до кнопки "Заказать" в теле страницы')
    def scroll_to_order_button_body(self):
        self.scroll_to_element(TestMainPageLocators.HOW_IT_WORKS_BLOCK)
        self.find_element_with_wait(TestMainPageLocators.ORDER_BUTTON_MIDDLE)

    @allure.step('Нажатие кнопки "Заказать" в теле страницы')
    def click_order_button_body(self):
        self.click_on_element(TestMainPageLocators.ORDER_BUTTON_MIDDLE)

    @allure.step('Закрытие окна куки')
    def close_cookie_window(self):
        self.find_element_with_wait(TestMainPageLocators.ACCEPT_COOKIE_BUTTON)
        self.click_on_element(TestMainPageLocators.ACCEPT_COOKIE_BUTTON)

