import allure

from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    @allure.step('Click "History of orders"link')
    def click_history_of_orders(self):
        self.click_to_element(ProfilePageLocators.LNK_HISTORY_OF_ORDERS)

    @allure.step('Click button "Exit"')
    def click_btn_exit(self):
        self.click_to_element(ProfilePageLocators.BTN_EXIT)


