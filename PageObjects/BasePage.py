from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator)).click()

    def scrollby(self, x, y):
        script = "window.scrollTo(" + x + "," + y + ")"
        self.driver.execute_script(script)

    def send_keys(self, locator, text):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator):
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))
        return element.text

    def get_title(self, title):
        WebDriverWait(self.driver, 15).until(EC.title_contains(title))
        return self.driver.title

    def is_visible(self, locator):
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))
        return bool(element)
