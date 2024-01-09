import allure

from locators.order_history_page_locators import \
    OrderHistoryPageLocators
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
    def click_order_for_popup(self):
        self.click_to_element(
            OrderHistoryPageLocators.TXT_ID_OF_LAST_ORDER_LOCATOR)

    @allure.step('Check success open pop-up "Details of order"')
    def success_open_popup_order_details(self):
        return self.find_my_element(
            OrderHistoryPageLocators.TXT_SUCCESS_OPEN_POP_UP_DETAILS_OF_INGREDIENT_LOCATOR)
