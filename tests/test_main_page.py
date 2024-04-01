import allure
from urls import Urls
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


class TestMainPage:

    @allure.title("Переход по клику на «Конструктор»")
    def test_switch_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_order_feed()
        main_page.go_to_constructor()
        main_page.url_to_be(Urls.url_main)
        assert main_page.current_url() == Urls.url_main

    @allure.title("Переход по клику на «Лента заказов»")
    def test_switch_to_order_history(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_order_feed()
        main_page.current_url()
        main_page.url_to_be(Urls.url_feed)
        assert main_page.current_url() == Urls.url_feed

    @allure.title("Если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_modal__window_after_click_to_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_ingredient()
        assert main_page.wait_details(), "Детали об ингредиенте не появились"

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_close_modal_window(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_ingredient()
        main_page.close_modal()
        assert main_page.closing_confirmation(), "Окно не закрылось по нажатию на крестик"

    @allure.title("При добавлении ингредиента в заказ счётчик этого ингридиента увеличивается")
    def test_order_registration(self, driver):
        main_page = MainPage(driver)
        main_page.drag_and_drop_for_order()
        quantity = main_page.number_of_ingredients().text
        assert quantity == '2', "Количество ингредиентов не совпадает"

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_making_an_order(self, driver):
        main_page = MainPage(driver)
        main_page.authenticate()
        main_page.drag_and_drop_for_order()
        main_page.make_an_order()
        assert main_page.confirmation_of_order(), "Заказ не сделан"
