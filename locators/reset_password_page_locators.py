from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    BTN_EYE_SHOW_HIDE_PASSWORD_LOCATOR = \
        By.XPATH, '//*[contains(@class, "input__icon-action")]/child::*'
    BTN_SAVE_LOCATOR = By.XPATH, '//*[text()= "Сохранить"'

    FLD_PASSWORD_FOCUSED_LOCATOR = \
        By.XPATH, '//*[contains(@class,"input__placeholder-focused")]'
