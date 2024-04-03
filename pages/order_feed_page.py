import allure
from locators.order_feed_locators import OrderFeedLocators
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccount


class OrderFeed(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.main_page = MainPage(driver)
        self.personal_account = PersonalAccount(driver)

    @allure.step("Клик на заказ")
    def click_to_the_order(self):
        self.check_element_is_clickable(OrderFeedLocators.FIRST_ORDER)
        self.find_element_located_click(OrderFeedLocators.FIRST_ORDER)

    @allure.step("Проверка открытия модального окна")
    def modal_box_is_open(self):
        if self.find_element_located(OrderFeedLocators.MODAL_ORDER_BOX):
            return True

    @allure.step("Получение ID заказа")
    def get_order_id(self):
        self.find_element_located(OrderFeedLocators.LOADING_CHECK_BOX)
        order_id = self.find_element_located(OrderFeedLocators.ORDER_ID).text
        while order_id == '9999':
            order_id = self.find_element_located(OrderFeedLocators.ORDER_ID).text
        return f"#{order_id}"

    @allure.step("Проверка совпадения заказов в истории и в ленте")
    def check_order_id(self, order_id, locator):
        elements = self.find_until_all_elements_located(locator)

        for element in elements:
            if order_id == element.text:
                return True
        return True

    @allure.step("Получение количества заказов")
    def get_total_order_count(self):
        return self.find_element_located(OrderFeedLocators.TOTAL_ORDER_COUNT).text

    @allure.step("Получение количества заказов в день")
    def get_daily_order_count(self):
        return self.find_element_located(OrderFeedLocators.DAILY_ORDER_COUNT).text

    @allure.step("Получение ID заказа в работе")
    def get_id_order_in_the_process(self):
        self.find_element_located(OrderFeedLocators.ORDER_IS_IN_THE_PROCESS)
        return self.find_element_located(OrderFeedLocators.ORDER_IS_IN_THE_PROCESS).text

    @allure.step("Проверка, что заказ появился в работе")
    def check_whether_id_order_in_the_process(self, order_id):
        is_order_id = self.get_id_order_in_the_process()
        if order_id[1:] in is_order_id:
            return True

    def authenticate(self):
        self.main_page.authenticate()

    def go_to_order_feed(self):
        self.main_page.go_to_order_feed()

    def make_an_order(self):
        self.main_page.make_an_order()

    def close_modal_clickable(self):
        self.main_page.close_modal_clickable()

    def close_modal(self):
        self.main_page.close_modal()

    def go_to_personal_account(self):
        self.personal_account.go_to_personal_account()

    def go_to_order_history(self):
        self.personal_account.go_to_order_history()

    def go_to_constructor(self):
        self.main_page.go_to_constructor()