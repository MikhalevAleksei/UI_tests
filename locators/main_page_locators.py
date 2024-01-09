from selenium.webdriver.common.by import By


class MainPageLocators:
    BTN_ENTER_IN_ACCOUNT_LOCATOR = By.LINK_TEXT, 'Войти в аккаунт'

    BTN_PERSONAL_AREA_LOCATOR = By.XPATH, '//p[text()="Личный Кабинет"]'

    BTN_MAKE_ORDER_LOCATOR = By.XPATH, '//button[text()= "Оформить заказ"]'

    LNK_BUN_R2_D3_LOCATOR = By.XPATH, '//*[text()= "Флюоресцентная булка R2-D3"]'
    LNK_BIOCUTLET_LOCATOR = By.XPATH, '//*[text()= "Биокотлета из марсианской Магнолии"]'
    LNK_CHEESE_LOCATOR = By.XPATH, '//*[text()= "Сыр с астероидной плесенью"]'

    FLD_ADD_INGREDIENT_LOCATOR = By.XPATH, '//*[text()= "Перетяните булочку сюда (верх)"]'

    FLD_CONSTRACTOR_LOCATOR = By.XPATH, '//*[text()= "Конструктор"]'

    FLD_LIST_OF_ORDERS_LOCATOR = By.XPATH, '//*[text()= "Лента Заказов"]'
    TXT_LIST_OF_ORDERS_LOCATOR = By.XPATH, '//*[text()= "В работе:"]'

    TXT_DETAILS_OF_INGREDIENT_LOCATOR = By.XPATH, '//*[text()= "Детали ингредиента"]'

    BTN_CREST_CLOSE_POPUP_DETAILS_OF_INGREDIENT_LOCATOR = '//*[contains(@class, "Modal_modal__close__TnseK")]/child::*'

    BTN_CREST_CLOSE_POPUP_SUCCESS_ORDER_LOCATOR = '//*[contains(@class,"Modal_modal__close__TnseK")]/child::*'

    TXT_SUCCESS_ORDER_LOCATOR = By.XPATH, '//*[text()= "Ваш заказ начали готовить"]'

    TXT_ID_OF_LIST_ORDER_LOCATOR = By.XPATH, '//*[starts-with(text(), "#")]'

    TXT_NUMBER_ORDERS_DURING_ALL_TIME_LOCATOR = By.XPATH, '//*[text()="Выполнено за все время:"]/following-sibling::p'
    TXT_NUMBER_ORDERS_DURING_DAY_LOCATOR = By.XPATH, '//*[text()="Выполнено за сегодня:"]/following-sibling::p'

    TXT_ID_OF_NEW_ORDER_LOCATOR = By.XPATH, '//*[contains(@class, "text_type_digits-large ")]'

    TXT_ID_OF_READY_ORDERS_LOCATOR = By.XPATH, '//*[contains(@class, "text text_type_main-small")]'

    TXT_COUNTER_OF_INGREDIENT_LOCATOR = By.XPATH, '//*[contains(@class, "counter_counter__num")]'
