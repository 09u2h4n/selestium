import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from bs4 import BeautifulSoup

class HTMLSession(requests.Session):
    def __init__(self, browser='firefox'):
        super().__init__()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        self.browser_type = browser.lower()
        self.driver = None  # Lazily initialize WebDriver

    def _initialize_driver(self):
        if self.browser_type == 'firefox':
            options = FirefoxOptions()
        elif self.browser_type == 'chrome':
            options = ChromeOptions()
        else:
            raise ValueError("Unsupported browser. Supported browsers are 'firefox' and 'chrome'.")
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        self.driver = webdriver.Firefox(options=options) if self.browser_type == 'firefox' else webdriver.Chrome(options=options)

    def get(self, url, render=False, **kwargs):
        if render:
            if not self.driver:
                self._initialize_driver()
            return self.render(url)
        else:
            response = super().get(url, headers=self.headers, **kwargs)
            response.raise_for_status()
            return HTMLResponse(response.content)

    def render(self, url):
        if not self.driver:
            self._initialize_driver()
        self.driver.get(url)
        html_content = self.driver.page_source
        response = HTMLResponse(html_content)
        # Close the WebDriver after rendering
        self.driver.quit()
        return response

    def controller(self):
        if not self.driver:
            self._initialize_driver()
        return self.driver

class HTMLResponse:
    def __init__(self, response):
        self.response = response
    
    @property
    def text(self):
        return self.response

    def html(self):
        return BeautifulSoup(self.text, "html.parser")

    def find(self, selector):
        return self.html().select(selector)

if __name__ == "__main__":
    # Example usage
    session = HTMLSession(browser='chrome')
    response = session.get("https://www.whatismybrowser.com/detect/is-javascript-enabled", render=True)
    print(response.find("#detected_value")[0].get_text())
    #driver = session.controller()
    #driver.get()
