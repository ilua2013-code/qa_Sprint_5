import pytest


from data import DATA
from locators import URL, KON
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestButtonSauces:
    def test_button_sauces(self, driver):
        driver.get(URL.current_url_home_page)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(KON.button_fillings))
        driver.find_element(*KON.button_fillings).click()

        active_tab = driver.find_element(*KON.active_tabl)
        assert "Начинки" in active_tab.text

        driver.find_element(*KON.button_buns).click()
        active_tab = driver.find_element(*KON.active_tabl)

        assert "Булки" in active_tab.text