from locators import  BUTTON, ENTRANCE, URL
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestTransionFromLogo:
    def test_transit_from_logo(self, driver):
        driver.get(URL.current_url_home_page)

        driver.find_element(*BUTTON.entrance_in_account).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ENTRANCE.entrance_button1))
        driver.find_element(*ENTRANCE.field_email).send_keys('ilya_volkov_31_749@yandex.ru')
        driver.find_element(*ENTRANCE.field_password).send_keys('123456')
        driver.find_element(*ENTRANCE.entrance_button1).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(BUTTON.place_an_order))

        driver.find_element(*BUTTON.personal_account_button).click()
        driver.find_element(*BUTTON.logo_button).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(BUTTON.place_an_order))
        assert driver.current_url == URL.current_url_home_page
