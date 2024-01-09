from selenium.webdriver.common.by import By


class IngredientPageLocators:
    FLD_ID_OF_ORDER = By.XPATH, '//*[contains(@class, "text_type_digits-large mb-8")]'

    BTN_CREST_CLOSE = By.XPATH, '//*[contains(@class, "Modal_modal__close")]'
