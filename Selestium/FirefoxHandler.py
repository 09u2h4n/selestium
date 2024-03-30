from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
import os, subprocess

class FirefoxHandler:
    def __init__(self) -> None:
        pass

    def detect_os(self):
        if os.name == "posix":
            try:
                uname_o_output = subprocess.check_output(["uname", "-o"]).decode().strip()
                return uname_o_output
            except subprocess.CalledProcessError:
                return "Error: Unable to execute uname -o command"

    def detect_geckodriver(self):
        paths = os.environ.get('PATH', '').split(os.pathsep)
        for path in paths:
            full_path = os.path.join(path, "geckodriver")
            if os.path.exists(full_path) and os.access(full_path, os.X_OK):
                return full_path
        return None
            
    def initialize_driver(self):
        options = FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        detected_os = self.detect_os()
        geckodriver_path = self.detect_geckodriver()
        if detected_os == "Andriod":
            service = FirefoxService(executable_path=geckodriver_path)
            driver = webdriver.Firefox(options=options, service=service)
        else:
            driver = webdriver.Firefox(options=options)
        return driver