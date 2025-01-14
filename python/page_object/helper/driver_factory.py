from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverFactory:
    @staticmethod
    def get_driver(browser="chrome"):
        """
        Returns a WebDriver instance based on the browser type.
        :param browser: str: Type of browser (chrome, firefox, edge)
        :return: WebDriver instance
        """
        if browser.lower() == "chrome":
            # Initialize Chrome WebDriver
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

        elif browser.lower() == "firefox":
            # Initialize Firefox WebDriver
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        else:
            raise ValueError(f"Unsupported browser: {browser}. Please choose 'chrome', 'firefox', or 'edge'.")

        # Maximize the browser window (optional)
        driver.maximize_window()
        return driver
