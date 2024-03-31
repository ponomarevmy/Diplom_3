from selenium.webdriver.common.by import By


class MainPageLocators:

    BTN_ENTER_ACCOUNT = By.XPATH, "//*[text()='Войти в аккаунт']"
    BTN_PERSONAL_ACCOUNT = By.XPATH, "//p[text()='Личный Кабинет']"
    ORDER_FEED = (By.XPATH, ".//li[@class='undefined ml-2']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and contains(text(), "
                                    "'Конструктор')]")
    ONE_INGREDIENT = (By.XPATH, "(.//p[@class='BurgerIngredient_ingredient__text__yp3dH'])[1]")
    DETAILS_BUTTON = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title') and contains(text(), 'Детали')]")
    CLOSE_MODAL = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')][1]")
    CLOSE_CONFIRMATION = (By.CLASS_NAME, "Modal_modal__P3_V5")
    BURGER_INGREDIENT = (By.XPATH, ".//img[@alt='Флюоресцентная булка R2-D3']")
    PLACE_FOR_ORDER = (By.CSS_SELECTOR, ".constructor-element_pos_top .constructor-element__row")
    NUMBER_OF_INGREDIENTS = (By.XPATH,
                             ".//a[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8']//p["
                             "@class='counter_counter__num__3nue1'][1]")
    MAKE_AN_ORDER_BUTTON = (By.CLASS_NAME, "button_button__33qZ0")
    CONFIRMATION_OF_MAKING_ORDER = (By.CLASS_NAME, "Modal_modal__image__2nh17")
    PLACE_FOR_INGREDIENTS = (By.XPATH, "//span[@class='constructor-element__text' and text()='Перетяните булочку сюда (верх)']")