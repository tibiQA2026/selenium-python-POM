"""
Base Page module is containing common methods for all page objects.
Implements Page Object Model design pattern.
"""
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    Base Page class that all page objects inherit from.
    Contains common methods used across all pages.
    """
    def __init__(self, driver):
        """
        Initialize BasePage with WebDriver instance.

        Args:
            driver: Selenium WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url: str) -> None:
        """
        Navigate to specified URL.

        Args:
            url: URL to navigate to
        """
        self.driver.get(url)

    def find_element(self, locator:tuple[str,str]) -> WebElement:
        """
        Finding an element

        Args:
            locator: Tuple of (By strategy, locator value)

        Returns:
            WebElement: Found element
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator:tuple[str, str]) -> None:
        """
        Click on element after waiting for it to be clickable.

        Args:
            locator: Tuple of (By strategy, locator value)
        """
        elem = self.wait.until(EC.element_to_be_clickable(locator))
        elem.click()

    def enter_text(self, locator:tuple[str, str], text:str) -> None:
        """
        Enter text into input field.

        Args:
            locator: Tuple of (By strategy, locator value)
            text: Text to enter
        """
        elem = self.find_element(locator)
        elem.clear()
        elem.send_keys(text)

    def get_text(self, locator: tuple[str, str]) -> str:
        """
        Get text from element.

        Args:
            locator: Tuple of (By strategy, locator value)
        Method:
            strip: Return a copy of the string without the leading and trailing characters
        Returns:
            str: Element text
        """
        return self.find_element(locator).text.strip()

    def is_element_visible(self, locator: tuple[str, str]) -> bool:
        """
        Check if element is displayed.

        Args:
            locator: Tuple of (By strategy, locator value)

        Returns:
            bool: True if displayed, False otherwise
        """
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

