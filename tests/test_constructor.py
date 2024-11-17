from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import test_locators
import test_url
from conftest import driver




class TestConstructor:

    def test_sause_button_in_constructor(self,driver):
        driver.get(test_url.url_main)
        button=driver.find_element(By.XPATH,test_locators.button_sause)
        button.click()
        assert 'current' in button.find_element(By.XPATH, './..').get_attribute('class')

    def test_filling_button_in_constructor(self,driver):
        driver.get(test_url.url_main)
        button=driver.find_element(By.XPATH,test_locators.button_filling)
        button.click()
        assert 'current' in button.find_element(By.XPATH, './..').get_attribute('class')

    def test_bread_button_in_constructor(self,driver):
        driver.get(test_url.url_main)
        button=driver.find_element(By.XPATH, test_locators.button_bread)
        driver.find_element(By.XPATH,test_locators.button_filling).click()
        button.click()
        assert 'current' in button.find_element(By.XPATH, './..').get_attribute('class')
