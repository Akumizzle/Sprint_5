import test_data
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import test_locators
import test_url



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def registration():
    driver = webdriver.Chrome()
    driver.get(test_url.url_registration)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def fill_login_fields(driver):
    def fill():
        driver.find_element(By.XPATH,test_locators.login_email).send_keys(test_data.email)
        driver.find_element(By.XPATH,test_locators.login_pass).send_keys(test_data.password)
        driver.find_element(By.CSS_SELECTOR, test_locators.login_button).click()  # Кликаем кнопку логина
    return fill
