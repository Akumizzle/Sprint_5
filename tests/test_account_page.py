from selenium.webdriver.common.by import By
from selenium import webdriver
import test_data
import pytest
from conftest import fill_login_fields
from conftest import driver



class TestAccountPage:

    def test_open_account_page(self,driver,fill_login_fields):
        driver.get(test_data.url_main)
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
        fill_login_fields()
        driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()
        assert driver.current_url==test_data.url_account
        driver.quit()

    @pytest.mark.parametrize('button', test_data.buttons)
    def test_open_constructor_from_account_page(self,driver,fill_login_fields,button):
        driver.get(test_data.url_main)
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
        fill_login_fields()
        driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()
        driver.find_element(By.CSS_SELECTOR,button).click()
        assert driver.current_url==test_data.url_main
        driver.quit()

    def test_logout_button(self,driver,fill_login_fields):
        driver.get(test_data.url_main)
        driver.find_element(By.XPATH, ".//button[text()='Войти в аккаунт']").click()
        fill_login_fields()
        driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()
        driver.find_element(By.CSS_SELECTOR,'.Account_button__14Yp3').click()
        assert driver.current_url==test_data.url_login
        driver.quit()