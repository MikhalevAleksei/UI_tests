import allure


class TestListOfOrders:
    @allure.title('Check click on order and open pop-up "Details of order"')
    def test_click_order_and_check_popup(self, driver,
                                         login_page,
                                         make_order_and_transfer_to_history_orders,
                                         order_history_page):
        login_page.registration_and_login()
        order_history_page.click_order_for_popup()

        assert order_history_page.success_open_popup_order_details()

    @allure.title(
        'Orders from "History of orders" are displayed in "List of orders"')
    def test_displayed_in_history_and_list_of_orders(self, driver,
                                                     login_page,
                                                     make_order,
                                                     main_page,
                                                     profile_page):
        login_page.registration_and_login()
        list_of_orders = main_page.check_ids_orders_in_list()

        assert profile_page.check_ids_orders_in_history(list_of_orders)

    @allure.title(
        'Check number of orders during all time is increased after new order')
    def test_sum_orders_for_all_time_increases(self, driver,
                                               login_page,
                                               main_page):
        login_page.registration_and_login()
        num_before = main_page.get_number_orders_during_all_time()
        main_page.make_order_and_close_success_popup()
        num_after = main_page.get_number_orders_during_all_time()

        assert num_after - num_before == 1

    @allure.title(
        'Check number of orders during day is increased after new order')
    def test_sum_orders_for_day_increases(self, driver,
                                          login_page,
                                          make_order, main_page):
        login_page.registration_and_login()
        num_before = main_page.get_number_orders_during_all_time()
        main_page.make_order_and_close_success_popup()
        num_after = main_page.get_number_orders_during_all_time()

        assert num_after - num_before == 1

    @allure.title('Check id of new order appear in section "At work"')
    def test_order_id_in_at_work(self, driver,
                                 login_page,
                                 main_page):
        login_page.registration_and_login()
        assert main_page.success_order_id_in_at_work()
