import allure

from data import Url
from conftest import driver, login, main_page, order_page, personal_account_page

class TestOrderFeed:

    @allure.title('При клике на заказ, открывается всплывающее окно с деталями')
    def test_open_order_details_popup(self, driver, order_page):
        driver.get(Url.FEED_URL)
        order_page.click_to_last_order()
        assert order_page.get_order_details()


    @allure.title('Заказы пользователя из раздела "История заказов" отображаются на странице "Лента заказов"')
    def test_user_order_in_order_feed(self, login, driver, main_page, order_page, personal_account_page):
        driver = login
        order_page.create_order()
        main_page.click_to_button_personal_account()
        personal_account_page.click_to_button_history_order()
        number_last_order = order_page.get_number_last_order()
        main_page.click_to_button_order_history()
        assert number_last_order in order_page.get_number_order_feed_list()


    @allure.title('При создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_counter_all_time_increases(self, login, driver, main_page, order_page):
        driver = login
        main_page.click_to_button_order_history()
        counter_all_time = order_page.get_all_time_orders()
        main_page.click_to_button_constructor()
        order_page.create_order()
        main_page.click_to_button_order_history()
        counter_all_time_new = order_page.get_all_time_orders()
        assert counter_all_time_new > counter_all_time


    @allure.title('При создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_counter_for_today_increases(self, login, driver, main_page, order_page):
        driver = login
        main_page.click_to_button_order_history()
        counter_for_today = order_page.get_for_today_orders()
        main_page.click_to_button_constructor()
        order_page.create_order()
        main_page.click_to_button_order_history()
        counter_for_today_new = order_page.get_for_today_orders()
        assert counter_for_today_new > counter_for_today


    @allure.title('После оформления заказа его номер появляется в разделе "В работе"')
    def test_order_number_in_work(self, login, driver, main_page, order_page):
        driver = login
        number_order = order_page.create_order()
        main_page.click_to_button_order_history()
        numbers_order_at_work = order_page.get_updated_order_number_in_list_at_work()
        assert number_order in numbers_order_at_work







