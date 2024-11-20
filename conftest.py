import test_data
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import test_locators




@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

