import pytest


from fixture import driver, generate_email, generate_password, generate_name

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import SIGNUP, BUTTON, ENTRANCE, URL

class TestTransitForm:
    def test_transit_form(self):
        d = driver()

        d.get(URL.current_url_home_page)

        d.find_element(*BUTTON.entrance_in_account).click()
        WebDriverWait(d, 3).until(expected_conditions.visibility_of_element_located(ENTRANCE.entrance_button1))
        d.find_element(*ENTRANCE.field_email).send_keys('ilya_volkov_31_749@yandex.ru')
        d.find_element(*ENTRANCE.field_password).send_keys('123456')
        d.find_element(*ENTRANCE.entrance_button1).click()
        WebDriverWait(d, 10).until(expected_conditions.visibility_of_element_located(BUTTON.place_an_order))

        d.find_element(*BUTTON.personal_account_button).click()
        d.find_element(*BUTTON.constructor_button).click()
        WebDriverWait(d, 3).until(expected_conditions.visibility_of_element_located(BUTTON.place_an_order))
        assert d.current_url == URL.current_url_home_page

        d.quit()