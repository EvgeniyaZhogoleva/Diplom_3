from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # Метод для ожидания появления элемента
    def find_element_with_wait(self, locator, wait_time=20):
        return WebDriverWait(self.driver, wait_time).until(expected_conditions.visibility_of_element_located(locator))

    # Метод для ожидания исчезновения модального окна
    def disappearance_element_with_wait(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(locator))

    # Метод для нажатия на элемент
    def click_to_element(self, locator):
        self.find_element_with_wait(locator).click()

    # Метод для ввода текста
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    # Метод для получения текста
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    # Метод для скролла до элемента
    def scroll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element_with_wait(locator))

    # Метод для перетаскивания элемента
    def drag_and_drop(self, source_locator, target_locator):
        source_element = self.find_element_with_wait(source_locator)
        target_element = self.find_element_with_wait(target_locator)
        action = ActionChains(self.driver)
        action.drag_and_drop(source_element, target_element).perform()

    # Метод для проверки видимости элемента
    def is_visible(self, locator):
        result = True
        try:
            WebDriverWait(self.driver, timeout=10).until(expected_conditions.visibility_of_element_located(locator))
        except TimeoutException:
            result = False
        return result

    # Метод для получения обновлённого текста
    def get_updated_text_from_element(self, locator, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        element = wait.until(expected_conditions.visibility_of_element_located(locator))
        current_text = element.text
        wait.until(lambda driver: element.text != current_text)
        updated_text = element.text
        return updated_text

