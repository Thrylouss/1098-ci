from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AuthPage:
    def __init__(self, driver):
        self.driver = driver
        self.login = (By.CSS_SELECTOR, "#app > div > div > div > div.log-in__content > form > label > input")
        self.next_btn = (By.CSS_SELECTOR, "#app > div > div > div > div.log-in__content > form > button")

    def enter_phone_number(self, phone):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.login)).send_keys(phone)

    def click_next_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.next_btn)).click()