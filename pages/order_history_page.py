import allure

from locators.order_history_page_locators import OrderHistoryPageLocators
from pages.base_page import BasePage


class OrderHistoryPage(BasePage):
    @allure.step('Check success transfer to "History of orders"')
    def success_transfer_order_history(self):
        return self.find_my_element(
            OrderHistoryPageLocators.TXT_COMPLETED_LOCATOR)

    @allure.step('Get number of last order')
    def get_id_of_last_order(self):
        self.get_text_from_element(
            OrderHistoryPageLocators.TXT_ID_OF_LAST_ORDER_LOCATOR)

    @allure.step('Click on order to open pop-up "Details of order"')
    def click_order_to_open_popup(self):
        self.click_to_element(
            OrderHistoryPageLocators.TXT_ID_OF_LAST_ORDER_LOCATOR)

    @allure.step('Check success open pop-up "Details of order"')
    def success_open_popup_order_details(self):
        return self.find_my_element(
            OrderHistoryPageLocators.TXT_SUCCESS_OPEN_POP_UP_DETAILS_OF_INGREDIENT_LOCATOR)

    @allure.step('Get list of orders from "History of orders"')
    def get_orders_from_history_orders(self):
        ids = self.get_text_from_elements(
            OrderHistoryPageLocators.TXT_ID_OF_HISTORY_ORDER_LOCATOR)
        history_ids_orders = [i for i in ids]

        return history_ids_orders

    def check_ids_orders_in_history(self, list_orders):
        history_orders = self.get_orders_from_history_orders()
        for i in history_orders:
            if i in list_orders:
                return True
            return False
