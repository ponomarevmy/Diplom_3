import allure
from user_data import UserData
from locators.personal_account_locators import PersonalAccountLocators
from locators.password_recovery_locators import ResetPasswordLocators
from pages.base_page import BasePage


class PersonalAccount(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Переход на страницу личного кабинета")
    def go_to_personal_account(self):
        self.find_element_located_click(PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Вход в личный кабинет")
    def authenticate(self):
        self.check_element_is_clickable(ResetPasswordLocators.ENTRANCE_FROM_MAIN)
        self.find_element_located_click(ResetPasswordLocators.ENTRANCE_FROM_MAIN)
        self.check_element_is_clickable(PersonalAccountLocators.BTN_ENTER)
        self.find_element_located_click(ResetPasswordLocators.MAIL_INPUT)
        self.find_element_send_key(ResetPasswordLocators.MAIL_INPUT, UserData.USER_MAIL)
        self.find_element_located_click(PersonalAccountLocators.PASSWORD_INPUT)
        self.find_element_send_key(PersonalAccountLocators.PASSWORD_INPUT, UserData.USER_PASSWORD)
        self.find_element_located_click(PersonalAccountLocators.BTN_ENTER)
        self.check_element_is_clickable(PersonalAccountLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Переход на страницу истории заказов")
    def go_to_order_history(self):
        self.find_element_located_click(PersonalAccountLocators.ORDER_HISTORY)

    @allure.step("Выход из личного кабинета")
    def exit_account(self):
        self.find_element_located_click(PersonalAccountLocators.EXIT_BUTTON)
