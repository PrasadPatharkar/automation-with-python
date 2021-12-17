from Core.Config import ConfigData
from Tests.test_Base import BaseTest
from PageObjects.LoginPage import LoginPage


class Test_LoginPage(BaseTest):
    title = "Amazon"

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.login_to_amazon(ConfigData.USERNAME, ConfigData.PASSWORD)
        actual_title = self.loginPage.get_title(self.title)
        assert self.title in actual_title
