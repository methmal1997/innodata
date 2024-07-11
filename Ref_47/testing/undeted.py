import undetected_chromedriver as uc
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller as chromedriver
chromedriver.install()


def initialize_undetected_chromedriver():
    try:
        options = uc.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--incognito')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-software-rasterizer')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-infobars')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-popup-blocking')
        options.add_argument('--user-agent=YOUR_USER_AGENT_STRING')
        options.add_argument('--version_main=108')
        driver = uc.Chrome(options=options)
        print("Using undetected_chromedriver.")
        return driver
    except Exception as e:
        return None



def initialize_regular_chromedriver(executable_path):
    try:
        options = webdriver.ChromeOptions()
        # Add any necessary options here
        driver = webdriver.Chrome(service=Service(r"./chromedriver.exe"), options=options)
        print("Using regular ChromeDriver.")
        return driver
    except WebDriverException as e:
        print(f"Failed to initialize regular ChromeDriver: {e}")
        return None


def main():
    driver = initialize_undetected_chromedriver()
    if not driver:
        try:
            driver = initialize_regular_chromedriver()
            return driver
        except:
            return None
    return driver


