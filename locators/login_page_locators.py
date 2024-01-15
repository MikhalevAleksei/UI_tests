from selenium.webdriver.common.by import By


class LoginPageLocators:
    LNK_RESTORE_PASSWORD_LOCATOR = By.LINK_TEXT, 'Восстановить пароль'

    FLD_EMAIL_LOCATOR = By.NAME, 'name'
    FLD_PASSWORD_LOCATOR = By.NAME, 'Пароль'

    BTN_ENTER_LOCATOR = By.XPATH, '//button[text()= "Войти"]'

    LNK_REGISTER_LOCATOR = By.XPATH, '//button[text()= "Зарегистрироваться"]'
