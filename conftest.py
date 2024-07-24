import pytest
from selenium import webdriver
from data import Url, email, password
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage

@pytest.fixture(params=["chrome", "firefox"], scope="class")
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    driver.get(Url.BASE_URL)
    main_page = MainPage(driver)
    main_page.click_to_button_personal_account()
    personal_account_page = PersonalAccountPage(driver)
    personal_account_page.input_email(email)
    personal_account_page.input_password(password)
    personal_account_page.click_to_button_in()
    return driver


