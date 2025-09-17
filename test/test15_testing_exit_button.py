import pytest


from fixture import driver, generate_email, generate_password, generate_name

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import SIGNUP, BUTTON, ENTRANCE, URL

class TestbuttonExit:
    def test_button_exit(self):
        d = driver()
        d.get(URL.current_url_home_page)

        d.find_element(*BUTTON.personal_account_button).click()
        WebDriverWait(d, 3).until(expected_conditions.visibility_of_element_located(ENTRANCE.entrance_button1))
        d.find_element(*ENTRANCE.field_email).send_keys('ilya_volkov_31_749@yandex.ru')
        d.find_element(*ENTRANCE.field_password).send_keys('123456')
        d.find_element(*ENTRANCE.entrance_button1).click()
        WebDriverWait(d, 3).until(expected_conditions.visibility_of_element_located(BUTTON.personal_account_button))
        d.find_element(*BUTTON.personal_account_button).click()
        WebDriverWait(d, 3).until(expected_conditions.visibility_of_element_located(BUTTON.exit_from_account))
        d.find_element(*BUTTON.exit_from_account).click()
        WebDriverWait(d, 3).until(expected_conditions.visibility_of_element_located(ENTRANCE.entrance_button1))
        assert d.current_url == URL.current_url_entrance
        d.quit()