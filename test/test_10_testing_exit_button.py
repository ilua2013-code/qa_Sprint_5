from data import DATA
from locators import  BUTTON, ENTRANCE
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestbuttonExit:
    def test_button_exit(self, driver, entrance_acc):
        """Тест кнопки Ваход"""
        driver.find_element(*BUTTON.personal_account_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BUTTON.exit_from_account))
        driver.find_element(*BUTTON.exit_from_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ENTRANCE.entrance_button1))
        assert driver.current_url == DATA.current_url_entrance
