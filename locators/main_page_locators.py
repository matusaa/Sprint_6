from selenium.webdriver.common.by import By


class TestMainPageLocators:
    # Надпись Яндекс в логотипе
    LOGO_YANDEX = By.CLASS_NAME, "Header_LogoYandex__3TSOI"
    # Надпись Самокат в логотипе
    LOGO_SAMOKAT = By.CLASS_NAME, "Header_LogoScooter__3lsAR"
    # Кнопка Заказать в шапке
    ORDER_BUTTON_HEADER = By.CLASS_NAME, 'Button_Button__ra12g'
    # Блок "Как это работает"
    HOW_IT_WORKS_BLOCK = By.CLASS_NAME, 'сHome_ThirdPart__LSTEE'
    # Кнопка Заказать в середине страницы
    ORDER_BUTTON_MIDDLE = By.CLASS_NAME, 'Button_Middle__1CSJM'
    # --------------------Блок FAQ-----------------------------
    # Сколько это стоит? И как оплатить?
    FAQ_QUESTION_1 = (By.XPATH, "//div[contains(@class, 'accordion__button') "
                                "and text()='Сколько это стоит? И как оплатить?']")
    FAQ_ANSWER_1 = (By.XPATH, "//div[contains(@class, 'accordion__panel')]//p[contains(text(), 'Сутки — 400 рублей')]")
    # Хочу сразу несколько самокатов! Так можно?
    FAQ_QUESTION_2 = (By.XPATH, "//div[contains(@class, 'accordion__button') "
                                "and text()='Хочу сразу несколько самокатов! Так можно?']")
    FAQ_ANSWER_2 = (By.XPATH, "//div[contains(@class, 'accordion__panel')]//p[contains(text(), 'Пока что у нас так')]")
    # Как рассчитывается время аренды?
    FAQ_QUESTION_3 = (By.XPATH, "//div[contains(@class, 'accordion__button') "
                                "and text()='Как рассчитывается время аренды?']")
    FAQ_ANSWER_3 = (By.XPATH, "//div[contains(@class, 'accordion__panel')]//p[contains(text(),"
                              " 'Допустим, вы оформляете заказ')]")
    # Можно ли заказать самокат прямо на сегодня?
    FAQ_QUESTION_4 = (By.XPATH, "//div[contains(@class, 'accordion__button') "
                                "and text()='Можно ли заказать самокат прямо на сегодня?']")
    FAQ_ANSWER_4 = (By.XPATH, "//div[contains(@class, 'accordion__panel')]//p[contains(text(), "
                              "'Только начиная с завтрашнего дня')]")
    # Можно ли продлить заказ или вернуть самокат раньше?
    FAQ_QUESTION_5 = (By.XPATH, "//div[contains(@class, 'accordion__button') "
                                "and text()='Можно ли продлить заказ или вернуть самокат раньше?']")
    FAQ_ANSWER_5 = (By.XPATH, "//div[contains(@class, 'accordion__panel')]//p[contains(text(), 'Пока что нет!')]")
    # Вы привозите зарядку вместе с самокатом?
    FAQ_QUESTION_6 = (By.XPATH, "//div[contains(@class, 'accordion__button') "
                                "and text()='Вы привозите зарядку вместе с самокатом?']")
    FAQ_ANSWER_6 = (By.XPATH, "//div[contains(@class, 'accordion__panel')]//p[contains(text(), "
                              "'Самокат приезжает к вам с полной зарядкой')]")
    # Можно ли отменить заказ?
    FAQ_QUESTION_7 = (By.XPATH, "//div[contains(@class, 'accordion__button') "
                                "and text()='Можно ли отменить заказ?']")
    FAQ_ANSWER_7 = (By.XPATH, "//div[contains(@class, 'accordion__panel')]//p[contains(text(), "
                              "'Да, пока самокат не привезли')]")
    # Я жизу за МКАДом, привезёте?
    FAQ_QUESTION_8 = (By.XPATH, "//div[contains(@class, 'accordion__button') "
                                "and text()='Я жизу за МКАДом, привезёте?']")
    FAQ_ANSWER_8 = (By.XPATH, "//div[contains(@class, 'accordion__panel')]//p[contains(text(), 'Да, обязательно')]")
    # Кнопка Принять куки
    ACCEPT_COOKIE_BUTTON = By.ID, 'rcc-confirm-button'