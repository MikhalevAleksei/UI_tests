from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait

from locators.main_page_locators import MainPageLocators


class BasePage:
    DEFAULT_TIMEOUT = 5

    def __init__(self, driver):
        self.driver = driver

    def find_my_element(self, locator, timeout=DEFAULT_TIMEOUT):
        return Wait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

    def find_all_elements(self, locator, timeout=DEFAULT_TIMEOUT):
        return Wait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator))

    def click_to_element(self, locator, timeout=DEFAULT_TIMEOUT):
        Wait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def set_text_to_element(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def get_text_from_element(self, locator):
        text_element = self.driver.find_element(*locator).text
        return text_element

    def get_text_from_elements(self, locator):
        text_elements = self.driver.find_all_elements(locator).text
        return text_elements

    def transit_to_another_page(self):
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

    def drag_and_drop(self, drag, drop):
        ActionChains(self.driver).drag_and_drop(drag, drop).perform()

    def wait_find_element(self, locator, timeout=DEFAULT_TIMEOUT):
        text_id = self.driver.find_element(
            MainPageLocators.TXT_ID_OF_NEW_ORDER_LOCATOR)
        return Wait(self.driver, timeout).until(text_id.text != "9999")
