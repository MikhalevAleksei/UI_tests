import allure


class TestListOfOrders:
    @allure.title('Check click on order and open pop-up "Details of order"')
    def test_click_order_and_check_popup(self,  main_page,
                                         login_page, register_page,
                                         profile_page,
                                         order_history_page):
        main_page.enter_account()
        login_page.click_registration_link()
        login_data = register_page.register_new_user()
        login_page.user_login(login_data)
        main_page.make_order_and_close_success_popup()
        main_page.transfer_to_personal_area_after_order()
        profile_page.click_history_of_orders()
        order_history_page.click_order_to_open_popup()

        assert order_history_page.success_open_popup_order_details()

    @allure.title(
        'Orders from "History of orders" are displayed in "List of orders"')
    def test_displayed_in_history_and_list_of_orders(self,
                                                     login_page,
                                                     make_order,
                                                     main_page,
                                                     profile_page,
                                                     register_page,
                                                     order_history_page):
        main_page.enter_account()
        login_page.click_registration_link()
        login_data = register_page.register_new_user()
        login_page.user_login(login_data)
        main_page.make_order_and_close_success_popup()
        main_page.click_btn_personal_area()
        profile_page.click_history_of_orders()
        list_of_orders = main_page.check_ids_orders_in_list()

        assert order_history_page.check_ids_orders_in_history(list_of_orders)

    @allure.title(
        'Check number of orders during all time is increased after new order')
    def test_sum_orders_for_all_time_increases(self,
                                               login_page,
                                               main_page,
                                               register_page):
        main_page.enter_account()
        login_page.click_registration_link()
        login_data = register_page.register_new_user()
        login_page.user_login(login_data)
        num_before = main_page.get_number_orders_during_all_time()
        main_page.make_order_and_close_success_popup()
        num_after = main_page.get_number_orders_during_all_time()

        assert num_after - num_before == 1

    @allure.title(
        'Check number of orders during day is increased after new order')
    def test_sum_orders_for_day_increases(self,
                                          login_page,
                                          make_order, main_page,
                                          register_page):
        main_page.enter_account()
        login_page.click_registration_link()
        login_data = register_page.register_new_user()
        login_page.user_login(login_data)
        num_before = main_page.get_number_orders_during_all_time()
        main_page.make_order_and_close_success_popup()
        num_after = main_page.get_number_orders_during_all_time()

        assert num_after - num_before == 1

    @allure.title('Check id of new order appear in section "At work"')
    def test_order_id_in_at_work(self,
                                 login_page,
                                 main_page,
                                 register_page):
        main_page.enter_account()
        login_page.click_registration_link()
        login_data = register_page.register_new_user()
        login_page.user_login(login_data)
        main_page.click_to_fld_list_of_orders()

        assert main_page.success_order_id_in_at_work()
