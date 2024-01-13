import allure


class TestMainFunctionality:
    @allure.title('Check transfer to "Contractor"')
    def test_transfer_to_constractor(self, main_page):
        main_page.click_fld_constructor()

        assert main_page.success_click_fld_constructor()

    @allure.title('Check transfer to "List of orders"')
    def test_transfer_to_list_of_orders(self, main_page):
        main_page.click_to_fld_list_of_orders()

        assert main_page.success_click_fld_list_of_orders()

    @allure.title('Check click to ingredient and pop-up window wit details')
    def test_click_ingredient(self, main_page):
        main_page.click_to_ingredient()

        assert main_page.success_transfer_to_ingredient_details()

    @allure.title('Check close pop-up "Details of ingredient" by cresr button')
    def test_close_popup_details_of_ingredient(self, main_page):
        main_page.click_to_close_popup_details_of_igredient_btn()

        assert main_page.success_close_ingredient_details_popup()

    @allure.title('Check ingredient count increases')
    def test_ingredient_count(
            self, login_page, main_page, register_page):
        main_page.enter_account()
        login_page.click_registration_link()
        login_data = register_page.register_new_user()
        login_page.user_login(login_data)
        count_before = main_page.get_number_of_ingredient_counter()
        main_page.make_order_and_close_success_popup()
        count_after = main_page.get_number_of_ingredient_counter()
        assert count_after > count_before

    @allure.title('Authorised user may make order')
    def test_authorised_user_order(
            self, login_page, make_order, main_page, register_page):
        main_page.enter_account()
        login_page.click_registration_link()
        login_data = register_page.register_new_user()
        login_page.user_login(login_data)
        assert main_page.success_make_order()
