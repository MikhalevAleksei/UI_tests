import allure

from locators.register_page_locators import RegisterPageLocators
from pages.base_page import BasePage


class RegisterPage(BasePage):
    @allure.step('Set name to registration fields')
    def register_name(self, text):
        self.set_text_to_element(RegisterPageLocators.FLD_NAME_LOCATOR, text)

    @allure.step('Set email to registration fields')
    def register_email(self, text):
        self.set_text_to_element(RegisterPageLocators.FLD_EMAIL_LOCATOR, text)

    @allure.step('Set password to registration fields')
    def register_password(self, text):
        self.set_text_to_element(
            RegisterPageLocators.FLD_PASSWORD_LOCATOR, text)

    @allure.step('Click button registration ')
    def click_btn_registration(self):
        self.click_to_element(RegisterPageLocators.BTN_REGISTER_LOCATOR)

    # TODO
    @allure.step('Register new user')
    def register_new_user(self, new_fake_data):
        fake_user = new_fake_data()
        name = fake_user['name']
        email = fake_user['email']
        password = fake_user['password']

        self.register_name(name)
        self.register_email(email)
        self.register_password(password)
        self.click_btn_registration()
