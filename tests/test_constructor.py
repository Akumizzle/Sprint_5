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


class TestConstructor:

    @pytest.mark.parametrize('title,header', test_data.headers.items(),ids=test_data.headers.keys())
    def test_sections_buttons_in_constructor(self,driver,title,header):
        driver.get(test_data.url_main)
        driver.find_element(By.XPATH,header).click()
        assert WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((By.XPATH,title)))
        driver.quit()