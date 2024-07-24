import allure

from locators import OrderLocators, MainPageLocators
from pages.base_page import BasePage
from pages.main_page import MainPage


class OrderPage(BasePage):

    @allure.step('Отображение надписи "Соберите бургер"')
    def check_display_title_burger(self):
        return self.get_text_from_element(OrderLocators.TITLE_BURGER)

    @allure.step('Отображение надписи "Лента заказов"')
    def check_display_title_order(self):
        return self.get_text_from_element(OrderLocators.TITLE_ORDER)

    @allure.step('Нажать на  ингредиент "Флюоресцентная булка"')
    def click_to_ingredient_fluorescent_bun(self):
        self.click_to_element(OrderLocators.FLUORESCEN_BUN)

    @allure.step('Отображение надписи "Детали ингредиента"')
    def check_display_title_ingredients_details(self):
        return self.get_text_from_element(OrderLocators.TITLE_INGREDIENTS_DETAILS)

    @allure.step('Закрыть всплывающее окно "Детали ингредиента"')
    def close_ingredient_details_popup(self):
        self.click_to_element(OrderLocators.BUTTON_CLOSE_INGREDIENT_DETAILS)

    @allure.step('Перетаскивание ингредиента в правую часть экрана')
    def drag_and_drop_fluorescent_bun_in_basket(self):
        self.driver.implicitly_wait(3)
        self.drag_and_drop(OrderLocators.FLUORESCEN_BUN, OrderLocators.BURGER_BASKET)

    @allure.step('Показать счётчик ингредиента из булок')
    def get_count_ingredient(self):
        return self.get_text_from_element(OrderLocators.COUNTER_OF_FLUORESCENT_BUN)

    @allure.step('Отображение надписи "Идентификатор заказа"')
    def check_display_title_order_id(self):
        return self.get_text_from_element(OrderLocators.ORDER_IDENTIFIER)

    @allure.step('Нажать на последний заказ')
    def click_to_last_order(self):
        return self.click_to_element(OrderLocators.LAST_ORDER)

    @allure.step('Получить детали заказа')
    def get_order_details(self):
        return self.find_element_with_wait(OrderLocators.POPUP_ORDER_DETAILS)

    @allure.step('Нажать на кнопку "Оформить заказ"')
    def click_to_button_order(self):
        self.click_to_element(MainPageLocators.BUTTON_ORDER)

    @allure.step('Получить номер заказа')
    def get_order_number(self):
        return self.get_updated_text_from_element(OrderLocators.ORDER_NUMBER, 5)

    @allure.step('Закрыть всплывающее окно с номером заказа')
    def close_order_number_popup(self):
        self.click_to_element(OrderLocators.BUTTON_CLOSE_INGREDIENT_DETAILS)

    @allure.step('Создание заказа')
    def create_order(self):
        self.drag_and_drop_fluorescent_bun_in_basket()
        self.click_to_button_order()
        order_number = self.get_order_number()
        self.close_order_number_popup()
        return order_number

    @allure.step('Получить номер последнего заказа')
    def get_number_last_order(self):
        return self.get_text_from_element(OrderLocators.NUMBER_LAST_ORDER)

    @allure.step('Получить номер заказов в ленте заказов')
    def get_number_order_feed_list(self):
        return self.get_text_from_element(OrderLocators.NUMBER_ORDER_FEED_LIST)

    @allure.step('Получить количество выполненных заказов за всё время')
    def get_all_time_orders(self):
        return self.get_text_from_element(OrderLocators.ORDER_ALL_TIME)

    @allure.step('Получить количество выполненных заказов за сегодня')
    def get_for_today_orders(self):
        return self.get_text_from_element(OrderLocators.ORDER_FOR_TODAY)

    @allure.step('Получить номер заказа, когда он появится "В работе"')
    def get_updated_order_number_in_list_at_work(self):
        self.find_element_with_wait(OrderLocators.NUMBER_ORDER_AT_WORK)
        return self.get_text_from_element(OrderLocators.NUMBER_ORDER_AT_WORK)







