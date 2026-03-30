from selenium.webdriver.common.by import By
from config.settings import BASE_URL


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(BASE_URL)

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        