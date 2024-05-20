import requests
from bs4 import BeautifulSoup
import os
import re
from datetime import datetime
import pandas as pd
import random
import time
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
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

def get_random_proxy():
    return random.choice(formatted_proxies)

url = "https://journals.biologists.com/"
# response = requests.get(url,proxies=get_random_proxy(),headers=headers)

def scrapper(url):
    payload = {'api_key': '7af826f113ca7a065f3e7b1f623431ee', 'url': url}
    r = requests.get('http://api.scraperapi.com', params=payload)
    s = r.text
    print(s)
    # return s

# print(scrapper(url))
scrapper(url)