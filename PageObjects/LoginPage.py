from selenium.webdriver.common.by import By
from Core.Config import ConfigData
from PageObjects.BasePage import BasePage

class LoginPage(BasePage):
    emailField = (By.CSS_SELECTOR, "input#ap_email")
    continueBtn = (By.CSS_SELECTOR, "input#continue")
    passwordField = (By.CSS_SELECTOR, "input#ap_password")
    loginBtn = (By.CSS_SELECTOR, "input#signInSubmit")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(ConfigData.LoginURL)

    def login_to_amazon(self, email_id, password):
        self.send_keys(self.emailField, email_id)
        self.click(self.continueBtn)
        self.send_keys(self.passwordField, password)
        self.click(self.loginBtn)

