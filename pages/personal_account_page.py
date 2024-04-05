import allure
from locators.personal_account_locators import PersonalAccountLocators
from pages.base_page import BasePage


class PersonalAccount(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Переход на страницу личного кабинета")
    def go_to_personal_account(self):
        self.find_element_located_click(PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Вход в личный кабинет")
    @allure.step("Переход на страницу истории заказов")
    def go_to_order_history(self):
        self.find_element_located_click(PersonalAccountLocators.ORDER_HISTORY)

    @allure.step("Выход из личного кабинета")
    def exit_account(self):
        self.find_element_located_click(PersonalAccountLocators.EXIT_BUTTON)