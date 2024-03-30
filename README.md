# Selestium

Selestium is a Python module for web scraping and automation using Selenium WebDriver.

## Features

- Provides a high-level interface for interacting with HTML content in web pages.
- Supports rendering JavaScript-based web pages using headless browsers (Firefox and Chrome).
- Allows easy navigation, element identification, and data extraction from web pages.

## Installation

You can install Selestium using pip:

```
pip install selestium
```

## Usage

Here's a basic example of how to use Selestium to render a web page and extract information:

### Make a Request Without Rendering:

```python
from Selestium import HTMLNavigator

# Initialize a HTMLNavigator instance with default settings (Firefox browser)
navigator = HTMLNavigator()

# Make a GET request to a web page without rendering
response = navigator.get("https://www.example.com")

# Extract information from the response
print(response.text)
```

### Make a Request With Rendering:

```python
from Selestium import HTMLNavigator

# Initialize a HTMLNavigator instance with Firefox browser
navigator = HTMLNavigator(browser='firefox')

# Get a web page and render it using the browser
response = navigator.get("https://www.example.com", render=True)

# Extract information from the rendered page
titles = response.find("h1")
for title in titles:
    print(title.text)
```

### Using the Controller Method:

```python
from Selestium import HTMLNavigator

# Initialize a HTMLNavigator instance with Chrome browser
navigator = HTMLNavigator(browser='chrome')

# Get the browser controller (WebDriver) instance
driver = navigator.browser_controller()

# Navigate to a web page
driver.get("https://www.example.com")

# Perform additional actions using the browser controller
# For example, click a button or fill out a form
# driver.find_element_by_id("button_id").click()
```

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/09u2h4n/selestium/blob/main/LICENSE) file for details.