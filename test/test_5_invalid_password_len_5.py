from data import DATA
from locators import SIGNUP, BUTTON, ENTRANCE
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class TestInvalidPass:
    def test_invalid_pass(self,  driver):
        """Тест регистрации с паролем меньше 6 символов"""
        driver.get(DATA.current_url_home_page)
        driver.find_element(*BUTTON.personal_account_button).click()
        driver.find_element(*ENTRANCE.signup).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(SIGNUP.entrance_button2))
        driver.find_element(*SIGNUP.field_name).send_keys(DATA.generate_name())
        driver.find_element(*SIGNUP.field_email).send_keys(DATA.generate_email())
        driver.find_element(*SIGNUP.field_password2).send_keys('1'*5)
        driver.find_element(*SIGNUP.button_signup).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(ENTRANCE.invalid_password))
        assert driver.current_url == DATA.current_url_form_signup
        