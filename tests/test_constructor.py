from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import test_data
import test_locators
import test_url
from conftest import driver




class TestConstructor:

    def test_sause_button_in_constructor(self,driver):
        driver.get(test_url.url_main)
        driver.find_element(By.XPATH,test_locators.button_sause).click()
        assert WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((By.XPATH,test_locators.text_sauce)))

    def test_filling_button_in_constructor(self,driver):
        driver.get(test_url.url_main)
        driver.find_element(By.XPATH,test_locators.button_filling).click()
        assert WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((By.XPATH,test_locators.text_filling)))

    def test_bread_button_in_constructor(self,driver):
        driver.get(test_url.url_main)
        driver.find_element(By.XPATH,test_locators.button_filling).click()
        driver.find_element(By.XPATH, test_locators.button_bread).click()
        assert WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((By.XPATH,test_locators.text_bread)))
