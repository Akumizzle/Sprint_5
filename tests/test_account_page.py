from selenium.webdriver.common.by import By
import test_data
import test_url
import pytest
from conftest import fill_login_fields
from conftest import driver
import test_locators



class TestAccountPage:

    def test_open_account_page(self,driver,fill_login_fields):
        driver.get(test_url.url_main)
        driver.find_element(By.XPATH, test_locators.button_signin).click()
        fill_login_fields()
        driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()
        assert driver.current_url==test_url.url_account

    @pytest.mark.parametrize('button', test_locators.buttons)
    def test_open_constructor_from_account_page(self,driver,fill_login_fields,button):
        driver.get(test_url.url_main)
        driver.find_element(By.XPATH, test_locators.button_signin).click()
        fill_login_fields()
        driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()
        driver.find_element(By.CSS_SELECTOR,button).click()
        assert driver.current_url==test_url.url_main

    def test_logout_button(self,driver,fill_login_fields):
        driver.get(test_url.url_main)
        driver.implicitly_wait(3) #у меня переход по страницам происходил слишком быстро получилось пройти проверку только с неявным ожиданием
        driver.find_element(By.XPATH, test_locators.button_signin).click()
        driver.find_element(By.XPATH,test_locators.login_email).send_keys(test_data.email)
        driver.find_element(By.XPATH,test_locators.login_pass).send_keys(test_data.password)
        driver.find_element(By.CSS_SELECTOR, test_locators.login_button).click()
        driver.find_element(By.LINK_TEXT, 'Личный Кабинет').click()
        driver.find_element(By.CSS_SELECTOR,test_locators.button_logout).click()
        assert driver.current_url==test_url.url_login