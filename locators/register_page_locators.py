from selenium.webdriver.common.by import By


class RegisterPageLocators:
    FLD_NAME_LOCATOR = By.NAME, 'name'
    FLD_EMAIL_LOCATOR = By.XPATH, '//*[text()= "Email"]'
    FLD_PASSWORD_LOCATOR = By.NAME, 'Пароль'

    BTN_REGISTER_LOCATOR = By.XPATH, '//button[text()= "Зарегистрироваться"]'
