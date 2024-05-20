import random
import time
import requests
from bs4 import BeautifulSoup
import os
import re
import common_function
from datetime import datetime
import pandas as pd
import captcha_main
import undeted
pdf_link=''
print("This is Ref_17")

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
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

proxies_list = [
    "141.98.155.137:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "185.205.199.161:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "216.10.5.126:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "2.58.80.143:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "185.207.96.233:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "67.227.121.110:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "67.227.127.100:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "181.177.76.122:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "185.207.97.85:3199:mariyarathna-dh3w3:IxjkW0fdJy",
    "186.179.21.77:3199:mariyarathna-dh3w3:IxjkW0fdJy"
]

formatted_proxies = []
for proxy in proxies_list:
    ip, port, user, password = proxy.split(':')
    formatted_proxy = f'http://{user}:{password}@{ip}:{port}'
    formatted_proxies.append({'http': formatted_proxy, 'https': formatted_proxy})


def get_current_cookies(url):
    driver = undeted.main()
    if not driver:
        Error_message = "Error in chrome driver or undeteted chrome :"
        print(Error_message)
        error_list.append(Error_message)
        return None
    driver.delete_all_cookies()
    driver.get(url)
    time.sleep(random.uniform(0, 3))
    selenium_cookies = driver.get_cookies()
    cookies_for_requests = {cookie['name']: cookie['value'] for cookie in selenium_cookies}
    return cookies_for_requests

with open('urlDetails.txt', 'r', encoding='utf-8') as file:
    url_list = file.read().split('\n')
print("Process started...")
print("This may take sometime.Please wait..........")
print("Urldetails text file was readed......")
try:
    with open('completed.txt', 'r', encoding='utf-8') as read_file:
        read_content = read_file.read().split('\n')
except FileNotFoundError:
    with open('completed.txt', 'w', encoding='utf-8'):
        with open('completed.txt', 'r', encoding='utf-8') as read_file:
            read_content = read_file.read().split('\n')

for i, url_url_id in enumerate(url_list):
    url, url_id = url_url_id.split(',')
    print(f"Executing this {url}")
    current_datetime = datetime.now()
    current_date = str(current_datetime.date())
    current_time = current_datetime.strftime("%H:%M:%S")

    ini_path = os.path.join(os.getcwd(), "Info.ini")
    Download_Path, Email_Sent, Check_duplicate, user_id = common_function.read_ini_file(ini_path)

    data = []
    pdf_count = 1
    Ref_value = "17"
    url_value = url.split('/')[-2]

    current_out = common_function.return_current_outfolder(Download_Path, user_id, url_id)
    out_excel_file = common_function.output_excel_name(current_out)

    response = requests.get(url, headers=headers, timeout=20, cookies=get_current_cookies(url))
    current_soup = BeautifulSoup(response.content, 'html.parser')
    check_1 = current_soup.find('span', class_='volume issue').text.strip().split(',')[0]

    Volume = re.sub(r'[^0-9]+', "", current_soup.find('span', class_='volume issue').text.strip().split(',')[0])
    Issue = re.sub(r'[^0-9]+', "", current_soup.find('span', class_='volume issue').text.strip().split(',')[1])
    Date,Month,Year = current_soup.find('div', class_='ii-pub-date').text.strip().split(' ')

    print(Month)