import allure


class TestPersonalArea:
    @allure.title('Check transfer by click button "Personal area"')
    def test_click_btn_personal_area(self, driver,
                                     main_page, registration_and_login):
        assert main_page.success_login(), 'Login was not successful.'

    @allure.title('Check transfer to section "History of orders"')
    def test_transfer_to_history_of_orders(
            self, driver, order_history_page, registration_and_login,
            make_order):
        make_order()
        assert order_history_page.success_transfer_order_history()

    @allure.title('Check exit from account')
    def test_exit_from_account(
            self, driver, registration_and_login, main_page, profile_page,
            login_page):
        main_page.click_btn_personal_area()
        profile_page.click_btn_exit()

        assert login_page.success_exit_from_account()
