import allure


class TestMainFunctionality:
    @allure.title('Check transfer to "Contractor"')
    def test_transfer_to_constractor(self, driver, main_page):
        main_page.click_fld_constructor()

        assert main_page.success_click_fld_constructor()

    @allure.title('Check transfer to "List of orders"')
    def test_transfer_to_list_of_orders(self, driver, main_page):
        main_page.click_to_fld_list_of_orders()

        assert main_page.success_click_fld_list_of_orders()

    @allure.title('Check click to ingredient and pop-up window wit details')
    def test_click_ingredient(self, driver, main_page):
        main_page.click_to_ingredient()

        assert main_page.success_transfer_to_ingredient_details()

    @allure.title('Check close pop-up "Details of ingredient" by cresr button')
    def test_close_popup_details_of_ingredient(self, driver, main_page):
        main_page.click_to_close_popup_details_of_igredient_btn()

        assert main_page.success_close_ingredient_details_popup()

    @allure.title('Check ingredient count increases')
    def test_ingredient_count(self, driver, registration_and_login,
                              make_order, main_page):
        count_before = main_page.get_number_of_ingredient_counter()
        make_order()
        count_after = main_page.get_number_of_ingredient_counter()
        assert count_after > count_before

    @allure.title('Authorised user may make order')
    def test_authorised_user_order(
            self, driver, registration_and_login, make_order, main_page):
        make_order()
        assert main_page.success_make_order()
