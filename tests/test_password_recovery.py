import allure
from urls import Urls
from user_data import UserData
from locators.password_recovery_locators import ResetPasswordLocators
from pages.password_recovery_page import ResetPassword


class TestResetPassword:
    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль")
    def test_page_recovery_password(self, driver):
        password_recovery = ResetPassword(driver)
        password_recovery.go_to_reset_password_page()
        password_recovery.current_url()
        assert password_recovery.current_url() == Urls.url_restore

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_reset_password(self, driver):
        password_recovery = ResetPassword(driver)
        password_recovery.go_to_reset_password_page()
        password_recovery.reset_confirmation()
        password_recovery.current_url()
        assert password_recovery.current_url() == Urls.url_reset

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_password_visibility(self, driver):
        password_recovery = ResetPassword(driver)
        password_recovery.go_to_reset_password_page()
        password_recovery.reset_confirmation()
        password_recovery.find_element_send_key(ResetPasswordLocators.PASSWORD_INPUT_IN_RESET_PAGE, UserData.USER_PASSWORD)
        password_recovery.check_element_is_clickable(ResetPasswordLocators.EYE_BUTTON)
        password_recovery.find_element_located_click(ResetPasswordLocators.EYE_BUTTON)
        assert password_recovery.find_element_located(ResetPasswordLocators.PASSWORD_VISIBLE)
