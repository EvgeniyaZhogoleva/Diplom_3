import pytest
import allure

from data import Url
from data import email
from pages.recovery_password_page import ForgotPasswordPage
from pages.main_page import MainPage
from conftest import driver


class TestRecoveryPassword:

    @allure.title('Переход на страницу восстановления пароля')
    @allure.description('Тест что при нажатии на кнопку "Восстановить пароль" отображается заголовок Восстановление пароля')
    def test_recovery_password_title(self, driver):
        driver.get(Url.BASE_URL)
        main_page = MainPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        main_page.disappearance_element_wait()
        main_page.click_to_button_personal_account()
        main_page.disappearance_element_wait()
        forgot_password_page.click_to_button_recover_password()
        assert forgot_password_page.check_display_title_recover_password() == 'Восстановление пароля', 'Не отображается надпись "Восстановление пароля"'


    @allure.title('Ввод почты и кликнуть на кнопку "Восстановить"')
    @allure.description('Тест что при введении почты и нажатии кнопки "Восстановить" отображается заголовок Восстановление пароля')
    def test_add_email_and_click_to_button_recover(self, driver):
        driver.get(Url.FORGOT_PASSWORD_URL)
        forgot_password_page = ForgotPasswordPage(driver)
        main_page = MainPage(driver)
        forgot_password_page.input_email(email)
        main_page.disappearance_element_wait()
        forgot_password_page.click_to_button_recover()
        assert forgot_password_page.check_display_title_recover_password, 'Восстановление пароля'


    @allure.title('Нажать на кнопку "Отображать пароль" делает поле активным')
    @allure.description('Тест что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_to_button_show_password(self, driver):
        driver.get(Url.FORGOT_PASSWORD_URL)
        forgot_password_page = ForgotPasswordPage(driver)
        main_page = MainPage(driver)
        forgot_password_page.input_email(email)
        forgot_password_page.click_to_button_recover()
        main_page.disappearance_element_wait()
        forgot_password_page.click_to_button_show_password()
        assert forgot_password_page.is_password_field_active(), 'Поле пароля не активно'