from selenium.webdriver.common.by import By


class ProfilePageLocators:
    LNK_HISTORY_OF_ORDERS = By.XPATH, '//*[text()= "История заказов"]'
    BTN_EXIT = By.XPATH, '//*[text()= "Выход"]'
