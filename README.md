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

## Dependencies for Termux
In Termux you need some dependencies to work. Later it will bee automatic.
#### !!CHROME DOES NOT WORK JUST FIREFOX IN TERMUX!!
First update and then install tur and x11 repos
```
pkg update -y; pkg install -y tur-repo x11-repo
```
Then install firefox and geckodriver
```
pkg install -y firefox geckodriver
```
And you are ready to go..

## Dependencies for Linux
In Linux also you need get [Firefox dependencies](https://www.mozilla.org/en-US/firefox/124.0.1/system-requirements/).

Please note that GNU/Linux distributors may provide packages for your distribution which have different requirements.

Firefox will not run at all without the following libraries or packages:
glibc 2.17 or higher
GTK+ 3.14 or higher
libglib 2.42 or higher
libstdc++ 4.8.1 or higher
X.Org 1.0 or higher (1.7 or higher is recommended)
For optimal functionality, we recommend the following libraries or packages:
DBus 1.0 or higher
NetworkManager 0.7 or higher
PulseAudio

For Debian-based distros:
```
sudo apt update -y && sudo apt install -y \
    libc6 \
    libgtk-3-0 \
    libglib2.0-0 \
    libstdc++6 \
    xorg
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