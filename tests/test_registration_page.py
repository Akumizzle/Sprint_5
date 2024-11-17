import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import test_data
import test_url
from conftest import driver
import test_locators
import random


class TestRegistrationPage:

    def test_registration_true(self,driver):
        driver.get(test_url.url_registration)
        email=''.join(random.choices(string.ascii_letters,k=10))
        driver.find_element(By.XPATH,test_locators.reg_name).send_keys(test_data.name)
        driver.find_element(By.XPATH,test_locators.reg_email).send_keys(f"{email}@yandex.ru")
        driver.find_element(By.XPATH,test_locators.reg_pass).send_keys(test_data.password)
        driver.find_element(By.CSS_SELECTOR,test_locators.reg_button).click()
        WebDriverWait(driver,3).until(expected_conditions.presence_of_element_located((By.XPATH,test_locators.button_enter)))
        assert driver.current_url==test_url.url_login

    def test_registation_with_short_length_password_false(self,driver):
        driver.find_element(By.XPATH,test_locators.reg_name).send_keys(test_data.name)
        driver.find_element(By.XPATH,test_locators.reg_email).send_keys(test_data.email)
        driver.find_element(By.XPATH,test_locators.reg_pass).send_keys(test_data.password_wrong)
        driver.find_element(By.CSS_SELECTOR, test_locators.reg_button).click()
        WebDriverWait(driver,3).until(expected_conditions.presence_of_element_located((By.XPATH,test_locators.reg_warning)))
        assert driver.current_url==test_url.url_registration


