import allure


class TestMakeOrder:
    @allure.title('Check "make_order"')
    def test_make_order(
            self, driver, login_page, main_page):
        login_page.registration_and_login()
        main_page.make_order()

        assert main_page.success_make_order()
