from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

class ChromeHandler:
    """
    A class for handling Chrome browser sessions.

    This class provides methods to initialize a WebDriver instance for Chrome.

    Attributes:
        None
    """

    def __init__(self) -> None:
        pass

    def initialize_driver(self):
        """
        Initializes a WebDriver instance for Chrome with headless mode enabled.

        Returns:
            WebDriver: The initialized WebDriver instance.
        """
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(options=options)
        return driver
