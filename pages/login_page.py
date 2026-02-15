from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    def load_login_page(self, base_url) -> None:
        self.open_url(base_url)

    def login_to_bank(self, username: str, password: str) -> None:
        self.enter_text(self.USERNAME, username)
        self.enter_text(self.PASSWORD, password)
        self.click_element(self.LOGIN_BTN)
