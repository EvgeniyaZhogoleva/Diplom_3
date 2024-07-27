import allure

from data import Url, Messages
from conftest import driver, login, main_page, order_page


class TestMainFunctionality:

    @allure.title('Переход по клику на "Конструктор"')
    @allure.description('Тест на переход по клику на "Конструктор" с главного экрана')
    def test_open_constructor(self, driver, main_page, order_page):
        driver.get(Url.BASE_URL)
        main_page.click_to_button_constructor()
        assert order_page.check_display_title_burger() == Messages.MAKE_BURGER, 'Заголовок не соответствует ожидаемому'


    @allure.title('Переход по клику на "Лента заказов"')
    @allure.description('Тест на переход по клику на "Лента заказов" с главного экрана')
    def test_open_order_history(self, driver, main_page, order_page):
        driver.get(Url.BASE_URL)
        main_page.click_to_button_order_history()
        assert order_page.check_display_title_burger, Messages.ORDER_FEED


    @allure.title('При клике на ингридиент, появляется всплывающее окно с деталями')
    def test_window_with_details(self, driver, main_page, order_page):
        driver.get(Url.BASE_URL)
        main_page.disappearance_element_wait()
        main_page.click_to_button_constructor()
        order_page.click_to_ingredient_fluorescent_bun()
        assert order_page.check_display_title_ingredients_details, Messages.DETAIL_INGREDIENT


    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_close_popup_window(self, driver, main_page, order_page):
        driver.get(Url.BASE_URL)
        main_page.click_to_button_constructor()
        order_page.click_to_ingredient_fluorescent_bun()
        order_page.close_ingredient_details_popup()
        assert order_page.check_display_title_burger, Messages.MAKE_BURGER


    @allure.title('При добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_counter_ingredient(self, driver, main_page, order_page):
        driver.get(Url.BASE_URL)
        main_page.click_to_button_constructor()
        order_page.drag_and_drop_fluorescent_bun_in_basket()
        assert order_page.get_count_ingredient() == '2'


    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_login_user_order(self, login, driver, main_page, order_page):
        driver = login
        main_page.click_to_button_order()
        assert order_page.check_display_title_order_id, Messages.ID










