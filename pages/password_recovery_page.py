import allure
from locators.personal_account_locators import PersonalAccountLocators
from urls import Urls
from user_data import UserData
from locators.password_recovery_locators import ResetPasswordLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class ResetPassword(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step("Переход на страницу восстановления пароля")
    def go_to_reset_password_page(self):
        self.check_element_is_clickable(MainPageLocators.BTN_ENTER_ACCOUNT)
        self.click_on_element(MainPageLocators.BTN_ENTER_ACCOUNT)
        self.check_element_is_clickable(ResetPasswordLocators.REF_RESTORE_PASSWORD)
        self.click_on_element(ResetPasswordLocators.REF_RESTORE_PASSWORD)

    @allure.step("Подтверждение восстановления пароля")
    def reset_confirmation(self):
        self.check_element_is_clickable(ResetPasswordLocators.MAIL_INPUT)
        self.find_element_located_click(ResetPasswordLocators.MAIL_INPUT)
        self.find_element_send_key(ResetPasswordLocators.MAIL_INPUT, UserData.USER_MAIL)
        self.find_element_located_click(ResetPasswordLocators.CONFIRMATION_BUTTON)
        self.url_to_be(Urls.url_reset)

    @allure.step("Авторизация")
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