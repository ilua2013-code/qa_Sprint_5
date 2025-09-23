from data import DATA
from locators import SIGNUP, BUTTON, ENTRANCE
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestSignup:
    """Тест регистрации"""
    def test_signup(self, driver):
        driver.get(DATA.current_url_home_page)
        driver.find_element(*BUTTON.personal_account_button).click()
        driver.find_element(*ENTRANCE.signup).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(SIGNUP.entrance_button2))
        driver.find_element(*SIGNUP.field_name).send_keys(DATA.generate_name())
        driver.find_element(*SIGNUP.field_email).send_keys(DATA.generate_email())
        driver.find_element(*SIGNUP.field_password2).send_keys(DATA.generate_password())
        driver.find_element(*SIGNUP.button_signup).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(ENTRANCE.entrance_button1))
        assert driver.current_url == DATA.current_url_entrance
    
    """Тест регистрации с пустым паролем"""  
    def test_none_pass(self, driver):
        driver.get(DATA.current_url_home_page)
        driver.find_element(*BUTTON.personal_account_button).click()
        driver.find_element(*ENTRANCE.signup).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(SIGNUP.entrance_button2))
        driver.find_element(*SIGNUP.field_name).send_keys(DATA.generate_name())
        driver.find_element(*SIGNUP.field_email).send_keys(DATA.generate_email())

        driver.find_element(*SIGNUP.button_signup).click()

        assert driver.current_url == DATA.current_url_form_signup

    """Тест регистрации с пустым именем"""
    def test_none_name(self, driver):
        driver.get(DATA.current_url_home_page)
        driver.find_element(*BUTTON.personal_account_button).click()
        driver.find_element(*ENTRANCE.signup).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(SIGNUP.entrance_button2))
        driver.find_element(*SIGNUP.field_email).send_keys(DATA.generate_email())
        driver.find_element(*SIGNUP.field_password2).send_keys(DATA.generate_password())
        driver.find_element(*SIGNUP.button_signup).click()
        assert driver.current_url == DATA.current_url_form_signup

    """Тест регистрации с пустым Email"""
    def test_none_email(self,  driver):
        driver.get(DATA.current_url_home_page)
        driver.find_element(*BUTTON.personal_account_button).click()
        driver.find_element(*ENTRANCE.signup).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(SIGNUP.entrance_button2))
        driver.find_element(*SIGNUP.field_name).send_keys(DATA.generate_name())

        driver.find_element(*SIGNUP.field_password2).send_keys(DATA.generate_password())
        driver.find_element(*SIGNUP.button_signup).click()

        assert driver.current_url == DATA.current_url_form_signup

    """Тест регистрации с паролем меньше 6 символов"""
    def test_invalid_pass(self,  driver):
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

    """Тест регистрации с данными существующего аккаунта"""
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
    
    """Тест регистрации с невалидным Email"""
    def test_invalid_email(self,  driver):
        driver.get(DATA.current_url_home_page)
        driver.find_element(*BUTTON.personal_account_button).click()
        driver.find_element(*ENTRANCE.signup).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(SIGNUP.entrance_button2))
        driver.find_element(*SIGNUP.field_name).send_keys(DATA.generate_name())
        driver.find_element(*SIGNUP.field_email).send_keys('ilua')
        driver.find_element(*SIGNUP.field_password2).send_keys(DATA.generate_password())
        driver.find_element(*SIGNUP.button_signup).click()
        assert driver.current_url == DATA.current_url_form_signup