import allure

from locators.ingredient_page_locators import IngredientPageLocators
from pages.base_page import BasePage


class IngredientPage(BasePage):
    @allure.step('Get id of order')
    def get_id_of_order(self):
        order_id = self.get_text_from_element(
            IngredientPageLocators.FLD_ID_OF_ORDER)
        return order_id

    @allure.step('Close pop-up of success order')
    def close_success_order_pop_up(self):
        self.click_to_element(IngredientPageLocators.BTN_CREST_CLOSE)
