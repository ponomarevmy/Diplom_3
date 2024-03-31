import allure
from locators.main_page_locators import MainPageLocators
from locators.order_feed_locators import OrderFeedLocators
from pages.order_feed_page import OrderFeed


class TestOrderFeed:
    @allure.title('Если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_modal_box_open_after_click_to_order(self, driver):
        order_feed = OrderFeed(driver)
        order_feed.authenticate()
        order_feed.go_to_order_feed()
        order_feed.click_to_the_order()
        assert order_feed.modal_box_is_open(), "Модальное окно не появилось"

    @allure.title('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_orders_in_history_and_in_feed_are_similar(self, driver):
        order_feed = OrderFeed(driver)
        order_feed.authenticate()
        order_feed.drag_and_drop(MainPageLocators.BURGER_INGREDIENT, MainPageLocators.PLACE_FOR_ORDER)
        order_feed.make_an_order()
        order_id = order_feed.get_order_id()
        order_feed.close_modal_clickable()
        order_feed.close_modal()
        order_feed.go_to_personal_account()
        order_feed.go_to_order_history()
        is_order_id_found_at_history = order_feed.check_order_id(order_id, OrderFeedLocators.ALL_ORDERS_AT_HISTORY)
        order_feed.go_to_order_feed()
        is_order_id_found_at_feed = order_feed.check_order_id(order_id, OrderFeedLocators.ALL_ORDERS_AT_FEED)
        assert is_order_id_found_at_history and is_order_id_found_at_feed, "Заказы в истории и в ленте не совпадают"

    @allure.title('При создании нового заказа счётчик "Выполнено" за всё время увеличивается')
    def test_total_order_count_increases(self, driver):
        order_feed = OrderFeed(driver)
        order_feed.authenticate()
        order_feed.go_to_order_feed()
        old_count = order_feed.get_total_order_count()
        order_feed.go_to_constructor()
        order_feed.drag_and_drop(MainPageLocators.BURGER_INGREDIENT, MainPageLocators.PLACE_FOR_ORDER)
        order_feed.make_an_order()
        order_feed.close_modal_clickable()
        order_feed.close_modal()
        order_feed.go_to_order_feed()
        new_count = order_feed.get_total_order_count()
        assert new_count > old_count, "Количество заказов не увеличилось"

    @allure.title('При создании нового заказа счётчик "Выполнено" за сегодня увеличивается')
    def test_daily_order_count_increases(self, driver):
        order_feed = OrderFeed(driver)
        order_feed.authenticate()
        order_feed.go_to_order_feed()
        old_count = order_feed.get_daily_order_count()
        order_feed.go_to_constructor()
        order_feed.drag_and_drop(MainPageLocators.BURGER_INGREDIENT, MainPageLocators.PLACE_FOR_ORDER)
        order_feed.make_an_order()
        order_feed.close_modal_clickable()
        order_feed.close_modal()
        order_feed.go_to_order_feed()
        new_count = order_feed.get_daily_order_count()
        assert new_count > old_count, "Количество заказов в день не увеличилось"

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_after_making_an_order_id_appears_in_the_process(self, driver):
        order_feed = OrderFeed(driver)
        order_feed.authenticate()
        order_feed.go_to_constructor()
        order_feed.drag_and_drop(MainPageLocators.BURGER_INGREDIENT, MainPageLocators.PLACE_FOR_ORDER)
        order_feed.make_an_order()
        order_id = order_feed.get_order_id()
        order_feed.close_modal_clickable()
        order_feed.close_modal()
        order_feed.go_to_order_feed()
        assert order_feed.check_whether_id_order_in_the_process(order_id), "Заказ не появился в работе"
