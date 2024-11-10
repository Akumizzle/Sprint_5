from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import test_data
import pytest
from conftest import fill_login_fields
from conftest import driver
import time


class TestLoginPage:

    def test_login_with_button_sign_in_on_main_true(self,driver,fill_login_fields):
        driver.get(test_data.url_main)
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
        fill_login_fields()
        time.sleep(2)
        assert driver.find_element(By.CSS_SELECTOR,'.button_button__33qZ0').text=='Оформить заказ'
        driver.quit()

    def test_login_with_button_account_on_main_true(self,driver,fill_login_fields):
        driver.get(test_data.url_main)
        driver.find_element(By.LINK_TEXT,'Личный Кабинет').click()
        fill_login_fields()
        time.sleep(2)
        assert driver.find_element(By.CSS_SELECTOR,'.button_button__33qZ0').text=='Оформить заказ'
        driver.quit()

    @pytest.mark.parametrize('url',test_data.url)
    def test_login_from_registration_password_reset_page(self,driver,fill_login_fields,url):
        driver.get(url)
        driver.find_element(By.LINK_TEXT, 'Войти').click()
        fill_login_fields()
        time.sleep(2)
        assert driver.find_element(By.CSS_SELECTOR, '.button_button__33qZ0').text == 'Оформить заказ'
        driver.quit()




