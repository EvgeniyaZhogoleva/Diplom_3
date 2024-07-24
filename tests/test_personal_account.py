import allure

from data import Url, email, password
from pages.personal_account_page import PersonalAccountPage
from pages.main_page import MainPage
from conftest import driver, login


class TestPersonalAccount:

    @allure.title('Переход по клику на страницу личного кабинета')
    def test_recovery_password_title(self, driver):
        driver.get(Url.BASE_URL)
        main_page = MainPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        main_page.disappearance_element_wait()
        main_page.click_to_button_personal_account()
        assert personal_account_page.check_display_title_enter, 'Вход'


    @allure.title('Переход в раздел «История заказов»')
    def test_go_to_order_history_section(self, login, driver):
        driver = login
        main_page = MainPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        main_page.click_to_button_personal_account()
        personal_account_page.click_to_button_history_order()
        assert personal_account_page.check_display_account_text, 'В этом разделе вы можете изменить свои персональные данные'


    @allure.title('Выход из аккаунта') # я не понимаю почему, когда запускаешь полностью, этот тест не работает, потому что когда отдельно все работает
    def test_logout_account(self, login, driver):
        driver = login
        main_page = MainPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        main_page.click_to_button_personal_account()
        personal_account_page.click_to_button_logout()
        assert personal_account_page.check_display_title_enter, 'Вход'








