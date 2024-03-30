from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

class ChromeHandler:
    def __init__(self) -> None:
        pass

    def initialize_driver(self):
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(options=options)
        return driver