from selenium.webdriver.common.by import By


class OrderHistoryPageLocators:
    TXT_COMPLETED_LOCATOR = By.XPATH, '//*[text()= "Выполнен"]'

    TXT_ID_OF_LAST_ORDER_LOCATOR = By.XPATH, '//*[contains(@class, "text_type_digits-default")]'

    TXT_SUCCESS_OPEN_POP_UP_DETAILS_OF_INGREDIENT_LOCATOR = By.XPATH, '//*[text()= "Cостав"]'

    TXT_ID_OF_HISTORY_ORDER_LOCATOR = By.XPATH, '//*[starts-with(text(), "#")]'
