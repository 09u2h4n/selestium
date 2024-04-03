from requests import Session
from bs4 import BeautifulSoup
from .FirefoxHandler import FirefoxHandler
from .ChromeHandler import ChromeHandler

class HTMLRequests(Session):
    """
    A class for navigating HTML content using Selenium with Firefox or Chrome browsers.

    Args:
        browser (str): The type of browser to use. Can be 'firefox' or 'chrome'. Defaults to 'firefox'.
    """

    def __init__(self, browser='firefox'):
        """
        Initialize the HTMLRequests object.

        Args:
            browser (str): The type of browser to use. Can be 'firefox' or 'chrome'. Defaults to 'firefox'.
        """
        super().__init__()
        self.browser_type = browser.lower()
        self.driver = None  # Lazily initialize WebDriver
        self.handler = None
        if self.browser_type == "firefox":
            self.handler = FirefoxHandler()
        elif self.browser_type == "chrome":
            self.handler = ChromeHandler()
        else:
            raise ValueError("Unsupported browser type. Supported types are 'firefox' and 'chrome'.")

    def get(self, url, render=False, stream=False, **kwargs):
        """
        Sends a GET request to the specified URL and returns the response.

        Args:
            url (str): The URL to send the request to.
            render (bool): Whether to render the page using a browser. Defaults to False.
            stream (bool): Whether to use streaming mode for the response. Defaults to False.
            **kwargs: Additional keyword arguments to pass to the underlying requests.get method.

        Returns:
            HTMLResponse or requests.Response: Depending on the value of the stream parameter.
        """
        if render and stream:
            raise ValueError("Cannot use streaming mode and rendering mode together.")

        if render:
            if not self.driver:
                self.driver = self.handler.initialize_driver()
            return self.render(url)
        else:
            response = super().get(url, stream=stream, **kwargs)
            if not stream:
                response.raise_for_status()
                response = HTMLResponse(response.content, original_response=response)
            return response

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

    def browser_controller(self, headless=True):
        """
        Returns the browser controller (WebDriver) instance.

        Returns:
            WebDriver: The browser controller instance.
        """
        if not self.driver:
            self.driver = self.handler.initialize_driver(headless=headless)
        return self.driver

class HTMLResponse:
    """
    A class representing an HTML response.

    Args:
        content (bytes): The response content.
        original_response (requests.Response): The original requests Response object.
    """

    def __init__(self, content, original_response=None):
        """
        Initialize the HTMLResponse object.

        Args:
            content (bytes): The response content.
            original_response (requests.Response): The original requests Response object.
        """
        self.content = content
        self.original_response = original_response
    
    @property
    def content(self):
        """str: The response content."""
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    def html(self):
        """BeautifulSoup: A BeautifulSoup object representing the parsed HTML."""
        return BeautifulSoup(self.content, "html.parser")

    def find(self, selector):
        """
        Finds all elements that match the given CSS selector.

        Args:
            selector (str): The CSS selector to search for.

        Returns:
            list: A list of BeautifulSoup Tag objects matching the selector.
        """
        return self.html().select(selector)

    # Forward other method calls to the original response object
    def __getattr__(self, name):
        if self.original_response:
            return getattr(self.original_response, name)
        else:
            raise AttributeError(f"'HTMLResponse' object has no attribute '{name}'")
