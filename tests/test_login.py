import time
from ..pages.login_page import LoginPage


def test_login(driver, base_url, credentials):
    login = LoginPage(driver)
    login.load_login_page(base_url)
    login.login_to_bank(credentials["username"], credentials["password"])

    time.sleep(2)
    assert "wrong url" in driver.current_url, "Login failed"

