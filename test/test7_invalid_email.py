import pytest


from fixture import driver, generate_email, generate_password, generate_name

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import SIGNUP, BUTTON, ENTRANCE, URL

class TestInvalidEmail:
    def test_invalid_email(self):
        d = driver()
        d.get(URL.current_url_home_page)

        d.find_element(*BUTTON.personal_account_button).click()
        d.find_element(*ENTRANCE.signup).click()
        WebDriverWait(d, 3).until(expected_conditions.visibility_of_element_located(SIGNUP.entrance_button2))
        d.find_element(*SIGNUP.field_name).send_keys(generate_name())
        d.find_element(*SIGNUP.field_email).send_keys('ilua')
        d.find_element(*SIGNUP.filed_password2).send_keys(generate_password())
        d.find_element(*SIGNUP.button_signup).click()

        assert d.current_url == URL.current_url_form_signup
        d.quit()
