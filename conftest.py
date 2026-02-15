"""
Pytest configuration file with fixtures for test automation framework.
"""

import pytest
import os
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
from screenshot_utility import take_screenshot

load_dotenv(override=True)

@pytest.fixture()
def driver():

    opts = Options()
    opts.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    })

    driver = webdriver.Chrome(options=opts)
    driver.maximize_window()

    yield driver
    driver.quit()

@pytest.fixture()
def base_url() -> str:
    return os.getenv("BASE_URL")

@pytest.fixture()
def credentials():
    return{
        "username": os.getenv("USERNAME"),
        "password": os.getenv("PASSWORD"),
    }

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            take_screenshot(driver, f"FAILED_{item.name}")