import allure
from pages.order_feed_page import OrderFeed
from pages.password_recovery_page import ResetPassword
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccount


class TestOrderFeed:
    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_modal_box_open_after_click_to_order(self, driver):
        order_feed = OrderFeed(driver)
        main_page = MainPage(driver)
        reset_password = ResetPassword(driver)
        reset_password.authenticate()
        main_page.go_to_order_feed()
        order_feed.click_to_the_order()
        assert order_feed.modal_box_is_open(), "Модальное окно не появилось"

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_orders_in_history_and_in_feed_are_similar(self, driver):
        order_feed = OrderFeed(driver)
        reset_password = ResetPassword(driver)
        main_page = MainPage(driver)
        personal_account = PersonalAccount(driver)
        reset_password.authenticate()
        main_page.drag_and_drop_for_order()
        main_page.make_an_order()
        main_page.close_modal_clickable()
        main_page.close_modal()
        personal_account.go_to_personal_account()
        personal_account.go_to_order_history()
        is_order_id_found_at_history = order_feed.is_order_id_found_at_history()
        main_page.go_to_order_feed()
        is_order_id_found_at_feed = order_feed.is_order_id_found_at_feed()
        assert is_order_id_found_at_history and is_order_id_found_at_feed, "Заказы в истории и в ленте не совпадают"

    @allure.title('При создании нового заказа счётчик "Выполнено" за всё время увеличивается')
    def test_total_order_count_increases(self, driver):
        order_feed = OrderFeed(driver)
        main_page = MainPage(driver)
        reset_password = ResetPassword(driver)
        reset_password.authenticate()
        main_page.go_to_order_feed()
        old_count = order_feed.get_total_order_count()
        main_page.go_to_constructor()
        main_page.drag_and_drop_for_order()
        main_page.make_an_order()
        main_page.close_modal_clickable()
        main_page.close_modal()
        main_page.go_to_order_feed()
        new_count = order_feed.get_total_order_count()
        assert new_count > old_count, "Количество заказов не увеличилось"

    @allure.title('При создании нового заказа счётчик "Выполнено" за сегодня увеличивается')
    def test_daily_order_count_increases(self, driver):
        order_feed = OrderFeed(driver)
        reset_password = ResetPassword(driver)
        main_page = MainPage(driver)
        reset_password.authenticate()
        main_page.go_to_order_feed()
        old_count = order_feed.get_daily_order_count()
        main_page.go_to_constructor()
        main_page.drag_and_drop_for_order()
        main_page.make_an_order()
        main_page.close_modal_clickable()
        main_page.close_modal()
        main_page.go_to_order_feed()
        new_count = order_feed.get_daily_order_count()
        assert new_count > old_count, "Количество заказов в день не увеличилось"

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_after_making_an_order_id_appears_in_the_process(self, driver):
        order_feed = OrderFeed(driver)
        reset_password = ResetPassword(driver)
        main_page = MainPage(driver)
        reset_password.authenticate()
        main_page.go_to_constructor()
        main_page.drag_and_drop_for_order()
        main_page.make_an_order()
        order_id = order_feed.get_order_id()
        main_page.close_modal_clickable()
        main_page.close_modal()
        main_page.go_to_order_feed()
        assert order_feed.check_whether_id_order_in_the_process(order_id), "Заказ не появился в работе"
