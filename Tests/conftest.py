import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from Core.Config import ConfigData


@pytest.fixture(params=['chrome'], scope='class')
def init_driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif request.param == 'firefox':
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.delete_all_cookies()
    driver.maximize_window()
    driver.implicitly_wait(ConfigData.IMPLICITLY_WAIT_TIMEOUT)
    driver.set_page_load_timeout(ConfigData.PAGE_LOAD_TIMEOUT)
    request.cls.driver = driver
    yield
    driver.close()

