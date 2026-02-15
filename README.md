# Selenium Python Automation Framework 
# Project: selenium-python-POM-portfolio

## 📌 Overview
This project is a production-ready Selenium test automation framework built with Python and pytest.  
It demonstrates end-to-end UI testing using the Page Object Model (POM) design pattern against the SauceDemo practice site.

## 🛠 Tech Stack
- Python
- Selenium WebDriver
- pytest
- WebDriver Manager
- PyCharm

## 📂 Project Structure
- `pages/` – Page Object classes
- `report/` - HTML Reports
- `tests/` – Test cases
- `.env` - Environment variables
- `conftest.py` – WebDriver setup and teardown
- `README.md` - Readme file
- `requirements.txt` - Dependencies

## 🚀 Setup Instructions

```bash
git clone https://github.com/your-username/selenium-python-pom-portfolio.git
cd selenium-python-pom-portfolio
pip install -r requirements.txt

## Test status
Test is failing because of the /tests/test_login.py assertion
Screenshot Failure is captured each time test is run