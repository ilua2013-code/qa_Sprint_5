import pytest


from data import DATA
from locators import KON, URL
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestButtonFillings:
    def test_button_fillings(self, driver):
        driver.get(URL.current_url_home_page)

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(KON.button_fillings))
        driver.find_element(*KON.button_fillings).click()


        active_tab = driver.find_element(*KON.active_tabl)

        assert "Начинки" in active_tab.text
