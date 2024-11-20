from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import test_locators
import test_url
from conftest import driver
from helper import fill_login_fields


class TestLoginPage:

    def test_login_with_button_sign_in_on_main_true(self,driver):
        driver.get(test_url.url_main)
        driver.find_element(By.XPATH, test_locators.button_signin).click()
        fill_login_fields(driver)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,test_locators.constructor)))
        assert driver.find_element(By.XPATH,test_locators.button_order).text=='Оформить заказ'

    def test_login_with_button_account_on_main_true(self,driver):
        driver.get(test_url.url_main)
        driver.find_element(By.LINK_TEXT,'Личный Кабинет').click()
        fill_login_fields(driver)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,test_locators.constructor)))
        assert driver.find_element(By.XPATH,test_locators.button_order).text=='Оформить заказ'

    @pytest.mark.parametrize('url',test_url.url)
    def test_login_from_registration_password_reset_page(self,driver,url):
        driver.get(url)
        driver.find_element(By.LINK_TEXT, 'Войти').click()
        fill_login_fields(driver)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,test_locators.constructor)))
        assert driver.find_element(By.XPATH, test_locators.button_order).text == 'Оформить заказ'



