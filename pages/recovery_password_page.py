import allure

from locators import ForgotPasswordPageLocators
from pages.base_page import BasePage

class ForgotPasswordPage(BasePage):

    @allure.step('Нажать на кнопку "Восстановить пароль"')
    def click_to_button_recover_password(self):
        self.click_to_element(ForgotPasswordPageLocators.BUTTON_RECOVER_PASSWORD)

    @allure.step('Отображение надписи "Восстановление пароля"')
    def check_display_title_recover_password(self):
        return self.get_text_from_element(ForgotPasswordPageLocators.TITLE_RECOVER_PASSWORD)

    @allure.step('Нажать на кнопку "Восстановить"')
    def click_to_button_recover(self):
        self.click_to_element(ForgotPasswordPageLocators.BUTTON_RECOVER)

    @allure.step('Ввести почту')
    def input_email(self, email):
        self.add_text_to_element(ForgotPasswordPageLocators.FORGOTTEN_EMAIL, email)

    @allure.step('Нажать на кнопку отображения пароля')
    def click_to_button_show_password(self):
        self.click_to_element(ForgotPasswordPageLocators.BUTTON_SHOW_PASSWORD)

    @allure.step('Проверить, что поле "Пароль" активно')
    def is_password_field_active(self):
        return self.is_visible(ForgotPasswordPageLocators.ACTIVE_PASSWORD_FIELD)

