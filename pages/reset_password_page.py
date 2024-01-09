import allure

from locators.reset_password_page_locators import \
    ResetPasswordPageLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):
    @allure.step('Make field password active')
    def make_field_password_active(self):
        self.click_to_element(
            ResetPasswordPageLocators.BTN_EYE_SHOW_HIDE_PASSWORD_LOCATOR)

    @allure.step('Check success for show password button')
    def is_success_for_show_password_button(self):
        return self.find_my_element(
            ResetPasswordPageLocators.FLD_PASSWORD_FOCUSED_LOCATOR)
