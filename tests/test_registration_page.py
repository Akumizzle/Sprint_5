import string
import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import test_data
import test_url
import pytest
from conftest import registration, driver
import test_locators
import random


class TestRegistrationPage:

    def test_registration_true(self,registration):
        email=''.join(random.choices(string.ascii_letters,k=10))
        registration.find_element(By.XPATH,test_locators.reg_name).send_keys(test_data.name)
        registration.find_element(By.XPATH,test_locators.reg_email).send_keys(f"{email}@yandex.ru")
        registration.find_element(By.XPATH,test_locators.reg_pass).send_keys(test_data.password)
        registration.find_element(By.CSS_SELECTOR,test_locators.reg_button).click()
        WebDriverWait(registration,3).until(expected_conditions.presence_of_element_located((By.XPATH,test_locators.button_enter)))
        assert registration.current_url==test_url.url_login

    def test_registation_with_short_length_password_false(self,registration):
        registration.find_element(By.XPATH,test_locators.reg_name).send_keys(test_data.name)
        registration.find_element(By.XPATH,test_locators.reg_email).send_keys(test_data.email)
        registration.find_element(By.XPATH,test_locators.reg_pass).send_keys(test_data.password_wrong)
        registration.find_element(By.CSS_SELECTOR, test_locators.reg_button).click()
        WebDriverWait(registration,3).until(expected_conditions.presence_of_element_located((By.XPATH,test_locators.reg_warning)))
        assert registration.current_url==test_url.url_registration


