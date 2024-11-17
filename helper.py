import test_data
from selenium.webdriver.common.by import By
import test_locators



def fill_login_fields(driver):
    driver.find_element(By.XPATH,test_locators.login_email).send_keys(test_data.email)
    driver.find_element(By.XPATH,test_locators.login_pass).send_keys(test_data.password)
    driver.find_element(By.CSS_SELECTOR, test_locators.login_button).click()  # Кликаем кнопку логина
    return fill_login_fields