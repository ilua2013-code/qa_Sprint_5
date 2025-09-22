from data import DATA
from locators import SIGNUP, BUTTON, ENTRANCE
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestInvalidEmail:
    def test_invalid_email(self,  driver):
        """Тест регистрации с невалидным Email"""
        driver.get(DATA.current_url_home_page)
        driver.find_element(*BUTTON.personal_account_button).click()
        driver.find_element(*ENTRANCE.signup).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(SIGNUP.entrance_button2))
        driver.find_element(*SIGNUP.field_name).send_keys(DATA.generate_name())
        driver.find_element(*SIGNUP.field_email).send_keys('ilua')
        driver.find_element(*SIGNUP.field_password2).send_keys(DATA.generate_password())
        driver.find_element(*SIGNUP.button_signup).click()

        assert driver.current_url == DATA.current_url_form_signup
        