from data import DATA
from locators import SIGNUP, BUTTON, ENTRANCE, RESTORE
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestEntrance:
    """Тест вход через кнопку в форме регистрации""" 
    def test_entrance_from_registration_form(self, driver):
        driver.get(DATA.current_url_recovery_password)
        driver.find_element(*SIGNUP.entrance_button2).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ENTRANCE.entrance_button1))
        driver.find_element(*ENTRANCE.field_email).send_keys(DATA.Email)
        driver.find_element(*ENTRANCE.field_password).send_keys(DATA.password)
        driver.find_element(*ENTRANCE.entrance_button1).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BUTTON.place_an_order))
        assert driver.current_url == DATA.current_url_home_page
    
    """Тест вход через кнопку в форме восстановления пароля"""
    def test_entrance_from_password_recovery_form(self, driver):
        driver.get(DATA.current_url_recovery_password)
        driver.find_element(*RESTORE.entrance_button3).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ENTRANCE.entrance_button1))

        driver.find_element(*ENTRANCE.field_email).send_keys(DATA.Email)
        driver.find_element(*ENTRANCE.field_password).send_keys(DATA.password)
        driver.find_element(*ENTRANCE.entrance_button1).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BUTTON.place_an_order))
        assert driver.current_url == DATA.current_url_home_page
    
    """Тест вход через кнопку на главной странице"""
    def test_login_via_the_button_on_the_main_page(self, driver):
        driver.get(DATA.current_url_home_page)

        driver.find_element(*BUTTON.entrance_in_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ENTRANCE.entrance_button1))
        driver.find_element(*ENTRANCE.field_email).send_keys(DATA.Email)
        driver.find_element(*ENTRANCE.field_password).send_keys(DATA.password)
        driver.find_element(*ENTRANCE.entrance_button1).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BUTTON.place_an_order))
        assert driver.current_url == DATA.current_url_home_page
    
    """Тест вход через кнопку в личном кабинете"""
    def test_login_via_the_button_in_your_personal_account(self, driver):
        driver.get(DATA.current_url_recovery_password)
        driver.find_element(*RESTORE.entrance_button3).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ENTRANCE.entrance_button1))

        driver.find_element(*ENTRANCE.field_email).send_keys(DATA.Email)
        driver.find_element(*ENTRANCE.field_password).send_keys(DATA.password)
        driver.find_element(*ENTRANCE.entrance_button1).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BUTTON.place_an_order))
        assert driver.current_url == DATA.current_url_home_page
        