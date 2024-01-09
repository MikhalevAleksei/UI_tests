import allure
from selenium.webdriver import ActionChains

from locators.ingredient_page_locators import IngredientPageLocators
from locators.main_page_locators import MainPageLocators


class TestMakeOrder:
    @allure.title('Check fixture "make_order"')
    def test_make_order(
            self, driver, registration_and_login, main_page, login_page,
            register_page, ingredient_page):
        drag_element = main_page.find_my_element(
            MainPageLocators.LNK_BUN_R2_D3_LOCATOR)
        drop_element = main_page.find_my_element(
            MainPageLocators.FLD_ADD_INGREDIENT_LOCATOR)

        ActionChains(driver).drag_and_drop(drag_element,
                                           drop_element).perform()
        main_page.click_to_element(MainPageLocators.BTN_MAKE_ORDER_LOCATOR)
        assert ingredient_page.find_my_element(
            IngredientPageLocators.FLD_ID_OF_ORDER)
