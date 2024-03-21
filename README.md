# Selestium

Selestium is a Python module for web scraping with Selenium and BeautifulSoup.

## Installation

You can install Selestium using pip:
` 
pip install selestium
` 

 ## Usage

Here's a simple example of how to use Selestium:

```python
from selestium import HTMLSession

session = HTMLSession(browser='firefox')
response = session.get("https://example.com")
print(response.find("h1").text)
```

For more information, please refer to the [documentation](https://github.com/yourusername/selestium)

## License

This project is licensed under the GPL-3.0 License - see the LICENSE file for details.