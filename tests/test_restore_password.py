import allure


class TestRestorePassword:
    @allure.title(' Check click button "Enter account" and enter login page')
    def test_enter_login_page(self, driver, main_page):
        main_page.enter_account()
        assert main_page.success_transfer_to_login_page()

    @allure.title('Check input email and click button "Restore"')
    def test_enter_button_restore(self, driver, forgot_password_page):
        forgot_password_page.transfer_to_restore_password_page()
        assert forgot_password_page.success_transfer_to_resset_password_page()

    @allure.title('Check click button show/hide make field password active ')
    def test_button_show_password(self, driver, reset_password_page):
        reset_password_page.make_field_password_active()
        assert reset_password_page.is_success_for_show_password_button()
