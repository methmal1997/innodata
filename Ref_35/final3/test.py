import time

import captcha_main
import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime
import common_function
import pandas as pd
import random
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0'
}


duplicate_list = []
error_list = []
completed_list = []
attachment = None
url_id = None
current_date = None
current_time = None
Ref_value = None
ini_path = None

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


# url = "https://journals.biologists.com/dev/"
# proxy_number = 0
# requests.get(url, proxies=)


# Function to get your original IP address
def get_original_ip():
    response = requests.get('https://api.ipify.org?format=json')
    return response.json()['ip']


# Function to get IP address using a proxy
def get_proxy_ip(proxy):
    response = requests.get('https://api.ipify.org?format=json', proxies=formatted_proxies[proxy_number])
    return response.json()['ip']

proxy_number = 0
# for i in range(0,len(proxies_list)):
#     proxy_number = i
#     original_ip = get_original_ip()
#     print('Original IP:', original_ip)
#
#
#     proxy_ip = get_proxy_ip(proxy)
#     print('Proxy IP:', proxy_ip)

# url = "https://journals.biologists.com/dev/"
# response = requests.get(url, proxies=formatted_proxies[proxy_number], headers=headers,timeout=20)
# print(response.status_code)
# print(response.content)

print("hi")

's' in 'hello s'