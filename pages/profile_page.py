import allure

from locators.profile_page_locators import ProfilePageLocators
from locators.order_history_page_locators import \
    OrderHistoryPageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    @allure.step('Click "History of orders"link')
    def click_history_of_orders(self):
        self.click_to_element(ProfilePageLocators.LNK_HISTORY_OF_ORDERS)

    @allure.step('Click button "Exit"')
    def click_btn_exit(self):
        self.click_to_element(ProfilePageLocators.BTN_EXIT)

    @allure.step('Get list of orders from "History of orders"')
    def get_orders_from_history_orders(self):
        ids = self.get_text_from_elements(
            OrderHistoryPageLocators.TXT_ID_OF_HISTORY_ORDER_LOCATOR)
        history_ids_orders = [i for i in ids]

        return history_ids_orders
