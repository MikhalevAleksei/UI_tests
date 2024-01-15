import allure


class TestPersonalArea:
    @allure.title('Check transfer by click button "Personal area"')
    def test_click_btn_personal_area(self,
                                     main_page, login_page):
        login_page.set_login_password()
        assert main_page.success_login(), 'Login was not successful.'

    @allure.title('Check transfer to section "History of orders"')
    def test_transfer_to_history_of_orders(
            self, order_history_page, main_page, login_page,
            register_page, profile_page):
        main_page.enter_account()
        login_page.click_registration_link()
        login_data = register_page.register_new_user()
        login_page.user_login(login_data)
        main_page.make_order_and_close_success_popup()
        main_page.click_btn_personal_area()
        profile_page.click_history_of_orders()

        assert order_history_page.success_transfer_order_history()

    @allure.title('Check exit from account')
    def test_exit_from_account(
            self, main_page, profile_page,
            login_page, register_page):
        main_page.enter_account()
        login_page.click_registration_link()
        login_data = register_page.register_new_user()
        login_page.user_login(login_data)
        main_page.click_btn_personal_area()
        profile_page.click_btn_exit()

        assert login_page.success_exit_from_account()
