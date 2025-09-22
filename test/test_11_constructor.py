import pytest
from data import DATA
from locators import KON
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestTab:
    """Тест переключения табов Соусы и Булки"""
    @pytest.mark.parametrize('text, tab_locotors', [
        ("Соусы", KON.button_sauces),
        ("Начинки", KON.button_fillings)
        ])
    def test_tab_fillings_and_sauces(self, driver, text, tab_locotors):
        driver.get(DATA.current_url_home_page)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(tab_locotors))
        driver.find_element(*tab_locotors).click()
        active_tab = driver.find_element(*tab_locotors)
        assert text in active_tab.text
    
    """Тест переключения с соусов обратно Булки"""
    def test_buns(self, driver):
        driver.get(DATA.current_url_home_page)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(KON.button_sauces))
        driver.find_element(*KON.button_sauces).click()
        active_tab = driver.find_element(*KON.active_tabl)
        assert "Соусы" in active_tab.text
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(KON.button_buns))
        driver.find_element(*KON.button_buns).click()
        active_tab = driver.find_element(*KON.active_tabl)

        assert "Булки" in active_tab.text
            