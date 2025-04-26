from selenium.webdriver.common.by import By


class TestOrderPageLocators:

    # ----------------Окно "Для кого самокат"-------------------
    # Поле Имя
    FIRST_NAME_INPUT = By.XPATH, "//input[@placeholder='* Имя']"
    # Поле Фамилия
    LAST_NAME_INPUT = By.XPATH, "//input[@placeholder='* Фамилия']"
    # Поле Адрес: куда привезти заказ
    ADDRESS_INPUT = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    # Поле Станция метро
    METRO_STATION_INPUT = By.XPATH, "//input[@placeholder='* Станция метро']"
    # Список станций метро
    METRO_STATION_LIST = By.CLASS_NAME, 'select-search__input'
    # Выбранная станция метро
    SELECTED_STATION = (By.XPATH, ".//li[@class='select-search__row']")
    # Поле Телефон
    PHONE_NUMBER_INPUT = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    # Кнопка Далее
    CONTINUE_BUTTON = By.XPATH, '//button[text()="Далее"]'

    # -------------------Окно "Про аренду"-----------------------
    # Заголовок формы Про аренду
    TITLE_ABOUT_RENT_FORM = By.CLASS_NAME, 'Order_Header__BZXOb'
    # Поле Когда привезти самокат
    RENTAL_DATE_INPUT = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    # Календарь

    CALENDAR = By.CLASS_NAME, 'react-datepicker__month-container'
    # Поле Срок аренды
    RENTAL_DURATION_INPUT = By.CLASS_NAME, 'Dropdown-placeholder'
    # Сегодняшняя дата в календаре
    TODAY_DATE_CALENDAR = By.CLASS_NAME, 'react-datepicker__day--today'
    # Доступные дни для выбора
    AVAILABLE_DAYS = (By.XPATH,
                      "//div[contains(@class, 'react-datepicker__day') and "
                      "not(contains(@class, 'react-datepicker__day--disabled')) and "
                      "not(contains(@class, 'react-datepicker__day-name'))]"
                      )
    # Выпадающий список с количеством дней аренды
    RENTAL_DURATION_LIST = By.CLASS_NAME, 'Dropdown-menu'
    # Семеро суток
    DROPDOWN_ITEM_RENTAL_PERIOD = (By.XPATH, ".//div[@class = 'Dropdown-menu']/div[text() ='семеро суток']")
    # Поле Срок аренды после выбора срока
    RENTAL_DURATION_AFTER_INPUT = By.CLASS_NAME, 'Dropdown-placeholder is-selected'
    # Поле выбора цвета
    CHOOSE_COLOR_FIELD = By.XPATH, '//div[text()="Цвет самоката"]'
    # Цвет черный жемчуг
    CHECKBOX_GREY = By.ID, 'black'
    # Поле комментарий
    COMMENT_FIELD = By.XPATH, '//input[@placeholder="Комментарий для курьера"]'
    # Кнопка Заказать
    ORDER_BUTTON = By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]'
    # Окно Хотите оформить заказ?
    POP_UP_CONFIRM_ORDER = By.CLASS_NAME, 'Order_ModalHeader__3FDaJ'

    # Кнопка Да в окне Хотите оформить заказ?
    YES_BUTTON_POP_UP_CONFIRM_ORDER = By.XPATH, '//button[text()="Да"]'
    # Окно Заказ оформлен
    POP_UP_COMPLETE_ORDER = By.CLASS_NAME, 'Order_ModalHeader__3FDaJ'