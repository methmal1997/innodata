
#
#


import requests

url = "https://journals.aai.org//immunohorizons/article-pdf/8/4/295/1655613/ih2300117.pdf"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

response = requests.get(url, headers=headers, allow_redirects=True)

final_url = response.url  # This will give you the final URL after redirection

print("Final URL after redirection:", final_url)



import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import common_function
import time
import undetected_chromedriver as uc
import pandas as pd

duplicate_list = []
error_list = []
completed_list = []
attachment = None
url_id = None
current_date = None
current_time = None
Ref_value = None
ini_path = None

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

url = "https://journals.aai.org//immunohorizons/article-pdf/8/4/295/1655613/ih2300117.pdf"




options = uc.ChromeOptions()
# options.add_argument('--headless')
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


# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.content, 'html.parser')
driver.delete_all_cookies()
driver.get(final_url)


time.sleep(100)

