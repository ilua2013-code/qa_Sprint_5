import pytest
from data import DATA
from selenium import webdriver
from locators import BUTTON, ENTRANCE
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope = "function")
def driver():
    driver = webdriver.Chrome() 
    yield driver
    driver.quit()

@pytest.fixture(scope = "function")
def entrance_acc(driver):
    driver.get(DATA.current_url_home_page)

    driver.find_element(*BUTTON.entrance_in_account).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ENTRANCE.entrance_button1))
    driver.find_element(*ENTRANCE.field_email).send_keys(DATA.Email)
    driver.find_element(*ENTRANCE.field_password).send_keys(DATA.password)
    driver.find_element(*ENTRANCE.entrance_button1).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BUTTON.place_an_order))