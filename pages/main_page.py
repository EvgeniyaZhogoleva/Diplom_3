import allure

from locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):

    @allure.step ('Метод для ожидания исчезновения модального окна')
    def disappearance_element_wait(self):
        self.disappearance_element_with_wait(MainPageLocators.SCREENSAVER)

    @allure.step('Нажать на кнопку "Личный кабинет"')
    def click_to_button_personal_account(self):
        self.find_element_with_wait(MainPageLocators.BUTTON_PERSONAL_ACCOUNT, wait_time=11)
        self.click_to_element(MainPageLocators.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Нажать на кнопку "Конструктор"')
    def click_to_button_constructor(self):
        self.find_element_with_wait(MainPageLocators.BUTTON_CONSTRUCTOR, wait_time=13)
        self.click_to_element(MainPageLocators.BUTTON_CONSTRUCTOR)

    @allure.step('Нажать на кнопку "Лента заказов"')
    def click_to_button_order_history(self):
        self.find_element_with_wait(MainPageLocators.BUTTON_ORDER_FEED, wait_time=11)
        self.click_to_element(MainPageLocators.BUTTON_ORDER_FEED)

    @allure.step('Нажать на кнопку "Войти в аккаунт"')
    def click_to_button_login(self):
        self.click_to_element(MainPageLocators.BUTTON_LOG_IN_ACCOUNT)

    @allure.step('Нажать на кнопку "Оформить заказ"')
    def click_to_button_order(self):
        self.find_element_with_wait(MainPageLocators.BUTTON_ORDER, wait_time=7)
        self.click_to_element(MainPageLocators.BUTTON_ORDER)

    @allure.step('Отображается надпись "Личный кабинет"')
    def check_display_personal_account(self):
        self.find_element_with_wait(MainPageLocators.BUTTON_PERSONAL_ACCOUNT)
        return self.is_visible(MainPageLocators.BUTTON_PERSONAL_ACCOUNT)

    @allure.step('Отображается ингридиент "Булка"')
    def check_display_bun(self):
        return self.is_visible(MainPageLocators.BUN_LIST)









