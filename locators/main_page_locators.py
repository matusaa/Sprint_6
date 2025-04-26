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
    FAQ_QUESTION_1 = By.ID, 'accordion__heading-0'
    FAQ_ANSWER_1 = (By.ID, "accordion__panel-0")
    # Хочу сразу несколько самокатов! Так можно?
    FAQ_QUESTION_2 = By.ID, 'accordion__heading-1'
    FAQ_ANSWER_2 = (By.ID, "accordion__panel-1")
    # Как рассчитывается время аренды?
    FAQ_QUESTION_3 = By.ID, 'accordion__heading-2'
    FAQ_ANSWER_3 = (By.ID, "accordion__panel-2")
    # Можно ли заказать самокат прямо на сегодня?
    FAQ_QUESTION_4 = By.ID, 'accordion__heading-3'
    FAQ_ANSWER_4 = (By.ID, "accordion__panel-3")
    # Можно ли продлить заказ или вернуть самокат раньше?
    FAQ_QUESTION_5 = By.ID, 'accordion__heading-4'
    FAQ_ANSWER_5 = (By.ID, "accordion__panel-4")
    # Вы привозите зарядку вместе с самокатом?
    FAQ_QUESTION_6 = By.ID, 'accordion__heading-5'
    FAQ_ANSWER_6 = (By.ID, "accordion__panel-5")
    # Можно ли отменить заказ?
    FAQ_QUESTION_7 = By.ID, 'accordion__heading-6'
    FAQ_ANSWER_7 = (By.ID, "accordion__panel-6")
    # Я жизу за МКАДом, привезёте?
    FAQ_QUESTION_8 = By.ID, 'accordion__heading-7'
    FAQ_ANSWER_8 = (By.ID, "accordion__panel-7")
    # Кнопка Принять куки
    ACCEPT_COOKIE_BUTTON = By.ID, 'rcc-confirm-button'