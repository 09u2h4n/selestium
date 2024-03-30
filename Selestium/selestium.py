import requests
from bs4 import BeautifulSoup
from .FirefoxHandler import FirefoxHandler
from .ChromeHandler import ChromeHandler

class HTMLNavigator(requests.Session):
    """
    A class for navigating HTML content using Selenium with Firefox or Chrome browsers.

    Args:
        browser (str): The type of browser to use. Can be 'firefox' or 'chrome'. Defaults to 'firefox'.
    """

    def __init__(self, browser='firefox'):
        super().__init__()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        self.browser_type = browser.lower()
        self.driver = None  # Lazily initialize WebDriver
        self.handler = None
        if self.browser_type == "firefox":
            self.handler = FirefoxHandler()
        elif self.browser_type == "chrome":
            self.handler = ChromeHandler()
        else:
            raise ValueError("Unsupported browser type. Supported types are 'firefox' and 'chrome'.")

    def get(self, url, render=False, **kwargs):
        """
        Sends a GET request to the specified URL and returns the response.

        Args:
            url (str): The URL to send the request to.
            render (bool): Whether to render the page using a browser. Defaults to False.
            **kwargs: Additional keyword arguments to pass to the underlying requests.get method.

        Returns:
            HTMLResponse: An HTMLResponse object containing the response content.
        """
        if render:
            if not self.driver:
                self.driver = self.handler.initialize_driver()
            return self.render(url)
        else:
            response = super().get(url, headers=self.headers, **kwargs)
            response.raise_for_status()
            return HTMLResponse(response.content)

    def render(self, url):
        """
        Renders the HTML content of the specified URL using a browser.

        Args:
            url (str): The URL to render.

        Returns:
            HTMLResponse: An HTMLResponse object containing the rendered HTML content.
        """
        if not self.driver:
            self.driver = self.handler.initialize_driver()
        self.driver.get(url)
        html_content = self.driver.page_source
        response = HTMLResponse(html_content)
        # Close the WebDriver after rendering
        self.driver.quit()
        return response

    def browser_controller(self):
        """
        Returns the browser controller (WebDriver) instance.

        Returns:
            WebDriver: The browser controller instance.
        """
        if not self.driver:
            self.driver = self.handler.initialize_driver()
        return self.driver

class HTMLResponse:
    """
    A class representing an HTML response.

    Args:
        response (bytes): The response content.
    """

    def __init__(self, response):
        self.response = response
    
    @property
    def text(self):
        """str: The response content as a string."""
        return self.response

    def html(self):
        """BeautifulSoup: A BeautifulSoup object representing the parsed HTML."""
        return BeautifulSoup(self.text, "html.parser")

    def find(self, selector):
        """
        Finds all elements that match the given CSS selector.

        Args:
            selector (str): The CSS selector to search for.

        Returns:
            list: A list of BeautifulSoup Tag objects matching the selector.
        """
        return self.html().select(selector)

if __name__ == "__main__":
    # Example usage
    navigator = HTMLNavigator(browser='firefox')
    response = navigator.get("https://www.whatismybrowser.com/detect/is-javascript-enabled", render=True)
    print(response.find("#detected_value")[0].get_text())
    #driver = navigator.browser_controller()
    #driver.get()
