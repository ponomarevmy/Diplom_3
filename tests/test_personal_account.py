import allure
from urls import Urls
from pages.personal_account_page import PersonalAccount


class TestPersonalAccount:

    @allure.title("Переход по клику на «Личный кабинет»")
    def test_switch_to_personal_account(self, driver):
        personal_account = PersonalAccount(driver)
        personal_account.authenticate()
        personal_account.go_to_personal_account()
        personal_account.current_url()
        personal_account.url_to_be(Urls.url_personal)
        assert personal_account.current_url() == Urls.url_personal

    @allure.title("Переход в раздел «История заказов»")
    def test_switch_to_order_history(self, driver):
        personal_account = PersonalAccount(driver)
        personal_account.authenticate()
        personal_account.go_to_personal_account()
        personal_account.go_to_order_history()
        personal_account.current_url()
        personal_account.url_to_be(Urls.url_history)
        assert personal_account.current_url() == Urls.url_history

    @allure.title("Выход из аккаунта")
    def test_exit_account(self, driver):
        personal_account = PersonalAccount(driver)
        personal_account.authenticate()
        personal_account.go_to_personal_account()
        personal_account.exit_account()
        personal_account.current_url()
        personal_account.url_to_be(Urls.url_login)
        assert personal_account.current_url() == Urls.url_login
