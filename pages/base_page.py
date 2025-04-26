import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Скролл до элемента {locator}')
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center"});', element)

    @allure.step('Найти элемент с ожиданием локатора: {locator}')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_url_to_be(self, url):
        return WebDriverWait(self.driver, 6).until((expected_conditions.url_to_be(url)))

    @allure.step('Кликнуть на элемент с локатором: {locator}')
    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    @allure.step('Ввести значение в поле ввода с локатором: {locator}')
    def set_text_to_elm(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    @allure.step('Получить текст на элементе с локатором: {locator}')
    def get_text_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    @allure.step('Перейти на другую вкладку')
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Проверить отображение элемента с локатором: {locator}')
    def check_displaying_of_element(self, locator):
        return self.find_element_with_wait(locator).is_displayed()