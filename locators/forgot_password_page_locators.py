from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    FILD_INPUT_EMAIL_LOCATOR = By.CLASS_NAME, 'name'

    BTN_RESTORE_LOCATOR = By.XPATH, "//button[text()='Восстановить'"
