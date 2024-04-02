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
            response = super().get(url, **kwargs)
            response.raise_for_status()
            return HTMLResponse(response.content, original_response=response)

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
        original_response (requests.Response): The original requests Response object.
    """

    def __init__(self, response, original_response=None):
        self.response = response
        self.original_response = original_response
    
    @property
    def content(self):
        """str: The response content."""
        return self.response

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

if __name__ == "__main__":
    # Example usage
    requests = HTMLRequests(browser='firefox')
    response = requests.get("https://www.whatismybrowser.com/detect/is-javascript-enabled", render=False)
    print(response.find("#detected_value")[0].get_text())
    #driver = navigator.browser_controller()
    #driver.get()
