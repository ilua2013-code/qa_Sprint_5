import pytest


from fixture import driver, generate_email, generate_password, generate_name

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import  URL, KON

class TestButtonBuns:
    def test_button_bums(self):
        d = driver()
        d.get(URL.current_url_home_page)

        WebDriverWait(d, 10).until(expected_conditions.visibility_of_element_located(KON.button_sauces))
        d.find_element(*KON.button_sauces).click()

        active_tab = d.find_element(*KON.active_tabl)

        assert "Соусы" in active_tab.text
        d.quit()