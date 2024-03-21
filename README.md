
# Selestium Documentation

Selestium is a Python module for web scraping with Selenium and BeautifulSoup. It provides a simple interface for making HTTP requests, rendering JavaScript content, and parsing HTML documents.

## Installation

You can install Selestium using pip:

`pip install selestium` 

## Usage

### Making HTTP Requests

You can use the `HTMLSession` class to make HTTP requests and retrieve HTML content. Here's a basic example:

```
from selestium import HTMLSession

session = HTMLSession()
response = session.get("https://example.com")
print(response.text)
```

### Rendering JavaScript Content

Selestium also allows you to render JavaScript content using Selenium WebDriver. Here's how you can render a page and extract HTML content:

```
from selestium import HTMLSession

session = HTMLSession()
response = session.get("https://example.com", render=True)
print(response.text)
```

### Parsing HTML Documents

You can use BeautifulSoup to parse HTML documents and extract data. Here's an example:

```
from selestium import HTMLSession

session = HTMLSession()
response = session.get("https://example.com")
soup = response.html()
print(soup.title)
```
