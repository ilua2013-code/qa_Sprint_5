import pytest
from locators import URL, KON
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestTab:
    @pytest.mark.parametrize('text, tab_locotors', [
        ("Булки", KON.button_buns),
        ("Соусы", KON.button_sauces),
        ("Начинки", KON.button_fillings)
        ])
    def test_tab(self, driver, text, tab_locotors):
        driver.get(URL.current_url_home_page)
        if text != 'Булки':
            WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(tab_locotors))
            driver.find_element(*tab_locotors).click()

            active_tab = driver.find_element(*tab_locotors)

            assert text in active_tab.text
        else:
            WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(tab_locotors))
            driver.find_element(*KON.button_sauces).click()
            active_tab = driver.find_element(*KON.active_tabl)
            assert "Соусы" in active_tab.text

            driver.find_element(*tab_locotors).click()
            active_tab = driver.find_element(*tab_locotors)

            assert text in active_tab.text
            