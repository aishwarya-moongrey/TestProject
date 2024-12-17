from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://example.com/login"  # Replace with the actual URL

    def navigate(self):
        self.driver.get(self.url)

    def enter_username(self, username):
        username_field = self.driver.find_element(By.NAME, "username")
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.clear()
        password_field.send_keys(password)

    def submit_login(self):
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys(Keys.RETURN)  # Submitting the form

    def get_error_message(self):
        return self.driver.find_element(By.CLASS_NAME, "error-message").text