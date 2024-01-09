import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Enter account')
    def click_link_restore_password(self):
        self.click_to_element(LoginPageLocators.LNK_RESTORE_PASSWORD_LOCATOR)

    @allure.step('Click registration link')
    def click_registration_link(self):
        self.click_to_element(LoginPageLocators.LNK_REGISTER_LOCATOR)

    @allure.step('Set email to login field')
    def set_login_email(self, text):
        self.set_text_to_element(LoginPageLocators.FLD_EMAIL_LOCATOR)

    @allure.step('Set password to login field')
    def set_login_password(self, text):
        self.set_text_to_element(LoginPageLocators.FLD_PASSWORD_LOCATOR)

    @allure.step('Click button login')
    def click_btn_login(self):
        self.click_to_element(LoginPageLocators.BTN_ENTER_LOCATOR)

    @allure.step('Check success exit from account')
    def success_exit_from_account(self):
        return self.find_my_element(LoginPageLocators.BTN_ENTER_LOCATOR)
