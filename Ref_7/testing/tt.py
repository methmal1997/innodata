import time
import requests
from bs4 import BeautifulSoup
import os
import re
import common_function
from datetime import datetime
import pandas as pd
import captcha_main
import random

import undetected_chromedriver as uc
import chromedriver_autoinstaller as chromedriver
chromedriver.install()

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



def get_current_cookies(url):

    try:
        driver.delete_all_cookies()
        driver.get(url)
        time.sleep(random.uniform(0, 3))
        selenium_cookies = driver.get_cookies()
        cookies_for_requests = {cookie['name']: cookie['value'] for cookie in selenium_cookies}
        driver.quit()
        return cookies_for_requests
    finally:
        driver.quit()