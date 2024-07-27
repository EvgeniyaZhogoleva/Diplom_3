import allure

from data import Url, Messages
from conftest import driver, login, main_page, personal_account_page


class TestPersonalAccount:

    @allure.title('Переход по клику на страницу личного кабинета')
    def test_recovery_password_title(self, driver, main_page, personal_account_page):
        driver.get(Url.BASE_URL)
        main_page.click_to_button_personal_account()
        assert personal_account_page.check_display_title_enter, Messages.ENTER


    @allure.title('Переход в раздел «История заказов»')
    def test_go_to_order_history_section(self, login, driver, main_page, personal_account_page):
        driver = login
        main_page.click_to_button_personal_account()
        personal_account_page.click_to_button_history_order()
        assert personal_account_page.check_display_account_text, Messages.CHANGE_PERSONAL_DATA


    @allure.title('Выход из аккаунта')
    def test_logout_account(self, login, driver, main_page, personal_account_page):
        driver = login
        main_page.click_to_button_personal_account()
        personal_account_page.click_to_button_logout()
        assert personal_account_page.check_display_title_enter, Messages.ENTER








