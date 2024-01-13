import allure


class TestMakeOrder:
    @allure.title('Check "make_order"')
    def test_make_order(
            self,  login_page, main_page, register_page):
        login_data = register_page.register_new_user()
        login_page.user_login(login_data)
        main_page.make_order()

        assert main_page.success_make_order()
