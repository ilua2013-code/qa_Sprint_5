import pytest


from data import DATA
from locators import URL, KON
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestButtonBuns:
    def test_button_bums(self, driver):
        driver.get(URL.current_url_home_page)

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(KON.button_sauces))
        driver.find_element(*KON.button_sauces).click()

        active_tab = driver.find_element(*KON.active_tabl)

        assert "Соусы" in active_tab.text