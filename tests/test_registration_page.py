from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import test_data
import pytest


class TestRegistrationPage:

    def test_registation_true(self,registration):
        registration.find_element(By.XPATH,'.//fieldset[1]//input').send_keys(test_data.name)
        registration.find_element(By.XPATH,'.//fieldset[2]//input').send_keys(test_data.email)
        registration.find_element(By.XPATH,'.//fieldset[3]//input').send_keys(test_data.password)
        registration.find_element(By.CSS_SELECTOR, '.button_button__33qZ0').click()
        #добавить ожидание загрузки страницы

        assert registration.current_url==test_data.url_login
        registration.quit()

    def test_registation_with_short_length_password_false(self,registration):
        registration.find_element(By.XPATH,'.//fieldset[1]//input').send_keys(test_data.name)
        registration.find_element(By.XPATH,'.//fieldset[2]//input').send_keys(test_data.email)
        registration.find_element(By.XPATH,'.//fieldset[3]//input').send_keys(test_data.password_wrong)
        registration.find_element(By.CSS_SELECTOR, '.button_button__33qZ0').click()
        WebDriverWait(registration,3).until(expected_conditions.presence_of_element_located((By.XPATH,".//p[text()='Некорректный пароль']")))

        assert registration.current_url==test_data.url_registration
        registration.quit()


