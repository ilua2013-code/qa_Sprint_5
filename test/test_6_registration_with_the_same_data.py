from data import DATA
from locators import SIGNUP, BUTTON, ENTRANCE
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestSameData:
    def test_same_data(self,  driver):
        driver.get(DATA.current_url_home_page)

        driver.find_element(*BUTTON.personal_account_button).click()
        driver.find_element(*ENTRANCE.signup).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(SIGNUP.entrance_button2))
        driver.find_element(*SIGNUP.field_name).send_keys(DATA.name)
        driver.find_element(*SIGNUP.field_email).send_keys(DATA.Email)
        driver.find_element(*SIGNUP.field_password2).send_keys(DATA.password)
        driver.find_element(*SIGNUP.button_signup).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(SIGNUP.text_during_dubbing))
        assert driver.current_url == DATA.current_url_form_signup