import pytest
import allure
from locators.main_page_locators import TestMainPageLocators
from constants import Constants
from conftest import driver, home_page
from urls import DZEN_URL, URL


class TestMainPageScooter:

    @allure.title('Проверка раздела "Вопросы о важном"')
    @allure.description('Проверка того, что при нажатии на каждый аккордеон открывается соответствующего текста ответ ')
    @pytest.mark.parametrize('question_locator, answer_locator, expected_text', [
        (TestMainPageLocators.FAQ_QUESTION_1, TestMainPageLocators.FAQ_ANSWER_1, Constants.expected_texts['faq1']),
        (TestMainPageLocators.FAQ_QUESTION_2, TestMainPageLocators.FAQ_ANSWER_2, Constants.expected_texts['faq2']),
        (TestMainPageLocators.FAQ_QUESTION_3, TestMainPageLocators.FAQ_ANSWER_3, Constants.expected_texts['faq3']),
        (TestMainPageLocators.FAQ_QUESTION_4, TestMainPageLocators.FAQ_ANSWER_4, Constants.expected_texts['faq4']),
        (TestMainPageLocators.FAQ_QUESTION_5, TestMainPageLocators.FAQ_ANSWER_5, Constants.expected_texts['faq5']),
        (TestMainPageLocators.FAQ_QUESTION_6, TestMainPageLocators.FAQ_ANSWER_6, Constants.expected_texts['faq6']),
        (TestMainPageLocators.FAQ_QUESTION_7, TestMainPageLocators.FAQ_ANSWER_7, Constants.expected_texts['faq7']),
        (TestMainPageLocators.FAQ_QUESTION_8, TestMainPageLocators.FAQ_ANSWER_8, Constants.expected_texts['faq8'])

    ])
    def test_faq_question_shows_answer(self, home_page, question_locator, answer_locator, expected_text):
        home_page.scroll_to_faq()
        home_page.click_the_question(question_locator)
        answer = home_page.get_the_answer_text(answer_locator)
        assert answer == expected_text

    @allure.title('Тест нажатия на надпись "Яндекс" в логотипе')
    @allure.description('Проверка открытия сайта Яндекс.Дзен при нажатии на логотип "Яндекс"')
    def test_click_yandex_logo_navigates_to_dzen(self, home_page):
        home_page.click_logo_yandex_open_dzen_page()
        assert home_page.get_current_url() == DZEN_URL

    @allure.title('Тест нажатия на надпись "Самокат" в логотипе')
    @allure.description('Проверка перехода на главную страницу при нажатии на логотип "Самокат"')
    def test_click_samokat_logo_opens_homepag(self, home_page):
        home_page.click_order_button_header()
        home_page.click_logo_open_home_page()
        assert home_page.get_current_url() == URL