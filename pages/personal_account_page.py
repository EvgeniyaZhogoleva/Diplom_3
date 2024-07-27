import allure

from locators import PersonalAccountLocators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):

    @allure.step('Отображение надписи "Вход"')
    def check_display_title_enter(self):
        return self.get_text_from_element(PersonalAccountLocators.TITLE_ENTER)

    @allure.step('Ввести почту')
    def input_email(self, email):
        self.find_element_with_wait(PersonalAccountLocators.FIELD_EMAIL, wait_time=10)
        self.add_text_to_element(PersonalAccountLocators.FIELD_EMAIL, email)

    @allure.step('Ввести пароль')
    def input_password(self, password):
        self.add_text_to_element(PersonalAccountLocators.FIELD_PASSWORD, password)

    @allure.step('Нажать на кнопку "Войти"')
    def click_to_button_in(self):
        self.find_element_with_wait(PersonalAccountLocators.BUTTON_IN)
        self.click_to_element(PersonalAccountLocators.BUTTON_IN)

    @allure.step('Нажать на кнопку "История заказов"')
    def click_to_button_history_order(self):
        self.find_element_with_wait(PersonalAccountLocators.BUTTON_HISTORY_ORDER, wait_time=10)
        self.click_to_element(PersonalAccountLocators.BUTTON_HISTORY_ORDER)

    @allure.step('Отображение надписи "В этом разделе вы можете изменить свои персональные данные"')
    def check_display_account_text(self):
        return self.get_text_from_element(PersonalAccountLocators.ACCOUNT_TEXT)

    @allure.step('Нажать на кнопку "Выход"')
    def click_to_button_logout(self):
        self.click_to_element(PersonalAccountLocators.BUTTON_LOGOUT)
