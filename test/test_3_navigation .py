import pytest
from data import DATA
from locators import BUTTON, ENTRANCE, KON
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestNavigation:
    url = DATA.current_url_home_page
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

    """Тест кнопки Выход"""
    def test_button_exit(self, driver, entrance_acc):
        driver.find_element(*BUTTON.personal_account_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BUTTON.exit_from_account))
        driver.find_element(*BUTTON.exit_from_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ENTRANCE.entrance_button1))
        assert driver.current_url == DATA.current_url_entrance

    """Тест переключения табов Соусы и Булки"""
    @pytest.mark.parametrize('text1, tab_locotors', [
        ("Соусы", KON.button_sauces),
        ("Начинки", KON.button_fillings)
        ])
    def test_tab_fillings_and_sauces(self, driver, text1, tab_locotors):
        driver.get(self.url)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(tab_locotors))
        driver.find_element(*tab_locotors).click()
        active_tab = driver.find_element(*tab_locotors)
        assert text1 in active_tab.text
    
    """Тест переключения с соусов обратно Булки"""
    def test_buns(self, driver):
        driver.get(self.url)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(KON.button_sauces))
        driver.find_element(*KON.button_sauces).click()
        active_tab = driver.find_element(*KON.active_tabl)
        assert "Соусы" in active_tab.text
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(KON.button_buns))
        driver.find_element(*KON.button_buns).click()
        active_tab = driver.find_element(*KON.active_tabl)

        assert "Булки" in active_tab.text