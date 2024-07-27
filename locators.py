from selenium.webdriver.common.by import By

class MainPageLocators:
    SCREENSAVER = (By.CSS_SELECTOR, "div.Modal_modal_overlay__x2ZCr") # заставка круги
    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, '//p[text()="Личный Кабинет"]')  # кнопка "Личный кабинет"
    BUTTON_CONSTRUCTOR = (By.XPATH, '//p[text()="Конструктор"]')  # кнопка "Конструктор"
    BUTTON_ORDER_FEED = (By.XPATH, '//p[text()="Лента Заказов"]') # кнопка "Лента заказов"
    BUTTON_LOG_IN_ACCOUNT = (By.XPATH, '//button[text()="Войти в аккаунт"]')  # кнопка "Войти в аккаунт"
    BUTTON_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]')  # кнопка "Оформить заказ" на главной странице
    BUN_LIST = (By.XPATH, '//h2[contains(text(),"Булки")]')


class ForgotPasswordPageLocators:
    BUTTON_RECOVER_PASSWORD = (By.XPATH, "//a[@href='/forgot-password']")  # кнопка "Восстановить пароль"
    FORGOTTEN_EMAIL = (By.CSS_SELECTOR, 'input.text.input__textfield.text_type_main-default[name=\'name\']') # поле "Email"
    BUTTON_RECOVER = (By.XPATH, '//button[text()="Восстановить"]') # кнопка "Восстановить"
    BUTTON_SHOW_PASSWORD = (By.CSS_SELECTOR, '.input__icon-action > svg') # кнопка "Показать пароль"
    ACTIVE_PASSWORD_FIELD = (By.XPATH, '//label[contains(@class,"input__placeholder-focused")]') # активное поле "Пароль"
    TITLE_RECOVER_PASSWORD = (By.XPATH, '//h2[text()="Восстановление пароля"]') # надпись "Восстановление пароля"

class PersonalAccountLocators:
    FIELD_EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input[@type='text']")  # поле Почта
    FIELD_PASSWORD = (By.NAME, "Пароль")  # поле Пароль
    BUTTON_IN = (By.XPATH, '//button[text()="Войти"]')  # кнопка "Войти"
    BUTTON_HISTORY_ORDER = (By.XPATH, '//a[text()="История заказов"]') # кнопка "История заказов"
    BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']")  # кнопка "Выйти" в личном кабинете
    TITLE_ENTER = (By.XPATH, "//h2[text()='Вход']")  # надпись "Вход"
    ACCOUNT_TEXT = (By.CSS_SELECTOR, "p.Account_text__fZAIn.text.text_type_main-default") # надпись "В этом разделе вы можете изменить свои персональные данные"

class OrderLocators:
    TITLE_BURGER = (By.XPATH, "//h1[text()='Соберите бургер']")  # надпись "Соберите бургер"
    TITLE_ORDER = (By.XPATH, '//h1[text()="Лента заказов"]') # надпись "Лента заказов"
    FLUORESCEN_BUN = (By.CSS_SELECTOR, "p.BurgerIngredient_ingredient__text__yp3dH") # кнопка "Флюоресцентная булка"
    TITLE_INGREDIENTS_DETAILS = (By.XPATH, '//h2[text()="Детали ингредиента"]') # надпись "Детали ингредиента"
    BUTTON_CLOSE_INGREDIENT_DETAILS = (By.CSS_SELECTOR, "button.Modal_modal__close_modified__3V5XS") # кнопка закрытия всплывающего окна
    BURGER_BASKET = (By.XPATH, '//section[@class="BurgerConstructor_basket__29Cd7 mt-25 "]') #корзина заказа
    COUNTER_OF_FLUORESCENT_BUN = (By.XPATH, '//ul[@class="BurgerIngredients_ingredients__list__2A-mT"][1]/child::'
                                            'a[1]//p[@class="counter_counter__num__3nue1"]') #счетчик количества булки
    ORDER_IDENTIFIER = (By.XPATH,"//p[text()='идентификатор заказа']") # надпись "идентификатор заказа"
    LAST_ORDER = (By.XPATH, '//a[contains(@href,"/feed/")][1]') # последний заказ
    POPUP_ORDER_DETAILS = (By.XPATH, '//section[contains(@class,"Modal_modal_opened__3ISw4 Modal_modal__P3_V5")]') # всплывающее окно заказа
    ORDER_NUMBER = (By.XPATH, '//div[contains(@class, "pt-30")]/child::h2') # номер заказа
    NUMBER_LAST_ORDER = (By.XPATH, '//li[last()]/a[contains(@href, "order-history")]/*/p[1]') # последний заказ
    NUMBER_ORDER_FEED_LIST = (By.XPATH, '//ul[contains(@class,"OrderFeed_list")]//p[contains(text(),"#")]') # номер заказа в ленте заказов
    ORDER_ALL_TIME = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::'
                                'p[contains(@class,"OrderFeed_number")]') # счетчик заказов за все время
    ORDER_FOR_TODAY = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class,"OrderFeed_number")]') # счетчик заказов за сегодня
    NUMBER_ORDER_AT_WORK = (By.XPATH, '//ul[contains(@class,"orderListReady")]/li[contains(@class,"mb-2")]') # номер заказа "В работе"














