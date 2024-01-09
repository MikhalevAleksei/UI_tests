import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators
from pages.profile_page import ProfilePage
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Enter account')
    def enter_account(self):
        self.find_my_element(
            MainPageLocators.BTN_ENTER_IN_ACCOUNT_LOCATOR)
        self.click_to_element(MainPageLocators.BTN_ENTER_IN_ACCOUNT_LOCATOR)

    @allure.step('Check success transfer to login page')
    def success_transfer_to_login_page(self):
        return self.find_my_element(
            LoginPageLocators.LNK_RESTORE_PASSWORD_LOCATOR)

    @allure.step('Click button "Personal area"')
    def click_btn_personal_area(self):
        self.click_to_element(MainPageLocators.BTN_PERSONAL_AREA_LOCATOR)

    @allure.step('Check success login')
    def success_login(self):
        return self.find_my_element(MainPageLocators.BTN_MAKE_ORDER_LOCATOR)

    @allure.step('Enter and exit from "Personal area"')
    def enter_and_exit_from_personal_area(self):
        self.click_btn_personal_area()
        ProfilePage.click_btn_exit()

    @allure.step('Click field "Constractor"')
    def click_fld_constructor(self):
        self.click_to_element(MainPageLocators.FLD_CONSTRACTOR_LOCATOR)

    @allure.step('Success click field "Constractor"')
    def success_click_fld_constructor(self):
        return self.find_my_element(
            MainPageLocators.FLD_ADD_INGREDIENT_LOCATOR)

    @allure.step('Click to field "List of orders"')
    def click_to_fld_list_of_orders(self):
        self.click_to_element(MainPageLocators.FLD_LIST_OF_ORDERS_LOCATOR)

    @allure.step('Success click field "List of orders"')
    def success_click_fld_list_of_orders(self):
        return self.find_my_element(
            MainPageLocators.TXT_LIST_OF_ORDERS_LOCATOR)

    @allure.step('Click to ingredient in "Constructor')
    def click_to_ingredient(self):
        self.click_to_element(MainPageLocators.LNK_BUN_R2_D3_LOCATOR)

    @allure.step('Check success transfer to pop-up window "Details of '
                 'ingredient"')
    def success_transfer_to_ingredient_details(self):
        return self.find_my_element(
            MainPageLocators.TXT_DETAILS_OF_INGREDIENT_LOCATOR)

    @allure.step('Click to close crest button  in pop-up "Details of '
                 'ingredient')
    def click_to_close_popup_details_of_igredient_btn(self):
        self.click_to_element(
            MainPageLocators.BTN_CREST_CLOSE_POPUP_DETAILS_OF_INGREDIENT_LOCATOR)

    @allure.step('Click to close crest button  in pop-up "Success of order"')
    def click_to_close_popup_success_order_btn(self):
        self.click_to_element(
            MainPageLocators.BTN_CREST_CLOSE_POPUP_SUCCESS_ORDER_LOCATOR)

    @allure.step('Check success close pop-up window "Details of '
                 'ingredient"')
    def success_close_ingredient_details_popup(self):
        return self.find_my_element(
            MainPageLocators.LNK_BUN_R2_D3_LOCATOR)

    @allure.step('Make order')
    def make_order(self):
        drag_element = self.find_my_element(
            MainPageLocators.LNK_BUN_R2_D3_LOCATOR)
        drop_element = self.find_my_element(
            MainPageLocators.FLD_ADD_INGREDIENT_LOCATOR)
        ActionChains(self.driver).drag_and_drop(drag_element,
                                                drop_element).perform()
        self.click_to_element(MainPageLocators.BTN_MAKE_ORDER_LOCATOR)

    @allure.step('Check success make order')
    def success_make_order(self):
        self.find_my_element(MainPageLocators.TXT_SUCCESS_ORDER_LOCATOR)

    @allure.step('Transfer to personal area after order')
    def transfer_to_personal_area_after_order(self):
        self.click_to_close_popup_details_of_igredient_btn()
        self.click_btn_personal_area()

    @allure.step('Make list of orders')
    def get_orders_from_list_orders(self):
        ids = self.get_text_from_elements(
            MainPageLocators.TXT_ID_OF_LIST_ORDER_LOCATOR)
        list_ids_orders = [i for i in ids]

        return list_ids_orders

    @allure.step('Check id is displayed in list and history of orders')
    def check_ids_orders_in_list_and_history(self):
        self.click_to_fld_list_of_orders()
        list_orders = self.get_orders_from_list_orders()
        self.click_btn_personal_area()
        ProfilePage.click_history_of_orders()
        history_orders = ProfilePage.get_orders_from_history_orders()
        for i in history_orders:
            if i in list_orders:
                return True
            return False

    @allure.step('Get number of orders during all time')
    def get_number_orders_during_all_time(self):
        self.click_to_fld_list_of_orders()
        sum_all = self.get_text_from_element(
            MainPageLocators.TXT_NUMBER_ORDERS_DURING_ALL_TIME_LOCATOR)
        self.click_fld_constructor()

        return sum_all

    @allure.step('Get number of orders during day')
    def get_number_orders_during_day(self):
        self.click_to_fld_list_of_orders()
        sum_day = self.get_text_from_element(
            MainPageLocators.TXT_NUMBER_ORDERS_DURING_DAY_LOCATOR)
        self.click_fld_constructor()

        return sum_day

    @allure.step('Wait until id not 9999')
    def wait_until_not_9999(self):
        text_id = self.find_my_element(
            MainPageLocators.TXT_ID_OF_NEW_ORDER_LOCATOR)
        if text_id.text == "9999":
            Wait(self.driver, 5).until_not(EC.text_to_be_present_in_element(
                text_id), "9999")
        else:
            return text_id.text

    @allure.step('Get order id')
    def get_order_id(self):
        return self.get_text_from_element(
            MainPageLocators.TXT_ID_OF_NEW_ORDER_LOCATOR)

    @allure.step('Get id of new order')
    def success_order_id_in_at_work(self):
        self.make_order()
        order_id = self.get_order_id()
        self.click_to_close_popup_success_order_btn()
        self.click_to_fld_list_of_orders()
        order_ids = self.get_text_from_elements(
            MainPageLocators.TXT_ID_OF_READY_ORDERS_LOCATOR)
        if order_id in order_ids:
            return True
        return False

    @allure.step('Get number of ingredient counter')
    def get_number_of_ingredient_counter(self):
        return self.get_text_from_element(
            MainPageLocators.TXT_COUNTER_OF_INGREDIENT_LOCATOR).text
