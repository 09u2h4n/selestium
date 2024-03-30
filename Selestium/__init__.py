# __init__.py

from .selestium import HTMLRequests

from .ChromeHandler import ChromeHandler
from .FirefoxHandler import FirefoxHandler

__all__ = ['HTMLRequests', 'ChromeHandler', 'FirefoxHandler']
