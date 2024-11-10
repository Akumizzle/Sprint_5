import test_data
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    return driver


@pytest.fixture
def registration():
    driver = webdriver.Chrome()
    driver.get(test_data.url_registration)
    return driver


@pytest.fixture(scope='function')
def fill_login_fields(driver):
    def fill():
        driver.find_element(By.XPATH,'/html/body/div/div/main/div/form/fieldset[1]/div/div/input').send_keys(test_data.email)
        driver.find_element(By.XPATH,'/html/body/div/div/main/div/form/fieldset[2]/div/div/input').send_keys(test_data.password)
        driver.find_element(By.CSS_SELECTOR, '.button_button__33qZ0').click()  # Кликаем кнопку логина
    return fill

