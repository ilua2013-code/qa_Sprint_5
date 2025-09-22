from data import DATA
from locators import BUTTON
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestTransitForm:
    
    """Тест перехода из ЛК в конструктор через кнопку 'Конструктор'"""
    def test_transit_form(self, driver, entrance_acc):

        driver.find_element(*BUTTON.personal_account_button).click()
        driver.find_element(*BUTTON.constructor_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BUTTON.place_an_order))
        assert driver.current_url == DATA.current_url_home_page

    """Тест перехода в личный кабинет"""
    def test_transit_person_acc(self, driver, entrance_acc):
        
        driver.find_element(*BUTTON.personal_account_button).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BUTTON.exit_from_account))
        assert driver.current_url == DATA.current_url_personal_account
   
    """Тест перехода из ЛК на главную через логотип"""
    def test_transit_from_logo(self, driver, entrance_acc):
        
        driver.find_element(*BUTTON.personal_account_button).click()
        driver.find_element(*BUTTON.logo_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BUTTON.place_an_order))
        assert driver.current_url == DATA.current_url_home_page
