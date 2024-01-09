import allure

from pages.base_page import BasePage
from locators.forgot_password_page_locators import \
    ForgotPasswordPageLocators
from locators.reset_password_page_locators import \
    ResetPasswordPageLocators
from helpers import make_new_fake_data


class ForgotPasswordPage(BasePage):
    @allure.step('Set some email to field restore password')
    def set_email_to_field_restore_password(self, text):
        self.set_text_to_element(
            ForgotPasswordPageLocators.FILD_INPUT_EMAIL_LOCATOR, text)

    @allure.step('Click restore button')
    def click_restore_button(self):
        self.click_to_element(ForgotPasswordPageLocators.BTN_RESTORE_LOCATOR)

    @allure.step('Transfer to reset password page')
    def transfer_to_restore_password_page(self):
        fake_dict = make_new_fake_data()
        text = fake_dict['email']
        self.set_email_to_field_restore_password(text)
        self.click_restore_button()

    @allure.step('Check success transfer to reset password page')
    def success_transfer_to_resset_password_page(self):
        return self.find_my_element(ResetPasswordPageLocators.BTN_SAVE_LOCATOR)
