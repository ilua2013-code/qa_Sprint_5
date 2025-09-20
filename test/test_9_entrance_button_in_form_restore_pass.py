from data import DATA
from locators import RESTORE, BUTTON, ENTRANCE, URL
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestFormRestore:
    def test_form_restore(self, driver):
        driver.get(URL.current_url_recovery_password)
        driver.find_element(*RESTORE.entrance_button3).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ENTRANCE.entrance_button1))

        driver.find_element(*ENTRANCE.field_email).send_keys(DATA.Email)
        driver.find_element(*ENTRANCE.field_password).send_keys(DATA.password)
        driver.find_element(*ENTRANCE.entrance_button1).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BUTTON.place_an_order))
        assert driver.current_url == URL.current_url_home_page
        